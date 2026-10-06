# Match evaluation metrics to the project.
metrics = {
    "classification": ["accuracy", "precision", "recall", "F1"],
    "retrieval": ["Recall@K", "Precision@K", "MRR"],
    "generation": ["groundedness", "relevance", "faithfulness"],
    "dashboard": ["data accuracy", "refresh reliability", "decision usefulness"],
}
for project_type, values in metrics.items():
    print(f"{project_type}: {', '.join(values)}")
