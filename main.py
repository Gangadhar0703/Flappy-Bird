import pyttsx3 as py
from random import randint
WIDTH=700 
HEIGHT=600
game_over=False
score = 0
bird_crash=False

bird=Actor("bird")
pole1=Actor("pole1")
pole2=Actor("pole2")
pole3=Actor("pole3")
pole4=Actor("pole4")
pole5=Actor("pole5")
pole6=Actor("pole6")

def reset_game():
    global bird, pole1, pole2, pole3, pole4,game_over,score
    game_over=False
    score=0

    bird.pos=100, 120
    pole1.pos=350, 520
    pole2.pos=350, -20
    pole3.pos=600, 500
    pole4.pos=600, -50
    pole5.pos=800, 600
    pole6.pos=800, 50

reset_game()

def draw():
    screen.clear()

    if game_over:       
        screen.fill("red")
        screen.draw.text(f"GAME OVER! Your Score is {score}!", color="white", center=((WIDTH/2)-10, (HEIGHT/2)-100), fontsize=(60))
        screen.draw.text("Press 'A' to Play Again.", color="white", center=(WIDTH/2, HEIGHT/2), fontsize=(40))

    else:
        screen.fill("lightblue")
        bird.draw()
        pole1.draw()
        pole2.draw()
        pole3.draw()
        pole4.draw()
        pole5.draw()
        pole6.draw()
        screen.draw.text("Score: " + str(int(score)), color="black", topleft=(10, 0))

def crash():
    global game_over
    game_over=True

def update():
    global bird_crash
    global game_over
    global score

    a,b = pole1.pos
    c,d = pole2.pos
    e,f = pole3.pos
    g,h = pole4.pos
    i,j = pole5.pos
    k,l = pole6.pos

    if score <= 105:
        pole1.pos=a - 2, b
        pole2.pos=c - 2, d
        pole3.pos=e - 2, f
        pole4.pos=g - 2, h
        pole5.pos=i - 2, j
        pole6.pos=k - 2, l

        x, y = bird.pos
        bird.pos = x, y + 2.5

        if keyboard.space:
            bird.y=bird.y-4.5

    if pole1.x < -15:
        gap_y = randint(150, HEIGHT - 150)
        pole1.y = gap_y + 300
        pole2.y = gap_y - 300
        pole1.x = WIDTH + 300
        pole2.x = WIDTH + 300

    if pole3.x < -20:
        gap_y = randint(150, HEIGHT - 150)
        pole3.y = gap_y + 300
        pole4.y = gap_y - 300
        pole3.x = WIDTH + 300
        pole4.x = WIDTH + 300

    if pole5.x < -30:
        gap_y = randint(150, HEIGHT - 150)
        pole5.y = gap_y + 300
        pole6.y = gap_y - 300
        pole5.x = WIDTH + 300
        pole6.x = WIDTH + 300

    if score >= 105:
        pole1.pos=a - 3.5, b
        pole2.pos=c - 3.5, d
        pole3.pos=e - 3.5, f
        pole4.pos=g - 3.5, h
        pole5.pos=i - 3.5, j
        pole6.pos=k - 3.5, l

        x, y = bird.pos
        bird.pos = x, y + 2.5

        if keyboard.space:
           bird.y=bird.y-5.5

    if pole1.x < -15:
        gap_y = randint(150, HEIGHT - 150)
        pole1.y = gap_y + 275
        pole2.y = gap_y - 275
        pole1.x = WIDTH + 500
        pole2.x = WIDTH + 500

    if pole3.x < -20:
        gap_y = randint(150, HEIGHT - 150)
        pole3.y = gap_y + 275
        pole4.y = gap_y - 275
        pole3.x = WIDTH + 500
        pole4.x = WIDTH + 500

    if pole5.x < -30:
        gap_y = randint(150, HEIGHT - 150)
        pole5.y = gap_y + 275
        pole6.y = gap_y - 275
        pole5.x = WIDTH + 500
        pole6.x = WIDTH + 500

    if score >= 200:
        pole1.pos=a - 4, b
        pole2.pos=c - 4, d
        pole3.pos=e - 4, f
        pole4.pos=g - 4, h
        pole5.pos=i - 4, j
        pole6.pos=k - 4, l

        x, y = bird.pos
        bird.pos = x, y + 3.25

        if keyboard.space:
           bird.y=bird.y-6

    if pole1.x < -15:
        gap_y = randint(150, HEIGHT - 150)
        pole1.y = gap_y + 250
        pole2.y = gap_y - 250
        pole1.x = WIDTH + 400
        pole2.x = WIDTH + 400

    if pole3.x < -20:
        gap_y = randint(150, HEIGHT - 150)
        pole3.y = gap_y + 250
        pole4.y = gap_y - 250
        pole3.x = WIDTH + 400
        pole4.x = WIDTH + 400

    if pole5.x < -30:
        gap_y = randint(150, HEIGHT - 150)
        pole5.y = gap_y + 250
        pole6.y = gap_y - 250
        pole5.x = WIDTH + 500
        pole6.x = WIDTH + 500


    if pole1.pos and pole2.pos < bird.pos:
        score+=1/6.6

    if pole3.pos and pole4.pos < bird.pos:
        score+=1/6.6

    if pole5.pos and pole6.pos < bird.pos:
        score+=1/6.6

    if game_over:
        score=(int(score))

    if bird.y <= 0 or bird.y >= HEIGHT:
        crash()

    bird_crash=bird.colliderect(pole1) or bird.colliderect(pole2) or \
    bird.colliderect(pole3) or bird.colliderect(pole4) or \
    bird.colliderect(pole5) or bird.colliderect(pole6)

    if bird_crash:
        crash()
        
    if game_over and keyboard.a:
        reset_game()

    if game_over:
        voice()

def voice():
        engine=py.init()
        engine.say(f"Game Over! Your score is {score}")
        engine.runAndWait()
        return()