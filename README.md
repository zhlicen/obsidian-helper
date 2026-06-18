# Obsidian Helper

[English](README.md) | [简体中文](README.zh-CN.md)

Obsidian Helper is a portable [Agent Skill](https://agentskills.io) for capturing, finding, organizing, developing, and reviewing knowledge in an Obsidian vault.

It is designed for Codex, OpenClaw, and other Agent Skills-compatible runtimes. The skill is written in English, while onboarding, notes, and reports use the user's configured working language.

## What it does

- Initializes itself without restructuring an existing vault.
- Captures ideas, notes, requirements, meetings, decisions, tasks, and references.
- Applies factual updates minimally, without adding unsolicited advice or artifacts.
- Searches and summarizes vault knowledge with source paths.
- Suggests metadata, links, names, moves, merges, and archives before applying them.
- Develops related ideas into PRDs, technical designs, plans, ADRs, and roadmaps.
- Enters idea incubation only when the user explicitly asks to expand, analyze, plan, or recommend.
- Manages tasks and reminders through runtime-provided scheduling when available.
- Produces periodic reviews, inbox reports, and vault health assessments.

All knowledge remains in the user's vault. Plugins are optional, and structural changes are suggestion-first by default.

## Prerequisites

1. Install the [latest stable Obsidian desktop app](https://obsidian.md/download).
2. Follow Obsidian's official instructions to [enable Obsidian CLI](https://obsidian.md/cli).
3. Keep Obsidian running for CLI-backed operations. The skill may start the installed app when the runtime permits it.

Python 3.9 or newer is optional and is used only by the bundled read-only environment checker.

## Installation

Clone this repository first:

```bash
git clone https://github.com/zhlicen/obsidian-helper.git
cd obsidian-helper
```

### Codex

Codex discovers personal skills in `~/.agents/skills` and supports symlinked skill directories:

```bash
mkdir -p ~/.agents/skills
ln -s "$PWD/skills/obsidian-helper" \
  ~/.agents/skills/obsidian-helper
```

After the repository is published, you can also tell Codex:

```text
$skill-installer Install https://github.com/zhlicen/obsidian-helper/tree/main/skills/obsidian-helper
```

Restart Codex only if the skill does not appear automatically. See the [official Codex skills documentation](https://developers.openai.com/codex/skills).

### OpenClaw

Copy the skill into the active OpenClaw workspace:

```bash
mkdir -p ~/.openclaw/workspace/skills
cp -R skills/obsidian-helper \
  ~/.openclaw/workspace/skills/obsidian-helper
openclaw skills info obsidian-helper
```

### Other compatible agents

Copy `skills/obsidian-helper` into the runtime's user or project skills directory. The destination must preserve `SKILL.md`, `references/`, `assets/`, and `scripts/` together. Consult that runtime's documentation for its discovery path.

## Usage

Invoke the skill explicitly or describe a matching task naturally:

```text
Use Obsidian Helper to initialize my vault.
```

```text
Capture this as an idea: A weekly digest that groups customer feedback by product area.
```

```text
Find everything we decided about offline sync in the last six months.
```

```text
Review my inbox and suggest how to organize it. Do not change files yet.
```

```text
Turn the related onboarding ideas into a draft PRD.
```

On first use, the skill identifies the vault and asks three short questions about working language, personal or team use, and approval preferences. It does not modify existing notes before confirmation.

## Repository layout

```text
skills/obsidian-helper/
├── SKILL.md
├── agents/openai.yaml
├── assets/
├── references/
└── scripts/check_environment.py
```

Run the optional environment check with:

```bash
python3 skills/obsidian-helper/scripts/check_environment.py
python3 skills/obsidian-helper/scripts/check_environment.py --vault "/path/to/vault" --deep
```

The script only reads local environment and vault metadata. It does not install software, enable plugins, or modify notes.

## Design principles

- Obsidian first: native behavior, official CLI, optional plugins, then safe Markdown access.
- User-owned data: no separate knowledge database.
- Graceful degradation: core capture and search continue without plugins.
- Reversible organization: archive instead of delete and record structural changes.
- Single writer: specialist roles may analyze in parallel, but formal mutations are coordinated.
- Portable runtime integration: reminders and automation use capabilities supplied by the host agent.

This project is not affiliated with or endorsed by Obsidian, OpenAI, or OpenClaw.

## License

[MIT](LICENSE)
