'''
Aqui será abordado: Classe, Métodos e Atributos.

Classe:
*É um molde de instruções contendo um motivo central com sub-propriedades e métodos para chamadas de aplicação;
*É a base da orientação a objetos;
*Define a forma como objetos python se comportam;
*Cada propriedade e método interno podem serem chamados individualmente;
*É definido com iniciais maiúsculas e CamelCase;
*Precisa ser instanciada para aplicação;
*Ela deve ser dinâmica.

Mais sobre classe:
https://www.youtube.com/embed/cV_Soy7jGns
https://www.youtube.com/embed/gtgI7PC_TJk
https://www.youtube.com/watch?v=j6B8shHXzks
https://pt.wikipedia.org/wiki/Classe_(programa%C3%A7%C3%A3o)

Métodos:
*Métodos são funções construidas e pertencentes a uma classe.
*Cada função ou método contém suas próprias funcionalidade.
*Os métodos devem conter a palavra chave "Self" como primeiro parâmetro, sendo isolado ou não.

Artigo sobre o uso do Self: http://archive.is/cX2mq
'''


'Criando uma classe e definindo métodos e atributos:'
# Usar Camel Case em caso de duas palavras.


class Pessoa:
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p)) # Modo errado.
    print(id(p))
    print(p.cumprimentar()) # Modo correto.


