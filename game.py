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
