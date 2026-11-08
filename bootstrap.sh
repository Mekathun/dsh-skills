#!/usr/bin/env bash
# 在新电脑上把 dsh-skills 仓库同步到 ~/.dsh/skills
# 用法: bash bootstrap.sh [仓库地址]
#   默认用 HTTPS；想走 SSH 就传 git@github.com:Mekathun/dsh-skills.git
set -euo pipefail

URL="${1:-https://github.com/Mekathun/dsh-skills.git}"
SKILLS="${DSH_SKILLS_DIR:-$HOME/.dsh/skills}"

mkdir -p "$(dirname "$SKILLS")"

if [ -e "$SKILLS" ]; then
  if [ -d "$SKILLS/.git" ]; then
    echo "==> $SKILLS 已经是 git 仓库，直接更新"
    git -C "$SKILLS" remote set-url origin "$URL" 2>/dev/null || git -C "$SKILLS" remote add origin "$URL"
    git -C "$SKILLS" pull --ff-only
    exit 0
  fi
  BAK="${SKILLS}.bak.$(date +%Y%m%d-%H%M%S)"
  echo "==> 备份现有目录到 $BAK"
  mv "$SKILLS" "$BAK"
fi

echo "==> 克隆 $URL 到 $SKILLS"
git clone "$URL" "$SKILLS"

echo "==> 完成，共 $(find "$SKILLS" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ') 个 skill"
echo "    更新: cd \"$SKILLS\" && git pull"
