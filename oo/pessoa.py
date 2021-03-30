class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=None, sobrenome=None):
        self.nome = nome
        self.idade = idade
        self.sobrenome = sobrenome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"Olá {id(self)}"

    def __str__(self):
        return f"Sr(a) {self.nome}"

    @staticmethod
    def metodo_estatico():
        return 'metodo estatico faz algo aqui sem depender da classe'

    @classmethod
    def metodo_nome_e_atributos_de_classe(cls):
        return f""" ==================================== ATRIBUTO DE CLASSE ===================================== \n
        *metodo que retorna atributos da propria classe*  \n Um exemplo A classe com seu nome:{cls}\n Um atributo da classe: olhos {cls.olhos}
                    \n================================= FIM DE ATRIBUTO DE CLASSE ================================="""


if __name__ == '__main__':
    p = Pessoa(nome='Marcos', idade=45, sobrenome='Viana')
    pessoa_filho = [Pessoa(nome='Layla', idade=21, sobrenome=p.sobrenome), Pessoa(nome='Isabel', idade=19, sobrenome=p.sobrenome)]
    print(Pessoa.cumprimentar(p))
    p.filhos = pessoa_filho
    p.mid_nome = 'Paulo'
    p.olhos = 1
    print(p.__dict__)
    del p.olhos
    del p.mid_nome
    print(p.__dict__)
    for filho in pessoa_filho:
        print(f" filho de {p}: {filho.nome} {filho.sobrenome}, {filho.idade}")
    print(Pessoa.metodo_nome_e_atributos_de_classe())
    print(p.metodo_nome_e_atributos_de_classe())

    print(p, p.idade)
