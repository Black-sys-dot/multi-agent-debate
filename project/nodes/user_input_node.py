def get_topic(raw_input: str) -> str:
    if len(raw_input.strip()) < 5:
        raise ValueError("Topic too short")
    return raw_input.strip()
