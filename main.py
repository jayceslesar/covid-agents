import os
from PIL import Image
import room as Room
import pygame
import sys
from pygame.locals import *
from pygame.rect import *
import csv
import json
import time

params_to_use = 'sim_params.json'
with open(params_to_use) as f:
    sim_params = json.load(f)

SCREEN, CLOCK = None, None
FAN_CYCLES = sim_params['FAN_CYCLES']


def draw(room, step):
    for x, i in enumerate(range(room.num_rows)):
        for y, j in enumerate(range(room.num_cols)):
            rect = pygame.Rect(y*height_per_block, x*height_per_block,
                               height_per_block, height_per_block)

            global SCREEN
            pygame.draw.rect(SCREEN, room.grid[i][j].get_color(), rect)
            if room.grid[i][j].sink:
                sink_img = pygame.image.load(os.path.join('images', 'sink.png'))
                fan_img = pygame.transform.scale(sink_img, (height_per_block, height_per_block))
                SCREEN.blit(fan_img, rect)
            if room.grid[i][j].agent is not None:
                pygame.draw.rect(SCREEN, room.grid[i][j].agent.get_color(), rect, 4)
                color_string = room.grid[i][j].agent.get_color_string()
                file_name = os.path.join('images', color_string + '_agent.png')
                agent_img = pygame.image.load(file_name)
                agent_img = pygame.transform.scale(agent_img, (height_per_block-2, height_per_block-2))
                SCREEN.blit(agent_img, rect)
            if room.grid[i][j].source:
                factor = FAN_CYCLES / 4
                if step % FAN_CYCLES < factor:
                    fan_img = pygame.image.load(os.path.join('images', 'fan1.png'))
                elif step % FAN_CYCLES < factor * 2:
                    fan_img = pygame.image.load(os.path.join('images', 'fan2.png'))
                elif step % FAN_CYCLES < factor * 3:
                    fan_img = pygame.image.load(os.path.join('images', 'fan3.png'))
                else:
                    fan_img = pygame.image.load(os.path.join('images', 'fan4.png'))
                fan_img = pygame.transform.scale(fan_img, (height_per_block, height_per_block))
                SCREEN.blit(fan_img, rect)


def viz(room):
    data_path = input("What would you like to name the data file? ")
    choice = input('do you want screenshots?\n')
    if choice == 'y':
        stills = []
        path = input("What folder do you want to save your screenshots into? Please specify the path \n")
        skip = int(input("How many steps between screenshots? \n"))
        os.makedirs(path, exist_ok=True)

    pygame.init()
    global SCREEN, CLOCK
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    steps_taken = 0
    while room.steps_taken < room.iterations:
        room._step()
        draw(room, steps_taken)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        if choice == 'y' and room.steps_taken % skip == 0:
            screenshot(SCREEN, path, room.steps_taken)
            stills.append(os.path.join(path, "step" + str(room.steps_taken) + ".png"))

        steps_taken += 1
        # time.sleep(.1)
    room.write_data(data_path)
        # pygame.quit()

    if choice == 'y':
        img, *imgs = [Image.open(f) for f in stills]
        img.save(fp=os.path.join(path, data_path+".png"), format='PNG', append_images=imgs, save_all=True, duration=20, loop=0)
        for im in stills:
            os.remove(im)


def screenshot(screen, path, step):
    title = "step" + str(step)
    file_save_as = os.path.join(path, title + ".png")
    pygame.image.save(screen, file_save_as)
    print(f"step {step} has been screenshotted")


BLACK = (0, 0, 0)
WINDOW_HEIGHT = sim_params['WINDOW_HEIGHT']
WINDOW_WIDTH = sim_params['WINDOW_WIDTH']
room = Room.Room(sim_params)

height_per_block = WINDOW_HEIGHT // room.num_rows
width_per_block = WINDOW_WIDTH // room.num_cols

if __name__ == '__main__':
    viz(room)
