print("SEJA BEM VINDO À BIBLIOTECA")
        


class Biblioteca:
    armazenamento = {}
    def __init__(self,livro):
        self.livro = livro

    def emprestar_livro(self):
        if self.livro.lower() in self.armazenamento:
            if self.armazenamento[self.livro.lower()]["disponivel"] == True:
                
                self.armazenamento[self.livro.lower()]["disponivel"] = False
                print("Livro emprestado com sucesso")
            
            else:
                print("Esse livro não está disponível!")
        else:
            print("Esse livro não existe!")

    def devolver_livro(self):
        if self.livro.lower() in self.armazenamento:
            if self.armazenamento[self.livro.lower()]["disponivel"] == False:
                self.armazenamento[self.livro.lower()]["disponivel"] = True
                print("Livro devolvido com sucesso!")
            else:
                print("Esse livro não está emprestado")

        else:
            print("Esse livro não existe!")

    def mostrar_biblioteca(self):
        if self.armazenamento:
            for key,value in self.armazenamento.items():
                print(f"{key}: {value}")
        else:
            print("Não existem livros no momento!")


class Livro:
    def __init__(self,titulo,autor,disponivel):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

    def adicionar_livro(self):
        if self.titulo.lower() not in Biblioteca.armazenamento:
            Biblioteca.armazenamento[self.titulo.lower()] = {"autor": self.autor, "disponivel":self.disponivel}
            print("Livro adicionado com sucesso!")
        else:
            print("Esse livro já existe em nosso armazenamento!")


while True:
    

    try:
        menu_biblioteca = int(input("1- Adicionar livro\n2- Emprestar livro\n3- Devolver livro\n4- Mostrar biblioteca\n5- Sair\nEscolha uma das opções: "))

        if menu_biblioteca == 1:
            titulo = input("digite o titulo do livro: ")
            autor = input("digite o autor do livro:")

            livro = Livro(titulo,autor,True)
            livro.adicionar_livro()

        elif menu_biblioteca == 2:
            titulo_emprestar = input("digite o titulo do livro que você deseja usar:")

            livro = Biblioteca(titulo_emprestar)
            livro.emprestar_livro()
        
        elif menu_biblioteca == 3:
            titulo_devolver = input("digite o titulo do livro que deseja devolver:")
            livro_devolver = Biblioteca(titulo_devolver)
            livro_devolver.devolver_livro()

        elif menu_biblioteca == 4:
            biblioteca = Biblioteca("livros")
            biblioteca.mostrar_biblioteca()

        elif menu_biblioteca == 5:
            print("Obrigado por usar nosso sistema de biblioteca!")
            break

        else:
            print("ERRO! Tente novamente utilizando apenas os numeros fornecidos!")

    except ValueError:
        print("Utilize apenas as opções fornecidas")
