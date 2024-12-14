from crewai import Agent
from models.emergency_exit import EmergencyExitInput, EmergencyExitOutput


# Definizione dell'agente emergency_exit_agent
emergency_exit_agent = Agent(
    role="Emergency Exit Planner",  # Specifica il ruolo dell'agente
    goal="Optimize emergency exit usage for safety during evacuation.",
    backstory="The agent has expertise in crowd management and evacuation scenarios.",
    model="openai:gpt-4"
)