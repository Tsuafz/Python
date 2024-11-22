import turtle
import time
import random

delay = 0.1

def validate_name(name):

    if isinstance(name, str) and 0 <= len(name) <= 5:
        return True
    else:
        return False

def get_player_name():
    while True:
        name = turtle.textinput("Nombre", "Ingrese nombre (Maximo 5 letras): ")
        if validate_name(name):
            return name
        else:
            turtle.textinput("Error", "Nombre inválido. Ingrese un nombre de 0 a 5 letras.")

# Puntuación
score = 0
high_score = 0
high_score_player = ""
current_player_name = get_player_name()

# Dificultad
difficulty_level = 1
last_score_check = 0

# Pantalla
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

# Cabeza de la serpiente
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Comida de la serpiente
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Puntaje de {} : {}  Puntaje maximo: {} por {}".format(current_player_name, score, high_score, high_score_player), align="center", font=("Courier", 14, "normal"))

# Funciones
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def restart_game():
    global score, high_score, delay, segments
    score = 0
    delay = 0.1
    
    for segment in segments:
        segment.goto(1000, 1000) 
    segments.clear()  
    
    head.goto(0, 0)  
    head.direction = "stop"  
    
    pen.clear() 
    pen.write("Puntaje de {} : {}  Puntaje maximo: {} por {}".format(current_player_name, score, high_score, high_score_player), align="center", font=("Courier", 14, "normal"))

def leave_game():
    wn.bye()     

def change_segments_color_to_yellow():
    for segment in segments:
        segment.color("yellow")

# Función para dibujar la cuadrícula
def draw_grid():
    grid_pen = turtle.Turtle()
    grid_pen.speed(0)
    grid_pen.color("lightgrey")
    grid_pen.penup()
    grid_pen.hideturtle()

    # Dibuja líneas verticales
    for x in range(-290, 300, 20):
        grid_pen.goto(x, 250)
        grid_pen.setheading(270)  # Apunta hacia abajo
        grid_pen.pendown()
        grid_pen.goto(x, -300)
        grid_pen.penup()

    # Dibuja líneas horizontales
    for y in range(-290, 270, 20):
        grid_pen.goto(-290, y)
        grid_pen.setheading(0)  # Apunta hacia la derecha
        grid_pen.pendown()
        grid_pen.goto(300, y)
        grid_pen.penup()

def setup_keybindings():
    wn.listen()
    wn.onkeypress(go_up, "Up")
    wn.onkeypress(go_up, "w")
    wn.onkeypress(go_up, "W")
    wn.onkeypress(go_down, "Down")
    wn.onkeypress(go_down, "s")
    wn.onkeypress(go_down, "S")
    wn.onkeypress(go_left, "Left")
    wn.onkeypress(go_left, "a")
    wn.onkeypress(go_left, "A")
    wn.onkeypress(go_right, "Right")
    wn.onkeypress(go_right, "d")
    wn.onkeypress(go_right, "D")
    wn.onkeypress(restart_game, "r")
    wn.onkeypress(restart_game, "R")
    wn.onkeypress(leave_game, "Q")  
    wn.onkeypress(leave_game, "q")  

def prompt_new_name():
    global current_player_name
    current_player_name = get_player_name()
    restart_game()
    setup_keybindings()   

# Llama a la función para dibujar la cuadrícula
draw_grid()        

# Teclas
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_up, "w")
wn.onkeypress(go_up, "W")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_down, "S")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_left, "A")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_right, "D")
wn.onkeypress(restart_game, "r")
wn.onkeypress(restart_game, "R")
wn.onkeypress(leave_game, "Q")  
wn.onkeypress(leave_game, "q")  

# Bucle principal del juego
while True:
    wn.update()

    # Revisa alguna colisión con los bordes de la zona jugable
    if head.xcor() > 270 or head.xcor() < -270 or head.ycor() > 220 or head.ycor() < -270:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Esconde los segmentos
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Limpia la lista de segmentos
        segments.clear()

        # Reinicia el puntaje
        score = 0

        # Reinicia el retraso
        delay = 0.1

        pen.clear()
        pen.write("Puntaje de {} : {}  Puntaje maximo: {} por {}".format(current_player_name, score, high_score, high_score_player), align="center", font=("Courier", 14, "normal")) 
        prompt_new_name()

    # Revisa alguna colisión con la comida
    if head.distance(food) < 20:
        # Mueve la comida a una posición aleatoria
        x = random.randint(-270, 270)
        y = random.randint(-270, 220)
        food.goto(x, y)

        # Añade un nuevo segmento a la serpiente
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Reduce el retraso
        delay -= 0.001

        # Aumenta la puntuación
        score += 10

    if score > high_score:
        high_score = score
        high_score_player = current_player_name
        change_segments_color_to_yellow() # Cambiar segmentos a amarillo

    if score // 50 > last_score_check // 50:  # Revisa si cruzamos un multiplo de 50
        difficulty_level += 1
        delay -= 0.01  # Incrementa la velocidad
        last_score_check = score  # Actualiza la variable 
        pen.clear()
        pen.write("Puntaje de {} : {}  Puntaje maximo: {} por {}".format(current_player_name, score, high_score, high_score_player), align="center", font=("Courier", 14, "normal"))

    pen.clear() 
    pen.goto(0, 260)  
    pen.write("Puntaje de {} : {}  Puntaje maximo: {} por {}".format(current_player_name, score, high_score, high_score_player), align="center", font=("Courier", 14, "normal"))

    # Mueve los segmentos desde el último en reversa para seguir el movimiento de la serpiente
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Mueve el segmento 0 a la posición donde está la cabeza de la serpiente
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()    

    # Revisa alguna colisión con el cuerpo de la serpiente
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
        
            # Esconde los segmentos
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Limpia la lista de segmentos
            segments.clear()

            # Reinicia la puntuación
            score = 0

            # Reinicia el retraso
            delay = 0.1
        
            # Actualiza la pantalla de puntuación
            pen.clear()
            pen.write("Puntaje de {} : {}  Puntaje maximo: {} por {}".format(current_player_name, score, high_score, high_score_player), align="center", font=("Courier", 14, "normal"))
            prompt_new_name()

    time.sleep(delay)
wn.mainloop()