# Data README

## Core files
- `interviews.csv`: planned interview schedule. This is the official plan, but it may become stale during the day.
- `candidate_checkins.csv`: venue arrival records. This does not indicate room-level queue position.
- `interview_events.csv`: actual interview lifecycle events. Some events may be missing or delayed.
- `operations_actions.csv`: coordinator interventions. Your product may write new actions here or to another small store.
- `candidates.csv`, `companies.csv`, `interviewers.csv`, `rooms.csv`: reference data.

## Important realism notes
- Waiting time must be approximated; exact queue join time is not available.
- The schedule is planned truth, not always live truth.
- Missing completion events are ambiguous: interview may be ongoing or event logging may be stale.
- There is no approved delay SLA. Leadership informally mentions 15 minutes.
- Do not expose unnecessary personal data in your UI.
