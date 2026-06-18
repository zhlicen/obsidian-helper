# Obsidian Helper

[English](README.md) | [简体中文](README.zh-CN.md)

Obsidian Helper 是一个可移植的 [Agent Skill](https://agentskills.io)，用于在 Obsidian Vault 中记录、查找、整理、沉淀和回顾知识。

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

所有知识都保存在用户自己的 Vault 中。插件属于可选依赖，涉及结构的修改默认采用“先建议、后执行”模式。

## 前置要求

1. 安装[最新稳定版 Obsidian 桌面应用](https://obsidian.md/download)。
2. 按照 Obsidian 的[官方说明启用 Obsidian CLI](https://obsidian.md/cli)。
3. 使用 CLI 操作时保持 Obsidian 运行。若运行环境允许，Skill 也可以启动已经安装的 Obsidian。

Python 3.9 或更高版本为可选依赖，仅用于运行附带的只读环境检查脚本。

## 安装

首先克隆仓库：

```bash
git clone https://github.com/zhlicen/obsidian-helper.git
cd obsidian-helper
```

### Codex

Codex 会从 `~/.agents/skills` 发现个人 Skill，并且支持符号链接：

```bash
mkdir -p ~/.agents/skills
ln -s "$PWD/skills/obsidian-helper" \
  ~/.agents/skills/obsidian-helper
```

仓库发布后，也可以直接告诉 Codex：

```text
$skill-installer Install https://github.com/zhlicen/obsidian-helper/tree/main/skills/obsidian-helper
```

如果 Skill 没有自动出现，再重启 Codex。具体说明参见 [Codex 官方 Skills 文档](https://developers.openai.com/codex/skills)。

### OpenClaw

将 Skill 复制到当前 OpenClaw 工作区：

```bash
mkdir -p ~/.openclaw/workspace/skills
cp -R skills/obsidian-helper \
  ~/.openclaw/workspace/skills/obsidian-helper
openclaw skills info obsidian-helper
```

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
