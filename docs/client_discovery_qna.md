# Client Discovery Q&A

Use this as the client evidence base. Ask questions, find the closest matching answer, and cite it in your reasoning. Do not treat this as a solution document.

## Event and scale

### Q: How large is the placement day?
Around 280 candidates are scheduled across one day. At peak time, around 90 candidates may be waiting or moving between rounds.

### Q: How many companies are interviewing?
Three companies are participating today: NovaBank, CloudKart and UrbanGrid. Each company has a different number of interviewers and interview rounds.

### Q: How many rooms are available?
There are 10 interview rooms. Two are usually kept as flexible rooms for overflow or rescheduling.

## Current workflow

### Q: What happens when a candidate arrives?
The candidate checks in at the placement desk using a QR code. The placement coordinator can see the check-in record, but the QR system only records arrival at the venue, not arrival outside a specific interview room.

### Q: What happens after check-in?
Candidates wait until a coordinator calls them for the assigned interview room. Coordinators currently use a spreadsheet and chat messages from room volunteers to decide whom to call next.

### Q: What happens when an interview starts or ends?
Room volunteers are expected to update the interview event sheet when a candidate enters and exits. Updates can lag when volunteers are busy.

### Q: What happens when an interview overruns?
Usually the room volunteer informs the placement coordinator through WhatsApp. The coordinator may move a later candidate, switch rooms, or ask candidates to wait.

### Q: Who currently resolves schedule chaos?
The placement coordinator is the primary operator during the day. The Placement Head gets involved only for company escalations or major delays.

## Stakeholders

### Q: What does the candidate care about?
Candidates care about knowing when they are likely to be called and avoiding long unexplained waiting.

### Q: What do recruiters care about?
Recruiters want interview slots to be filled efficiently and do not want interviewers waiting for candidates.

### Q: What does the placement coordinator care about?
The coordinator needs to know which interviews need attention now, which candidates are ready, and what action to take next.

### Q: What does the Placement Head care about?
The Placement Head cares about overall schedule smoothness, company experience, candidate experience and avoiding escalations.

## Data sources

### Q: Where is the planned schedule stored?
The official interview plan is in the placement scheduling system. For the exercise, it is represented as `data/interviews.csv`.

### Q: Where do candidate arrival records live?
Candidate arrival is recorded in the QR check-in system. For the exercise, it is represented as `data/candidate_checkins.csv`.

### Q: Where do actual interview starts and completions live?
Actual interview progress is captured in the interview event log. For the exercise, it is represented as `data/interview_events.csv`.

### Q: Where are coordinator interventions recorded?
Today, interventions are mostly informal. For your solution, you may record them in `operations_actions.csv` or an equivalent application store.

## Data semantics and limits

### Q: What does candidate check-in time mean?
It means the candidate arrived at the placement venue. It does not mean they are sitting outside the correct room.

### Q: Can we measure true candidate waiting time exactly?
Not exactly. We can approximate from venue check-in to actual interview start, but there is no room-queue join timestamp.

### Q: Are schedule times always current?
No. The schedule may become outdated during the day if interviews overrun or rooms are reassigned manually.

### Q: Does an interview without an end event mean it is still ongoing?
Maybe. It might be ongoing, or the volunteer may have forgotten to record completion. This needs operational caution.

### Q: What counts as a delayed interview?
There is no formally approved SLA. Leadership informally says delays over 15 minutes feel bad, but this is not yet a documented business rule.

### Q: Can the system automatically move candidates between rooms?
No. A placement coordinator must approve room changes because companies and interviewers may have constraints.

### Q: Can the system automatically message candidates?
It can draft or suggest messages, but mass or sensitive communication should be approved by a coordinator.

### Q: Are candidate phone numbers available?
Yes, but avoid exposing personal phone numbers in the first classroom demo unless absolutely necessary. Use candidate names or masked identifiers.

## Constraints

### Q: Can we replace the scheduling system today?
No. The first solution should sit on top of the existing schedule and event records.

### Q: Can we add new hardware or room sensors?
No. Work with the available data. You may list better instrumentation as a future recommendation.

### Q: Does the solution need to be fully production-ready today?
No. The expected output is a thin vertical slice that proves the workflow end-to-end.

## Success

### Q: What does success look like to leadership?
Fewer unexplained candidate waits, fewer recruiter complaints and better visibility into interviews that need attention.

### Q: What does success look like to the coordinator?
The coordinator can quickly see what needs attention, understand why, take an action and record the action.

### Q: Is the KPI already finalized?
No. The team should propose a primary KPI and a few supporting metrics based on the workflow and data limitations.
