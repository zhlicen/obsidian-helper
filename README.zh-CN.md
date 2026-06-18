# Obsidian Helper

[English](README.md) | [简体中文](README.zh-CN.md)

Obsidian Helper 是一个面向个人和团队的可移植 [Agent Skill](https://agentskills.io)，用于在 Obsidian Vault 中记录、查找、整理、沉淀和回顾知识。

它适用于 Codex、OpenClaw 以及其他兼容 Agent Skills 的运行环境。Skill 本身使用英文编写，初始化引导、笔记和报告则使用用户配置的工作语言。

## 功能

- 在不重构现有 Vault 的前提下完成初始化。
- 记录灵感、笔记、需求、会议、决策、任务和参考资料。
- 最小化更新已有内容，不擅自增加建议或额外产物。
- 搜索并总结 Vault 中的知识，同时提供来源路径。
- 在执行前提出元数据、链接、命名、移动、合并和归档建议。
- 将相关灵感沉淀为 PRD、技术方案、计划、ADR 和路线图。
- 只有用户明确要求展开、分析、规划或推荐时，才进入灵感孵化。
- 在运行环境支持时管理任务和提醒计划。
- 生成周期回顾、Inbox 报告和 Vault 健康检查。
- 识别人员、别名、项目、客户、系统和技术实体，支持团队知识管理。

所有知识都保存在用户自己的 Vault 中。插件属于可选依赖，涉及结构的修改默认采用“先建议、后执行”模式。

## 知识生命周期

`记录或更新 → Inbox → 查找 → 整理 → 知识库 → 孵化 → 知识资产 → 回顾`

记录和事实更新保持最小化；只有用户明确要求展开、分析、规划或推荐时，才进入孵化阶段。

## 使用模式

- **Personal（个人）**：私人知识库。除非用户明确要求，否则内容不会离开 Vault。
- **Team（团队）**：共享知识库，支持人员、角色、项目、实体、团队报告和谨慎的身份归一。
- **Hybrid（混合）**：在同一个 Vault 中管理个人与共享知识，通过可见性边界隔离；个人笔记不会进入团队报告。

使用模式在初始化时选择，后续可以调整，不需要重构 Vault。

## 专家角色编排

用户只需要和 Obsidian Helper 对话。它会根据请求自动选择最合适的逻辑专家：

- **Onboarding Architect（初始化架构师）**：初始化、配置、依赖检查、Vault 评估和迁移规划。
- **Capture Curator（记录管理员）**：最小化记录和事实更新，不主动提供建议。
- **Knowledge Librarian（知识检索员）**：只读搜索、证据排序、对比和带来源的总结。
- **Knowledge Architect（知识架构师）**：分类体系、元数据、标签、链接、模板、索引、仪表盘和整理方案。
- **Idea Strategist（灵感策划师）**：在用户明确要求时，将灵感孵化为 PRD、技术方案、项目计划、ADR 和路线图。
- **Action Manager（行动管理员）**：任务、提醒、时区、重复规则、发送渠道和调度一致性。
- **Review Analyst（回顾分析师）**：日报、周报、月报、季度报告、项目报告、Inbox 报告和团队报告。
- **Entity Curator（实体管理员）**：维护人员、别名、角色、项目、客户、系统、技术和关系。

运行环境支持时，多个专家可以并行进行只读分析；Obsidian Helper 始终是唯一正式写入者，并向用户返回一份统一结果。

## 前置要求

1. 安装[最新稳定版 Obsidian 桌面应用](https://obsidian.md/download)。
2. 按照 Obsidian 的[官方说明启用 Obsidian CLI](https://obsidian.md/cli)。
3. 使用 CLI 操作时保持 Obsidian 运行。若运行环境允许，Skill 也可以启动已经安装的 Obsidian。

Python 3.9 或更高版本为可选依赖，仅用于运行附带的只读环境检查脚本。

## 安装

### OpenClaw

把下面这句话发给 OpenClaw：

```text
请安装这个 Agent Skill：https://github.com/zhlicen/obsidian-helper/tree/main/skills/obsidian-helper 。安装后请验证 obsidian-helper 已经可用，并告诉我安装路径。
```

### Codex

把下面这句话发给 Codex：

```text
$skill-installer Install https://github.com/zhlicen/obsidian-helper/tree/main/skills/obsidian-helper
```

Codex 通常会自动发现新安装的 Skill；没有出现时再重启。具体说明参见 [Codex 官方 Skills 文档](https://developers.openai.com/codex/skills)。

<details>
<summary>手动安装备用方案</summary>

克隆仓库：

```bash
git clone https://github.com/zhlicen/obsidian-helper.git
cd obsidian-helper
```

安装到 Codex：

```bash
mkdir -p ~/.agents/skills
cp -R skills/obsidian-helper ~/.agents/skills/obsidian-helper
```

安装到 OpenClaw：

```bash
mkdir -p ~/.openclaw/workspace/skills
cp -R skills/obsidian-helper \
  ~/.openclaw/workspace/skills/obsidian-helper
openclaw skills info obsidian-helper
```

</details>

### 其他兼容 Agent

将 `skills/obsidian-helper` 复制到运行环境的用户级或项目级 Skills 目录。复制时必须完整保留 `SKILL.md`、`references/`、`assets/` 和 `scripts/`。具体发现路径请参考对应运行环境的文档。

## 使用示例

可以明确指定 Skill，也可以直接描述相关任务：

```text
使用 Obsidian Helper 初始化我的 Vault。
```

```text
把这个记录成灵感：每周按照产品模块汇总客户反馈。
```

```text
查找过去半年所有关于离线同步的决策。
```

```text
检查我的 Inbox 并提出整理建议，暂时不要修改文件。
```

```text
把与用户引导有关的灵感整理成一份 PRD 草稿。
```

首次使用时，Skill 会识别 Vault，并依次询问三个简短问题：工作语言、个人或团队使用方式，以及修改前是否需要确认。在用户确认之前，它不会修改现有笔记。

## 仓库结构

```text
skills/obsidian-helper/
├── SKILL.md
├── agents/openai.yaml
├── assets/
├── references/
└── scripts/check_environment.py
```

运行可选的环境检查：

```bash
python3 skills/obsidian-helper/scripts/check_environment.py
python3 skills/obsidian-helper/scripts/check_environment.py --vault "/path/to/vault" --deep
```

该脚本只读取本地环境和 Vault 元数据，不会安装软件、启用插件或修改笔记。

## 设计原则

- Obsidian 优先：依次使用原生能力、官方 CLI、可选插件和安全的 Markdown 访问。
- 用户拥有数据：不建立独立的知识数据库。
- 优雅降级：没有插件时仍然可以完成核心记录和搜索。
- 可逆整理：优先归档而不是删除，并记录结构变更。
- 单一写入者：专家角色可以并行分析，但正式修改由 Obsidian Helper 统一协调。
- 运行环境无关：提醒和自动化使用宿主 Agent 提供的能力。

本项目与 Obsidian、OpenAI 和 OpenClaw 均不存在隶属或官方认可关系。

## 许可证

[MIT](LICENSE)
