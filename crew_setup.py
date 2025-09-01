import yaml
from crewai import Agent, Task, Crew
from models import ProjectPlan

def load_agents_tasks():
    files = {
        'agents': 'agents.yaml',
        'tasks': 'tasks.yaml'
    }
    configs = {}
    for config_type, file_path in files.items():
        with open(file_path, 'r') as file:
            configs[config_type] = yaml.safe_load(file)
    return configs['agents'], configs['tasks']

def create_crew():
    agents_config, tasks_config = load_agents_tasks()
    project_planning_agent = Agent(config=agents_config['project_planning_agent'])
    estimation_agent = Agent(config=agents_config['estimation_agent'])
    resource_allocation_agent = Agent(config=agents_config['resource_allocation_agent'])

    task_breakdown = Task(config=tasks_config['task_breakdown'], agent=project_planning_agent)
    time_resource_estimation = Task(config=tasks_config['time_resource_estimation'], agent=estimation_agent)
    resource_allocation = Task(config=tasks_config['resource_allocation'], agent=resource_allocation_agent, output_pydantic=ProjectPlan)

    crew = Crew(
        agents=[project_planning_agent, estimation_agent, resource_allocation_agent],
        tasks=[task_breakdown, time_resource_estimation, resource_allocation],
        verbose=True
    )
    return crew
