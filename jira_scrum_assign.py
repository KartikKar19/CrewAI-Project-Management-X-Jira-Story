import random
import requests

import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

# Load secrets from .env file (never hardcode secrets in code or push them to GitHub)
load_dotenv()
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
JIRA_BASE_URL = os.getenv("JIRA_BASE_URL",)
PROJECT_KEY = os.getenv("JIRA_PROJECT_KEY")
BOARD_ID = int(os.getenv("JIRA_BOARD_ID", "1"))

auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)
HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}


# Validate required secrets and config
if not all([JIRA_EMAIL, JIRA_API_TOKEN, JIRA_BASE_URL, PROJECT_KEY]):
    raise EnvironmentError("One or more Jira credentials or settings are missing in .env")

# Load project manager and team members from .env
PROJECT_MANAGER = os.getenv("PROJECT_MANAGER_EMAIL")
TEAM_MEMBERS = [email.strip() for email in os.getenv("TEAM_MEMBERS_EMAILS", "").split(",") if email.strip()]
if not PROJECT_MANAGER or not TEAM_MEMBERS:
    raise EnvironmentError("PROJECT_MANAGER_EMAIL or TEAM_MEMBERS_EMAILS missing or empty in .env")

# SDLC Phases -> Scrum Epics
SDLC_PHASES = [
    "Requirements Gathering",
    "System Design",
    "Development",
    "Testing",
    "Deployment",
    "Maintenance"
]

# Example stories for each phase
STORIES = {
    "Requirements Gathering": ["Interview stakeholders", "Document requirements", "Review approval"],
    "System Design": ["Create UML diagrams", "Database schema design", "Architecture review"],
    "Development": ["Frontend implementation", "Backend APIs", "Integrate DB"],
    "Testing": ["Unit testing", "Integration testing", "Bug fixing"],
    "Deployment": ["CI/CD pipeline", "Deploy to staging", "Deploy to production"],
    "Maintenance": ["Monitor system", "Patch bugs", "Feature updates"]
}

def get_account_id(email):
    """Fetch the Atlassian accountId for a given email."""
    url = f"{JIRA_BASE_URL}/rest/api/3/user/search?query={email}"
    response = requests.get(url, auth=auth, headers=HEADERS)
    if response.status_code == 200:
        users = response.json()
        if users:
            return users[0]["accountId"]
    print(f"❌ Could not find accountId for {email}")
    return None

def create_issue(project_key, summary, issue_type, assignee_email, epic_key=None):
    """Create a Jira issue (Epic/Story/Task)."""
    account_id = get_account_id(assignee_email)
    url = f"{JIRA_BASE_URL}/rest/api/3/issue"
    data = {
        "fields": {
            "project": {"key": project_key},
            "summary": summary,
            "issuetype": {"name": issue_type}
        }
    }
    if account_id:
        data["fields"]["assignee"] = {"id": account_id}
    if epic_key:
        data["fields"]["parent"] = {"key": epic_key}
    response = requests.post(url, auth=auth, headers=HEADERS, json=data)
    if response.status_code == 201:
        issue_key = response.json()["key"]
        print(f"✅ Created {issue_type}: {summary} → {issue_key} (assigned to {assignee_email})")
        return issue_key
    else:
        print(f"❌ Failed to create {issue_type}: {summary}")
        print(response.text)
        return None

def main():
    project_key = "SCRUM"  # Replace with your Jira Scrum project key

    # Step 1: Create Epics for each SDLC phase
    epic_keys = {}
    for phase in SDLC_PHASES:
        epic_key = create_issue(project_key, phase, "Epic", PROJECT_MANAGER)
        if epic_key:
            epic_keys[phase] = epic_key

    # Step 2: Create Stories under each Epic, assign randomly to team
    for phase, stories in STORIES.items():
        for story in stories:
            assignee = random.choice(TEAM_MEMBERS)
            create_issue(project_key, story, "Story", assignee, epic_keys.get(phase))

if __name__ == "__main__":
    main()
