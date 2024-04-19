"""
Nick Lagges and Ben Wechsler

State Savior Game
"""
import pygame
from pygame.locals import *
import sys
from button import Button
from countryStats import Country

'''
Utils:
 - text can go to col 80 before needing a new line
 - 
'''

# Initialize Pygame
pygame.init()

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (227,10,23)
GREEN = (0, 255, 0)
BLUE = (0,0,255)
TURQUOISE = (64,224,208)
PEACH = (255,100,0)

# Set up screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

# Set up button dimensions
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 100

#First Options Button dimensions
OPT1_WIDTH = 400
OPT2_WIDTH = 400

# Set up font
FONT = pygame.font.SysFont("footlight", 50)
FONT2 = pygame.font.SysFont("arial", 17)
FONT3 = pygame.font.SysFont("footlight", 35)

# Options font

OPT_FONT = pygame.font.SysFont("footlight", 30)

# Title Font

Title_Font = pygame.font.SysFont("footlight", 100)

# choices made
R = 0
E = 1
EU = 2
D = 3

#Class Variables
REFORM = False
ALLIES = False
WALK = False
RELATIONS = False
INTERNAL = False
TAXES = False
INVESTMENT = False
SYRIA = False
SPENDING = False

# Country Statistics

ECONOMIC_STRENGTH = 60
QUALITY_OF_LIFE = 55
POLITICAL_STABILITY = 45
DIPLOMACY = 55
INFRASTRUCTURE = 60
DEFENSE = 65
START_OVERALL = 57

turkey = Country(ECONOMIC_STRENGTH, QUALITY_OF_LIFE, POLITICAL_STABILITY, DIPLOMACY, INFRASTRUCTURE, DEFENSE, REFORM, ALLIES, WALK, RELATIONS, INTERNAL, TAXES, INVESTMENT, SYRIA, SPENDING)

# Function to draw text on the screen
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

# Function to check if a button is clicked
def is_button_clicked(pos, button_rect):
    if button_rect.collidepoint(pos):
        return True
    return False
#Function to display pre-game explanation screen
def display_pre_screen(screen):
    screen.fill(WHITE)
    draw_text("Turkey is facing four main issues: A refugee crisis, economic,", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 30)
    draw_text("challenges, maintaining relaitons with the EU, and maintaining defense", FONT3, BLACK, screen, (SCREEN_WIDTH // 2) + 10, 60)
    
    draw_text("Refugee Crisis: ", FONT, BLACK, screen, SCREEN_WIDTH // 4, 100)
    draw_text("Turkey currently hosts the most refugees in the world at 3.6 million.", FONT2, BLACK, screen, SCREEN_WIDTH // 4, 125)
    draw_text("This large influx has put straing on resources and infrastructure, presenting", FONT2, BLACK, screen, SCREEN_WIDTH // 4, 150)
    draw_text("Challenges for Turkey. Despite some previous efforts to remedy this issue,", FONT2, BLACK, screen, SCREEN_WIDTH // 4, 175)
    draw_text("refugees continue to flood into Turkey", FONT2, BLACK, screen, SCREEN_WIDTH // 4, 200)
    refugeePic = pygame.image.load("refugeeSmall.jpg").convert()
    screen.blit(refugeePic, (175, 275))
    
    draw_text("Economic Issues: ", FONT, BLACK, screen, SCREEN_WIDTH - (SCREEN_WIDTH // 4), 100)
    draw_text("Turkey has faced many economic challenges recently, such as high inflation,", FONT2, BLACK, screen, SCREEN_WIDTH - (SCREEN_WIDTH // 4), 125)
    draw_text("a weakening currency, and rising unenployment rates. These issues have only ", FONT2, BLACK, screen, SCREEN_WIDTH - (SCREEN_WIDTH // 4), 150)
    draw_text("grown worse due to the various other issues Turkey is facing right now. The", FONT2, BLACK, screen, SCREEN_WIDTH - (SCREEN_WIDTH // 4), 175)
    draw_text("Turkish lira is now worth 0.031 USD, decreasing in value by 141% since", FONT2, BLACK, screen, SCREEN_WIDTH - (SCREEN_WIDTH // 4), 200)
    draw_text("2019. Additionally, a large spending deficit and high natinoal debt have", FONT2, BLACK, screen, SCREEN_WIDTH - (SCREEN_WIDTH // 4), 225)
    draw_text("led to increased challenges for the country.", FONT2, BLACK, screen, SCREEN_WIDTH - (SCREEN_WIDTH // 4), 250)
    econPic = pygame.image.load("econSmall.jpg").convert()
    screen.blit(econPic, (675, 275))

    draw_text("EU Relations: ", FONT, BLACK, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT - 300)
    draw_text("Turkeys current relationship with the EU is complicated. Although Turkey", FONT2, BLACK, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT - 275)
    draw_text("does participate in EU programs, tensions have been rising between the EU", FONT2, BLACK, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT - 250)
    draw_text("and Turkey over policy dissagreements. The EU has become concerned with", FONT2, BLACK, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT - 225)
    draw_text("human rights issues in Turkey, with Turkey coming under fire from the EU ", FONT2, BLACK, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT - 200)
    draw_text("because of a lack of freedom of expression, press, and assembly. Turkey has", FONT2, BLACK, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT - 175)
    draw_text("reportedly been restricting media access as well, all sparking concerns that", FONT2, BLACK, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT - 150)
    draw_text("Turkey is not being complient with EU standards.", FONT2, BLACK, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT - 125)
    euPic = pygame.image.load("euSmall.jpg").convert()
    screen.blit(euPic, (175, 600)) 
    
    draw_text("Defence: ", FONT, BLACK, screen, SCREEN_WIDTH - (SCREEN_WIDTH // 4), SCREEN_HEIGHT - 300)
    draw_text("Turkeys defence decisions are determined by both internal and external factors.", FONT2, BLACK, screen, SCREEN_WIDTH - (SCREEN_WIDTH // 4), SCREEN_HEIGHT - 275)
    draw_text("The Kurdistan Workers' Party (PKK) is a militant terrorist organization causing", FONT2, BLACK, screen, SCREEN_WIDTH - (SCREEN_WIDTH // 4), SCREEN_HEIGHT - 250)
    draw_text("uprises throughout Turkey, leading to civil unrest and instability. Additionally, ", FONT2, BLACK, screen, SCREEN_WIDTH - (SCREEN_WIDTH // 4), SCREEN_HEIGHT - 225)
    draw_text("Islamic extremism has plagued the citizens of Turkey. While the country is", FONT2, BLACK, screen, SCREEN_WIDTH - (SCREEN_WIDTH // 4), SCREEN_HEIGHT - 200)
    draw_text("handling both of these issues, Turkey is also involved abroad in a Syrian", FONT2, BLACK, screen, SCREEN_WIDTH - (SCREEN_WIDTH // 4), SCREEN_HEIGHT - 175)
    draw_text("conflict. While Turkey works to navigate their many challenges, maintaining ", FONT2, BLACK, screen, SCREEN_WIDTH - (SCREEN_WIDTH // 4), SCREEN_HEIGHT - 150)
    draw_text("international relationships is key.", FONT2, BLACK, screen, SCREEN_WIDTH - (SCREEN_WIDTH // 4), SCREEN_HEIGHT - 125)
    defensePic = pygame.image.load("militarySmall.jpg").convert()
    screen.blit(defensePic, (675, 600))
    
    button1_rect = pygame.Rect(SCREEN_WIDTH -50 - BUTTON_WIDTH // 2, SCREEN_HEIGHT -10, BUTTON_WIDTH -50, BUTTON_HEIGHT -50)

    
    NEXT = Button(FONT, GREEN, button1_rect.x, button1_rect.y, BUTTON_WIDTH -50, BUTTON_HEIGHT -50, "Next")
   

    NEXT.draw(screen)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    display_course(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    
# Function to display options screen
def display_course(screen):
    screen.fill(WHITE)
    background = pygame.image.load("course.jpg").convert()
    screen.blit(background, (-220,0))
    pygame.draw.rect(screen, WHITE, (10, 10, 1000, 175))
    
    draw_text("Decide which course of action to pursue.", FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    draw_text("Tip: The order in which you make decisions may affect the success", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 100)
    draw_text("of another.", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 150)

    button1_rect = pygame.Rect(0,0,1,1)
    button2_rect = pygame.Rect(0,0,1,1)
    button3_rect = pygame.Rect(0,0,1,1)
    button4_rect = pygame.Rect(0,0,1,1)
    button5_rect = pygame.Rect(0,0,1,1)

    if len(turkey.CHOICES) < 3:
        if R not in turkey.CHOICES:
            button1_rect = pygame.Rect(50, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
            opt1 = Button(OPT_FONT, WHITE, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Refugee Crisis")
            opt1.draw(screen)
        if E not in turkey.CHOICES:
            button2_rect = pygame.Rect(550, SCREEN_HEIGHT // 2 - 50, OPT2_WIDTH, BUTTON_HEIGHT)
            opt2 = Button(OPT_FONT, TURQUOISE, button2_rect.x, button2_rect.y, OPT2_WIDTH, BUTTON_HEIGHT, "Economic Challenges")
            opt2.draw(screen)
        if EU not in turkey.CHOICES:
            button3_rect = pygame.Rect(50, SCREEN_HEIGHT // 2 + 150, OPT2_WIDTH, BUTTON_HEIGHT)
            opt3 = Button(OPT_FONT, PEACH, button3_rect.x, button3_rect.y, OPT2_WIDTH, BUTTON_HEIGHT, "European Union Relations")
            opt3.draw(screen)
        if D not in turkey.CHOICES:
            button4_rect = pygame.Rect(550, SCREEN_HEIGHT // 2 + 150, OPT2_WIDTH, BUTTON_HEIGHT)
            opt4 = Button(OPT_FONT, RED, button4_rect.x, button4_rect.y, OPT2_WIDTH, BUTTON_HEIGHT, "Defense")
            opt4.draw(screen)
    elif len(turkey.CHOICES) > 2:
        button5_rect = pygame.Rect(300, SCREEN_HEIGHT // 2, OPT2_WIDTH, BUTTON_HEIGHT)
        opt5 = Button(OPT_FONT, (255,125,0), button5_rect.x, button5_rect.y, OPT2_WIDTH, BUTTON_HEIGHT, "View Results")
        opt5.draw(screen)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    turkey.CHOICES.append(R)
                    display_refugee(screen)
                elif is_button_clicked(mouse_pos, button2_rect):
                    turkey.CHOICES.append(E)
                    display_economic(screen)
                elif is_button_clicked(mouse_pos, button3_rect):
                    turkey.CHOICES.append(EU)
                    display_EU(screen)
                elif is_button_clicked(mouse_pos, button4_rect):
                    turkey.CHOICES.append(D)
                    display_defense(screen)
                elif is_button_clicked(mouse_pos, button5_rect):
                    display_end_of_game(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_end_of_game(screen):
    screen.fill(WHITE)
    OVERALL = round( (turkey.ECONOMIC_STRENGTH + turkey.QUALITY_OF_LIFE + turkey.POLITICAL_STABILITY + turkey.DIPLOMACY + turkey.INFRASTRUCTURE + turkey.DEFENSE), 0 ) // 6

    if OVERALL < START_OVERALL:
        background = pygame.image.load("riot.jpg").convert()
        screen.blit(background, (0,0))
        pygame.draw.rect(screen, BLACK, (10, 525, 975, 50))
        draw_text("You made the country worse overall as a leader. You Lost! :(", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 550)
    elif (OVERALL - START_OVERALL) <= 1:
        background = pygame.image.load("fail.jpg").convert()
        screen.blit(background, (0,0))
        pygame.draw.rect(screen, BLACK, (10, 525, 975, 110))
        draw_text("You were an average leader, but Turkey saw little to no improvement.", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 550)
        draw_text("You Lose!", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 600)
    elif (OVERALL - START_OVERALL) <= 3:
        background = pygame.image.load("celebration.jpg").convert()
        screen.blit(background, (0,0))
        pygame.draw.rect(screen, BLACK, (10, 525, 975, 50))
        draw_text("You made the country slightly better overall as a leader. You Win!", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 550)
    else:
        background = pygame.image.load("celebration.jpg").convert()
        screen.blit(background, (0,0))
        pygame.draw.rect(screen, BLACK, (10, 525, 975, 110))
        draw_text("You made the country better overall as a leader. You Win! :)", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 550)
        draw_text("You were a great leader!", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 600)
    pygame.draw.rect(screen, BLACK, (10, 10, 900, 75))
    draw_text("After governing Turkey for 3 years, here are the results:", FONT3, WHITE, screen, SCREEN_WIDTH // 2 - 50, 50)

    pygame.draw.rect(screen, BLACK, (10, 75, 420, 300))
    
    draw_text("Economic Strength:", FONT3, WHITE, screen, 150, 100)
    draw_text(str(turkey.ECONOMIC_STRENGTH), OPT_FONT, WHITE, screen, 150 + 200, 100)
    if turkey.ECONOMIC_STRENGTH - ECONOMIC_STRENGTH >= 0:
        res = "+" + str(turkey.ECONOMIC_STRENGTH - ECONOMIC_STRENGTH)
        draw_text(res, OPT_FONT, WHITE, screen, 150 + 250, 100)
    else:
        draw_text(str(turkey.ECONOMIC_STRENGTH - ECONOMIC_STRENGTH), OPT_FONT, WHITE, screen, 150 + 250, 100)

    draw_text("Quality of Life:", FONT3, WHITE, screen, 150, 140)
    draw_text(str(turkey.QUALITY_OF_LIFE), OPT_FONT, WHITE, screen, 150 + 200, 140)
    if turkey.QUALITY_OF_LIFE - QUALITY_OF_LIFE >= 0:
        res = "+" + str(turkey.QUALITY_OF_LIFE - QUALITY_OF_LIFE)
        draw_text(res, OPT_FONT, WHITE, screen, 150 + 250, 140)
    else:
        draw_text(str(turkey.QUALITY_OF_LIFE - QUALITY_OF_LIFE), OPT_FONT, WHITE, screen, 150 + 250, 140)

    draw_text("Political Stability:", FONT3, WHITE, screen, 150, 180)
    draw_text(str(turkey.POLITICAL_STABILITY), OPT_FONT, WHITE, screen, 150 + 200, 180)
    if turkey.POLITICAL_STABILITY - POLITICAL_STABILITY >= 0:
        res = "+" + str(turkey.POLITICAL_STABILITY - POLITICAL_STABILITY)
        draw_text(res, OPT_FONT, WHITE, screen, 150 + 250, 180)
    else:
        draw_text(str(turkey.POLITICAL_STABILITY - POLITICAL_STABILITY), OPT_FONT, WHITE, screen, 150 + 250, 180)

    draw_text("Diplomacy:", FONT3, WHITE, screen, 150, 220)
    draw_text(str(turkey.DIPLOMACY), OPT_FONT, WHITE, screen, 150 + 200, 220)
    if turkey.DIPLOMACY - DIPLOMACY >= 0:
        res = "+" + str(turkey.DIPLOMACY - DIPLOMACY)
        draw_text(res, OPT_FONT, WHITE, screen, 150 + 250, 220)
    else:
        draw_text(str(turkey.DIPLOMACY - DIPLOMACY), OPT_FONT, WHITE, screen, 150 + 250, 220)

    draw_text("Infrastructure:", FONT3, WHITE, screen, 150, 260)
    draw_text(str(turkey.INFRASTRUCTURE), OPT_FONT, WHITE, screen, 150 + 200, 260)
    if turkey.INFRASTRUCTURE - INFRASTRUCTURE >= 0:
        res = "+" + str(turkey.INFRASTRUCTURE - INFRASTRUCTURE)
        draw_text(res, OPT_FONT, WHITE, screen, 150 + 250, 260)
    else:
        draw_text(str(turkey.INFRASTRUCTURE - INFRASTRUCTURE), OPT_FONT, WHITE, screen, 150 + 250, 260)

    draw_text("Defense:", FONT3, WHITE, screen, 150, 300)
    draw_text(str(turkey.DEFENSE), OPT_FONT, WHITE, screen, 150 + 200, 300)
    if turkey.DEFENSE - DEFENSE >= 0:
        res = "+" + str(turkey.DEFENSE - DEFENSE)
        draw_text(res, OPT_FONT, WHITE, screen, 150 + 250, 300)
    else:
        draw_text(str(turkey.DEFENSE - DEFENSE), OPT_FONT, WHITE, screen, 150 + 250, 300)
        
    draw_text("Overall:", FONT3, WHITE, screen, 150, 340)
    draw_text(str(OVERALL), FONT3, WHITE, screen, 150 + 200, 340)
    if OVERALL - 57 >= 0:
        res = "+" + str(OVERALL - 57)
        draw_text(res, OPT_FONT, WHITE, screen, 150 + 250, 340)
    else:
        draw_text(str(OVERALL - 57), OPT_FONT, WHITE, screen, 150 + 250, 340)

    button1_rect = pygame.Rect(SCREEN_WIDTH -50 - BUTTON_WIDTH // 2, SCREEN_HEIGHT -10, BUTTON_WIDTH -50, BUTTON_HEIGHT -50)
    MENU = Button(FONT, GREEN, button1_rect.x, button1_rect.y, BUTTON_WIDTH -50, BUTTON_HEIGHT -50, "Menu")
    MENU.draw(screen)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    turkey.reset()
                    display_main_screen(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_economic(screen):
    screen.fill(WHITE)
    background = pygame.image.load("rising.jpg").convert()
    screen.blit(background, (0,0))
    
    draw_text("How should Turkey proceed?", FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    
    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    button2_rect = pygame.Rect(3 * SCREEN_WIDTH // 4 - OPT2_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT2_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Stimulus Package")
    opt2 = Button(OPT_FONT, GREEN, button2_rect.x, button2_rect.y, OPT2_WIDTH, BUTTON_HEIGHT, "Austerity Measures")

    opt1.draw(screen)
    opt2.draw(screen)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    display_economic_stim(screen)
                elif is_button_clicked(mouse_pos, button2_rect):
                    display_economic_aust(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_economic_stim(screen):
    screen.fill(WHITE)

    background = pygame.image.load("rising.jpg").convert()
    screen.blit(background, (0,0))
    
    draw_text("How do you want to take stimulus measures?", FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    
    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    button2_rect = pygame.Rect(3 * SCREEN_WIDTH // 4 - OPT2_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT2_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Increase Investment")
    opt2 = Button(OPT_FONT, GREEN, button2_rect.x, button2_rect.y, OPT2_WIDTH, BUTTON_HEIGHT, "Direct Cash Transfers")

    opt1.draw(screen)
    opt2.draw(screen)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    display_investment_result(screen)
                elif is_button_clicked(mouse_pos, button2_rect):
                    display_cash_result(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_investment_result(screen):
    screen.fill(WHITE)
    background = pygame.image.load("economyUp.jpg").convert()
    screen.blit(background, (0,0))
    
    draw_text("You increased investment into the economy, stimulating growth in", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 50)
    draw_text("the short run. There is an increase in job creation,", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 100)
    draw_text("infrastructure, and consumer condfidence. However, inflation", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 150)
    draw_text("continues to rise at an alarming rate.", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 200)

    turkey.INVESTMENT = True

    turkey.ECONOMIC_STRENGTH += 5
    turkey.QUALITY_OF_LIFE += 2
    turkey.INFRASTRUCTURE += 2
    
    button1_rect = pygame.Rect(SCREEN_WIDTH -50 - BUTTON_WIDTH // 2, SCREEN_HEIGHT -10, BUTTON_WIDTH -50, BUTTON_HEIGHT -50)
    
    NEXT = Button(FONT, GREEN, button1_rect.x, button1_rect.y, BUTTON_WIDTH -50, BUTTON_HEIGHT -50, "Next")
   
    NEXT.draw(screen)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    display_course(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_cash_result(screen):
    screen.fill(WHITE)
    background = pygame.image.load("cash.jpg").convert()
    screen.blit(background, (0,0))
    
    draw_text("You made direct cash transfers to citizens, stimulating economic", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 50)
    draw_text("growth in the short run. Stimulus cash transfers boost consumer", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 100)
    draw_text("spending and address income inequalities. However, issuing stimilus", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 150)
    draw_text("cash transfers has allowed inflation to continue its climb.", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 200)

    turkey.ECONOMIC_STRENGTH += 4
    turkey.QUALITY_OF_LIFE += 4
    
    button1_rect = pygame.Rect(SCREEN_WIDTH -50 - BUTTON_WIDTH // 2, SCREEN_HEIGHT -10, BUTTON_WIDTH -50, BUTTON_HEIGHT -50)
    
    NEXT = Button(FONT, GREEN, button1_rect.x, button1_rect.y, BUTTON_WIDTH -50, BUTTON_HEIGHT -50, "Next")
   
    NEXT.draw(screen)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    display_course(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()


def display_economic_aust(screen):
    screen.fill(WHITE)
    background = pygame.image.load("rising.jpg").convert()
    screen.blit(background, (0,0))
    
    draw_text("How do you want to take austerity measures?", FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    
    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    button2_rect = pygame.Rect(3 * SCREEN_WIDTH // 4 - OPT2_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT2_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Increase Taxes")
    opt2 = Button(OPT_FONT, GREEN, button2_rect.x, button2_rect.y, OPT2_WIDTH, BUTTON_HEIGHT, "Reduce Spending")

    opt1.draw(screen)
    opt2.draw(screen)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    display_tax_result(screen)
                elif is_button_clicked(mouse_pos, button2_rect):
                    display_reduce_spend_result(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_reduce_spend_result(screen):
    screen.fill(WHITE)
    background = pygame.image.load("economyDown.jpg").convert()
    screen.blit(background, (0,0))

    turkey.SPENDING = True

    turkey.ECONOMIC_STRENGTH += 3
    turkey.QUALITY_OF_LIFE -= 3
    turkey.INFRASTRUCTURE -= 3
    
    draw_text("You reduced government spending, cutting social welfare programs", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 50)
    draw_text("pension reforms, causing protests and challenges to political", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 100)
    draw_text("stability. The reduced spending, on the other hand, has reduced", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 150)
    draw_text("governmental budget issues, improved investor confidence, and more", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 200)
    draw_text("stable inflation.", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 250)

    button1_rect = pygame.Rect(SCREEN_WIDTH -50 - BUTTON_WIDTH // 2, SCREEN_HEIGHT -10, BUTTON_WIDTH -50, BUTTON_HEIGHT -50)
    
    NEXT = Button(FONT, GREEN, button1_rect.x, button1_rect.y, BUTTON_WIDTH -50, BUTTON_HEIGHT -50, "Next")
   
    NEXT.draw(screen)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    display_course(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_tax_result(screen):
    screen.fill(WHITE)
    background = pygame.image.load("tax.jpg").convert()
    screen.blit(background, (0,0))

    turkey.TAXES = True

    turkey.ECONOMIC_STRENGTH += 4
    turkey.INFRASTRUCTURE += 4
    turkey.QUALITY_OF_LIFE -=2
    turkey.POLITICAL_STABILITY -=2
    turkey.DEFENSE += 3

    pygame.draw.rect(screen, WHITE, (10, 10, 1000, 210))
    
    draw_text("You increased taxes, sparking protests, challenging social cohesion", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 50)
    draw_text("and political stability. Tax increases have reduced the overall", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 100)
    draw_text("demand of the economy. However, governmental budget deficits have", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 150)
    draw_text("been cut and inflation is at a more stable level.", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 200)

    button1_rect = pygame.Rect(SCREEN_WIDTH -50 - BUTTON_WIDTH // 2, SCREEN_HEIGHT -10, BUTTON_WIDTH -50, BUTTON_HEIGHT -50)
    
    NEXT = Button(FONT, GREEN, button1_rect.x, button1_rect.y, BUTTON_WIDTH -50, BUTTON_HEIGHT -50, "Next")
   
    NEXT.draw(screen)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    display_course(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_refugee(screen):
    screen.fill(WHITE)
    background = pygame.image.load("refugee.jpg").convert()
    screen.blit(background, (0,0))
    
    draw_text("How should the country proceed?", FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    
    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    button2_rect = pygame.Rect(3 * SCREEN_WIDTH // 4 - OPT2_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT2_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "International Cooperation")
    opt2 = Button(OPT_FONT, GREEN, button2_rect.x, button2_rect.y, OPT2_WIDTH, BUTTON_HEIGHT, "Internal Restructuring")

    opt1.draw(screen)
    opt2.draw(screen)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    display_international_coop(screen)
                elif is_button_clicked(mouse_pos, button2_rect):
                    display_internal(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_international_coop(screen):
    screen.fill(WHITE)
    background = pygame.image.load("refugee.jpg").convert()
    screen.blit(background, (0,0))
    
    draw_text("How should Turkey proceed?", FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    
    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    button2_rect = pygame.Rect(3 * SCREEN_WIDTH // 4 - OPT2_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT2_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Work with United Nations")
    opt2 = Button(OPT_FONT, GREEN, button2_rect.x, button2_rect.y, OPT2_WIDTH, BUTTON_HEIGHT, "Address Syrian Issues")

    opt1.draw(screen)
    opt2.draw(screen)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    display_UN_result(screen)
                elif is_button_clicked(mouse_pos, button2_rect):
                    display_syrian_result(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_UN_result(screen):
    screen.fill(WHITE)
    background = pygame.image.load("UN.jpg").convert()
    screen.blit(background, (0,0))

    if turkey.REFORM:
        draw_text("You have decided to address the refugee crisis by consulting", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 50)
        draw_text("the United Nations. Since you have previously decided to", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 100)
        draw_text("reform to European Union Standards, the United Nations is more", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 150)
        draw_text("likely to support Turkey. With the aid from the UN, refugees", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 200)
        draw_text("have seen improvements in living conditions and quality of life.", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 250)

        turkey.QUALITY_OF_LIFE += 5
        turkey.INFRASTRUCTURE += 1
        turkey.POLITICAL_STABILITY += 2
        
    elif turkey.ALLIES:
        draw_text("You have decided to address the refugee crisis by consulting", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 50)
        draw_text("the United Nations. This approach will take time, but citizens", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 100)
        draw_text("are already starting to see improvements due to the aid from", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 150)
        draw_text("neighboring allies. Although the UN is not yet directly", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 200)
        draw_text("involved, they have made a statement promising future support", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 250)
        draw_text("for the refugees in Turkey.", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 300)

        turkey.QUALITY_OF_LIFE += 4
        turkey.POLITICAL_STABILITY += 2
        
    elif turkey.WALK:
        draw_text("You have decided to address the refugee crisis by consulting", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 50)
        draw_text("the United Nations. Since you have previously walked away from", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 100)
        draw_text(" attempts to join the European Union, EU countries in the UN", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 150)
        draw_text("have been less responsive to Turkey's calls for aid. You hope", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 200)
        draw_text("other opportunities can help improve the well being of the", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 250)
        draw_text("refugees, but for now their quality of life slightly improves.", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 300)

        turkey.QUALITY_OF_LIFE += 2
        turkey.POLITICAL_STABILITY -= 1
        
    else:
        draw_text("You have decided to address the refugee crisis by consulting", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 50)
        draw_text("the United Nations. Due to Turkey's complex relationship with", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 100)
        draw_text("the UN, they have been slightly receptive to your call for", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 150)
        draw_text("help. They have supplied aid, but not as much as necessary to", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 200)
        draw_text("greatly improve refuge equality of life.", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 250)

        turkey.QUALITY_OF_LIFE += 3
        turkey.POLITICAL_STABILITY += 1

    button1_rect = pygame.Rect(SCREEN_WIDTH -50 - BUTTON_WIDTH // 2, SCREEN_HEIGHT -10, BUTTON_WIDTH -50, BUTTON_HEIGHT -50)
    
    NEXT = Button(FONT, GREEN, button1_rect.x, button1_rect.y, BUTTON_WIDTH -50, BUTTON_HEIGHT -50, "Next")
   
    NEXT.draw(screen)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    display_course(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_syrian_result(screen):
    screen.fill(WHITE)
    background = pygame.image.load("syria.png").convert()
    screen.blit(background, (0,0))

    turkey.SYRIA = True

    if turkey.RELATIONS:
        draw_text("You have decided to address the refugee crisis by addressing", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 50-10)
        draw_text("the Syrian issue at its core. This is a solid approach and", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 100-10)
        draw_text("shows your commitment to the issue. Because of your previous", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 150-10)
        draw_text("commitments, your relationship with Syria has improved,", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 200-10)
        draw_text("resulting to them being receptive, helping your efforts.", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 250-10)

        turkey.DIPLOMACY += 5
        turkey.POLITICAL_STABILITY += 2
        turkey.QUALITY_OF_LIFE += 2
        
    else:
        draw_text("You have decided to address the refugee crisis by addressing", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 50-10)
        draw_text("the Syrian issue at its core. This is a solid approach and shows", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 100-10)
        draw_text(" your commitment to the issue. However, geopolitical issues and", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 150-10)
        draw_text("strains in your relationship with neighboring countries have", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 200-10)
        draw_text("slowed down results.", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 250-10)

        turkey.POLITICAL_STABILITY += 1
        turkey.QUALITY_OF_LIFE += 1
        
    button1_rect = pygame.Rect(SCREEN_WIDTH -50 - BUTTON_WIDTH // 2, SCREEN_HEIGHT -10, BUTTON_WIDTH -50, BUTTON_HEIGHT -50)
    
    NEXT = Button(FONT, GREEN, button1_rect.x, button1_rect.y, BUTTON_WIDTH -50, BUTTON_HEIGHT -50, "Next")
   
    NEXT.draw(screen)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    display_course(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_internal(screen):
    screen.fill(WHITE)
    background = pygame.image.load("refugee.jpg").convert()
    screen.blit(background, (0,0))

    turkey.INTERNAL = True
    
    draw_text("How should Turkey deal with refugee issues?", FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    
    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    button2_rect = pygame.Rect(3 * SCREEN_WIDTH // 4 - OPT2_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT2_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Improve Opportunities")
    opt2 = Button(OPT_FONT, GREEN, button2_rect.x, button2_rect.y, OPT2_WIDTH, BUTTON_HEIGHT, "Limit Refugees")

    opt1.draw(screen)
    opt2.draw(screen)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    display_opportunity_result(screen)
                elif is_button_clicked(mouse_pos, button2_rect):
                    display_limit_result(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_opportunity_result(screen):
    screen.fill(WHITE)
    background = pygame.image.load("refugeeOpp.jpg").convert()
    screen.blit(background, (0,0))

    turkey.QUALITY_OF_LIFE += 5
    turkey.INFRASTRUCTURE += 2
    turkey.ECONOMIC_STRENGTH += 2

    pygame.draw.rect(screen, WHITE, (10, 10, 1000, 210))
    
    draw_text("You decided to improve opportunities for refugees. This has led to", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 50)
    draw_text("improvements in education and the job market. There has been an", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 100)
    draw_text("increase in refugees participating in the Turkish economy, leading", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 150)
    draw_text("to slightly less reliance on government support.", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 200)
    
    button1_rect = pygame.Rect(SCREEN_WIDTH -50 - BUTTON_WIDTH // 2, SCREEN_HEIGHT -10, BUTTON_WIDTH -50, BUTTON_HEIGHT -50)
    
    NEXT = Button(FONT, GREEN, button1_rect.x, button1_rect.y, BUTTON_WIDTH -50, BUTTON_HEIGHT -50, "Next")
   
    NEXT.draw(screen)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    display_course(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_limit_result(screen):
    screen.fill(WHITE)
    background = pygame.image.load("limit.jpg").convert()
    screen.blit(background, (0,50))

    turkey.QUALITY_OF_LIFE += 6
    turkey.POLITICAL_STABILITY -= 1
    turkey.ECONOMIC_STRENGTH += 2
    turkey.DIPLOMACY -= 2

    pygame.draw.rect(screen, WHITE, (10, 10, 1000, 460))
    
    draw_text("You chose to deal with the refugee crisis by reducing the amount", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 50)
    draw_text("of refugees accepted into Turkey. While many were grateful for", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 100)
    draw_text("Turkey housing refugees, the massive influx had put a strain on", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 150)
    draw_text("the economy. Despite efforts to support and integrate refugees, the", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 200)
    draw_text("increased demand for resources had stretched the government to its", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 250)
    draw_text("limits, prompting citizens to resent the refugees. Now, you have", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 300)
    draw_text("decided to limit the number of refugees allowed into Turkey.", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 350)
    draw_text("Neighboring countries, along with the UN, have been upset by this,", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 400)
    draw_text("but quality of life has improved for your citizens.", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 450)
    
    button1_rect = pygame.Rect(SCREEN_WIDTH -50 - BUTTON_WIDTH // 2, SCREEN_HEIGHT -10, BUTTON_WIDTH -50, BUTTON_HEIGHT -50)
    
    NEXT = Button(FONT, GREEN, button1_rect.x, button1_rect.y, BUTTON_WIDTH -50, BUTTON_HEIGHT -50, "Next")
   
    NEXT.draw(screen)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    display_course(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_EU(screen):
    screen.fill(WHITE)
    background = pygame.image.load("eu.jpg").convert()
    screen.blit(background, (-60,0))
    
    draw_text("How should the country proceed?", FONT, WHITE, screen, SCREEN_WIDTH // 2, 50)
    
    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    button2_rect = pygame.Rect(3 * SCREEN_WIDTH // 4 - OPT2_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT2_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Reform to EU Standards")
    opt2 = Button(OPT_FONT, GREEN, button2_rect.x, button2_rect.y, OPT2_WIDTH, BUTTON_HEIGHT, "Negotiate with EU")

    opt1.draw(screen)
    opt2.draw(screen)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    display_reform(screen)
                elif is_button_clicked(mouse_pos, button2_rect):
                    display_negotiate(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_reform(screen):
    screen.fill(WHITE)
    background = pygame.image.load("eu.jpg").convert()
    screen.blit(background, (-60,0))
    
    draw_text("How should the country reform?", FONT, WHITE, screen, SCREEN_WIDTH // 2, 50)
    
    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    button2_rect = pygame.Rect(3 * SCREEN_WIDTH // 4 - OPT2_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT2_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Protecting Human Rights")
    opt2 = Button(OPT_FONT, GREEN, button2_rect.x, button2_rect.y, OPT2_WIDTH, BUTTON_HEIGHT, "Strengthening Democracy")

    opt1.draw(screen)
    opt2.draw(screen)
    
    pygame.display.update()
    turkey.REFORM = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    display_protect_result(screen)
                elif is_button_clicked(mouse_pos, button2_rect):
                    display_democracy_result(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_protect_result(screen):
    screen.fill(WHITE)
    background = pygame.image.load("hr.jpg").convert()
    screen.blit(background, (0,0))

    turkey.QUALITY_OF_LIFE += 8
    turkey.POLITICAL_STABILITY += 2
    turkey.DIPLOMACY += 3

    pygame.draw.rect(screen, WHITE, (10, 10, 1000, 175))
    
    draw_text("You have chosen to make reforms and protect the human rights of", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 50)
    draw_text("the citizens of Turkey. As a result, your citizens have become", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 100)
    draw_text("happier and you are in better standing with the UN.", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 150)

    button1_rect = pygame.Rect(SCREEN_WIDTH -50 - BUTTON_WIDTH // 2, SCREEN_HEIGHT -10, BUTTON_WIDTH -50, BUTTON_HEIGHT -50)
    
    NEXT = Button(FONT, GREEN, button1_rect.x, button1_rect.y, BUTTON_WIDTH -50, BUTTON_HEIGHT -50, "Next")
   
    NEXT.draw(screen)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    display_course(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_democracy_result(screen):
    screen.fill(WHITE)
    background = pygame.image.load("democracy.jpg").convert()
    screen.blit(background, (0,0))

    turkey.POLITICAL_STABILITY += 4
    turkey.ECONOMIC_STRENGTH -= 2
    turkey.DIPLOMACY += 2

    draw_text("You have chosen to increase democracy within the country. Although", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 50)
    draw_text("this decision was met with backlash from the interests of ", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 100)
    draw_text("influential steakholders and political opposition. Despite these", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 150)
    draw_text("obstacles, you have gained the trust of the UN and promoted", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 200)
    draw_text("domestic stability.", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 250)

    button1_rect = pygame.Rect(SCREEN_WIDTH -50 - BUTTON_WIDTH // 2, SCREEN_HEIGHT -10, BUTTON_WIDTH -50, BUTTON_HEIGHT -50)
    
    NEXT = Button(FONT, GREEN, button1_rect.x, button1_rect.y, BUTTON_WIDTH -50, BUTTON_HEIGHT -50, "Next")
   
    NEXT.draw(screen)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    display_course(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_negotiate(screen):
    screen.fill(WHITE)
    background = pygame.image.load("eu.jpg").convert()
    screen.blit(background, (0,0))
    
    draw_text("How should Turkey negotiate with the EU?", FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    
    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    button2_rect = pygame.Rect(3 * SCREEN_WIDTH // 4 - OPT2_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT2_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Build Alliances")
    opt2 = Button(OPT_FONT, GREEN, button2_rect.x, button2_rect.y, OPT2_WIDTH, BUTTON_HEIGHT, "Explore Alternative Options")

    opt1.draw(screen)
    opt2.draw(screen)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    display_alliances_result(screen)
                elif is_button_clicked(mouse_pos, button2_rect):
                    display_alternatives_result(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_alliances_result(screen):
    screen.fill(WHITE)
    background = pygame.image.load("alliance.jpg").convert()
    screen.blit(background, (0,0))

    turkey.ALLIES = True

    turkey.DIPLOMACY += 5
    turkey.DEFENSE += 3
    turkey.POLITICAL_STABILITY += 2
    
    draw_text("You have built back alliances with the EU members through", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 50)
    draw_text("negotiations. While maintaining some traditional practices, you've", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 100)
    draw_text("made commitments to change key issues regarding human rights. This", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 150)
    draw_text("balanced approach has improved your standing with the EU, while", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 200)
    draw_text("keeping political opponents relatively at bay.", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 250)
    button1_rect = pygame.Rect(SCREEN_WIDTH -50 - BUTTON_WIDTH // 2, SCREEN_HEIGHT -10, BUTTON_WIDTH -50, BUTTON_HEIGHT -50)
    
    NEXT = Button(FONT, GREEN, button1_rect.x, button1_rect.y, BUTTON_WIDTH -50, BUTTON_HEIGHT -50, "Next")
   
    NEXT.draw(screen)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    display_course(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_alternatives_result(screen):
    screen.fill(WHITE)
    background = pygame.image.load("noEU.png").convert()
    screen.blit(background, (-60,0))

    turkey.WALK = True

    turkey.DIPLOMACY -= 5
    turkey.POLITICAL_STABILITY -= 2
    turkey.DEFENSE -= 2

    pygame.draw.rect(screen, WHITE, (10, 10, 1000, 260))
    
    draw_text("You have decided to step away from the EU and explore alternatives.", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 50)
    draw_text("Although this allows for some more innovation and flexibility, this", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 100)
    draw_text("decision has put you at odds with the international community. This", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 150)
    draw_text("drastic policy choice has sparked opposition to criticize your", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 200)
    draw_text("decision making.", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 250)

    button1_rect = pygame.Rect(SCREEN_WIDTH -50 - BUTTON_WIDTH // 2, SCREEN_HEIGHT -10, BUTTON_WIDTH -50, BUTTON_HEIGHT -50)
    
    NEXT = Button(FONT, GREEN, button1_rect.x, button1_rect.y, BUTTON_WIDTH -50, BUTTON_HEIGHT -50, "Next")
   
    NEXT.draw(screen)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    display_course(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_defense(screen):
    screen.fill(WHITE)
    background = pygame.image.load("defense.jpg").convert()
    screen.blit(background, (0,0))
    
    draw_text("How should the country defend itself?", FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    
    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    button2_rect = pygame.Rect(3 * SCREEN_WIDTH // 4 - OPT2_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT2_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Enhance Diplomatic Relations")
    opt2 = Button(OPT_FONT, GREEN, button2_rect.x, button2_rect.y, OPT2_WIDTH, BUTTON_HEIGHT, "Counterterrorism Efforts")

    opt1.draw(screen)
    opt2.draw(screen)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    display_relations(screen)
                elif is_button_clicked(mouse_pos, button2_rect):
                    display_counterterrorism(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_relations(screen):
    screen.fill(WHITE)
    background = pygame.image.load("defense.jpg").convert()
    screen.blit(background, (0,0))
    
    draw_text("How should the country improve its relations?", FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)

    turkey.RELATIONS = True
    
    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    button2_rect = pygame.Rect(3 * SCREEN_WIDTH // 4 - OPT2_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT2_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Leverage Cultural Ties")
    opt2 = Button(OPT_FONT, GREEN, button2_rect.x, button2_rect.y, OPT2_WIDTH, BUTTON_HEIGHT, "Strengthen Economic Connectivity")

    opt1.draw(screen)
    opt2.draw(screen)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    display_cultural_result(screen)
                elif is_button_clicked(mouse_pos, button2_rect):
                    display_strengthen_econ_result(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                
def display_cultural_result(screen):
    screen.fill(WHITE)
    background = pygame.image.load("culturalTies.jpg").convert()
    screen.blit(background, (0,0))

    pygame.draw.rect(screen, WHITE, (10, 10, 1000, 160))

    turkey.QUALITY_OF_LIFE += 2
    turkey.DIPLOMACY += 3
    turkey.POLITICAL_STABILITY -= 2
    
    draw_text("You have decided to use soft power and leverage cultural ties with", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 50)
    draw_text("neighboring countries. Although this doesn't give immediate results,", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 100)
    draw_text("this has improved your relationship with neighboring countries.", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 150)

    button1_rect = pygame.Rect(SCREEN_WIDTH -50 - BUTTON_WIDTH // 2, SCREEN_HEIGHT -10, BUTTON_WIDTH -50, BUTTON_HEIGHT -50)
    
    NEXT = Button(FONT, GREEN, button1_rect.x, button1_rect.y, BUTTON_WIDTH -50, BUTTON_HEIGHT -50, "Next")
   
    NEXT.draw(screen)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    display_course(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_strengthen_econ_result(screen):
    screen.fill(WHITE)
    background = pygame.image.load("connectivity.jpg").convert()
    screen.blit(background, (0,350))

    #pygame.draw.rect(screen, WHITE, (10, 10, 1000, 300))

    if turkey.TAXES:
        draw_text("You have chosen to increase economic interdependence with", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 50)
        draw_text("neighboring countries. This decision has built mutural trust", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 100)
        draw_text("with your neighbors. Due to your previous decision to raise", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 150)
        draw_text("taxes, the effect has been beneficial, but not as much as", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 200)
        draw_text("predicted. The tax increase has slightly discouraged trade", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 250)
        draw_text("between Turkey and neighboring countries, but there is still", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 300)
        draw_text("economic growth.", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 350)

        turkey.ECONOMIC_STRENGTH += 3
        turkey.DIPLOMACY += 4
        turkey.POLITICAL_STABILITY += 2
    
    elif turkey.INVESTMENT:
        draw_text("You have chosen to increase economic interdependence with", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 50)
        draw_text("neighboring countries. This decision has built mutural trust", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 100)
        draw_text("with your neighbors. Due to your previous decision to invest", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 150)
        draw_text("into your economy, the results have been very beneficial for", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 200)
        draw_text("you and the neighboring countries that Turkey is in agreement", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 250)
        draw_text("with. Despite some issues in neighboring countries, Turkey's", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 300)
        draw_text("economy is on the climb", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 350)

        turkey.ECONOMIC_STRENGTH += 6
        turkey.DIPLOMACY += 5
        turkey.POLITICAL_STABILITY += 3
        
    else:
        draw_text("You have chosen to increase economic interdependence with", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 50)
        draw_text("neighboring countries. This decision has built mutural trust", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 100)
        draw_text("with your neighbors and has benefited all included economies.", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 150)
        draw_text("However, the issues your neighbors are facing, the economy has", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 200)
        draw_text("not improved to the desired extent.", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 250)

        turkey.ECONOMIC_STRENGTH += 4
        turkey.DIPLOMACY += 4
        turkey.POLITICAL_STABILITY += 3

    button1_rect = pygame.Rect(SCREEN_WIDTH -50 - BUTTON_WIDTH // 2, SCREEN_HEIGHT -10, BUTTON_WIDTH -50, BUTTON_HEIGHT -50)
    
    NEXT = Button(FONT, GREEN, button1_rect.x, button1_rect.y, BUTTON_WIDTH -50, BUTTON_HEIGHT -50, "Next")
   
    NEXT.draw(screen)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    display_course(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_counterterrorism(screen):
    screen.fill(WHITE)
    background = pygame.image.load("defense.jpg").convert()
    screen.blit(background, (0,0))
    
    draw_text("How should the country counter terrorism?", FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    
    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    button2_rect = pygame.Rect(3 * SCREEN_WIDTH // 4 - OPT2_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT2_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Invest in Military")
    opt2 = Button(OPT_FONT, GREEN, button2_rect.x, button2_rect.y, OPT2_WIDTH, BUTTON_HEIGHT, "Combat Root Causes")

    opt1.draw(screen)
    opt2.draw(screen)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    display_military_result(screen)
                elif is_button_clicked(mouse_pos, button2_rect):
                    display_causes_result(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_military_result(screen):
    screen.fill(WHITE)
    background = pygame.image.load("military.jpg").convert()
    screen.blit(background, (0,0))

    pygame.draw.rect(screen, WHITE, (10, 10, 1000, 260))

    if turkey.REFORM or turkey.ALLIES:
        if turkey.SPENDING:
            draw_text("Because you have already chosen to reduce spending, your", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 50)
            draw_text("military is not at full strength. However, due to your", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 100)
            draw_text("improved relations with EU members, they have committed to", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 150)
            draw_text("helping your cause. With their help, your counterterrorism", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 200)
            draw_text("efforts have seen some success.", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 250)

            turkey.DEFENSE += 4
            turkey.POLITICAL_STABILITY += 3
    
        else:
            draw_text("Due to your improved relations with EU members, they have", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 50)
            draw_text("committed to helping your cause. With your newfound allies,", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 100)
            draw_text("along with the Turkish military, your counterterrorism", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 150)
            draw_text("efforts have seen great success! Your citizens are more", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 200)
            draw_text("confident in their safety than ever before.", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 250)

            turkey.DEFENSE += 8
            turkey.POLITICAL_STABILITY += 3

    elif turkey.SPENDING:
        draw_text("Because you have already chosen to reduce spending, your", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 50)
        draw_text("military is not at full strength. Because of this, your", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 100)
        draw_text("military has been unable to defend against multiple PPK", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 150)
        draw_text("demonstrations and attacks.", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 200)

        turkey.DEFENSE += 4
        
    else:
        draw_text("You have chosen to try to put a stop to the terrorist", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 50)
        draw_text("demonstrations in Turkey by strengthening the military.", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 100)
        draw_text("Although there has been definite improvements, the PKK is still", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 150)
        draw_text("a dominant force. The citizens of Turkey are feel more secure.", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 200)
        
        turkey.DEFENSE += 8

    button1_rect = pygame.Rect(SCREEN_WIDTH -50 - BUTTON_WIDTH // 2, SCREEN_HEIGHT -10, BUTTON_WIDTH -50, BUTTON_HEIGHT -50)
    
    NEXT = Button(FONT, GREEN, button1_rect.x, button1_rect.y, BUTTON_WIDTH -50, BUTTON_HEIGHT -50, "Next")
   
    NEXT.draw(screen)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    display_course(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_causes_result(screen):
    screen.fill(WHITE)
    background = pygame.image.load("terrorism.jpg").convert()
    screen.blit(background, (0,0))

    if turkey.SYRIA:
        #pygame.draw.rect(screen, WHITE, (10, 10, 1000, 410))
        draw_text("You chose to seek out the causes of terrorism in Turkey to", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 50)
        draw_text("counter Islamic extremism. Since your previously improved", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 100)
        draw_text("your cultural relations with Syria, they are more likely to", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 150)
        draw_text("allow Turkey's investigation. With Syria's support, it will be", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 200)
        draw_text("easier for Turkey to determine its next course of action to", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 250)
        draw_text("combat the causes of terrorism, such as securing the border", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 300)
        draw_text("between Turkey and Syria and implementing counter-radicalization", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 350)
        draw_text("programs.", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 400)

        turkey.POLITICAL_STABILITY += 4
        turkey.QUALITY_OF_LIFE += 3
    
    else:
        #pygame.draw.rect(screen, WHITE, (10, 10, 1000, 360))
        draw_text("You chose to seek out the causes of terrorism in Turkey to", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 50)
        draw_text("counter Islamic extremism. Due to the complex relationship with", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 100)
        draw_text("Syria, seeking out terrorism will be difficult without their", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 150)
        draw_text("support. Turkey's goal to combat terrorism at its root could be", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 200)
        draw_text("challenged by Syria's unwillingness to assit efforts. However,", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 250)
        draw_text("Turkey's determination will help slightly prevent terrorism", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 300)
        draw_text("growth.", FONT3, WHITE, screen, SCREEN_WIDTH // 2, 350)

        turkey.POLITICAL_STABILITY += 4
        turkey.DIPLOMACY -= 2
        turkey.QUALITY_OF_LIFE += 1

    button1_rect = pygame.Rect(SCREEN_WIDTH -50 - BUTTON_WIDTH // 2, SCREEN_HEIGHT -10, BUTTON_WIDTH -50, BUTTON_HEIGHT -50)
    
    NEXT = Button(FONT, GREEN, button1_rect.x, button1_rect.y, BUTTON_WIDTH -50, BUTTON_HEIGHT -50, "Next")
   
    NEXT.draw(screen)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    display_course(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        
# Function to display main screen
def display_main_screen(screen):
    screen.fill(WHITE)
    background = pygame.image.load("mainBackground.jpg").convert()
    screen.blit(background, (0,0))

    draw_text("State Savior", Title_Font, BLACK, screen, (SCREEN_WIDTH // 2) + 3, 78)
    draw_text("Manage Turkey to try to improve its overall score!", OPT_FONT, BLACK, screen, (SCREEN_WIDTH // 2) + 3, 151)
    
    draw_text("State Savior", Title_Font, WHITE, screen, SCREEN_WIDTH // 2, 75)
    draw_text("Manage Turkey to try to improve its overall score!", OPT_FONT, WHITE, screen, SCREEN_WIDTH // 2, 150)
    
    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - BUTTON_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, BUTTON_WIDTH, BUTTON_HEIGHT)
    button2_rect = pygame.Rect(3 * SCREEN_WIDTH // 4 - BUTTON_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, BUTTON_WIDTH, BUTTON_HEIGHT)
    
    play = Button(FONT, GREEN, button1_rect.x, button1_rect.y, BUTTON_WIDTH, BUTTON_HEIGHT, "Play")
    end = Button(FONT, RED, button2_rect.x, button2_rect.y, BUTTON_WIDTH, BUTTON_HEIGHT, "Exit")

    play.draw(screen)
    end.draw(screen)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    display_pre_screen(screen)
                elif is_button_clicked(mouse_pos, button2_rect):
                    pygame.quit()
                    sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

# Set up the screen
screen = pygame.display.set_mode((1024, 768))
#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("State Savior")

# Main loop
def main():
    display_main_screen(screen)

if __name__ == "__main__":
    main()
