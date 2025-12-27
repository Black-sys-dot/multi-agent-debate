from utils.llm_client import call_llm

def judge(memory):
    prompt = f"""
    Review this debate:
    {memory}
    Declare a winner first and then justify.
    """
    return call_llm(prompt)
