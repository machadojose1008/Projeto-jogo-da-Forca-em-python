# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe

class Hangman:

    # Construtor
    def __init__(self, word):
        self.word = list(word)
        #print("A palavra é: ") usados no teste do programa
        #print(self.word)
        self.revelado = ['_'] * len(word) # Criação da lista do tamanho da palavra com as letras escondidas
        self.historico_certas = []
        self.historico_erradas = []

    # Método para revelar as letras que forem acertadas
    def hide_word(self, acerto):
        for i in range(0, len(self.word)):
            if self.word[i] == acerto:
                self.revelado[i] = acerto
        print(self.revelado)


    # Método de teste da letra
    def guess(self, letter):
        count = 0
        for i in self.word:
            if i == letter:
                print("Letra correta!\n")
                self.hide_word(letter) # Envio para o método imprimir as letras que já foram encontradas
                self.historico(letter, 'Certa') # Envia para o método imprimir o histórico de letras tentadas
                count += 1
        if count == 0:
            print("Letra Incorreta!\n")
            self.historico(letter, 'Errada')


    # Método para mostrar as últimas letras tentadas
    def historico(self, letra, identificador):
        if identificador == 'Certa' and letra not in self.historico_certas:
            self.historico_certas.append(letra)
        if identificador == 'Errada' and letra not in self.historico_erradas:
            self.historico_erradas.append(letra)
        print('Letras Corretas: %s' %self.historico_certas)
        print('Letras Erradas: %s' %self.historico_erradas)


    # Método para imprimir o board na tela
    def print_game_status(self):
        # Imprime a posição atual da lista do board
        print(board[len(self.historico_erradas)])


    # Método para verificar se o jogo terminou
    def hangman_over(self):
        # Faz a verificação se a pessoa venceu (hangman.won == true) ou se o tamanho da lista de letras erradas chegou a 6
        # Se a lista chegar a 6 o jogo encerra e faz um último teste para verificar se a pessoa venceu
        return self.hangman_won() or (len(self.historico_erradas) == 6)


    # Método para verificar se o jogo foi ganho
    def hangman_won(self):
        if '_' not in self.revelado:
            return True
        return False


# Funcao para gerar uma palavra aleatoria a partir da lista
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()

def main():
    # Instanciando o objeto
    game = Hangman(rand_word())

    # Função para executar o código enquanto o jogo não estiver concluído

    while not game.hangman_over():
        game.print_game_status()
        letra = input("Digite a letra: ")
        game.guess(letra)
        # Verifica o status do jogo

    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print("\nParabéns você venceu")
    else:
        print("\nPerdeu, que pena")
# Executa o programa

if __name__ == "__main__":
    main()