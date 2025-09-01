flowchart TD
    %% Project Node
    PROJECT[Project: SCRUM]

    %% Epics (SDLC Phases)
    REQ[Requirements Gathering (Epic)]
    DESIGN[System Design (Epic)]
    DEV[Development (Epic)]
    TEST[Testing (Epic)]
    DEPLOY[Deployment (Epic)]
    MAINT[Maintenance (Epic)]

    %% Connect Epics to Project
    PROJECT --> REQ
    PROJECT --> DESIGN
    PROJECT --> DEV
    PROJECT --> TEST
    PROJECT --> DEPLOY
    PROJECT --> MAINT

    %% Requirements Gathering Stories
    REQ1[Interview stakeholders]
    REQ2[Document requirements]
    REQ3[Review approval]

    REQ --> REQ1
    REQ --> REQ2
    REQ --> REQ3

    %% System Design Stories
    DES1[Create UML diagrams]
    DES2[Database schema design]
    DES3[Architecture review]

    DESIGN --> DES1
    DESIGN --> DES2
    DESIGN --> DES3

    %% Development Stories
    DEV1[Frontend implementation]
    DEV2[Backend APIs]
    DEV3[Integrate DB]

    DEV --> DEV1
    DEV --> DEV2
    DEV --> DEV3

    %% Testing Stories
    TEST1[Unit testing]
    TEST2[Integration testing]
    TEST3[Bug fixing]

    TEST --> TEST1
    TEST --> TEST2
    TEST --> TEST3

    %% Deployment Stories
    DEP1[CI/CD pipeline]
    DEP2[Deploy to staging]
    DEP3[Deploy to production]

    DEPLOY --> DEP1
    DEPLOY --> DEP2
    DEPLOY --> DEP3

    %% Maintenance Stories
    MAINT1[Monitor system]
    MAINT2[Patch bugs]
    MAINT3[Feature updates]

    MAINT --> MAINT1
    MAINT --> MAINT2
    MAINT --> MAINT3

    %% Optional: you can show assignees in parentheses or as labels
    %% Example: REQ1["Interview stakeholders (John Doe)"]


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
