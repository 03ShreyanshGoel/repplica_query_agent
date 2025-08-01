# def is_query_valid(query):
#     invalid_examples = ["walk my pet", "add apples to grocery", "buy milk"]
#     # Simple rule-based check for demo purposes:
#     if any(phrase in query.lower() for phrase in invalid_examples) or "," in query:
#         return False
#     if len(query.strip()) < 3:
#         return False
#     return True


# import logging

# logger = logging.getLogger("validator")

# def is_query_valid(query):
#     invalid_examples = ["walk my pet", "add apples to grocery", "buy milk"]
#     if any(phrase in query.lower() for phrase in invalid_examples) or "," in query:
#         logger.info(f"Query marked invalid by phrase check: {query}")
#         return False
#     if len(query.strip()) < 3:
#         logger.info(f"Query too short, invalid: {query}")
#         return False
#     logger.debug(f"Query is valid: {query}")
#     return True

import logging
import re

logger = logging.getLogger("validator")

INTERROGATIVE_WORDS = {
    "who", "what", "when", "where", "why", "how",
    "is", "are", "do", "does", "can", "will", "could", "should", "would"
}
COMPARATORS = {
    "best", "worst", "top", "highest", "lowest", "cheapest",
    "fastest", "biggest", "smallest", "recommend", "rated", "review"
}

MULTI_COMMAND_PATTERN = re.compile(r"[,\.;]| and | then | also ", re.IGNORECASE)

MIN_QUERY_LENGTH = 3

def is_query_valid(query: str) -> bool:
    query_stripped = query.strip().lower()

    if len(query_stripped) < MIN_QUERY_LENGTH:
        logger.info(f"Query too short, invalid: {query}")
        return False

    # Reject queries with multiple commands or clauses
    if MULTI_COMMAND_PATTERN.search(query):
        logger.info(f"Query contains multiple commands or clauses: {query}")
        return False

    # Accept if query contains any question mark anywhere
    if "?" in query_stripped:
        logger.debug(f"Query contains question mark, valid: {query}")
        return True

    # Accept if query starts with interrogative or auxiliary verbs
    first_word = query_stripped.split()[0] if query_stripped else ""
    if first_word in INTERROGATIVE_WORDS:
        logger.debug(f"Query starts with interrogative/auxiliary word, valid: {query}")
        return True

    # Accept if query contains any comparator word
    if any(comp in query_stripped.split() for comp in COMPARATORS):
        logger.debug(f"Query contains comparator keyword, valid: {query}")
        return True

    logger.info(f"Query does not appear to be a question, comparator-based query, or valid query: {query}")
    return False
