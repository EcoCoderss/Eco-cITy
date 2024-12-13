from crewai import Agent
from models.staff_estimation import StaffEstimationInput, StaffEstimationOutput

staff_estimation_agent = Agent(
    model="openai:gpt-4",
    deps_type=StaffEstimationInput,
    result_type=StaffEstimationOutput,
    system_prompt="Estimate the public staff required for a given event."
)
