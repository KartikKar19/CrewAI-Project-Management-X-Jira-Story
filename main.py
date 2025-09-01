import os
import yaml
import warnings
import pandas as pd
import json
import matplotlib.pyplot as plt
import itertools
import collections
from helper import load_env, get_openai_api_key
from crew_setup import create_crew

warnings.filterwarnings('ignore')
load_env()
os.environ['OPENAI_MODEL_NAME'] = os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini")

with open("project_config.yaml", "r") as f:
    inputs = yaml.safe_load(f)

crew = create_crew()

try:
    result = crew.kickoff(inputs=inputs)
except Exception as e:
    print("❌ Crew execution failed:", str(e))
    exit(1)

# Usage metrics
prompt_tokens = crew.usage_metrics.prompt_tokens
completion_tokens = crew.usage_metrics.completion_tokens
total_tokens = prompt_tokens + completion_tokens
costs = 0.150 * total_tokens / 1_000_000

print(f"Prompt tokens: {prompt_tokens}")
print(f"Completion tokens: {completion_tokens}")
print(f"Total tokens: {total_tokens}")
print(f"Estimated cost: ${costs:.4f}")

num_tasks = len(result.pydantic.dict().get('tasks', []))
avg_tokens_per_task = total_tokens / num_tasks if num_tasks else 0
print(f"Average tokens per task: {avg_tokens_per_task:.2f}")

num_agents = len(crew.agents) if hasattr(crew, 'agents') else 0
cost_per_agent = costs / num_agents if num_agents else 0
print(f"Cost per agent: ${cost_per_agent:.4f}")

BUDGET = 0.50
if costs > BUDGET:
    print(f"⚠️ Cost (${costs:.4f}) exceeds budget (${BUDGET:.2f})!")
else:
    print(f"✅ Cost (${costs:.4f}) is within budget (${BUDGET:.2f})")

df_usage_metrics = pd.DataFrame([crew.usage_metrics.dict()])
df_usage_metrics

with open("project_plan.json", "w") as f:
    json.dump(result.pydantic.dict(), f, indent=2)
print("Project plan saved to project_plan.json")

tasks = result.pydantic.dict()['tasks']
df_tasks = pd.DataFrame(tasks)
df_tasks.to_csv("tasks.csv", index=False)
print("Tasks saved to tasks.csv")

plt.figure(figsize=(10, 6))
plt.bar(df_tasks['task_name'], df_tasks['estimated_time_hours'], color='skyblue')
plt.xlabel('Task Name')
plt.ylabel('Estimated Hours')
plt.title('Estimated Hours per Task')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('estimated_hours_per_task.png')
plt.close()
print("Bar chart saved to estimated_hours_per_task.png")

resources = list(itertools.chain.from_iterable(df_tasks['required_resources']))
resource_counts = collections.Counter(resources)
plt.figure(figsize=(8, 8))
plt.pie(resource_counts.values(), labels=resource_counts.keys(), autopct='%1.1f%%', startangle=140)
plt.title('Resource Allocation (by mentions)')
plt.tight_layout()
plt.savefig('resource_allocation_pie.png')
plt.close()
print("Pie chart saved to resource_allocation_pie.png")

milestones = result.pydantic.dict()['milestones']
df_milestones = pd.DataFrame(milestones)
df_milestones.to_csv("milestones.csv", index=False)
print("Milestones saved to milestones.csv")
