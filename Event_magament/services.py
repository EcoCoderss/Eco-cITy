from agents.crowd_agent import simulate_crowd_flow
from agents.emergency_agent import simulate_emergency_scenario

def run_simulations(bim_model):
    crowd_results = simulate_crowd_flow(bim_model)
    emergency_results = simulate_emergency_scenario(bim_model)
    return {
        "crowd": crowd_results,
        "emergency": emergency_results
    }