import sys
import random
import pygame
import time

"""     TASKS
Here you guys are going to create a Magic 8 Ball.
Below I have provided a template for the control flow
of the program but it is up to you to develop the core functionality.

 At the least, your magic 8 ball should have a button that will display
 a randomly selected response from the list of responses given below.
 and you are welcome to change the responses.
 All necessary tasks are given as TODOs below. Have Fun!
"""


"""     CHALLENGES
- Center the button
- Fill make button function definition so that it can make a button given x, y coordinates with text on the button.
- Allow make button to take in parameters for the size of the button
- Generate Response by accepting text input from the user

"""


########  GLOBAL VARIABLES  ################
pygame.init()

responses = ["Step on me.", "YAINT", "Speak up, dumbass", "That sounds epic",  "You're mum gae", "Coughfefe haha", "What does your heart say?"]
WHITE = (255, 255, 255)
screen_width = 820
screen_height =  480


screen = pygame.display.set_mode((screen_width,screen_height), 0, 32) # Resolution == width and height
pygame.display.set_caption("Epic 8 Button")
mouse_pos = pygame.mouse.get_pos()

mainButton = pygame.Rect(300, 150, 200, 200)



def make_Button(x, y, buttonText):
    # TODO: Make generic code for creating a Button (Optional)
    """Note a button can simply be a shape drawn to the screen
    that you will eventually detect a collision with"""
    pass





########   Displays the screen and magic 8 ball button
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Get the mouse position when mouse is clicked
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = event.pos




    # Randomly displays a response if mouse is clicked within the central button
    """Here you'll notice that this block of code will continue getting run.
            This is because the mouse_pos will always equal the position that it was
            set to in the if block above unless the user clicks somewhere else.
            Is there anything that you can do to mouse_pos here to prevent it from
            saying the user is still clicking the button?"""

    if mainButton.collidepoint(mouse_pos):

        #TODO: Select one of the responses in the list responese at random. (Required)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print(random.choice(responses))
        mouse_pos = (1000, 1000)
        #TODO: Display Response to Screen (Required)
        #print('button was pressed at {0}'.format(mouse_pos))




    # Draw Magic Button To Screen.
    mainButton.center = (screen_width/2, screen_height/2)
    pygame.draw.rect(screen, WHITE, mainButton)

    pygame.display.update()
