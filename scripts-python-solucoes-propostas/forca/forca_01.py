# Hangman Game
# Programando Orientado a Objeto
# import
import random

# Board (tabulerio)
board = [
    '''
        >>>>>>>>>>HAGMAN<<<<<<<<<<<
        
        +---+
        |   |
            |
            |
            |
            |
       ===== ===== 
    ''',
    '''
        +---+
        |   |
        0   |
            |
            |
            |
       ===== =====
    ''',
    '''
        +---+
        |   |
        0   |
        |   |
            |
            |
       ===== =====
    ''',
    '''
        +---+
        |   |
        0   |
       /|   |
            |
            |
       ===== =====
    ''',
    '''
        +---+
        |   |
        0   |
       /|\  |
            |
            |
       ===== ===== 
    ''',
    '''
        +---+
        |   |
        0   |
       /|\  |
       /    |
            |
       ===== =====
    ''',
    '''
        +---+
        |   |
        0   |
       /|\  |
       / \  |
            |
       ===== =====
    '''
]

# class
class Hangman:
    #  método construtor
    def __init__(self, word):
        self.word = word
        self.missed_letters = []
        self.guessed_letters = []

    # método para adivinhar letra
    def guess(self, letter):
        if letter in self.word and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
        elif letter not in self.word and letter not in self.missed_letters:
            self.missed_letters.append(letter)
        else:
            return False
        return True

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        return self.hangemn_won() or (len(self.missed_letters) == 6)

    # Método para verificar se o jogador venceu
    def hangemn_won(self):
        if '_' not in self.hide_word():
            return True
        return False

    # Método para não mostrar a letra no board
    def hide_word(self):
        rtn = ''
        for letter in self.word:
            if letter not in self.guessed_letters:
                rtn += '_'
            else:
                rtn += letter
        return rtn

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(board[len(self.missed_letters)])
        print('\nPalavras: '+ self.hide_word())
        print('\nLetras erradas: ',)
        for letter in self.missed_letters:
            print(letter,)
        print()
        print('Letras corretas: ',)
        for letter in self.guessed_letters:
            print(letter,)
        print()

def rand_word():
    '''
        ler a palavra de forma
        aleatória
    '''
    with open('arquivo.txt', 'rt') as file:
        bank = file.readline()
        return bank[random.randint(0, len(bank))].strip()

def main():
    '''
        executa o programa
    '''
    game = Hangman(rand_word())
    # enquanto o jogo não tiver terminado, print do status
    # solicita uma letra e faz a leitura do caracter
    while not game.hangman_over():
        game.print_game_status()
        user_input = input('\nDigite uma letra: ')
        game.guess(user_input)

    # verifica o status do jogo
    game.print_game_status()
    #  De acordo com status imprime na tela para o usuário
    if game.hangemn_won():
        print('\nParabéns! Você venceu!')
    else:
        print('A palavra era '+ game.hide_word())

    #  Executa o programa
    if __name__ == '__main__':
        main()