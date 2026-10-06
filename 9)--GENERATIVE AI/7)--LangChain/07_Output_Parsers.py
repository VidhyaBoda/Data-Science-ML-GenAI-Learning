# 07 - Output Parsers

raw_output = "Python, SQL, Power BI"
skills = [item.strip() for item in raw_output.split(",")]

print("Raw:", raw_output)
print("Parsed:", skills)
print("Type:", type(skills).__name__)
