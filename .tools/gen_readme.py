#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate README.md inventory for the ~/.dsh/skills repo."""
import os, re, sys, json

ROOT = os.path.expanduser("~/.dsh/skills")
if len(sys.argv) > 1:
    ROOT = sys.argv[1]

CATEGORIES = [
    ("学术与研究", """academic-paper academic-paper-reviewer academic-pipeline deep-research research sr-screener
        understand understand-chat understand-dashboard understand-diff understand-domain understand-explain
        understand-figma understand-knowledge understand-onboard to-spec to-tickets to-questionnaire"""),
    ("工程与代码", """ds-mode ds-plan-loop ds-principles ds-blueprint ds-tdd ds-verify-loop ds-review-loop ds-jury
        ds-ship ds-ready ds-watch-pr ds-pr ds-pr-comments ds-adopt ds-revive ds-catchup ds-context-reset
        ds-ledger ds-lessons ds-explanation ds-explain ds-sharpen ds-swarm ds-best-of-n ds-blast-radius
        ds-unstick ds-unslop ds-design ds-design-audit
        ponytail ponytail-audit ponytail-review ponytail-debt ponytail-gain ponytail-help
        caveman caveman-commit caveman-compress caveman-discover caveman-evidence-review caveman-explore
        caveman-help caveman-learn caveman-manage caveman-optimize caveman-review caveman-setup caveman-stats
        megacave ultracave cavecrew
        code-review codebase-design domain-modeling improve-codebase-architecture setup-ts-deep-modules
        karpathy-guidelines lean-build migration safe-refactor surgical-patch mp-prototype prototype
        systematic-debugging diagnosing-bugs diagnosing-superpowers investigate-first
        tdd test-driven-development scaffold-exercises
        writing-plans executing-plans subagent-driven-development dispatching-parallel-agents
        using-git-worktrees finishing-a-development-branch
        requesting-code-review receiving-code-review verification-before-completion verify-and-stop
        git-guardrails-claude-code setup-pre-commit using-superpowers
        reverse-engineer-anything software-factory triage implement implement-spec wayfinder wait-what
        ask-sonner brainstorming ds-help migrate-to-shoehorn write-swift"""),
    ("设计与前端", """impeccable apple-design emil-design-eng mobile-native break-ui pick-ui-library
        find-animation-opportunities improve-animations review-animations remove-animations
        animate animate-expo animation-performance animation-vocabulary
        gsap-core gsap-react gsap-timeline gsap-scrolltrigger gsap-plugins gsap-performance
        gsap-utils gsap-frameworks
        hyperframes hyperframes-cli hyperframes-registry video-shotcraft media-use"""),
    ("像素与建模", """minecraft-intake minecraft-java-build minecraft-paper-plugin minecraft-spigot-legacy
        minecraft-fabric-mod minecraft-forge-mod minecraft-neoforge-mod minecraft-major-mods
        blockbench-mcp-modeling"""),
    ("写作与表达", """humanizer writing-skills writing-for-agents writing-beats writing-fragments writing-shape
        ds-unslop pr teach retro grill-me grill-with-docs grilling chief-of-staff handoff claude-handoff
        ask-matt loop-me setup-matt-pocock-skills wizard"""),
]

KNOWN = set()
for _, names in CATEGORIES:
    KNOWN.update(names.split())

def parse_frontmatter(path):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        text = f.read()
    name, desc = None, None
    if text.startswith("---"):
        end = text.find("\n---", 3)
        block = text[3:end] if end != -1 else text[3:]
    else:
        block = ""
    lines = block.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if m and m.group(1) in ("name", "description"):
            key, rest = m.group(1), m.group(2).strip()
            # block scalar
            if rest in (">", "|", ">-", "|-", ">+", "|+"):
                parts = []
                i += 1
                while i < len(lines) and (lines[i].strip() == "" or lines[i].startswith((" ", "\t"))):
                    parts.append(lines[i].strip())
                    i += 1
                val = " ".join(p for p in parts if p)
            elif rest.startswith('"'):
                buf = rest[1:]
                while not re.search(r'(?<!\\)"\s*$', buf) and i + 1 < len(lines):
                    i += 1
                    buf += " " + lines[i].strip()
                val = re.sub(r'\\"', '"', buf.rstrip().rstrip('"'))
                val = val.replace("\\\\", "\\")
            elif rest.startswith("'"):
                buf = rest[1:]
                while not buf.rstrip().endswith("'") and i + 1 < len(lines):
                    i += 1
                    buf += " " + lines[i].strip()
                val = buf.rstrip().rstrip("'").replace("''", "'")
            else:
                val = rest
            if key == "name":
                name = val
            else:
                desc = val
        i += 1
    if not desc:
        # fallback: first non-empty paragraph after frontmatter
        body = text[end + 4:] if text.startswith("---") and end != -1 else text
        for para in re.split(r"\n\s*\n", body):
            p = para.strip()
            if p and not p.startswith("#!"):
                p = re.sub(r"^#+\s*", "", p)
                desc = p
                break
    return name, (desc or "").strip()

def shorten(desc, limit=130):
    d = re.sub(r"\s+", " ", desc).strip()
    cut = re.split(r"(?i)\b(Triggers?:|Use when|Use this|Use for|Use after|Use before)\b", d, maxsplit=1)
    if len(cut) > 1 and len(cut[0]) >= 40:
        d = cut[0].rstrip(" .;,-")
    if len(d) > limit:
        d = d[:limit].rsplit(" ", 1)[0] + "…"
    return d.replace("|", "\\|")

rows = []
for entry in sorted(os.listdir(ROOT)):
    d = os.path.join(ROOT, entry)
    md = os.path.join(d, "SKILL.md")
    if not os.path.isdir(d) or not os.path.isfile(md):
        continue
    name, desc = parse_frontmatter(md)
    nfiles, nbytes = 0, 0
    for base, _, files in os.walk(d):
        for fn in files:
            fp = os.path.join(base, fn)
            try:
                nbytes += os.path.getsize(fp)
                nfiles += 1
            except OSError:
                pass
    rows.append({
        "dir": entry,
        "name": name or entry,
        "desc": shorten(desc),
        "files": nfiles,
        "kb": round(nbytes / 1024),
    })

grouped = {}
for r in rows:
    cat = "其他"
    for cname, names in CATEGORIES:
        if r["dir"] in names.split():
            cat = cname
            break
    grouped.setdefault(cat, []).append(r)

order = [c for c, _ in CATEGORIES] + ["其他"]
total_files = sum(r["files"] for r in rows)
total_kb = sum(r["kb"] for r in rows)

out = []
out.append("# DSH Skills 仓库\n")
out.append(
    "这台机器上 DeepSeek Harness 的 skill 全集，共 **%d 个**、%d 个文件、约 %.1f MB。"
    "仓库根目录就是 `~/.dsh/skills` 的目录结构，clone 下来直接可用。\n"
    % (len(rows), total_files, total_kb / 1024)
)
out.append("## 怎么用\n")
out.append("```bash")
out.append("# 第一次在新电脑上同步（会先备份已有的 skills 目录）")
out.append("bash bootstrap.sh https://github.com/Mekathun/dsh-skills.git")
out.append("")
out.append("# 以后更新：拉最新，推本机改动")
out.append("cd ~/.dsh/skills && git pull && git push")
out.append("```\n")
out.append("仓库是私有的，新电脑要先登录过 GitHub（`git` 会走系统凭据管理器），"
           "或者用 `git clone git@github.com:Mekathun/dsh-skills.git`（需要该机器已加 SSH key）。\n")
out.append("手动安装：")
out.append("```bash")
out.append("mv ~/.dsh/skills ~/.dsh/skills.bak.$(date +%s)")
out.append("git clone https://github.com/Mekathun/dsh-skills.git ~/.dsh/skills")
out.append("```\n")
out.append("## 不在本仓库里的 skill\n")
out.append("下面这些也出现在对话的 skill 列表里，但不在 `~/.dsh/skills`，"
           "它们是 DSH 自带（office 系列随安装包）或由 bundle / 插件带进来的。"
           "换电脑装上同样的 DSH 版本和这些 bundle 就有，不用（也不该）复制进 skills 目录，"
           "否则同名 skill 会重复注册。\n")
out.append("| skill | 来源 |")
out.append("| --- | --- |")
for nm, src in [
    ("office / office-docx / office-pptx / office-xlsx / office-render / office-export-pdf / office-recalculate", "DSH 安装包自带 `resources/runtime/office-skills`"),
    ("minecraft-intake / -java-build / -paper-plugin / -spigot-legacy / -fabric-mod / -forge-mod / -neoforge-mod / -major-mods", "`minecraft-dev` bundle"),
    ("music-studio", "`@jypjypjypjyp/dsh-music-studio` bundle"),
    ("nekowhale-stickers", "`dsh-nekowhale-stickers` 插件"),
    ("humanizer / fishtalk / media-use / hyperframes / hyperframes-cli / hyperframes-registry / browser-skill / diagnose-windows-sandbox-acl / web-design-skill / reverse-engineer-anything", "bundle / 插件提供"),
]:
    out.append("| %s | %s |" % (nm, src))
out.append("")
out.append("新增或删除 skill 后，跑 `python .tools/gen_readme.py` 重新生成本文件。\n")
out.append("## 清单\n")
for cat in order:
    items = grouped.get(cat)
    if not items:
        continue
    out.append("### %s（%d）\n" % (cat, len(items)))
    out.append("| skill | 简介 | 文件 |")
    out.append("| --- | --- | ---: |")
    for r in items:
        out.append("| `%s` | %s | %d |" % (r["dir"], r["desc"], r["files"]))
    out.append("")
with open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(out))

print("skills:", len(rows), "files:", total_files, "size MB:", round(total_kb / 1024, 1))
for cat in order:
    print(" ", cat, len(grouped.get(cat, [])))
print("其他:", [r["dir"] for r in grouped.get("其他", [])])
