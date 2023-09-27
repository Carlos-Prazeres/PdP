class Document:
    
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

    def list_contents(self):
        return [self.name]

# Sem hierarquia
document1 = Document("documento1.txt", 100)
document2 = Document("documento2.txt", 200)
document3 = Document("planilha.xlsx", 300)

print("Tamanho do documento1:", document1.get_size(), "bytes")
print("Conteúdo do documento1:", document1.list_contents())

documents = [document1, document2, document3]
total_size = sum(doc.get_size() for doc in documents)
print("Tamanho total de documentos:", total_size, "bytes")
