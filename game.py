import pygame

pygame.init()


WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
MAZE_COLOR = (0, 0, 0)  
PLAYER_COLOR = (0, 255, 0)  
GOAL_COLOR = (255, 0, 0) 
BACKGROUND_COLOR = (255, 255, 255)  

MAZE = [
    "####################",
    "#   #        #     #",
    "#   ### #####   ###",
    "#   #  #     #  #  #",
    "#      #  ##  #  #",
    "#   #  #  #    #  #",
    "#   #  #  #  # #  #",
    "#   #  #  #  ##   #",
    "#   #  #  #  #  # #",
    "#   #  #  #     # #",
    "#   #     #  ## # ##",
    "#   #  #       #   #",
    "#   #  ########### #",
    "#   #  #           #",
    "#   #  ########### #",
    "#         #      # #",
    "####################"
]
'''
## you can select any of these mazes

MAZE = [
    "####################",
    "#   #              #",
    "#   #  #######  ###",
    "#   #  #     #  #  #",
    "#   #  #  ##  #  #",
    "#   #  #  #    #  #",
    "#   #  #  #  ###  #",
    "#   #  #  #  #    #",
    "#   #  #  #  #  ###",
    "#   #  #  #       #",
    "#   #  #  #  #######",
    "#   #  #  #        #",
    "#   #  #  ##########",
    "#   #  #           #",
    "#   #  ########### #",
    "#                # #",
    "####################"
]

MAZE = [
    "####################",
    "#        #        #",
    "# ###### # ###### #",
    "# #    # # #    # #",
    "# # #### # #### # #",
    "# #    # #    # # #",
    "# ###### # ###### #",
    "#        #        #",
    "####################"
]

MAZE = [
    "####################",
    "#        #        #",
    "# ## #### ## #### #",
    "# #    #  #    # #",
    "# #####  ##### # #",
    "#     #  #     # #",
    "# ####  #### # # #",
    "#        #    # #",
    "# ######## #### #",
    "#        #    # #",
    "####################"
]

MAZE = [
    "##########",
    "#        #",
    "# ## ## #",
    "# #  # #",
    "# ## ## #",
    "#        #",
    "##########"
]

MAZE = [
    "####################",
    "#        #        #",
    "# ## #### ##    # #",
    "# #    #  # #### # #",
    "# #####  ##### # #",
    "#     #  #     # #",
    "# ####  #### # # #",
    "#        #    # #",
    "# ######## #### #",
    "#        #    # #",
    "####################"
]

MAZE = [
    "############################",
    "#                #        #",
    "# #### ######## ## #### #",
    "# #    #        # #    #",
    "# # #### #### ## #### #",
    "# #    #        # #    #",
    "# ######## #### ########",
    "#        #        #    #",
    "# #### ## #### ## #### #",
    "# #    #        # #    #",
    "# # #### #### ## #### #",
    "# #    #        # #    #",
    "# #### ######## ## #### #",
    "#                #        #",
    "############################"
]
'''
def draw_maze(screen, maze):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == '#':
                pygame.draw.rect(screen, MAZE_COLOR, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def main():
    clock = pygame.time.Clock()

    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("game :: solve the maze")

    
    player_x, player_y = 1, 1 
    goal_x, goal_y = len(MAZE[0]) - 2, len(MAZE) - 2  


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if MAZE[player_y][player_x - 1] != '#':
                player_x -= 1
        if keys[pygame.K_RIGHT]:
            if MAZE[player_y][player_x + 1] != '#':
                player_x += 1
        if keys[pygame.K_UP]:
            if MAZE[player_y - 1][player_x] != '#':
                player_y -= 1
        if keys[pygame.K_DOWN]:
            if MAZE[player_y + 1][player_x] != '#':
                player_y += 1

        
        if player_x == goal_x and player_y == goal_y:
            print("You did it!")
            running = False

       
        screen.fill(BACKGROUND_COLOR)
        draw_maze(screen, MAZE)
        pygame.draw.rect(screen, PLAYER_COLOR, (player_x * GRID_SIZE, player_y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, GOAL_COLOR, (goal_x * GRID_SIZE, goal_y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        pygame.display.flip()

        clock.tick(10)  

    pygame.quit()

if __name__ == "__main__":
    main()
