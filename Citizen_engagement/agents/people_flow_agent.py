
from crewai import Agent

people_flow_agent = Agent(
    model="openai:gpt-4",
    role="Simulate and analyze people flow during events.",
    goal="Optimize the number of emergency exits and staff requirements for safety and efficiency.",
    backstory="An AI agent designed to assist in event safety planning using historical and real-time data.",
    system_prompt="Analyze the provided data to simulate people flow and optimize safety measures."
)
