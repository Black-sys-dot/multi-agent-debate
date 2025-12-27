from utils.llm_client import call_llm
from config.personas import PERSONAS

def agent_response(agent_name, topic, memory):
    persona= PERSONAS[agent_name]
    prompt = f"""
You are a {persona['role']}.
Your tone should be {persona['tone']}.
Your style should be {persona['style']}.
Debate topic: {topic}
Previous discussion:
{memory}

Respond with just your next argument , without any additional commentary.
"""
    return call_llm(prompt)
