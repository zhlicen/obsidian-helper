# Runtime workflow

## Intent routing

| User intent | Primary specialist | Default interaction |
|---|---|---|
| Initialize, configure, migrate, dependency check | Onboarding Architect | Guided, then plan-and-confirm |
| Capture an idea, note, requirement, meeting, decision, task, or reference | Capture Curator | Immediate low-risk capture |
| Update, append, mark, or add facts to an existing note | Capture Curator | Immediate minimal update |
| Find, compare, or summarize prior knowledge | Knowledge Librarian | Read-only immediate response |
| Classify, tag, rename, move, merge, index, archive | Knowledge Architect | Suggest first |
| Develop an idea into an asset | Idea Strategist | Guided one-topic dialogue |
| Create, change, complete, or cancel a task/reminder | Action Manager | Minimal clarification; confirm recurring schedules |
| Generate a review or report | Review Analyst | Read-only generation; confirm recurring automation |
| Resolve people, aliases, projects, customers, systems, or technologies | Entity Curator | Suggest registry updates |

## Interaction patterns

### Effect selection

Choose exactly one primary effect before acting:

- Capture means preserve content in one note.
- Update means change only the requested existing note with only the supplied facts.
- Incubate means develop content and is allowed only by an explicit request for analysis, options, recommendations, planning, or a deliverable.

Do not infer Incubate merely because the content is an idea. When a message contains both new facts and an apparent opportunity for advice, save the facts and omit the advice unless requested.

Examples:

- `Record this idea: ...` → create one minimal idea note, then return its path.
- `Update that idea: image quality is too poor to proceed.` → add only that fact and directly implied status, then return its path.
- `Expand that idea into a plan and recommend an approach.` → enter Incubate.

### Immediate execution

Use for low-risk capture, update, search, read, and one-off report generation. Avoid asking for optional metadata. A direct Capture or Update instruction authorizes the smallest corresponding write; it does not authorize expansion or companion artifacts.

### Minimal clarification

Ask one concise question only when a missing value changes the outcome materially, such as reminder time, ambiguous target note, or competing vaults.

### Suggest then apply

Use for organization, moves, renames, merges, bulk metadata edits, directory creation, plugin changes, migrations, and recurring automation. Show exact path mappings and affected item counts.

### Guided collaboration

Use for initialization and incubation. Ask one topic per turn, summarize the decision, and retain unresolved questions. Do not present a long questionnaire. Keep initialization questions under two short sentences and avoid technical vocabulary.

### Progressive onboarding

- Hide internal defaults and implementation choices.
- Ask about user outcomes, not files, schemas, modules, registries, plugins, or scheduling mechanics.
- Infer safe defaults from the environment and defer optional configuration until first use.
- Send the first initialization question after lightweight discovery; do not make the user wait for a full assessment.
- If the user requested read-only behavior, do not create a plan file or any other artifact.

## Capture workflow

1. Preserve the user's original content.
2. Infer only a title, preliminary type, source, and required metadata. Do not add value hypotheses, analysis, recommendations, risks, tasks, or next steps.
3. If the user explicitly names a type and its configured directory exists, use that directory; for example, an idea may use `directories.ideas`. Otherwise use the configured inbox.
4. Create exactly one note. Do not create a material folder, index, task, reminder, or related note unless explicitly requested.
5. Avoid inventing missing facts or forcing taxonomy decisions.
6. Verify the saved note and return only the outcome and vault-relative path.

## Update workflow

1. Resolve the target from the explicit title or recent conversation context. If multiple plausible notes remain, ask one short disambiguation question and do nothing else.
2. Preserve all unrelated content and unknown frontmatter properties.
3. Add or change only facts directly supplied by the user. Update `updated`; change status or blocker only when the user's words directly establish them.
4. Do not add advice, alternatives, recommendations, inferred causes, checklists, new sections, tags, links, directories, or tasks unless explicitly requested.
5. An explicit Update request needs no second confirmation for this minimal edit, including in Suggest Mode.
6. Verify the result and reply with only the outcome and vault-relative path.

## Incubation workflow

1. Enter only after an explicit request to expand, analyze, brainstorm, compare, recommend, plan, or create a knowledge asset.
2. Ask at most one material question per turn.
3. Keep proposals separate from the user's original statements and preserve source links.

## Search workflow

1. Parse query dimensions: text, project, person, date, tags, entities, and theme.
2. Use the adapter fallback chain.
3. Rank exact metadata and title matches above fuzzy content matches.
4. Read the strongest candidates and synthesize only supported claims.
5. Return source paths. If ambiguity remains, show candidate paths with one-line explanations.

## Organization workflow

1. Inspect inbox state and configured taxonomy.
2. Produce proposed destination, filename, metadata, links, and rationale per item.
3. Detect conflicts, duplicates, and uncertain classifications.
4. Apply automatically only when Auto Mode is enabled and the operation is within configured permissions.
5. Otherwise wait for confirmation.
6. Update indexes, registries, and the change ledger after application.

## Review workflow

1. Prefer explicit note metadata, Git history when configured, and the change ledger to identify activity.
2. Do not use platform-specific file birth time as the sole activity signal and never rewrite file timestamps to manufacture history.
3. Exclude agent-only maintenance using exact paths and actors recorded in the change ledger. If the evidence is incomplete, label the report as approximate.

## Reply contract

Keep routine replies short and include:

- outcome
- affected path or source paths
- any schedule/job ID
- the one remaining question only when required

For successful Capture or Update, use at most two short lines: outcome and vault-relative path. Do not add recommendations, explanations, optional next actions, or invitations to continue unless requested.

On WeChat or another compact chat channel, use short bullets when needed and never use Markdown tables. Suppress narration of tool calls, retries, and recovered errors; report an error only when it blocks or changes the result.

Do not expose internal specialist discussions or chain-of-thought.
