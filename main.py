import pygame
from pygame.locals import *
import sys
from button import Button
from countryStats import Country

# Initialize Pygame
pygame.init()

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0,0,255)

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
FONT = pygame.font.SysFont(None, 50)
FONT2 = pygame.font.SysFont(None, 20)
FONT3 = pygame.font.SysFont(None, 35)

# Options font

OPT_FONT = pygame.font.SysFont(None, 30)

# choices made
CHOICES = []

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
    draw_text("Turkey is facing four main issues: A refugee crisis, economic challenges,", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 30)
    draw_text("maintaining relaitons with the UN, and maintaining its defence", FONT3, BLACK, screen, SCREEN_WIDTH // 2, 60)
    draw_text("Refugee Crisis: ", FONT, BLACK, screen, SCREEN_WIDTH // 4, 100)
    draw_text("Turkey currently hosts the most refugees in the world at 3.6 million.", FONT2, BLACK, screen, SCREEN_WIDTH // 4, 125)
    draw_text("This large influx has put straing on resources and infrastructure, presenting", FONT2, BLACK, screen, SCREEN_WIDTH // 4, 150)
    draw_text("Challenges for Turkey. Despite some previous efforts to remedy this issue,", FONT2, BLACK, screen, SCREEN_WIDTH // 4, 175)
    draw_text("refugees continue to flood into Turkey", FONT2, BLACK, screen, SCREEN_WIDTH // 4, 200)
    
    draw_text("Economic Issues: ", FONT, BLACK, screen, SCREEN_WIDTH - (SCREEN_WIDTH // 4), 100)
    draw_text("Turkey has faced many economic challenges recently, such as high inflation,", FONT2, BLACK, screen, SCREEN_WIDTH - (SCREEN_WIDTH // 4), 125)
    draw_text("a weakening currency, and rising unenployment rates. These issues have only ", FONT2, BLACK, screen, SCREEN_WIDTH - (SCREEN_WIDTH // 4), 150)
    draw_text("grown worse due to the various other issues Turkey is facing right now. The", FONT2, BLACK, screen, SCREEN_WIDTH - (SCREEN_WIDTH // 4), 175)
    draw_text("Turkish lira is now worth 0.031 USD, decreasing in value by 141% since", FONT2, BLACK, screen, SCREEN_WIDTH - (SCREEN_WIDTH // 4), 200)
    draw_text("2019. Additionally, a large spending deficit and high natinoal debt have", FONT2, BLACK, screen, SCREEN_WIDTH - (SCREEN_WIDTH // 4), 225)
    draw_text("led to increased challenges for the country.", FONT2, BLACK, screen, SCREEN_WIDTH - (SCREEN_WIDTH // 4), 250)
    

    draw_text("UN Relations: ", FONT, BLACK, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT - 300)
    draw_text("Turkeys current relationship with the UN is complicated. Although Turkey", FONT2, BLACK, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT - 275)
    draw_text("does participate in UN programs, tensions have been rising between the UN", FONT2, BLACK, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT - 250)
    draw_text("and Turkey over policy dissagreements. The UN has become concerned with", FONT2, BLACK, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT - 225)
    draw_text("human rights issues in Turkey, with Turkey coming under fire from the UN ", FONT2, BLACK, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT - 200)
    draw_text("because of a lack of freedom of expression, press, and assembly. Turkey has", FONT2, BLACK, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT - 175)
    draw_text("reportedly been restricting media access as well, all sparking concerns that", FONT2, BLACK, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT - 150)
    draw_text("Turkey is not being complient with UN standards.", FONT2, BLACK, screen, SCREEN_WIDTH // 4, SCREEN_HEIGHT - 125)
    
    draw_text("Defence: ", FONT, BLACK, screen, SCREEN_WIDTH - (SCREEN_WIDTH // 4), SCREEN_HEIGHT - 300)
    draw_text("Turkeys defence decisions are determined by both internal and external factors.", FONT2, BLACK, screen, SCREEN_WIDTH - (SCREEN_WIDTH // 4), SCREEN_HEIGHT - 275)
    draw_text("The Kurdistan Workers' Party (PKK) is a militant terrorist organization causing", FONT2, BLACK, screen, SCREEN_WIDTH - (SCREEN_WIDTH // 4), SCREEN_HEIGHT - 250)
    draw_text("uprises throughout Turkey, leading to civil unrest and instability. While", FONT2, BLACK, screen, SCREEN_WIDTH - (SCREEN_WIDTH // 4), SCREEN_HEIGHT - 225)
    draw_text("the country is dealing with this issue, Turkey is involved abroad in a Syrian", FONT2, BLACK, screen, SCREEN_WIDTH - (SCREEN_WIDTH // 4), SCREEN_HEIGHT - 200)
    draw_text("conflict. While Turkey works to handle both these situations, maintaining ", FONT2, BLACK, screen, SCREEN_WIDTH - (SCREEN_WIDTH // 4), SCREEN_HEIGHT - 175)
    draw_text("international relationships is key.", FONT2, BLACK, screen, SCREEN_WIDTH - (SCREEN_WIDTH // 4), SCREEN_HEIGHT - 150)
    
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
    screen.blit(background, (-200,0))
    draw_text("What should the focus be for this year you govern?", FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    draw_text(str(CHOICES), FONT, BLACK, screen, SCREEN_WIDTH // 2, 150)

    button1_rect = pygame.Rect(0,0,1,1)
    button2_rect = pygame.Rect(0,0,1,1)
    button3_rect = pygame.Rect(0,0,1,1)
    button4_rect = pygame.Rect(0,0,1,1)
    button5_rect = pygame.Rect(0,0,1,1)

    if len(CHOICES) < 3:
        if R not in CHOICES:
            button1_rect = pygame.Rect(50, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
            opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Refugee Crisis")
            opt1.draw(screen)
        if E not in CHOICES:
            button2_rect = pygame.Rect(550, SCREEN_HEIGHT // 2 - 50, OPT2_WIDTH, BUTTON_HEIGHT)
            opt2 = Button(OPT_FONT, GREEN, button2_rect.x, button2_rect.y, OPT2_WIDTH, BUTTON_HEIGHT, "Economic Challenges")
            opt2.draw(screen)
        if EU not in CHOICES:
            button3_rect = pygame.Rect(50, SCREEN_HEIGHT // 2 + 150, OPT2_WIDTH, BUTTON_HEIGHT)
            opt3 = Button(OPT_FONT, BLUE, button3_rect.x, button3_rect.y, OPT2_WIDTH, BUTTON_HEIGHT, "European Union Relations")
            opt3.draw(screen)
        if D not in CHOICES:
            button4_rect = pygame.Rect(550, SCREEN_HEIGHT // 2 + 150, OPT2_WIDTH, BUTTON_HEIGHT)
            opt4 = Button(OPT_FONT, (255,125,0), button4_rect.x, button4_rect.y, OPT2_WIDTH, BUTTON_HEIGHT, "Defense")
            opt4.draw(screen)
    elif len(CHOICES) > 2:
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
                    CHOICES.append(R)
                    display_refugee(screen)
                elif is_button_clicked(mouse_pos, button2_rect):
                    CHOICES.append(E)
                    display_economic(screen)
                elif is_button_clicked(mouse_pos, button3_rect):
                    CHOICES.append(EU)
                    display_EU(screen)
                elif is_button_clicked(mouse_pos, button4_rect):
                    CHOICES.append(D)
                    display_defense(screen)
                elif is_button_clicked(mouse_pos, button5_rect):
                    display_end_of_game(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_end_of_game(screen):
    screen.fill(WHITE)
    background = pygame.image.load("course.jpg").convert()
    screen.blit(background, (-200,0))
    CHOICES = []
    draw_text("After governing Turkey for 3 years, here are the results:", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    
    draw_text("Economic Strength:", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 100)
    draw_text(str(turkey.ECONOMIC_STRENGTH), OPT_FONT, BLACK, screen, (SCREEN_WIDTH // 2) + 120, 100)

    draw_text("Quality of Life:", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 120)
    draw_text(str(turkey.QUALITY_OF_LIFE), OPT_FONT, BLACK, screen, (SCREEN_WIDTH // 2) + 120, 120)

    draw_text("Political Stability:", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 140)
    draw_text(str(turkey.POLITICAL_STABILITY), OPT_FONT, BLACK, screen, (SCREEN_WIDTH // 2) + 120, 140)

    draw_text("Diplomacy:", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 160)
    draw_text(str(turkey.DIPLOMACY), OPT_FONT, BLACK, screen, (SCREEN_WIDTH // 2) + 120, 160)

    draw_text("Infrastructure:", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 180)
    draw_text(str(turkey.INFRASTRUCTURE), OPT_FONT, BLACK, screen, (SCREEN_WIDTH // 2) + 120, 180)

    draw_text("Defense:", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 200)
    draw_text(str(turkey.DEFENSE), OPT_FONT, BLACK, screen, (SCREEN_WIDTH // 2) + 120, 200)

    OVERALL = ( turkey.ECONOMIC_STRENGTH + turkey.QUALITY_OF_LIFE + turkey.POLITICAL_STABILITY + turkey.DIPLOMACY + turkey.INFRASTRUCTURE + turkey.DEFENSE ) // 6
    draw_text("Overall:", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 220)
    draw_text(str(OVERALL), OPT_FONT, BLACK, screen, (SCREEN_WIDTH // 2) + 120, 220)    

    button1_rect = pygame.Rect(50, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Main Menu")
    opt1.draw(screen)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_button_clicked(mouse_pos, button1_rect):
                    print(CHOICES)
                    display_main_screen(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_economic(screen):
    screen.fill(WHITE)
    background = pygame.image.load("economyDown.jpg").convert()
    screen.blit(background, (0,0))
    
    draw_text("How should the country proceed?", FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    
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

    background = pygame.image.load("economyDown.jpg").convert()
    screen.blit(background, (0,0))
    
    draw_text("How do you want to take stimulus measures?", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    
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
    background = pygame.image.load("economyDown.jpg").convert()
    screen.blit(background, (0,0))
    
    draw_text("You increased investment into the economy, stimulating growth in the short run.", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)

    turkey.INVESTMENT = True

    turkey.ECONOMIC_STRENGTH += 5
    
    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    button2_rect = pygame.Rect(3 * SCREEN_WIDTH // 4 - OPT2_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT2_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Next")

    opt1.draw(screen)
    
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
    background = pygame.image.load("economyDown.jpg").convert()
    screen.blit(background, (0,0))
    
    draw_text("You made direct cash transfers to citizens, stimulating economic growth in the short run.", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)

    turkey.ECONOMIC_STRENGTH += 5
    
    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    button2_rect = pygame.Rect(3 * SCREEN_WIDTH // 4 - OPT2_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT2_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Next")

    opt1.draw(screen)
    
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
    background = pygame.image.load("economyDown.jpg").convert()
    screen.blit(background, (0,0))
    
    draw_text("How do you want to take austerity measures?", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    
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

    turkey.ECONOMIC_STRENGTH += 5
    turkey.QUALITY_OF_LIFE -= 3
    
    draw_text("You reduced government spending, cutting social welfare programs and pension reforms, causing", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    draw_text("protests and challenges to political stability. The reduced spending, on the other hand, has", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 100)
    draw_text("reduced governmental budget issues, imporved investor confidence, and more stable inflation.", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 150)

    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Next")

    opt1.draw(screen)
    
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
    background = pygame.image.load("economyDown.jpg").convert()
    screen.blit(background, (0,0))

    turkey.TAXES = True

    turkey.ECONOMIC_STRENGTH += 5
    turkey.INFRASTRUCTURE += 3
    turkey.QUALITY_OF_LIFE -=2
    turkey.POLITICAL_STABILITY -=2
    
    draw_text("You increased taxes, sparking protests, challenging social cohesion and political stability.", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    draw_text("Tax increases have reduced the overall demand of the economy. However, governmental budget", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 100)
    draw_text("deficits have been cut and inflation is at a more stable level. ", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 150)

    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Next")

    opt1.draw(screen)
    
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
    background = pygame.image.load("economyDown.jpg").convert()
    screen.blit(background, (0,0))
    
    draw_text("How should the country proceed?", FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    
    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    button2_rect = pygame.Rect(3 * SCREEN_WIDTH // 4 - OPT2_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT2_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "International Cooperation")
    opt2 = Button(OPT_FONT, GREEN, button2_rect.x, button2_rect.y, OPT2_WIDTH, BUTTON_HEIGHT, "Internal Empowerment")

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
                    display_internal_emp(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_international_coop(screen):
    screen.fill(WHITE)
    background = pygame.image.load("economyDown.jpg").convert()
    screen.blit(background, (0,0))
    
    draw_text("How should Turkey go about international affairs?", FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    
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
    background = pygame.image.load("economyDown.jpg").convert()
    screen.blit(background, (0,0))

    turkey.DIPLOMACY += 7
    turkey.POLITICAL_STABILITY += 2
    turkey.INFRASTRUCTURE += 1

    if turkey.REFORM:
        draw_text("You have decided to address the refugee crisis by consulting the United Nations.", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
        draw_text("Since you have previously decided to reform to European Union Standards, the United", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 100)
        draw_text("Nations is more likely to support Turkey. With the aid from the UN, refugees have", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 150)
        draw_text("seen improvements in living conditions and quality of life.", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 200)
    elif turkey.ALLIES:
        draw_text("You have decided to address the refugee crisis by consulting the United Nations.", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
        draw_text("This approach will take time, but citizens are already starting to see improvements due", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 100)
        draw_text("to the aid from neighboring allies. Although the UN is not yet directly involved, they", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 150)
        draw_text("have made a statement promising future support for the refugees in Turkey.", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 200)
    elif turkey.WALK:
        draw_text("You have decided to address the refugee crisis by consulting the United Nations. Since you", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
        draw_text("have previously walked away from attempts to join the European Union, EU countries in the", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 100)
        draw_text("UN have been less responsive to Turkey's calls for aid. You hope other opportunities can help", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 150)
        draw_text("improve the well being of the refugees, but for now their quality of life only slightly improves.", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 200)
    else:
        draw_text("You have decided to address the refugee crisis by consulting the United Nations. Due to", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
        draw_text("Turkey's complex relationship with the UN, they have been slightly receptive to your call", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 100)
        draw_text("for help. They have supplied aid, but not as much as necessary to greatly improve refugee", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 150)
        draw_text("quality of life.", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 200)

    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Next")

    opt1.draw(screen)
    
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
    background = pygame.image.load("economyDown.jpg").convert()
    screen.blit(background, (0,0))

    turkey.SYRIA = True

    turkey.DIPLOMACY += 5
    turkey.DEFENSE -= 2

    if turkey.RELATIONS:
        draw_text("You have decided to address the refugee crisis by addressing the Syrian issue at its", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
        draw_text("core. This is a solid approach and shows your commitment to the issue. Because of your", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 100)
        draw_text("previous commitments, your relationship with Syria has improved, resulting to them being", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 150)
        draw_text("receptive, helping greatly to your efforts.", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 150)
    else:
        draw_text("You have decided to address the refugee crisis by addressing the Syrian issue at its", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
        draw_text("core. This is a solid approach and shows your commitment to the issue. However, geopolitical", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 100)
        draw_text("issues and strains in your relationship with neighboring countries have slowed down results.", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 150)

    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Next")

    opt1.draw(screen)
    
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

def display_internal_emp(screen):
    screen.fill(WHITE)
    background = pygame.image.load("economyDown.jpg").convert()
    screen.blit(background, (0,0))

    turkey.INTERNAL = True
    
    draw_text("How should Turkey support refugees within the country?", FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    
    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    button2_rect = pygame.Rect(3 * SCREEN_WIDTH // 4 - OPT2_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT2_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Improve Opportunities")
    opt2 = Button(OPT_FONT, GREEN, button2_rect.x, button2_rect.y, OPT2_WIDTH, BUTTON_HEIGHT, "Promote Acceptance")

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
                    display_acceptance_result(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_opportunity_result(screen):
    screen.fill(WHITE)
    background = pygame.image.load("economyDown.jpg").convert()
    screen.blit(background, (0,0))

    turkey.QUALITY_OF_LIFE += 5
    turkey.INFRASTRUCTURE += 2
    
    
    draw_text("You decided to improve opportunities for refugees. This has led to improvements in education", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    draw_text("and the job market. However, word of these improved opportunities has spread, attracting more", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 100)
    draw_text("refugees to seek asylum in Turkey, putting a strain on resources, and exacerbating the refugee crisis.", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 150)

    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Next")

    opt1.draw(screen)
    
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

def display_acceptance_result(screen):
    screen.fill(WHITE)
    background = pygame.image.load("economyDown.jpg").convert()
    screen.blit(background, (0,0))

    turkey.QUALITY_OF_LIFE += 5
    turkey.POLITICAL_STABILITY += 3
    turkey.ECONOMIC_STRENGTH -= 2
    
    draw_text("You chose to deal with the refugee crisis by increasing acceptance. While many are grateful", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    draw_text("for Turkey's assistance in housing refugees, this massive influx has put a massive strain on", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 100)
    draw_text("the economy. Despite efforts to support and integrate refugees, the increased demand for", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 150)
    draw_text("resources has stretched the government to its limits, prompting citizens to resent the refugees.", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 200)
    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Next")

    opt1.draw(screen)
    
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
    background = pygame.image.load("economyDown.jpg").convert()
    screen.blit(background, (0,0))
    
    draw_text("How should the country proceed?", FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    
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
    background = pygame.image.load("economyDown.jpg").convert()
    screen.blit(background, (0,0))
    
    draw_text("How should the country reform to fit EU standards?", FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    
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
    background = pygame.image.load("economyDown.jpg").convert()
    screen.blit(background, (0,0))

    turkey.QUALITY_OF_LIFE += 8
    turkey.POLITICAL_STABILITY += 3
    turkey.INFRASTRUCTURE += 2
    turkey.ECONOMIC_STRENGTH -=1
    
    draw_text("You have chosen to make reforms and protect the human rights of the citizens of Turkey. As", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    draw_text("a result, your citizens have become happier and you are in better standing with the UN. However,", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 100)
    draw_text("some of your reforms have faced backlash from domestic stakeholders, slowing down progress.", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 150)

    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Next")

    opt1.draw(screen)
    
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
    background = pygame.image.load("economyDown.jpg").convert()
    screen.blit(background, (0,0))

    turkey.POLITICAL_STABILITY += 8
    turkey.ECONOMIC_STRENGTH -= 2
    turkey.DIPLOMACY += 2

    draw_text("You have chosen to increase democracy within the country. Although this decision was met", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    draw_text("with backlash from the interests of influential steakholders and political opposition.", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 100)
    draw_text("Despite these obstacles, you have gained the trust of the UN and promoted stability domestically.", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 150)

    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Next")

    opt1.draw(screen)
    
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
    background = pygame.image.load("economyDown.jpg").convert()
    screen.blit(background, (0,0))
    
    draw_text("How should the country negotiate with the UN?", FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    
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
    background = pygame.image.load("economyDown.jpg").convert()
    screen.blit(background, (0,0))

    turkey.ALLIES = True

    turkey.DIPLOMACY += 5
    turkey.DEFENSE += 3
    turkey.POLITICAL_STABILITY += 2
    turkey.QUALITY_OF_LIFE -= 2
    
    draw_text("You have built back alliances with the EU members through negotiations. While maintaining some traditional", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    draw_text("practices, you've made commitments to change key issues regarding human rights. This balanced", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 100)
    draw_text("approach has improved your standing with the EU, while keeping political opponents relatively at bay.", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 150)

    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Next")

    opt1.draw(screen)
    
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
    background = pygame.image.load("economyDown.jpg").convert()
    screen.blit(background, (0,0))

    turkey.WALK = True

    turkey.DIPLOMACY += 2
    turkey.POLITICAL_STABILITY += 3
    
    draw_text("You have decided to step away from the EU and explore alternatives. Although this", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    draw_text("allows for some more innovation and flexibility, this decision has put you at odds with", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 100)
    draw_text("the internatinoal community. This durastic policy choice has sparked opposition to", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 150)
    draw_text("criticize your decision making.", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 200)

    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Next")

    opt1.draw(screen)
    
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
    background = pygame.image.load("economyDown.jpg").convert()
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
    background = pygame.image.load("economyDown.jpg").convert()
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
    background = pygame.image.load("economyDown.jpg").convert()
    screen.blit(background, (0,0))

    turkey.QUALITY_OF_LIFE += 2
    turkey.DIPLOMACY += 3
    turkey.POLITICAL_STABILITY -= 2
    
    draw_text("You have decided to use soft power and leverage cultural ties with neighboring", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    draw_text("countries. Although this doesn't give immediate results, this has improved your", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 100)
    draw_text("relationship with neighboring countries.", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 150)

    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Next")

    opt1.draw(screen)
    
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
    background = pygame.image.load("economyDown.jpg").convert()
    screen.blit(background, (0,0))

    turkey.ECONOMIC_STRENGTH += 4
    turkey.DIPLOMACY += 7
    turkey.POLITICAL_STABILITY += 2
    
    draw_text("You have chosen to increase economic interdependence with neighboring countries", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    draw_text("This decision has built mutural trust with your neighbors. However, the issues", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 100)
    draw_text("your neighbors are facing have slightly stifled your economy.", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 150)

    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Next")

    opt1.draw(screen)
    
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
    background = pygame.image.load("economyDown.jpg").convert()
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
    background = pygame.image.load("economyDown.jpg").convert()
    screen.blit(background, (0,0))

    turkey.DEFENSE += 8
    turkey.POLITICAL_STABILITY += 3
    
    
    draw_text("Explain this result", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    draw_text("Explain this result", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 100)
    draw_text("Explain this result", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 150)

    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Next")

    opt1.draw(screen)
    
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
    background = pygame.image.load("economyDown.jpg").convert()
    screen.blit(background, (0,0))

    turkey.DIPLOMACY -= 3
    turkey.POLITICAL_STABILITY += 4
    
    draw_text("Explain this result", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    draw_text("Explain this result", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 100)
    draw_text("Explain this result", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 150)

    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Next")

    opt1.draw(screen)
    
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
    
    draw_text("State Savior", FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    draw_text("Manage Turkey to try to get the country above a 70 overall", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 150)
    
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
#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("State Savior")

# Main loop
def main():
    display_main_screen(screen)

if __name__ == "__main__":
    main()
