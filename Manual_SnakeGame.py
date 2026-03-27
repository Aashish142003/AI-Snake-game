import pygame, random, sys
from pygame.locals import *

# Initialize Pygame
pygame.init()
s = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

# Fonts
font_large = pygame.font.SysFont('Arial', 50)
font_medium = pygame.font.SysFont('Arial', 30)
font_small = pygame.font.SysFont('Arial', 20)

def collide(x1, x2, y1, y2, w1, w2, h1, h2):
    if x1 + w1 > x2 and x1 < x2 + w2 and y1 + h1 > y2 and y1 < y2 + h2:
        return True
    return False

def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    s.blit(img, (x, y))

def start_screen():
    while True:
        s.fill((255, 255, 255))
        draw_text('SNAKE GAME', font_large, (255, 0, 0), 160, 200)
        draw_text('Press SPACE to Start', font_medium, (0, 0, 0), 175, 300)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    return

def game_over_screen(score):
    while True:
        s.fill((255, 255, 255))
        draw_text('GAME OVER', font_large, (255, 0, 0), 165, 200)
        draw_text(f'Score: {score}', font_medium, (0, 0, 0), 250, 280)
        draw_text('Press R to Retry or Q to Quit', font_small, (0, 0, 0), 185, 350)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    return True
                if event.key == K_q:
                    return False

def game_loop():
    xs = [290, 290, 290, 290, 290]
    ys = [290, 270, 250, 230, 210]
    dirs = 0 # 0: down, 1: right, 2: up, 3: left
    score = 0
    applepos = (random.randint(0, 580), random.randint(0, 580))
    
    appleimage = pygame.Surface((10, 10))
    appleimage.fill((0, 255, 0))
    img = pygame.Surface((20, 20))
    img.fill((255, 0, 0))

    while True:
        clock.tick(15)
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()
            elif e.type == KEYDOWN:
                if (e.key == K_UP or e.key == K_w) and dirs != 0: dirs = 2
                elif (e.key == K_DOWN or e.key == K_s) and dirs != 2: dirs = 0
                elif (e.key == K_LEFT or e.key == K_a) and dirs != 1: dirs = 3
                elif (e.key == K_RIGHT or e.key == K_d) and dirs != 3: dirs = 1

        # Check collision with self
        for i in range(2, len(xs)):
            if collide(xs[0], xs[i], ys[0], ys[i], 20, 20, 20, 20):
                return score

        # Check collision with apple
        if collide(xs[0], applepos[0], ys[0], applepos[1], 20, 10, 20, 10):
            score += 1
            xs.append(700)
            ys.append(700)
            applepos = (random.randint(0, 580), random.randint(0, 580))

        # Check boundaries
        if xs[0] < 0 or xs[0] > 580 or ys[0] < 0 or ys[0] > 580:
            return score

        # Move bodies
        for i in range(len(xs) - 1, 0, -1):
            xs[i] = xs[i-1]
            ys[i] = ys[i-1]
        
        # Move head
        if dirs == 0: ys[0] += 20
        elif dirs == 1: xs[0] += 20
        elif dirs == 2: ys[0] -= 20
        elif dirs == 3: xs[0] -= 20

        # Draw
        s.fill((255, 255, 255))
        for i in range(len(xs)):
            s.blit(img, (xs[i], ys[i]))
        s.blit(appleimage, applepos)
        draw_text(f'Score: {score}', font_small, (0, 0, 0), 10, 10)
        pygame.display.update()

def main():
    start_screen()
    while True:
        score = game_loop()
        if not game_over_screen(score):
            break
    pygame.quit()

if __name__ == '__main__':
    main()
