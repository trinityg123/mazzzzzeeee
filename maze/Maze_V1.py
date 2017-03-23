# Imports//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
import pygame
import math

# Initialize game engine///////////////////////////////////////////////////////////////////////////////////////////////////////////////
pygame.init()


# Window//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
HEIGHT = 700
WIDTH = 1275
SIZE = (WIDTH, HEIGHT)
TITLE = "MAZE"

pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode(SIZE)

# Timer//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
clock = pygame.time.Clock()
refresh_rate = 60


# maze image to be deleted later*****************************************************************************************************
maze = pygame.image.load("mazeDiagram.jpg")
maze = pygame.transform.scale(maze, [WIDTH, HEIGHT])


# Colors//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
GRAY = (191, 191, 191)
GREEN = (0, 51, 0)
BLACK = (0, 0, 0)
CREAM = (153, 102, 51)

    
# walls man//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
wall1 = [0, 0, 25, 700] #outside walls
wall2 = [0, 0, 1300, 25]
wall3 = [0, 675, 1300, 25]
wall4 = [1250, 0, 25, 325]
wall5 = [1250, 350, 25, 325]

wall6 = [50, 50, 25, 600] # left insides barrier

wall7 = [75, 350, 200, 25] #left upper curl
wall8 = [75, 50, 275, 25]

wall9 = [75, 625, 300, 25]
wall10 = [350, 50, 25, 125]

wall11 = [100, 100, 25, 225]
wall12 = [125, 100, 200, 25]
wall13 = [150, 150, 225, 25]

wall14 = [400, 50, 200, 25] # left upper curl
wall15 = [575, 75, 25, 100]
wall16 = [400, 100, 150, 25]
wall17 = [400, 125, 25, 50]
wall18 = [425, 150, 175, 25]

wall19 = [150, 200, 25, 125] # left start of upper snake
wall20 = [175, 200, 50, 25]
wall21 = [200, 200, 25, 125]
wall22 = [250, 200, 25, 125]
wall23 = [300, 200, 25, 125]
wall24 = [350, 200, 25, 125]
wall25 = [400, 200, 25, 125]
wall26 = [450, 200, 25, 125]
wall27 = [500, 200, 25, 125]
wall28 = [550, 200, 25, 125]
wall29 = [600, 200, 25, 125]
wall30 = [650, 200, 25, 125]
wall31 = [700, 200, 25, 125]
wall32 = [750, 200, 25, 125]
wall33 = [800, 200, 25, 125]
wall34 = [850, 200, 25, 125]
wall35 = [900, 200, 25, 125]
wall36 = [950, 200, 25, 125]
wall37 = [1000, 200, 25, 125]
wall38 = [1050, 200, 25, 125]
wall39 = [1100, 200, 25, 125] # end of upper snake walls

wall40 = [275, 200, 25, 25] # upper snake connectors
wall41 = [375, 200, 25, 25]
wall42 = [475, 200, 25, 25]
wall43 = [575, 200, 25, 25]
wall44 = [675, 200, 25, 25]
wall45 = [775, 200, 25, 25]
wall46 = [875, 200, 25, 25]
wall47 = [975, 200, 25, 25]
wall48 = [1075, 200, 25, 25]
wall49 = [225, 300, 25, 25]
wall50 = [325, 300, 25, 25]
wall51 = [425, 300, 25, 25]
wall52 = [525, 300, 25, 25]
wall53 = [625, 300, 25, 25]
wall54 = [725, 300, 25, 25]
wall55 = [825, 300, 25, 25]
wall56 = [925, 300, 25, 25]
wall57 = [1025, 300, 25, 25] # end of upper snake

wall58 = [1200, 50, 25, 600] # right inside barrier
wall59 = [1000, 350, 200, 25]
wall60 = [300, 350, 675, 25]

wall61 = [1150, 100, 25, 225]

wall62 = [900, 50, 300, 25] # right upper curl
wall63 = [900, 75, 25, 100]
wall64 = [925, 150, 200, 25]
wall65 = [950, 100, 200, 25]

wall66 = [675, 50, 200, 25]
wall67 = [675, 75, 25, 100]
wall68 = [700, 150, 175, 25]
wall69 = [850, 100, 25, 50]
wall70 = [725, 100, 125, 25]

wall71 = [625, 50, 25, 125] # upper  middle wall

wall72 = [625, 525, 25, 125]

wall73 = [900, 625, 325, 25]
wall74 = [400, 625, 200, 25]
wall75 = [675, 625, 200, 25]

walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12,
         wall13, wall14, wall15, wall16, wall17, wall18, wall19, wall20, wall21, wall22, wall23, wall24,
         wall25, wall26, wall27, wall28, wall29, wall30, wall31, wall32, wall33, wall34, wall35, wall36,
         wall37, wall38, wall39, wall40, wall41, wall42, wall43, wall44, wall45, wall46, wall47, wall48,
         wall49, wall50, wall51, wall52, wall53, wall54, wall55, wall56, wall57, wall58, wall59, wall60,
         wall61, wall62, wall63, wall64, wall65, wall66, wall67, wall68, wall69, wall70, wall71, wall72,
         wall73, wall74, wall75]




# Game loop/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # Game logic (Check for collisions, update points, etc.)
     

    # Drawing code (Describe the picture. It isn't actually drawn yet.)
            # x, y, width, length

    # draw *************************************************************************************************************************
    screen.fill(GRAY)
    screen.blit(maze, (0, 0))   

    
    
    # grid   
    for y in range(0, HEIGHT, 25):
        pygame.draw.line(screen, BLACK, [0, y], [WIDTH, y])

    for x in range(0, WIDTH, 25):
        pygame.draw.line(screen, BLACK, [x, 0], [x, HEIGHT])


    # draw wall loop
    for w in walls:
        pygame.draw.rect(screen, GREEN, w)
    

    # Update window
    pygame.display.update()
    clock.tick(refresh_rate)


# Close window and quit//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
pygame.quit()
