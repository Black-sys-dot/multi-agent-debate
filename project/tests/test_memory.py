from nodes.memory_node import (
    init_agent_memory,
    add_turn,
    add_agent_turn,
    get_memory,
    get_agent_memory
)

def test_memory_system():
    # setup
    init_agent_memory(["Scientist", "Philosopher"])

    # simulate debate
    add_turn(1, "Scientist", "AI should be regulated.")
    add_agent_turn("Scientist", "AI should be regulated.")

    add_turn(2, "Philosopher", "Regulation harms innovation.")
    add_agent_turn("Philosopher", "Regulation harms innovation.")

    # assertions
    memory = get_memory()

    assert len(memory["turns"]) == 2
    assert memory["turns"][0]["agent"] == "Scientist"
    assert memory["turns"][1]["agent"] == "Philosopher"

    assert get_agent_memory("Scientist")[0] == "AI should be regulated."
    assert get_agent_memory("Philosopher")[0] == "Regulation harms innovation."

    print("TEST PASSED — memory system works correctly")

if __name__ == "__main__":
    test_memory_system()
