import turtle
import os


tela=turtle.Screen()
tela.title("Jogo com Turtle")
tela.bgcolor("green")
tela.setup(width=800,height=600)
tela.tracer(0)

#barra A
barra_A=turtle.Turtle()
barra_A.speed(0)
barra_A.shape('square')
barra_A.color('black')
barra_A.shapesize(stretch_wid=5,stretch_len=1)
barra_A.penup()
barra_A.goto(-350,0)

#barra B
barra_B=turtle.Turtle()
barra_B.speed(0)
barra_B.shape('square')
barra_B.color('black')
barra_B.shapesize(stretch_wid=5,stretch_len=1)
barra_B.penup()
barra_B.goto(350,0)

#bola
bola=turtle.Turtle()
bola.speed(0)
bola.shape('square')
bola.color('black')
bola.penup()
bola.goto(0,0)
#adicionando o movimento
bola.dx=0.4
bola.dy=0.4


#atribuindo pontuação
pontuacao_A=0
pontuacao_B=0

#desenhando o placar
placar=turtle.Turtle()
placar.speed()
placar.color("black")
placar.penup()
placar.hideturtle()
placar.goto(0,260)
placar.write("Papai: {} vs Gianluca: {}".format(pontuacao_A,pontuacao_B),align="center",font=("Courier",24,"normal"))

#funções para os movimentos

#cima
def barra_A_cima():
    y = barra_A.ycor()
    y=y+20
    barra_A.sety(y)

#baixo
def barra_A_baixo():
    y = barra_A.ycor()
    y=y-20
    barra_A.sety(y)

#cima
def barra_B_cima():
    y = barra_B.ycor()
    y=y+20
    barra_B.sety(y)

#baixo
def barra_B_baixo():
    y = barra_B.ycor()
    y=y-20
    barra_B.sety(y)

#recebendo dados do teclado
tela.listen()
tela.onkeypress(barra_A_cima,"w")
tela.onkeypress(barra_A_baixo,"s")
tela.onkeypress(barra_B_cima,"Up")
tela.onkeypress(barra_B_baixo,"Down")

#loop principal
while True:
    tela.update()

    #adicionando o movimento da bola
    bola.setx(bola.xcor()+bola.dx)
    bola.sety(bola.ycor()+bola.dy)

    #definindo as bordas da imagem
    if bola.ycor()>290:
        bola.sety(290)
        #reverte o movimento
        bola.dy=bola.dy*-1

    #definindo as bordas da imagem
    if bola.ycor()<-290:
        bola.sety(-290)
        #reverte o movimento
        bola.dy=bola.dy*-1

    #definindo as bordas da imagem
    if bola.xcor()>390:
        bola.goto(0,0)
        #reverte o movimento
        bola.dx=bola.dx*-1
        pontuacao_A=pontuacao_A+1
        placar.clear()
        placar.write("GOOOOOOOOOOOLLLLLLL Flavio: {} vs Gianluca: {}".format(pontuacao_A,pontuacao_B),align="center",font=("Courier",24,"normal"))

    #definindo as bordas da imagem
    if bola.xcor()<-390:
        bola.goto(0,0)
        #reverte o movimento
        bola.dx=bola.dx*-1
        pontuacao_B=pontuacao_B+1
        placar.clear()
        placar.write("Papai Flavio: {} vs GOOOOOOOOOOOLLLLLLL Gianluca: {}".format(pontuacao_A,pontuacao_B),align="center",font=("Courier",24,"normal"))
        
    #quando a bola atinge a barra do jogador    
    if (bola.xcor()>340 and bola.xcor()<350) and (bola.ycor() < barra_B.ycor() +40 and bola.ycor()> barra_B.ycor() - 40):
        bola.setx(340)
        bola.dx=bola.dx*-1

    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < barra_A.ycor() +40 and bola.ycor()> barra_A.ycor() -40):
        bola.setx(-340)
        bola.dx=bola.dx*-1
