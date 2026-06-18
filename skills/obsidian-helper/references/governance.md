# Governance

## Organization modes

### Suggest Mode

Default. Analyze and propose changes without structural mutation. Routine capture into the inbox and read-only operations remain immediate.

An explicit request to capture or minimally update a note remains immediate in Suggest Mode. The authorization covers only that single minimal write.

### Auto Mode

May apply only configured low-risk transformations. Auto Mode never overrides confirmation requirements for high-impact or external actions.

## Confirmation gates

Require confirmation before:

- creating or changing the top-level directory structure
- creating companion directories or additional artifacts not explicitly requested
- moving, renaming, merging, or bulk-editing existing notes
- applying a migration
- installing or enabling plugins
- enabling Auto Mode
- creating recurring schedules
- sending vault content outside the local environment
- destructive actions or permanent deletion

## Reversibility

- Archive rather than delete.
- Record structural changes in the change ledger with timestamp, actor, operation, source, destination, and reason.
- For bulk changes, create a manifest with every affected path and original metadata sufficient to reverse the operation. A count-only ledger entry is insufficient.
- Never silently overwrite a conflicting note.
- Never rewrite file timestamps to hide an agent modification or simulate historical activity.

## Scope control

- Treat the user's verb as the scope boundary: record means record, update means update, organize means organize, and advise means advise.
- Do not bundle optional improvements into an authorized mutation.
- Do not create directories, indexes, tasks, schedules, or recommendations while performing a routine Capture or Update.

## Privacy

- Keep all user content and configuration in the vault.
- Redact secrets, credentials, identity numbers, contact details, financial details, precise addresses, health information, and private evaluations from chat summaries and reports unless explicitly requested in a private context.
- Apply stricter anonymization in team, group, or delegated-agent contexts.
- Do not alter source notes merely to redact an output.
- Do not transmit vault data to external APIs for classification, embeddings, or summarization without explicit configuration and authorization.

## Team and Hybrid mode

- Respect note visibility and team boundaries.
- Do not include personal notes in team reports.
- Resolve identity aliases conservatively.
- Record report evidence and source paths without exposing private content.

## Failure handling

- If a write fails, report it and do not update indexes as if it succeeded.
- If an index update fails after a note write, report partial completion and queue repair.
- If runtime scheduling fails after a reminder note is created, mark the reminder unscheduled and report it.
- If configuration is invalid, stop mutations and offer a repair plan.
