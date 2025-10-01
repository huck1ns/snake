import pygame
import random




class Direction:
    UP = [0,-1]
    DOWN = [0,1]
    LEFT = [-1,0]
    RIGHT = [1,0]

class Snake:
    def __init__(self,x,y):
        self.snakePositions = [Position(x, y)]
        self.snakeLength = 1
        self.direction = Direction.RIGHT

    def move(self, food):

        new = Position(self.snakePositions[0].x+self.direction[0], self.snakePositions[0].y+self.direction[1])
        self.snakePositions.insert(0, new)
        if new.equals(food.foodPosition):
            food.newFood(self)
            self.snakeLength += 1
            return
        else: self.snakePositions.pop()

    def checkLoss(self):
        head = self.snakePositions[0]

        for snakePosition in self.snakePositions[1:]:
            if head.equals(snakePosition):
                print("Snake inside itself")
                return True
        if (head.x>=20 or head.y>=20) or (head.x<=0 or head.y<=0):
            print("Snake out of bounds")
            return True
        return False

class Position:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def equals(self, other):
        return self.x == other.x and self.y == other.y


class Food:
    foodPosition = None
    def __init__(self,snake):
        self.newFood(snake)

    def newFood(self, snake):
        while True:
            x = random.randint(0,19)
            y = random.randint(0,19)
            in_snake = False
            for position in snake.snakePositions:
                if position.x == x and position.y == y:
                    in_snake = True
                    break
            if not in_snake:
                break

        self.foodPosition = Position(x, y)




pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
running = True

def drawSnake(snake):
    for snakePiece in snake.snakePositions:
        currentPiece=pygame.Rect(snakePiece.x*40,snakePiece.y*40,40,40)
        pygame.draw.rect(screen, "green", currentPiece)

def drawFood(food):
    currentFood = pygame.Rect(food.foodPosition.x*40,food.foodPosition.y*40,40,40)
    pygame.draw.rect(screen, "red", currentFood)

gameSnake = Snake(10, 10)
food = Food(gameSnake)

LOGIC_UPDATE_INTERVAL = 1000 // 6
last_update_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a] and gameSnake.direction != Direction.RIGHT:
        gameSnake.direction = Direction.LEFT
    if keys[pygame.K_RIGHT] or keys[pygame.K_d] and gameSnake.direction != Direction.LEFT:
        gameSnake.direction = Direction.RIGHT
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and gameSnake.direction != Direction.DOWN:
        gameSnake.direction = Direction.UP
    if keys[pygame.K_DOWN] or keys[pygame.K_s] and gameSnake.direction != Direction.UP:
        gameSnake.direction = Direction.DOWN

    current_time = pygame.time.get_ticks()
    if current_time - last_update_time >= LOGIC_UPDATE_INTERVAL:
        gameSnake.move(food)

        if gameSnake.checkLoss():
            print("Game Over")
            running = False
        last_update_time = current_time

    screen.fill((0,0,0))
    drawSnake(gameSnake)
    drawFood(food)

    pygame.display.flip()

    clock.tick()


















