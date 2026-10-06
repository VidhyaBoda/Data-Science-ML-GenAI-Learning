# 10 - Sequential Workflows

def clean(text):
    return " ".join(text.strip().split())

def summarize(text):
    return text[:80] + ("..." if len(text) > 80 else "")

def format_result(text):
    return f"SUMMARY:\n{text}"

input_text = "   LangChain helps developers compose language model application components.   "
print(format_result(summarize(clean(input_text))))
