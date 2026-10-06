# Basic reconciliation example.
source_total = 125000
dashboard_total = 125000

if source_total == dashboard_total:
    print("PASS: dashboard total matches source.")
else:
    print("FAIL: investigate reconciliation difference.")
