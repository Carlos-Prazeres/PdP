from abc import ABC, abstractmethod

class Component(ABC):
  
    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def list_contents(self):
        pass

class File(Component):
  
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

    def list_contents(self):
        return [self.name]

class Folder(Component):
    def __init__(self, name):
        self.name = name
        self.contents = []

    def get_size(self):
        total_size = sum(item.get_size() for item in self.contents)
        return total_size

    def list_contents(self):
        contents = [self.name + '/']
        for item in self.contents:
            contents.extend(['  ' + name for name in item.list_contents()])
        return contents

    def add(self, component):
        self.contents.append(component)

    def remove(self, component):
        self.contents.remove(component)

# Criando a hierarquia de pastas e documentos
folder1 = Folder("Pasta A")
folder1.add(File("documento1.txt", 100))
folder1.add(File("documento2.txt", 200))

subfolder = Folder("Subpasta")
subfolder.add(File("planilha.xlsx", 300))
folder1.add(subfolder)

# Calculando o tamanho total e listando conteúdos
print("Tamanho total da Pasta A:", folder1.get_size(), "bytes")
print("Conteúdo da Pasta A:")
for item in folder1.list_contents():
    print(item)
