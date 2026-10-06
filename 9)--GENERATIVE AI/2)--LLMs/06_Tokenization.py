"""06 - Tokenization"""

def simple_token_view(text):
    # This is only a teaching example, not a real LLM tokenizer.
    tokens = text.split()
    print("Text:", text)
    print("Simple whitespace tokens:", tokens)
    print("Token count:", len(tokens))

simple_token_view("Generative AI is changing software development.")

print("\nReal LLM tokenizers are more sophisticated.")
print("A token can be a word, part of a word, punctuation, or another subword unit.")
