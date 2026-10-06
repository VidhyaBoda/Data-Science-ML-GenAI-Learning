# 12 - Document Loaders

class Document:
    def __init__(self, page_content, metadata=None):
        self.page_content = page_content
        self.metadata = metadata or {}

class TextLoader:
    def __init__(self, text):
        self.text = text

    def load(self):
        return [Document(self.text, {"source": "example.txt"})]

docs = TextLoader("LangChain can load documents into a common document representation.").load()

for doc in docs:
    print(doc.page_content)
    print(doc.metadata)
