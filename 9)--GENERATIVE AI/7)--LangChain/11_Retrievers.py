# 11 - Retrievers

documents = [
    "LangChain provides tools for LLM application development.",
    "Retrievers select relevant documents for a query.",
    "Agents can choose tools dynamically."
]

def retrieve(query, docs, k=2):
    query_terms = set(query.lower().split())
    scored = []
    for doc in docs:
        terms = set(doc.lower().replace(".", "").split())
        scored.append((len(query_terms & terms), doc))
    return [doc for score, doc in sorted(scored, reverse=True)[:k] if score > 0]

for doc in retrieve("retrievers relevant documents", documents):
    print("-", doc)
