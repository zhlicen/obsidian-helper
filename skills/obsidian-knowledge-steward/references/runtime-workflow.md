# Runtime workflow

## Intent routing

| User intent | Primary specialist | Default interaction |
|---|---|---|
| Initialize, configure, migrate, dependency check | Onboarding Architect | Guided, then plan-and-confirm |
| Capture an idea, note, requirement, meeting, decision, task, or reference | Capture Curator | Immediate low-risk capture |
| Find, compare, or summarize prior knowledge | Knowledge Librarian | Read-only immediate response |
| Classify, tag, rename, move, merge, index, archive | Knowledge Architect | Suggest first |
| Develop an idea into an asset | Idea Strategist | Guided one-topic dialogue |
| Create, change, complete, or cancel a task/reminder | Action Manager | Minimal clarification; confirm recurring schedules |
| Generate a review or report | Review Analyst | Read-only generation; confirm recurring automation |
| Resolve people, aliases, projects, customers, systems, or technologies | Entity Curator | Suggest registry updates |

## Interaction patterns

### Immediate execution

Use for low-risk capture, append, search, read, and one-off report generation. Avoid asking for optional metadata. Store uncertain new content in the configured inbox.

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
2. Infer a preliminary type and lightweight metadata.
3. Detect explicit project, person, customer, system, technology, date, and source mentions.
4. Write to the configured inbox unless the user explicitly names a destination.
5. Avoid inventing missing facts or forcing taxonomy decisions.
6. Return the saved path and inferred type.

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

## Reply contract

Keep routine replies short and include:

- outcome
- affected path or source paths
- any schedule/job ID
- the one remaining question or recommended next action, if needed

Do not expose internal specialist discussions or chain-of-thought.
