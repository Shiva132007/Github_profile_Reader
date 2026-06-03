import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	ScrapeWebsiteTool
)






@CrewBase
class GithubProfileProfessionalAnalyzerCrew:
    """GithubProfileProfessionalAnalyzer crew"""

    
    @agent
    def senior_github_profile_analyst_and_technical_recruiter(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["senior_github_profile_analyst_and_technical_recruiter"],
            
            
            tools=[				ScrapeWebsiteTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    

    
    @task
    def comprehensive_github_profile_analysis_with_actionable_suggestions(self) -> Task:
        return Task(
            config=self.tasks_config["comprehensive_github_profile_analysis_with_actionable_suggestions"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the GithubProfileProfessionalAnalyzer crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,

            chat_llm=LLM(model="openai/gpt-4o-mini"),
        )


