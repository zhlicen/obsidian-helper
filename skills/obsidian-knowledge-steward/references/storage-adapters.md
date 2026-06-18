# Storage adapters

## Adapter priority

Prefer capabilities in this order:

1. Obsidian native behavior
2. Official Obsidian CLI
3. Configured Obsidian plugins
4. Direct Markdown filesystem access

Never require a plugin for core data access.

## Application lifecycle

Before a CLI-backed operation:

1. Detect whether the Obsidian desktop app is running with an operating-system-appropriate process check.
2. If absent and the runtime permits local app startup, start the installed app using the operating system's normal launcher.
3. Wait briefly, then retry `obsidian version` a small bounded number of times.
4. Do not ask merely to start an already-installed local application.
5. If startup or CLI readiness fails, fall back safely and report the fallback.

Require the latest stable Obsidian desktop app and enable its CLI by following [Obsidian's official CLI documentation](https://obsidian.md/cli). Use only the official `obsidian` CLI. Pass `vault="<configured-name>"` when ambiguous. Inspect CLI output before reporting success.

## Search fallback

1. Omnisearch when installed and callable
2. Official Obsidian search
3. Dataview query when appropriate
4. `rg` over Markdown files
5. bounded Markdown scan

Search must remain functional without plugins.

## Recommended soft dependencies

- Dataview
- Templater
- Tasks
- Omnisearch
- Calendar
- Periodic Notes

Detect them but do not install or enable them without confirmation.

## Direct Markdown access

Use direct access for deterministic bulk reads, exact frontmatter edits, configuration, registries, change ledger, and operations not exposed by the CLI. Preserve line endings, YAML validity, links, and unknown properties.

Avoid writing inside `.obsidian/` except for an explicitly confirmed plugin or settings action.

## Attachments

Store attachments under the configured attachment directory. Use collision-safe names, preserve original extensions, and create Obsidian-compatible links. Do not upload attachments externally unless explicitly authorized.
