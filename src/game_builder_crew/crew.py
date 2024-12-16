from typing import List
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class GameBuilderCrew():
    """GameBuilder crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self, llm):
        self.custom_llm = llm

    @agent
    def senior_engineer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['senior_engineer_agent'], # type: ignore
            allow_delegation=False,
            verbose=True,
            llm=self.custom_llm
        ) # type: ignore
    
    @agent
    def qa_engineer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['qa_engineer_agent'], # type: ignore
            allow_delegation=False,
            verbose=True,
            llm=self.custom_llm
        ) # type: ignore
    
    @agent
    def chief_qa_engineer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['chief_qa_engineer_agent'], # type: ignore
            allow_delegation=True,
            verbose=True,
            llm=self.custom_llm
        ) # type: ignore
    

    @task
    def code_task(self) -> Task:
        return Task(
            config=self.tasks_config['code_task'], # type: ignore
            agent=self.senior_engineer_agent(),
            output_file='generated_game.py' 
        ) # type: ignore

    @task
    def review_task(self) -> Task:
        return Task(
            config=self.tasks_config['review_task'], # type: ignore
            agent=self.qa_engineer_agent(),
            #### output_json=ResearchRoleRequirements
        ) # type: ignore

    @task
    def evaluate_task(self) -> Task:
        return Task(
            config=self.tasks_config['evaluate_task'], # type: ignore
            agent=self.chief_qa_engineer_agent()
        ) # type: ignore

    @crew
    def crew(self) -> Crew:
        """Creates the GameBuilderCrew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator # type: ignore
            tasks=self.tasks,  # Automatically created by the @task decorator # type: ignore
            process=Process.sequential,
            verbose=True, 
        )