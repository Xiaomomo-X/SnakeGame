import pygame
import random

pygame.init()

width,height=800,600
cell_size=20
screen_size=(width,height)
screen=pygame.display.set_mode(screen_size)
pygame.display.set_caption("贪吃蛇")


#设置颜色
black=(0,0,0)
green=(0,255,0)
red=(255,0,0)
white=(255,255,255)

#设置字体
font = pygame.font.SysFont("Comic Sans MS", 26)

#设置游戏频率
clock=pygame.time.Clock()

#随机出现食物
def random_food(snake):
    while True:
        x = random.randint(0, (width - cell_size) // cell_size) * cell_size
        y = random.randint(0, (height - cell_size) // cell_size) * cell_size
        if (x, y) not in snake:  # 确保不在蛇身体上
            return x, y


#重新初始化游戏
def reset_game():
    global cell_size
    new_snake=[(100,100),(80,100),(60,100)]
    new_direction=(cell_size,0)
    new_score=0
    new_food=random_food(new_snake)
    return new_snake,new_direction, new_score, new_food

#初始化游戏
snake,direction,score,food=reset_game()
#游戏是否结束
game_over=False

running=True
while running:
    clock.tick(8)# 控制FPS

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        elif event.type==pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_UP and direction != (0, cell_size):
                    direction = (0, -cell_size)
                elif event.key == pygame.K_DOWN and direction != (0, -cell_size):
                    direction = (0, cell_size)
                elif event.key == pygame.K_LEFT and direction != (cell_size, 0):
                    direction = (-cell_size, 0)
                elif event.key == pygame.K_RIGHT and direction != (-cell_size, 0):
                    direction = (cell_size, 0)
            else:
                if event.key==pygame.K_SPACE:
                    snake, direction, score, food = reset_game()
                    game_over=False

    if not game_over:
        head_x,head_y=snake[0]
        new_head=(head_x+direction[0],head_y+direction[1])

        #撞墙或者咬到自己，游戏结束
        if (not (0<=new_head[0]<width and 0<=new_head[1]<height)) or new_head in snake:
            game_over=True

        #吃到食物就长大一点
        if new_head==food:
            snake=[new_head]+snake
            food=random_food(snake)
            score+=1
        else:
            snake=[new_head]+snake[:-1]

    screen.fill(black)
    for temp in snake:
        pygame.draw.rect(screen,green,(*temp,cell_size,cell_size))

    # 画食物
    x, y = food
    pygame.draw.circle(screen, red, (x + cell_size // 2, y + cell_size // 2), cell_size // 2 - 1)

    #显示分数
    score_text = font.render(f"score: {score}", True, white)
    screen.blit(score_text, (10, 10))#贴到screen里面

    # Game Over
    if game_over:
        over_text = font.render("Game Over!  SPACE  for  REPLAY", True, white)
        screen.blit(over_text, (width // 2 - 200, height // 2))

    pygame.display.flip()
pygame.quit()








