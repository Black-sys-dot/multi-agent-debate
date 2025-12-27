from nodes.controller_node import run_debate
from nodes.user_input_node import get_topic

if __name__ == "__main__":
    topic = input("Enter debate topic: ")
    topic=get_topic(topic)
    run_debate(topic)
