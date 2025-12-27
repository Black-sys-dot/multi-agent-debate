from config.settings import ROUNDS, AGENTS
from nodes.agent_node import agent_response
from nodes.memory_node import add_turn, get_memory,init_agent_memory, add_agent_turn
from nodes.logger_node import log_event
from nodes.summarise_node import summarise_response, is_repetitive, retry_response
from nodes.judge_node import judge
import random

def process_turn(round_no,agent,topic):

    #log_event(f"Round {round_no} started by {agent}")

    memory = get_memory()
    response = agent_response(agent, topic, memory)
    if is_repetitive(response, agent):
        response = retry_response(response, memory)
        if is_repetitive(response,agent):
            response = "I have no point to add at this time."

    print(f"{agent}: {response}")     # Added to see progress

    add_turn(round_no, agent, summarise_response(response))  # Summarising as after 6-7 turns memory explodes and model throws error
    add_agent_turn(agent, response) 

    log_event({
        "round": round_no,
        "agent": agent,
        "text": response,
        "memory-snapshot": get_memory()
    })



def run_debate(topic):
    persons = AGENTS
    init_agent_memory(persons)

    log_event(f"Debate started on topic: {topic}")
    print(f"Starting debate between {persons[0]} and {persons[1]} ....")

    first = random.choice(persons)   # Just for fairness
    second = persons[1] if first == persons[0] else persons[0]

    for round_no in range(1, ROUNDS + 1):
        agent = first if round_no % 2 == 1 else second

        print(f"[Round{round_no}] ",end="")

        process_turn(round_no, agent, topic)    

    log_event("Debate ended.")
    winner = judge(get_memory())
    log_event(f"Winner determined: {winner}")
    print(f"[Judge] : {winner}")
