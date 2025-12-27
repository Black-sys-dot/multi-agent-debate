memory = {
    "turns": []
}

agents_memory={}

def add_turn(round_no, agent, text):
    memory["turns"].append({
        #"round": round_no,
        "agent": agent,
        "text": text
    })

def get_memory():
    return memory

def init_agent_memory(agent_names):
    global agents_memory
    agents_memory = {name: [] for name in agent_names}

def add_agent_turn(agent_name , text):
    agents_memory[agent_name].append(text)

def get_agent_memory(agent_name):
    return agents_memory[agent_name]
