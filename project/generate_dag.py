from graphviz import Digraph

def create_dag():
    dot = Digraph("Debate_System", format="png")

    dot.attr(rankdir="TB", size="8,10")

    # Nodes
    dot.node("User", "User Input")
    dot.node("Controller", "Controller\n(run_debate)")
    dot.node("Agent", "Agent\n(agent_response)")
    dot.node("Memory", "Memory\n(add_turn / get_memory)")
    dot.node("Logger", "Logger\n(log_event)")
    dot.node("Judge", "Judge\n(judge)")

    # Edges
    dot.edge("User", "Controller")
    dot.edge("Controller", "Agent")
    dot.edge("Agent", "Memory")
    dot.edge("Memory", "Logger")
    dot.edge("Logger", "Judge")

    return dot


if __name__ == "__main__":
    dag = create_dag()
    dag.render("dag", cleanup=True)
    print("DAG generated as dag.png")
