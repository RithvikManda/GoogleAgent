from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool



@CrewBase
class LatestAiDevelopment():

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'
	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			verbose=True,
			# tools=[SerperDevTool()]
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			verbose=True
		)
	@agent
	def resoure_asset(self) -> Agent:
		return Agent(
			config=self.agents_config['resoure_asset'],
			# tools=[SerperDevTool()],
			verbose=True
		)
	

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
		)
	@task
	def resoure_asset_task(self) -> Task:
		return Task(
			config=self.tasks_config['resoure_asset_task'],
			output_file='report.md'
		)
	


	@crew
	def crew(self) -> Crew:
		return Crew(
			agents=self.agents, 
			tasks=self.tasks, 
			process=Process.sequential,
			verbose=True,
		)
			
