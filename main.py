import pygame
from pygame.locals import *
import sys
from button import Button

# Initialize Pygame
pygame.init()

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

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

# Options font

OPT_FONT = pygame.font.SysFont(None, 30)

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

# Function to display options screen
def display_first_course(screen):
    screen.fill(WHITE)
    draw_text("What should the focus be for the first year you govern?", FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    
    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    button2_rect = pygame.Rect(3 * SCREEN_WIDTH // 4 - OPT2_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT2_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Refugee Crisis")
    opt2 = Button(OPT_FONT, GREEN, button2_rect.x, button2_rect.y, OPT2_WIDTH, BUTTON_HEIGHT, "Economic Challenges")

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
                    print("Option 1 selected!")
                elif is_button_clicked(mouse_pos, button2_rect):
                    display_economic(screen)
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
    draw_text("You increased investment into the economy, stimulating growth in the short run.", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    
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
                    display_second_course_E(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_cash_result(screen):
    screen.fill(WHITE)
    draw_text("You made direct cash transfers to citizens, stimulating economic growth in the short run.", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    
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
                    display_second_course_E(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()


def display_economic_aust(screen):
    screen.fill(WHITE)
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
                    display_second_course_E(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_tax_result(screen):
    screen.fill(WHITE)
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
                    display_second_course_E(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_second_course_E(screen):
    screen.fill(WHITE)
    draw_text("What should the focus be for the second year you govern?", FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    
    button1_rect = pygame.Rect(SCREEN_WIDTH // 4 - OPT1_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT1_WIDTH, BUTTON_HEIGHT)
    button2_rect = pygame.Rect(3 * SCREEN_WIDTH // 4 - OPT2_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, OPT2_WIDTH, BUTTON_HEIGHT)
    
    opt1 = Button(OPT_FONT, RED, button1_rect.x, button1_rect.y, OPT1_WIDTH, BUTTON_HEIGHT, "Refugee Crisis")
    opt2 = Button(OPT_FONT, GREEN, button2_rect.x, button2_rect.y, OPT2_WIDTH, BUTTON_HEIGHT, "European Union Relations")

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
                    display_refugee(screen)
                elif is_button_clicked(mouse_pos, button2_rect):
                    display_economic(screen)
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
                    print("h")
                    #display_economic_stim(screen)
                elif is_button_clicked(mouse_pos, button2_rect):
                    print("d")
                    #display_economic_aust(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def display_internal_emp(screen):
    screen.fill(WHITE)

    background = pygame.image.load("economyDown.jpg").convert()

    screen.blit(background, (0,0))
    
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
                    print("d")
                    #display_economic_stim(screen)
                elif is_button_clicked(mouse_pos, button2_rect):
                    print("d")
                    #display_economic_aust(screen)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        
# Function to display main screen
def display_main_screen(screen):
    screen.fill(WHITE)
    draw_text("State Savior", FONT, BLACK, screen, SCREEN_WIDTH // 2, 50)
    draw_text("Manage Turkey for 4 years without getting impeached!", OPT_FONT, BLACK, screen, SCREEN_WIDTH // 2, 150)
    
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
                    display_first_course(screen)
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
