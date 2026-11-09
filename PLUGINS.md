# 插件清单

这台机器上装的 DSH（DeepSeek Harness）插件。113 个 npm 包里真正当插件用的就下面这些，其余是依赖。

profile 主要在 `desktop`，少数在 `web` / `headless`。标了「本地」的是自己写或改过的，源码在 `link:` 指向的目录里，npm 上装不到。

## 会话与上下文

| 插件 | 版本 | 干什么 |
| --- | --- | --- |
| `billion-context` | 0.1.212 | 上下文压缩。长会话把旧内容折叠成摘要，`compress` / `decompress` / `search_context` 三个工具，窗口 100K 也够用一个月 |
| `dsh-session-navigator` | 1.1.2 | 会话资源管理器：虚拟文件夹、标签、备注、回收站、跨 workspace 浏览。本地 |
| `dsh-session-progress` | 0.11.4 | 会话进度：嵌套清单带权重，输入框一圈进度环，右侧面板 |
| `dsh-unlag` | 1.16.0 | 桌面端刷新按钮，改完插件不用重启 DSH，正在跑的会话不受影响 |
| `dsh-memo` | 0.1.0 | 备忘录查询接口：按目录、按节、全文搜、项目卡、速查表。查一个事实几百 token，不用把整份 MEMO.md 塞进上下文。本地 |

## 浏览器与网页

| 插件 | 版本 | 干什么 |
| --- | --- | --- |
| `dsh-builtin-browser` | 0.5.6 | 可见的真浏览器，`dsh_browser_*` 工具驱动。人和 agent 共用一个窗口，能接管；按任务隔离会话，cookie 持久化，有验证码检测。本地 |
| `@wxg-prc-cpg/browser-skill-dsh-plugin` | 0.4.1 | 另一条路：`bsk_*` 工具，接管你自己登录着的 Chromium |
| `dsh-doyourweb` | 0.1.7 | 浏览器标签管理、页面批注，以及 MCP/CLI 优先的桌面 app 控制（`browser_read` / `browser_act` / `app_desktop`） |
| `dsh-web-file-uploader` | 1.0.0-rc.1 | 输入框的回形针按钮，传文件到 DSH 主机，图片按多模态模型给 image block |

## 模型与代理

| 插件 | 版本 | 干什么 |
| --- | --- | --- |
| `dsh-our-free-model` | 2.8.0 | 不填 API Key 就能用的模型通道：DeepSeek V4.1 Flash、Kimi K3 等，接了十个账号渠道，带本地 OpenAI 网关和局域网转发。本地 |
| `@deepseek-ai/dsh-subagent-claude-code` | 0.2.1-rc.2 | 用官方 Agent SDK 起一次性的 Claude Code 子代理 |
| `@nanmicoder/dsh-agent-teams` | 0.1.28 | AgentTeams：captain + 成员 + 带依赖的任务图 + 消息，`agent_teams_*` 一整套 |
| `@michengai/dsh-agency-agents` | 1.2.1 | 331 个可召唤的领域专家（`spawn_teammate` / `team_task_*`） |
| `@michengai/dsh-skills-manager` | 1.2.26 | skill 的统一加载与安全管理 |
| `@linxin666/dsh-client-ui-skill-explorer` | 0.4.7 | skill 中心面板：按来源（内置/项目/用户/自定义）看，能启停、新建、删除 |
| `minecraft-dev` | 0.9.1 | Minecraft 开发全家桶：8 个 skill、`mc_scaffold` / `mc_gradle`、Minecraft 架构师 preset、四子代理 A/B/C/D 流水线 |

## 内容生产

| 插件 | 版本 | 干什么 |
| --- | --- | --- |
| `@jypjypjypjyp/dsh-music-studio` | 0.2.1 | 写乐谱，`play_score` 渲染成带卷帘图、能播放、能导出 WAV/JSON 的卡片；长曲用 `score_new` / `score_edit` / `score_export` |
| `dsh-video-storyboard` | 0.7.0 | 视频转分镜图，一个镜头一格，带时间戳索引，`video_*` 工具族。本地 |
| `eac-design-world` | 0.6.0 | 自主视频生产（设计世界到成片）。本地 |
| `dsh-meme` | 0.1.76 | 表情包：图库/情绪筛选、关键词搜图、AI 学图，`send_meme` |
| `dsh-nekowhale-stickers` | 1.1.1 | 大肥鱼 / GPT娘 表情与自定义文字梗图（`sticker_*`、`meme_render`） |
| `fishtalk` | 0.3.6 | 教 AI 说人话：只读语料，说之前查一遍八股，`fishtalk_*`。本地 |
| `dsh-bili-scroll` | 2.0.4 | 每天替你刷一轮 B 站：读字幕挑值得看的，写日报，值得的 @ 你（`bili_*`） |
| `dsh-bili-tz-fix` | 0.1.0 | 让上面那个按北京时间算峰谷，不按系统本地时钟。本地 |
| `dsh-tieba-scroll` | 1.28.2 | 刷贴吧：读帖、写日报、自动签到、可选回帖，带人设和日记（`tieba_*`）。本地 |

## 界面与远程

| 插件 | 版本 | 干什么 |
| --- | --- | --- |
| `@linxin666/dsh-web-all` | 0.4.7 | 全家桶：任务板（`task_board_*`）、Git 分支图、皮肤中心、社区插件市场、宠物、设置页分组 |
| `dsh-pocket` | 2.12.0 | 手机扫码连电脑上的 DSH，局域网或公网，实时同屏 |
| `@linxin666/dsh-remote-web-ui` | 0.4.7 | 扫码配对，一个界面同时服务手机和电脑，带一次性 token 和可撤销设备会话 |
| `dsh-whale-widget` | 0.4.0 | 右下角余额小鲸鱼：余额/今日/峰谷，可换角色、音效、点击序列 |
| `dsh-mobile-layout-fix` | 0.1.0 | 窄屏竖屏时把对话列钉回中间，不然聊天区宽度塌成 0。本地 |
| `dshmarket` | 1.66.14 | 可视化插件市场，逛一逛点一下装好 |
| `dsh-mcp-connector` | 0.2.93 | MCP 连接器：接企业、金融、法律、专利、研究数据，支持 OAuth / API key / stdio（`mcp_connector_*`） |

## 底层

| 插件 | 版本 | 干什么 |
| --- | --- | --- |
| `dsh-ops` | 0.3.0 | Windows 上的 bash 5.3、PowerShell 7.6、一套 Rust 工具（`win_bash`、`job_*`、`terminal_*`，FastCtx 的读写检索） |
| `qq-agent-presets` / `qq-mode-console` | 0.2.0-r3 | QQ 桥的两个 agent preset 和模式开关（chat / closed-agent） |

## 顺带挂着的 MCP server

这五个不是 npm 插件，是 MCP server：

- `agentnative-government-open-data` — 政府开放数据，先免费取样，要付费得另批
- `aseprite` — 驱动 Aseprite 画像素画
- `blockbench` — 驱动 Blockbench 做模型、贴图、动画
- `ilostat-labour-statistics` — ILOSTAT 劳动统计（就业、失业、工资、工时）
- `imf-macroeconomic-statistics` — IMF 宏观数据（WEO、BOP、CPI 等）

## 换电脑怎么装回来

DSH 版本先对齐（插件都是和 0.2.x 的 harness 配着跑的）。

装单个：

```bash
dsh plugin --profile desktop add <包名>@<版本>
```

一次全装：把本机的 `.tools/profile-desktop.package.json` 两段（`dependencies` 和 `dsh.profile.bundles`）拷进新电脑的 `~/.dsh/profiles/desktop/package.json`，然后：

```bash
cd ~/.dsh/profiles/desktop && pnpm install
```

`link:` 开头的那些是本地路径，拷过去会指空。它们对应的源码在：

| 插件 | 源码位置 | 上游 |
| --- | --- | --- |
| `dsh-builtin-browser` | `~/.dsh/plugins/dsh-builtin-browser` | 无 |
| `dsh-memo` | `~/.dsh/plugins/dsh-memo` | github.com/wonderandyou/dsh-memo |
| `our-free-model` | `~/.dsh/plugins/our-free-model` | 无 |
| `dsh-session-navigator` | `~/.dsh/plugins/dsh-session-navigator` | 无 |
| `dsh-video-storyboard` | `~/.dsh/plugins/dsh-video-storyboard` | 无 |
| `eac-design-world` | `~/.dsh/plugins/eac-design-world` | 无 |
| `qq-agent-presets` / `qq-mode-console` | `~/.dsh/plugins/` 同名目录 | github.com/Derpyu520/qq-bridge |
| `fishtalk` | `default-workspace/fishtalk` | github.com/Nozzi2455/fishtalk |
| `dsh-bili-tz-fix` / `dsh-mobile-layout-fix` | `default-workspace/` 同名目录 | 无 |

标「无」的那几个要自己在两台机器之间拷目录，或者另开仓库。
