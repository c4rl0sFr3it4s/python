# Game Ping-Pong

from tkinter import *   # modulo para gráfico
import random           # módulo de randomização do processador
import time             # módulo para tempo, data

level = int(input("Qual nível você gostaria de jogar? 1/2/3/4/5 \n")) # entrada de valor inteiro no sistema
length = 500/level # variável length, sendo atribuido a divisão de 500, por level.


root = Tk() # variável root, recebendo uma instancia da função TK()
root.title("Ping Pong") # objeto root setando o título
root.resizable(0,0) # objeto root modificando a primeira letra para maiuscula
root.wm_attributes("-topmost", -1) # objeto root utilizando o metodo wm_attributes, com 2 argumentos

canvas = Canvas(root, width=800, height=600, bd=0,highlightthickness=0) # variável canvas recebendo uma instancia de Canvas, com args
canvas.pack() # objeto canvas, utilizando o metodo pack()

root.update() # objeto root, atualizando

count = 0 # variavel count sendo atribuido 0
lost = False # variavel lost sendo atribuido um valor boolean false

class Bola: # idealizando uma classe
    def __init__(self, canvas, Barra, color): # incializando da funcao da classe, com argumentos
        self.canvas = canvas # atributo da classe Bola
        self.Barra = Barra # atributo da classe Bola
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color) # atributo da classe Bola, recebendo objeto canvas, utilizando metodo create
        self.canvas.move(self.id, 245, 200) # atributo da classe canvas, metodo move, recebendo como argumentos id

        starts_x = [-3, -2, -1, 1, 2, 3] # lista de inteiros
        random.shuffle(starts_x) # utilizando o modulo random.shuffle, embaralhando os valores

        self.x = starts_x[0] # atributo do eixo x, recebendo a lista no indice[0]
        self.y = -3 # atributo do eixo y, recebendo numero inteiro

        self.canvas_height = self.canvas.winfo_height() # atributo canvas_height recebendo canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width() # atribuito canvas_width recebendo canvas.winfo_widrh()


    def draw(self): # funcao draw
        self.canvas.move(self.id, self.x, self.y) # atributo canvas.move, recebendo argumentos id, x, y 

        pos = self.canvas.coords(self.id) # variavel pos, recebendo objeto canvas.coords

        if pos[1] <= 0: # estrutura de decisão se pos[0] for menor e igual a 0
            self.y = 3

        if pos[3] >= self.canvas_height:
            self.y = -3

        if pos[0] <= 0:
            self.x = 3
            
        if pos[2] >= self.canvas_width:
            self.x = -3

        self.Barra_pos = self.canvas.coords(self.Barra.id)


        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2]: # estrutura de decisão se pos[2] for maior e igual a, and E, operador lógico
            if pos[3] >= self.Barra_pos[1] and pos[3] <= self.Barra_pos[3]:
                self.y = -3
                global count # definindo uma variável global
                count +=1 # atribuindo mais um ao contador
                score() # chamando a função score()


        if pos[3] <= self.canvas_height: # estrutura de decisao se pos[3] for menor e igual a canvas_height
            self.canvas.after(10, self.draw)
        else: # senao 
            game_over() # chamando a funcao game_over()
            global lost # definindo uma variável global
            lost = True # atribuindo um boolean para mudar o valor lógico de lost


class Barra: # nova classe Barra
    def __init__(self, canvas, color): # inicio da classe Barra
        self.canvas = canvas # atributos da classe
        self.id = canvas.create_rectangle(0, 0, length, 10, fill=color) # atributo id, recebendo objeto canvas
        self.canvas.move(self.id, 200, 400) # objeto canvas.move()

        self.x = 0 # atributo x, sendo atribuido 0

        self.canvas_width = self.canvas.winfo_width() # atributo canvas_windth, recebendo objeto da funcao canvas.winfo_width()

        self.canvas.bind_all("<KeyPress-Left>", self.move_left) # objeto canvas.bind_all, recebendo 2 argumentos
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

    def draw(self): # funcao draw
        self.canvas.move(self.id, self.x, 0) # objeto canvas.move, recebendo o argumento id, x

        self.pos = self.canvas.coords(self.id) # atributo pos, recebendo objeto canvas.coords

        if self.pos[0] <= 0: # estrutura de decusao se, pos[0] for menor ou igual a 0
            self.x = 0 # self.x vai receber 0
        
        if self.pos[2] >= self.canvas_width:
            self.x = 0
        
        global lost # variável global lost
        
        if lost == False: # estrutura de decisão se, lost for igual a False
            self.canvas.after(10, self.draw)# self.canvas.after, vai receber os argumentos, 10, self.draw

    def move_left(self, event):# funcao mover para esquerda dentro da classe Barra
        if self.pos[0] >= 0:
            self.x = -3

    def move_right(self, event):# funcao mover para a direita dentro da classe Barra
        if self.pos[2] <= self.canvas_width:
            self.x = 3


def start_game(event): # funcao inicio do game na classe Bola
    global lost, count # declarando variavel global
    lost = False # declarando uma váriavel local de escopo
    count = 0 # declarando uma váriavel local de escopo
    score() # chamando a funcao score()
    canvas.itemconfig(game, text=" ") # objeto canvas, com o arqumento game, text=" "

    time.sleep(1) # definindo um tempo para dormir em modulo time
    Barra.draw() # objeto Barra desenhar
    Bola.draw() # objeto Bola desenhar


def score(): # funcao score, 
    canvas.itemconfig(score_now, text="Pontos: " + str(count))

def game_over():# funcao game over
    canvas.itemconfig(game, text="Game over!")


Barra = Barra(canvas, "orange")
Bola = Bola(canvas, Barra, "purple")


score_now = canvas.create_text(430, 20, text="Pontos: " + str(count), fill = "green", font=("Arial", 16))
game = canvas.create_text(400, 300, text=" ", fill="red", font=("Arial", 40))


canvas.bind_all("<Button-1>", start_game)

root.mainloop()