from crewai import Agent

class PeopleFlowAgent(Agent):
    def run(self, data: dict):
        """
        Simula il flusso delle persone e calcola la densità e il tasso di flusso.
        """
        total_people = data.get("total_people", 0)
        entrances = data.get("entrances", 1)
        exits = data.get("exits", 1)
        area = data.get("area", 1)

        if area <= 0 or entrances <= 0 or exits <= 0:
            return {"error": "I dati devono essere positivi e maggiori di zero."}

        # Calcoli di esempio
        density = total_people / area
        flow_rate = total_people / (entrances + exits)

        return {
            "density": density,
            "flow_rate": flow_rate,
            "total_people": total_people,
            "entrances": entrances,
            "exits": exits,
            "area": area,
        }

# Creazione dell'agente personalizzato
people_flow_agent = PeopleFlowAgent(
    model="openai:gpt-4",
    role="Simulate and analyze people flow during events.",
    goal="Optimize the number of emergency exits and staff requirements for safety and efficiency.",
    backstory="An AI agent designed to assist in event safety planning using historical and real-time data.",
    system_prompt="Analyze the provided data to simulate people flow and optimize safety measures."
)
