from utils.llm_client import call_llm
from nodes.memory_node import get_agent_memory
import re


def summarise_response(response):
    summary_prompt = f"Summarise the following response consisely without adding any other information:\n{response}"

    return call_llm(summary_prompt)

def retry_response(response, memory):
    retry_prompt = f"""
    The following response seems repetitive.
    {response}
    Please provide a fresh argument on the same topic.

    Previous discussion:
    {memory}

    """
    return call_llm(retry_prompt)


def semantic_repeat_check(new_text, old_text):
    prompt = f"""
    Compare the following two arguments.
    Are they essentially the same idea?

    A: {old_text}
    B: {new_text}

    Answer only YES or NO.
    """
    result = call_llm(prompt)
    return "yes" in result.lower()


def normalize(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text


def is_repetitive(new_text, agent, threshold=0.8):
    previous_texts=get_agent_memory(agent)
    new_words = set(normalize(new_text).split())

    for old in previous_texts:
        old_words = set(normalize(old).split())
        overlap = len(new_words & old_words) / max(len(new_words), 1)

        if 0.5<overlap<0.8:
            if semantic_repeat_check(new_text, old):
                return True

        if overlap > threshold:
            return True

    return False
