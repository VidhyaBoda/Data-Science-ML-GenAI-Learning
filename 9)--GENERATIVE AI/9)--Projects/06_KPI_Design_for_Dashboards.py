# KPI design: each KPI should answer a business question.
kpis = {
    "Total Revenue": "How much revenue was generated?",
    "Orders": "How many orders were completed?",
    "Average Order Value": "What is the average value per order?",
    "Unique Customers": "How many customers purchased?",
    "Repeat Customer Rate": "How strong is customer retention?",
}
for name, question in kpis.items():
    print(f"{name}: {question}")
