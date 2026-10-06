# 23 - Mini LangChain-Style Application

def prompt_template(topic):
    return f"Explain {topic} in three practical points."

def model(prompt):
    return f"MODEL RESPONSE -> {prompt}"

def output_parser(response):
    return {"raw_response": response, "status": "parsed"}

def chain(topic):
    return output_parser(model(prompt_template(topic)))

print(chain("LangChain"))
print("Composable flow: Prompt Template -> Model -> Output Parser")
