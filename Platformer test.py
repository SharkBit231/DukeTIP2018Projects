import pygame
####Global contants####
# Colors
BLACK =( 0, 0, 0)
WHITE =(255, 255, 255)
BLUE =(0, 0, 255)
RED =(255, 0, 0)
GREEN =(0, 255, 0)

#Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    #Represents Player

    # -- Attributes
    #Set speed vector of Player
    change_x = 0
    change_y = 0

    # List of sprites we can bump against
    level = None

    # -- Methods
    def __init__(self):
        """Constructor function"""

        #Call the parents Constructor
        pygame.sprite.Sprite.__init__(self)

        width = 40
        height = 60
        self.image = pygame.Surfact([width, height])
        self.image.fill(RED)

        #Set a reference to the image rect.
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the player """
        #gravity
        self.calc_grav()

        #Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit list:
            #IF we are moving right, set right side to left of item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite
                self.rect.left = block.rect.right

        #move up/down
        self.rect.y += self.change_y

        #Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            #Reset our position based on the top/bottom of the object.
            if sef.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0
                self.rect.top = block.rect.bottom
    def calc_grav(self):
        ####calculate effect of gravity
        if self.change_y == 0: # <--- for moving platforms going downward
            self.change_y = 1
        else:
            self.change_y += .35 ## <--- amount of gravity

        #See if we are on the ground (bottom of screen = ground)
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >=0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """ Called when the user hits the 'jump' button"""

        #move down a bit and see if there is a platform below us
        #move down 2 pixels because it doesn't work well if we only move down 1
        #when working with a platform moving down.
        self.rect.y += 2
        platform_hit list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y == 2

        # if it is okay to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:

    # Player-controlled movement:
    def go_left(self):
        """Called when the user hist the left arrow."""
        self.change_x = -6

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6

        ########### TIME STAMP FOR TUTORIAL = 4:51 #############
