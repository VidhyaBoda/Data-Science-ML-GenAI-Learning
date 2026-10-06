# UI/UX quality checklist for portfolio dashboards.
checklist = {
    "Hierarchy": "Most important KPIs are visually dominant",
    "Consistency": "Same units, fonts, labels, and spacing",
    "Filters": "Filters are purposeful and easy to reset",
    "Accessibility": "Readable contrast and non-color cues",
    "Performance": "Avoid unnecessary high-cardinality visuals",
    "Trust": "Show data period and source/methodology",
}
for k, v in checklist.items():
    print(f"{k}: {v}")
