# Power BI implementation checklist.
power_bi_steps = [
    "Load cleaned data",
    "Create star-schema model where appropriate",
    "Create Date table",
    "Create DAX measures",
    "Add slicers and drill-through",
    "Build KPI cards",
    "Add trend and category visuals",
    "Add tooltip pages",
    "Validate totals against source data",
    "Publish and document refresh assumptions",
]
for i, step in enumerate(power_bi_steps, 1):
    print(f"{i:02}. {step}")
