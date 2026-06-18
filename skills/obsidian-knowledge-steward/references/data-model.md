# Data model

## Note types

- `note`: general knowledge or observation
- `idea`: early concept or opportunity
- `requirement`: requested capability or constraint
- `meeting`: discussion, decisions, and actions
- `decision`: selected option, rationale, and consequences
- `task`: actionable work with state or due date
- `reference`: external or supporting material

## Common frontmatter

Use English metadata keys and the configured working language for human-readable values.

```yaml
---
id: ks-20260618-example
type: idea
status: inbox
created: 2026-06-18T11:30:00+08:00
updated: 2026-06-18T11:30:00+08:00
author: Hang
source: chat
project: []
entities: []
tags: []
visibility: personal
---
```

Required: `id`, `type`, `status`, `created`, `updated`, `source`.

Optional fields should be omitted or empty, never fabricated. Preserve unknown custom properties on edits.

## Status lifecycle

Primary states:

- `inbox`: captured and not reviewed
- `reviewed`: understood and classified
- `incubating`: actively developing
- `promoted`: converted into a durable knowledge asset
- `archived`: inactive but retained

Tasks may additionally use `todo`, `doing`, `done`, `cancelled`, or `deferred` in a task-specific field.

## Registries

People entries contain canonical name, aliases, role, optional email, and visibility.

Entity entries contain canonical name, type (`project`, `customer`, `system`, `technology`, or custom), aliases, status, and related entities.

Use canonical IDs for relationships when available. Never overwrite an alias mapping automatically when multiple canonical matches are plausible.

## Knowledge assets

Promoted outputs include `prd`, `technical-design`, `project-plan`, `decision-record`, and `roadmap`. Every asset must link back to source inbox items or ideas.

## Directory mappings

Resolve logical locations such as `inbox`, `ideas`, `projects`, and `archive` through `skill-config.yaml`. Do not hardcode default directories after initialization.
