import os
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
try:
    import pygame
    import random
    from tkinter import messagebox
    import pygame.font
    import tkinter as tk
except ModuleNotFoundError as e:
    print(e)
    print("You havent installed Requirements. IF NOT WORK RUN requirements.bat")
    print(bcolors.OKCYAN,"Installing requirements!.....",bcolors.ENDC)
    os.system("pip install -r requirements.txt")
    
print(bcolors.OKBLUE,"WELCOMEEE",bcolors.ENDC)
    

WIDTH, HEIGHT = 400, 400
PADDLE_WIDTH, PADDLE_HEIGHT = 80, 10
BALL_RADIUS = 10
PADDLE_COLOR = (0, 0, 255)
BALL_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)
SCORE = 0
QUESTIONMODE = 1

# Quit Pygame

def quitgame():    
    pygame.quit()

app = tk.Tk()
app.title("Choose Mode")
app.geometry("500x500")

def changeModeEasy():
    global QUESTIONMODE, app
    QUESTIONMODE = 0
    app.quit()

def changeModeNormal():
    global QUESTIONMODE, app
    QUESTIONMODE = 1
    app.quit()

def changeModeHard():
    global QUESTIONMODE, app
    QUESTIONMODE = 2
    app.quit()
    
def exit_app():
    global app
    app.quit()
    quitgame()
    exit()

app.protocol("WM_DELETE_WINDOW",exit_app)

lbl1 = tk.Label(app,text="Choose difficulty")
lbl1.pack()

btnEasy = tk.Button(app,text="Easy", command=changeModeEasy)
btnEasy.pack()

btnNormal = tk.Button(app, text="Normal",command=changeModeNormal)
btnNormal.pack()

btnHard = tk.Button(app,text="Hard",command=changeModeHard)
btnHard.pack()


app.mainloop()


# Initialize Pygame
pygame.init()

# Constants


def restart_game():
    global paddle_x, paddle_y, ball_x, ball_y, SCORE
    ball_x = random.randint(0, WIDTH - BALL_RADIUS)
    ball_y = 0
    SCORE = 0

font = pygame.font.Font(None, 36)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball Game")

# Initial position of the paddle
paddle_x = (WIDTH - PADDLE_WIDTH) // 2
paddle_y = HEIGHT - PADDLE_HEIGHT

# Initial position of the ball
ball_x = random.randint(0, WIDTH - BALL_RADIUS)
ball_y = 0

# Set the speed of the ball
if QUESTIONMODE == 0:
    ball_speed = 0.05
elif QUESTIONMODE == 1:
    ball_speed = 0.1
else:
    ball_speed = 0.2

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Move the paddle with the mouse
    paddle_x, _ = pygame.mouse.get_pos()

    # Move the ball
    ball_y += ball_speed

    # Draw the paddle
    pygame.draw.rect(screen, PADDLE_COLOR, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # Draw the ball
    pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), BALL_RADIUS)

    # Check if the ball is caught by the paddle
    if ball_y + BALL_RADIUS >= paddle_y and paddle_x <= ball_x <= paddle_x + PADDLE_WIDTH:
        SCORE += 1
        ball_y = 0
        ball_x = random.randint(0, WIDTH - BALL_RADIUS)

    #End Game
    if ball_y > paddle_y:
        restart = messagebox.askyesno("GAME OVER", f"YOU DIDNT CATCH THE BALL SCORE: {SCORE}, RESTART?",)
        if restart:
            restart_game()
        else:
            running = False

    score_lb = font.render(f"SCORE: {SCORE}",True,(1,1,1))
    screen.blit(score_lb,(10,10))

    # Update the display
    pygame.display.flip()

# Quit Pygame

pygame.quit()
