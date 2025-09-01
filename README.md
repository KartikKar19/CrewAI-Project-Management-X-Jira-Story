1️⃣ Diagram: SDLC → Epics → Stories → Assignees
PROJECT (SCRUM)
│
├─ Epic: Requirements Gathering (Assigned: Project Manager)
│    ├─ Story: Interview stakeholders  → Assigned to: Team Member 1
│    ├─ Story: Document requirements   → Assigned to: Team Member 2
│    └─ Story: Review approval          → Assigned to: Team Member 3
│
├─ Epic: System Design (Assigned: Project Manager)
│    ├─ Story: Create UML diagrams     → Assigned to: Team Member 4
│    ├─ Story: Database schema design  → Assigned to: Team Member 1
│    └─ Story: Architecture review     → Assigned to: Team Member 2
│
├─ Epic: Development (Assigned: Project Manager)
│    ├─ Story: Frontend implementation → Assigned to: Team Member 3
│    ├─ Story: Backend APIs            → Assigned to: Team Member 4
│    └─ Story: Integrate DB            → Assigned to: Team Member 1
│
├─ Epic: Testing (Assigned: Project Manager)
│    ├─ Story: Unit testing            → Assigned to: Team Member 2
│    ├─ Story: Integration testing     → Assigned to: Team Member 3
│    └─ Story: Bug fixing               → Assigned to: Team Member 4
│
├─ Epic: Deployment (Assigned: Project Manager)
│    ├─ Story: CI/CD pipeline          → Assigned to: Team Member 1
│    ├─ Story: Deploy to staging       → Assigned to: Team Member 2
│    └─ Story: Deploy to production    → Assigned to: Team Member 3
│
└─ Epic: Maintenance (Assigned: Project Manager)
     ├─ Story: Monitor system          → Assigned to: Team Member 4
     ├─ Story: Patch bugs              → Assigned to: Team Member 1
     └─ Story: Feature updates         → Assigned to: Team Member 2


Explanation of diagram:

Each Epic represents a SDLC phase.

Each Story is a task under the Epic.

Project Manager is assigned as the Epic owner.

Stories are randomly assigned to team members.

On Jira Scrum board, these Stories appear under their Epics, ready for sprint planning.

2️⃣ README for this project
# Jira SDLC Automation Script

This Python script automates the creation of Jira Epics and Stories for an entire Software Development Lifecycle (SDLC) using a Scrum template. It automatically assigns the project manager to Epics and randomly distributes Stories among team members.

---

## Features
- Automatically creates **Epics** for each SDLC phase:
  - Requirements Gathering
  - System Design
  - Development
  - Testing
  - Deployment
  - Maintenance
- Creates **Stories** under each Epic.
- Randomly assigns Stories to team members.
- Uses **Jira REST API** for issue creation.
- Fully configurable via `.env` file:
  - Jira credentials
  - Project key
  - Project manager email
  - Team members emails

---

## Prerequisites

- Python 3.11+
- Jira account with API token
- Python libraries:
  - `requests`
  - `python-dotenv`

Install required packages:
```bash
pip install requests python-dotenv

Setup

Clone this repository.

Create a .env file with the following variables:

JIRA_EMAIL=your_email@example.com
JIRA_API_TOKEN=your_api_token
JIRA_BASE_URL=https://yourdomain.atlassian.net
JIRA_PROJECT_KEY=SCRUM
JIRA_BOARD_ID=1
PROJECT_MANAGER_EMAIL=project_manager@example.com
TEAM_MEMBERS_EMAILS=member1@example.com,member2@example.com,member3@example.com

Usage

Run the script:

python jira_sdlc_automation.py


The script will:

Create Epics for each SDLC phase.

Create Stories under each Epic.

Assign Stories randomly to team members.

Success or failure messages will be printed for each issue created.

How it works

Load Environment Variables
Credentials and project info are loaded from .env.

Fetch Jira Account IDs
Converts team member emails into Jira accountIds.

Create Epics
For each SDLC phase, an Epic is created and assigned to the project manager.

Create Stories
For each Story under an Epic:

Assigned randomly to a team member.

Linked to the parent Epic.
