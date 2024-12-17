# Agente per simulazioni di flussi
from crewai import SimulationEngine

def simulate_crowd_flow(bim_model):
    engine = SimulationEngine(bim_data=bim_model)
    simulation_results = engine.run()
    return simulation_results