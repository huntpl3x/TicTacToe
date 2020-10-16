import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

def changeGrid(xClick, yClick, player):
    sizeBtwn = width // rows
    i = 2
    j = 2
    if xClick < sizeBtwn - 1:
        i = 0
    if xClick > sizeBtwn + 1 and xClick < sizeBtwn*2 - 1:
        i = 1
    if yClick < sizeBtwn - 1:
        j = 0
    if yClick > sizeBtwn + 1 and yClick < sizeBtwn*2 - 1:
        j = 1
    if grid[j][i] == 'n':
        grid[j][i] = player
        return True
    return False

def checkWin():
    for row in range(rows):
        countX = 0
        countO = 0
        for coulmn in range(rows):
            if grid[row][coulmn] == 'x':
                countX += 1
                countO = 0
            elif grid[row][coulmn] == 'o':
                countO += 1
                countX = 0
            else:
                countX = 0
                countO = 0
            if countX == 3:
                return 'x'
            if countO == 3:
                return 'o'

    for coulmn in range(rows):
        countX = 0
        countO = 0
        for row in range(rows):
            if grid[row][coulmn] == 'x':
                countX += 1
                countO = 0
            elif grid[row][coulmn] == 'o':
                countO += 1
                countX = 0
            else:
                countX = 0
                countO = 0
            if countX == 3:
                return 'x'
            if countO == 3:
                return 'o'

    if grid[0][0] == grid[1][1] and grid[0][0] == grid[2][2] and grid[0][0] != 'n':
        if grid[0][0] == 'x':
            return 'x'
        if grid[0][0] == 'o':
            return 'o'
    if grid[2][0] == grid[1][1] and grid[0][2] == grid[2][0] and grid[2][0] != 'n':
        if grid[2][0] == 'x':
            return 'x'
        if grid[2][0] == 'o':
            return 'o'
    if grid[0].count('n') + grid[1].count('n') + grid[2].count('n') == 0 and firstRound == False:
        return 't'
    return 'n'

def drawX(surface):
    sizeBtwn = width // rows

    x = 10
    y = 10
    for i in range(rows):
        for l in range(1,rows+1):
            if grid[i][l-1] == 'x':
                pygame.draw.line(surface, (255,255,255), (sizeBtwn*(l-1)+15,15+sizeBtwn*i),(sizeBtwn*l-15,sizeBtwn-15+sizeBtwn*i),5)
                pygame.draw.line(surface, (255,255,255), (sizeBtwn*(l-1)+15,sizeBtwn-15+sizeBtwn*i), (sizeBtwn*l-15,15+sizeBtwn*i),5)
            x = x + sizeBtwn
            y = y + sizeBtwn

def drawO(surface):
    sizeBtwn = width // rows

    for i in range(1,rows+1):
        for l in range(1,rows+1):
            if grid[i-1][l-1] == 'o':
                pygame.draw.circle(surface, (255,255,255), (sizeBtwn//2+sizeBtwn*(l-1),sizeBtwn*(i-1)+sizeBtwn//2),(sizeBtwn//2)-15,4)

def drawGrid(surface):
    sizeBtwn = width // rows

    x = 0
    y = 0

    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255,255,255), (x,0),(x,width),3)
        pygame.draw.line(surface, (255,255,255), (0,y),(width,y),3)

    drawX(surface)
    drawO(surface)

def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

def redrawWindow(surface):
    surface.fill((0,0,0))
    drawGrid(surface)
    pygame.display.update()

def main():
    global width, rows, grid, firstRound
    firstRound = True
    grid = [['n','n','n'],
            ['n','n','n'],
            ['n','n','n']]
    width = 600
    reset = False
    rows = 3
    win = pygame.display.set_mode((width, width))
    flag = True

    clock = pygame.time.Clock()
    pygame.display.set_caption('Tic Tac Toe')

    player = 'x'

    while flag:
        pygame.time.delay(50)
        clock.tick(10)

        ev = pygame.event.get()

        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                if reset == False and changeGrid(x, y, player):
                    if firstRound:
                        firstRound = False
                    if player == 'x':
                        player = 'o'
                    else:
                        player = 'x'
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
#ez
        if reset:
            reset = False

        redrawWindow(win)

        if checkWin() == 'x':
            message_box('X Won!', 'X Won! \nPlay again...')
            player = 'x'
        elif checkWin() == 'o':
            message_box('O Won!', 'O Won! \nPlay again...')
            player = 'o'
        elif checkWin() == 't':
            message_box('Tie!', 'Tie! \nPlay again...')

        if checkWin() != 'n':
            grid = [['n','n','n'],
                    ['n','n','n'],
                    ['n','n','n']]
            firstRound = True
            reset = True

    pass

if __name__ == '__main__':
    main()
