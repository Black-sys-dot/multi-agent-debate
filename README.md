# Multi-Agent Debate System

This project implements a structured multi-agent debate system where two AI agents engage in a controlled discussion over a given topic. The system enforces turn-taking, maintains memory, prevents repetition, and produces a final judgment based on the full debate.

---

## Overview

The system simulates a debate between two agents (e.g., Scientist and Philosopher).  
Each agent responds in alternating turns, with the system ensuring:

- Strict turn order  
- Memory-aware responses  
- Repetition detection  
- Structured logging  
- Final judgment generation  

All components are modular and designed to reflect a clean multi-agent architecture.

---

## Project Structure

```
project/
├── nodes/
│   ├── agent_node.py
│   ├── controller_node.py
│   ├── memory_node.py
│   ├── judge_node.py
│   ├── logger_node.py
│   └── user_input_node.py
│
├── config/
│   └── personas.py
│
├── logs/
│   └── debate_log_<timestamp>.json
│
├── tests/
│   └── test_memory.py
│
├── generate_dag.py
├── run_debate.py

```


---

## How It Works

1. The user provides a debate topic.
2. The controller initializes two agents.
3. Agents take turns responding to the topic.
4. Each response is checked for repetition and stored in memory.
5. All interactions are logged with timestamps.
6. After all rounds, a judge evaluates the debate and declares a winner.

---

## Requirements

### Software Requirements
- Python 3.9 or higher
- pip (Python package manager)

### Python Dependencies
Install required packages using:

pip install -r requirements.txt

---


## Running the Program

Run the system using:

```bash
python run_debate.py