import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((400,400))


def getKey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyinput = pygame.key.get_pressed()
    mykey = getattr(pygame,'K_{}'.format(keyName))
    if keyinput[mykey]:
        ans = True
        pygame.display.update()
    return ans

def main():
    if getKey("LEFT"):
        print("Left key pressed")
    if getKey("RIGHT"):
        print("Right key pressed")

if __name__ == '__main__':
    init()
    while True:
        main()