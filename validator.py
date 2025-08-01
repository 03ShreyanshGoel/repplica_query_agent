def is_query_valid(query):
    invalid_examples = ["walk my pet", "add apples to grocery", "buy milk"]
    # Simple rule-based check for demo purposes:
    if any(phrase in query.lower() for phrase in invalid_examples) or "," in query:
        return False
    if len(query.strip()) < 3:
        return False
    return True
