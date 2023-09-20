
class Aluno:
    def __init__(self, ra, nome):
        self.ra = ra
        self.nome = nome

    def imprimir_info(self):
        print(f"RA: {self.ra}")
        print(f"Nome: {self.nome}")


class MeuAluno(Aluno):
    def verifica_ra(self):
        meu_ra = "N019395"
        if self.ra == meu_ra:
            print("Este RA pertence a você!")
        else:
            print("Este RA não pertence a você.")

ra_inserido = input("Insira seu RA: ")
nome_inserido = input("Insira seu nome: ")


meu_aluno = MeuAluno(ra_inserido, nome_inserido)


meu_aluno.imprimir_info()


meu_aluno.verifica_ra()
