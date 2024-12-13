from crewai import Agent
from models.emergency_exit import EmergencyExitInput, EmergencyExitOutput

emergency_exit_agent = Agent(
    model="openai:gpt-4",
    deps_type=EmergencyExitInput,
    result_type=EmergencyExitOutput,
    system_prompt="Calculate optimal emergency exits for a given scenario."
)
