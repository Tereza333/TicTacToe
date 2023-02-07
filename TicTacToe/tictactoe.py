import time
import pygame_menu
from pygame_menu import themes
import pygame as pg
import numpy as np
import pygame
import random
import copy
import sys

# sound effects
pygame.mixer.init()
pygame.mixer.music.load("the-sound-of-the-entire-game.mp3")
pygame.mixer.music.play(loops=-1)

sound_victory = pygame.mixer.Sound("sound-of-victory.mp3")
gameOver = pygame.mixer.Sound("game over.mp3")
ixik_nolik = pygame.mixer.Sound("ixik-nolik-voice.mp3")
button_sound = pygame.mixer.Sound("button-sound.mp3")
loading = pygame.mixer.Sound("loading1.wav")
account = pygame.mixer.Sound("winning.mp3")

# screen creation
pygame.init()
screen = pygame.display.set_mode((500, 500), pygame.NOFRAME)
pygame.display.set_caption('Tic Tac Toe')
pygame.display.flip()
imp = pygame.image.load("44.png").convert()
DEFAULT_IMAGE_SIZE = (500, 500)
image = pygame.transform.scale(imp, DEFAULT_IMAGE_SIZE)
screen.blit(pygame.transform.scale(imp, (500, 500)), (0, 0))

buttons = []
score1 = 0
score2 = 0
score3 = 0
score4 = 0
score5 = 0
score6 = 0

# Button creation
class Button:
    def __init__(self, text, translation, width, height, pos, elevation):
        # Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.original_y_pos = pos[1]

        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#1E90FF'
        self.translation = translation
        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, height))
        self.bottom_color = '#009ACD'
        # text
        self.text = text
        self.text_surf = gui_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
        buttons.append(self)


    def draw(self):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=12)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = "#FF4040"
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed == True:
                    # self.pressed = False

                    surface = pygame.display.set_mode((500, 500), pygame.NOFRAME)
                    pygame.display.update()


                    def smenu():
                        mainmenu._open(player1option)

                    def ssmenu():
                        mainmenu._open(player2option)


                    def level_menu():
                        global score1, score2, score3, score4, score5, score6
                        screen = pg.display.set_mode((500, 500), pg.NOFRAME)
                        pg.display.flip()
                        Img = pg.image.load('TicTac.jpg').convert()
                        Image_Size = (500, 500)
                        image = pg.transform.scale(Img, Image_Size)
                        screen.blit(pg.transform.scale(Img, (500, 500)), (0, 0))

                        color = (0, 0, 0)
                        # light shade of the button
                        color_light = (170, 170, 170)
                        # stores the width and height of the screen into a variable
                        wth = screen.get_width()
                        hght = screen.get_height()
                        # defining a font
                        smallfont = pg.font.SysFont('Corbel', 40)
                        font2 = pg.font.SysFont('Segoe UI', 40)
                        font3 = pg.font.SysFont('serif', 40)
                        text_2player = font3.render('2 Player', True, color)
                        text_1player = font3.render('1 Player', True, color)
                        account.play()
                        text2 = smallfont.render('Win | Draw | Lose', True, color)
                        text7 = smallfont.render('Win | Draw | Lose', True, color)
                        text3 = smallfont.render('Back', True, color)
                        text4 = font2.render(str(int(score1/300)), True, color)
                        text5 = font2.render(str(int(score2/300)), True, color)
                        text_score3 = font2.render(str(int(score3/300)), True, color)
                        text_score4 = font2.render(str(int(score4/300)), True, color)
                        text_score5 = font2.render(str(int(score5 / 300)), True, color)
                        text_score6 = font2.render(str(int(score6 / 300)), True, color)
                        pg.draw.rect(screen, color_light, [(wth / 3 - 130), (hght / 2 + 115), 140, 40])
                        screen.blit(text_2player, (wth / 3 + 160, hght / 2 - 140))
                        screen.blit(text_1player, (wth / 3 + 160, hght / 2 + 30))
                        screen.blit(text2, (wth / 3 + 40, hght / 2 - 90))
                        screen.blit(text7, (wth / 3 + 40, hght / 2 + 90))
                        # superimposing the text onto our button
                        screen.blit(text3, (wth / 3 - 100, hght / 2 + 115))
                        screen.blit(text_score3, (wth / 3 + 160, hght / 2 - 40))
                        screen.blit(text5, (wth / 3 + 250, hght / 2 - 40))
                        screen.blit(text4, (wth / 3 + 70, hght / 2 - 40))
                        screen.blit(text_score4, (wth / 3 + 70, hght / 2 + 130))
                        screen.blit(text_score5, (wth / 3 + 160, hght / 2 + 130))
                        screen.blit(text_score6, (wth / 3 + 250, hght / 2 + 130))

                        while True:
                            for ev in pg.event.get():
                                if ev.type == pg.QUIT:
                                    pg.quit()
                                    # checks if a mouse is clicked
                                if ev.type == pg.MOUSEBUTTONDOWN:
                                    # if the mouse is clicked on the button the game is terminated
                                    mouse = pg.mouse.get_pos()
                                    if wth / 3 - 120 <= mouse[0] <= wth / 3 and hght / 2 <= mouse[1] <= hght / 2 + 140:
                                        player1option = pygame_menu.Menu('Select a Difficulty', 500, 500,
                                                                         theme=themes.THEME_BLUE)


                                        player1option = pygame_menu.Menu('Menu', 500, 500,
                                                                         theme=themes.THEME_BLUE)

                                        player1option.add.button("Restart", smenu)
                                        button_sound.play()
                                        player1option.add.button("Score", level_menu)
                                        player1option.add.button("Quit", pygame_menu.events.EXIT)
                                        button_sound.play()


                                        arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15))

                                        while True:
                                            events = pygame.event.get()
                                            for event in events:
                                                pass

                                                if event.type == pygame.QUIT:
                                                    exit()
                                            if mainmenu.is_enabled():
                                                mainmenu.update(events)
                                                mainmenu.draw(surface)
                                                if (mainmenu.get_current().get_selected_widget()):
                                                    arrow.draw(surface, mainmenu.get_current().get_selected_widget())
                                            pygame.display.update()
                                    else:
                                        self.dynamic_elecation = self.elevation
                                        self.top_color = '#00BFFF'

                            # updates the frames of the game
                            pg.display.update()


                    def player1():  # Play with computer
                        mainmenu._open(player1option)
                        button_sound.play()
                        time.sleep(0.2)

                        # Loading start
                        pygame.init()
                        loading.play()

                        width = 500
                        height = 500
                        fps = 60
                        speed = 130
                        fps = 90
                        speed = 180

                        boarder_rect = [20, 325, 260, 50]
                        inner_rect = [25, 330, 0, 40]
                        green = (0, 154, 205)
                        white = (199, 206, 230)
                        surface = pygame.display.set_mode((width, height), pygame.NOFRAME)
                        f = pygame.font.SysFont("myriadProFont", 50)
                        text = f.render(" LOADING... ", 1, (0, 154, 205), (199, 206, 230))
                        x, y = 155, 140

                        clock = pygame.time.Clock()
                        gameloop = True
                        surface.fill(white)
                        surface.blit(text, (x, y))

                        while gameloop == True:
                            clock.tick(fps)

                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    gameloop = False
                            if inner_rect[2] <= 249:
                                inner_rect[2] += speed / fps
                            if inner_rect[2] - 2 == 248.0:
                                break

                            pygame.draw.rect(surface, green, (120, 190, 260, 50), 3)
                            pygame.draw.rect(surface, green, (125, 195, int(inner_rect[2]), (inner_rect[3])))
                            pygame.display.flip()
                            clock.tick(95)

                        WIDTH = 500  # Play with computer
                        HEIGHT = 500
                        ROWS = 3
                        COLS = 3
                        SQSIZE = WIDTH // COLS
                        LINE_WIDTH = 15
                        CIRC_WIDTH = 15
                        CROSS_WIDTH = 20
                        RADIUS = SQSIZE // 4
                        OFFSET = 50

                        # colors
                        BG_COLOR = (230,230,250)
                        LINE_COLOR = (0,154,205)
                        CIRC_COLOR = (255,64,64)
                        CROSS_COLOR = (0,201,87)

                        # pygame setup
                        pygame.init()
                        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
                        screen.fill(BG_COLOR)

                        # pygame setup
                        pygame.init()
                        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
                        pygame.display.set_caption('TicTacToeAI')
                        screen.fill(BG_COLOR)

                        # classes
                        class Board:
                            def __init__(self):
                                self.squares = np.zeros((ROWS, COLS))
                                self.empty_sqrs = self.squares  # [squares]
                                self.marked_sqrs = 0

                            def final_state(self, show=False):
                                # @return 0 if there is no win yet
                                # @return 1 if player 1 wins
                                # @return 2 if player 2 wins
                                # vertical wins
                                for col in range(COLS):
                                    if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                                        if show:
                                            color = CIRC_COLOR if self.squares[0][col] == 2 else CROSS_COLOR
                                            iPos = (col * SQSIZE + SQSIZE // 2, 20)
                                            fPos = (col * SQSIZE + SQSIZE // 2, HEIGHT - 20)
                                            pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH)
                                        return self.squares[0][col]
                                # horizontal wins
                                for row in range(ROWS):
                                    if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                                        if show:
                                            color = CIRC_COLOR if self.squares[row][0] == 2 else CROSS_COLOR
                                            iPos = (20, row * SQSIZE + SQSIZE // 2)
                                            fPos = (WIDTH - 20, row * SQSIZE + SQSIZE // 2)
                                            pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH)
                                        return self.squares[row][0]
                                # desc diagonal
                                if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
                                    if show:
                                        color = CIRC_COLOR if self.squares[1][1] == 2 else CROSS_COLOR
                                        iPos = (20, 20)
                                        fPos = (WIDTH - 20, HEIGHT - 20)
                                        pygame.draw.line(screen, color, iPos, fPos, CROSS_WIDTH)
                                    return self.squares[1][1]
                                # asc diagonal
                                if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
                                    if show:
                                        color = CIRC_COLOR if self.squares[1][1] == 2 else CROSS_COLOR
                                        iPos = (20, HEIGHT - 20)
                                        fPos = (WIDTH - 20, 20)
                                        pygame.draw.line(screen, color, iPos, fPos, CROSS_WIDTH)
                                    return self.squares[1][1]
                                # no win yet
                                return 0

                            def mark_sqr(self, row, col, player):
                                self.squares[row][col] = player
                                self.marked_sqrs += 1

                            def empty_sqr(self, row, col):
                                return self.squares[row][col] == 0

                            def get_empty_sqrs(self):
                                empty_sqrs = []
                                for row in range(ROWS):
                                    for col in range(COLS):
                                        if self.empty_sqr(row, col):
                                            empty_sqrs.append((row, col))
                                return empty_sqrs

                            def isfull(self):
                                return self.marked_sqrs == 9

                            def isempty(self):
                                return self.marked_sqrs == 0

                        class AI:

                            def __init__(self, level=1, player=2):
                                self.level = level
                                self.player = player

                            def rnd(self, board):
                                empty_sqrs = board.get_empty_sqrs()
                                idx = random.randrange(0, len(empty_sqrs))
                                return empty_sqrs[idx]  # (row, col)

                            # minimax
                            def minimax(self, board, maximizing):
                                # terminal case
                                case = board.final_state()
                                # player 1 wins
                                if case == 1:
                                    return 1, None  # eval, move
                                # player 2 wins
                                if case == 2:
                                    return -1, None
                                # draw
                                elif board.isfull():
                                    return 0, None
                                if maximizing:
                                    max_eval = -100
                                    best_move = None
                                    empty_sqrs = board.get_empty_sqrs()
                                    for (row, col) in empty_sqrs:
                                        temp_board = copy.deepcopy(board)
                                        temp_board.mark_sqr(row, col, 1)
                                        eval = self.minimax(temp_board, False)[0]
                                        if eval > max_eval:
                                            max_eval = eval
                                            best_move = (row, col)
                                    return max_eval, best_move
                                elif not maximizing:
                                    min_eval = 100
                                    best_move = None
                                    empty_sqrs = board.get_empty_sqrs()
                                    for (row, col) in empty_sqrs:
                                        temp_board = copy.deepcopy(board)
                                        temp_board.mark_sqr(row, col, self.player)
                                        eval = self.minimax(temp_board, True)[0]
                                        if eval < min_eval:
                                            min_eval = eval
                                            best_move = (row, col)
                                    return min_eval, best_move

                            def eval(self, main_board):
                                if self.level == 0:
                                    # random choice
                                    eval = 'random'
                                    move = self.rnd(main_board)
                                else:
                                    # minimax algo choice
                                    eval, move = self.minimax(main_board, False)

                                return move  # row, col

                        class Game:
                            def __init__(self):
                                self.board = Board()
                                self.ai = AI()
                                self.player = 1  # 1-cross  #2-circles
                                self.gamemode = 'ai'  # pvp or ai
                                self.running = True
                                self.show_lines()

                            # draw methods
                            def show_lines(self):
                                # bg
                                screen.fill(BG_COLOR)
                                # vertical
                                pygame.draw.line(screen, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
                                pygame.draw.line(screen, LINE_COLOR, (WIDTH - SQSIZE, 0), (WIDTH - SQSIZE, HEIGHT),
                                                 LINE_WIDTH)
                                # horizontal
                                pygame.draw.line(screen, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
                                pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - SQSIZE), (WIDTH, HEIGHT - SQSIZE),
                                                 LINE_WIDTH)

                            def draw_fig(self, row, col):
                                if self.player == 1:
                                    # draw cross
                                    # desc line
                                    start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
                                    end_desc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET)
                                    pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
                                    ixik_nolik.play()
                                    # asc line
                                    start_asc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
                                    end_asc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET)
                                    pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)
                                    ixik_nolik.play()
                                elif self.player == 2:
                                    # draw circle
                                    center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)
                                    pygame.draw.circle(screen, CIRC_COLOR, center, RADIUS, CIRC_WIDTH)
                                    ixik_nolik.play()

                            # other methods
                            def make_move(self, row, col):
                                self.board.mark_sqr(row, col, self.player)
                                self.draw_fig(row, col)
                                self.next_turn()

                            def next_turn(self):
                                self.player = self.player % 2 + 1

                            def change_gamemode(self):
                                self.gamemode = 'ai' if self.gamemode == 'pvp' else 'pvp'

                            def isover(self):
                                return self.board.final_state(show=True) != 0 or self.board.isfull()

                            def reset(self):
                                self.__init__()

                            def my_salut_draw(self):
                                pygame.init()
                                global score5
                                W = H = 500
                                sc = pygame.display.set_mode((W, H), pygame.NOFRAME)
                                pygame.display.set_caption("TicTacToe")
                                animation_set_1 = []
                                for i in range(11, 15):
                                    temp1 = pygame.image.load(f"{i}.png").convert()
                                    temp_rect1 = temp1.get_rect(center=(W // 2, H // 2))
                                    animation_set_1.append(temp1)
                                clock = pygame.time.Clock()
                                cl = 300
                                i = 0
                                while cl > 0:
                                    sc.fill((250, 250, 250))
                                    sc.blit(animation_set_1[i // 15], temp_rect1)
                                    pygame.display.update()
                                    i += 1
                                    if i == 60:
                                        i = 0
                                    pygame.display.flip()
                                    clock.tick(60)
                                    cl -= 1
                                    score5 += 1

                            def my_salut_0(self):
                                pygame.init()
                                global score6
                                green = ( 255,64,64)
                                W = H = 500
                                sc = pygame.display.set_mode((W, H), pygame.NOFRAME)
                                animation_set = []
                                for i in range(1, 11):
                                    temp = pygame.image.load(f"{i}.png").convert_alpha()
                                    temp_rect = temp.get_rect(center=(W // 2, H // 2))
                                    animation_set.append(temp)
                                cl = 300
                                i = 0
                                while cl > 0:
                                    sc.fill((0, 0, 0))
                                    sc.blit(animation_set[i // 6], temp_rect)
                                    pygame.draw.circle(sc, green, (H // 2, W // 2), H // 8, 15)
                                    pygame.display.update()
                                    i += 1
                                    pygame.time.delay(20)
                                    if i == 60:
                                        i = 0
                                    pygame.display.flip()
                                    cl -= 1
                                    score6 += 1

                        def main():
                            # objects
                            game = Game()
                            board = game.board
                            ai = game.ai
                            # mainloop
                            while True:
                                # pygame events
                                for event in pygame.event.get():
                                    # quit event
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    # keydown event
                                    if event.type == pygame.KEYDOWN:
                                        # g-gamemode
                                        if event.key == pygame.K_g:
                                            game.change_gamemode()
                                        # r-restart
                                        if event.key == pygame.K_r:
                                            game.reset()
                                            board = game.board
                                            ai = game.ai
                                        # 0-random ai
                                        if event.key == pygame.K_0:
                                            ai.level = 0
                                        # 1-random ai
                                        if event.key == pygame.K_1:
                                            ai.level = 1
                                    # click event
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        pos = event.pos
                                        row = pos[1] // SQSIZE
                                        col = pos[0] // SQSIZE
                                        # human mark sqr
                                        if board.empty_sqr(row, col) and game.running:
                                            game.make_move(row, col)
                                            if game.isover():
                                                ixik_nolik.stop()
                                                gameOver.play()
                                                game.my_salut_draw()
                                                game.running = False
                                                time.sleep(1)
                                                return player1option
                                # AI initial call
                                if game.gamemode == 'ai' and game.player == ai.player and game.running:
                                    # update the screen
                                    pygame.display.update()
                                    # eval
                                    row, col = ai.eval(board)
                                    game.make_move(row, col)
                                    if game.isover():
                                        ixik_nolik.stop()
                                        gameOver.play()
                                        game.my_salut_0()
                                        game.running = False
                                        time.sleep(3)
                                        return player1option
                                pygame.display.update()

                        main()  # End of the game

                        pygame.display.update()  # End of the loading part


                    def player2():  # Play with 2 player
                        mainmenu._open(player2option)
                        button_sound.play()
                        time.sleep(0.2)

                        # Loading start
                        pygame.init()
                        loading.play()

                        width = 500
                        height = 500
                        fps = 60
                        speed = 130
                        fps = 90
                        speed = 180

                        boarder_rect = [20, 325, 260, 50]
                        inner_rect = [25, 330, 0, 40]
                        green = (0, 154, 205)
                        white = (199, 206, 230)
                        surface = pygame.display.set_mode((width, height), pygame.NOFRAME)
                        f = pygame.font.SysFont("myriadProFont", 50)
                        text = f.render(" LOADING... ", 1, (0, 154, 205), (199, 206, 230))
                        x, y = 155, 140

                        clock = pygame.time.Clock()
                        gameloop = True
                        surface.fill(white)
                        surface.blit(text, (x, y))

                        while gameloop == True:
                            clock.tick(fps)

                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    gameloop = False
                            if inner_rect[2] <= 249:

                                inner_rect[2] += speed / fps
                            if inner_rect[2] - 2 == 248.0:
                                break

                            pygame.draw.rect(surface, green, (120, 190, 260, 50), 3)
                            pygame.draw.rect(surface, green, (125, 195, int(inner_rect[2]), (inner_rect[3])))

                            pygame.display.flip()

                            clock.tick(95)  # End of the loading part

                        pg.init()   # Game start

                        class Two_players_game:

                            def __init__(self):

                                self.W = self.H = 500
                                self.margin = 15
                                self.size_block = (self.H - 2 * self.margin) // 3
                                self.mas = [[0] * 3 for i in range(3)]
                                self.flag = 0
                                self.sc = pg.display.set_mode((self.W, self.H), pg.NOFRAME)
                                self.game_over = False
                                self.animation_set = []
                                self.animation_set_1 = []
                                self.temp_set = []
                                self.sc.fill((0, 154, 205))
                                self.clock = pg.time.Clock()

                                for i in range(1, 15):  # creat animation`s lists
                                    self.temp = pg.image.load(f"{i}.png").convert_alpha()
                                    self.rect = self.temp.get_rect(center=(self.W // 2 + 25, self.H // 2 - 30))
                                    self.rect1 = self.temp.get_rect(center=(self.W // 2, self.H // 2))
                                    self.temp_set.append(self.temp)
                                self.animation_set = self.temp_set[0:10]
                                self.animation_set_1 = self.temp_set[10:]

                            def check_win(self, sign):
                                zeroes = 0
                                for row in self.mas:
                                    zeroes += row.count(0)
                                    if row.count(sign) == 3:
                                        pg.time.delay(300)
                                        return sign
                                for col in range(3):
                                    if self.mas[0][col] == sign and self.mas[1][col] == sign and self.mas[2][
                                        col] == sign:
                                        pg.time.delay(300)
                                        return sign
                                if self.mas[0][0] == sign and self.mas[1][1] == sign and self.mas[2][2] == sign:
                                    pg.time.delay(300)
                                    return sign
                                if self.mas[0][2] == sign and self.mas[1][1] == sign and self.mas[2][0] == sign:
                                    pg.time.delay(300)
                                    return sign
                                if zeroes == 0:
                                    pg.time.delay(300)
                                    return 'None'
                                return False

                            def salut_draw(self):
                                global score3
                                cl = 300
                                i = 0
                                while cl > 0:
                                    self.sc.fill((250, 250, 250))
                                    self.sc.blit(self.animation_set_1[i // 15], self.rect1)
                                    pg.display.update()
                                    i += 1
                                    if i == 60:
                                        i = 0
                                    pg.display.flip()
                                    self.clock.tick(60)
                                    cl -= 1
                                    score3 += 1
                            def salut_0(self):
                                global score2
                                cl = 300
                                i = 0
                                while cl > 0:
                                    self.sc.fill((0, 0, 0))
                                    self.sc.blit(self.animation_set[i // 6], self.rect)
                                    pg.draw.circle(self.sc, (255, 64, 64), (self.H // 2, self.W // 2), self.H // 8, 15)
                                    pg.display.update()
                                    i += 1
                                    if i == 60:
                                        i = 0
                                    pg.display.flip()
                                    self.clock.tick(60)
                                    cl -= 1
                                    score2 += 1
                            def salut_x(self):
                                global score1
                                cl = 300
                                i = 0
                                while cl > 0:
                                    self.sc.fill((0, 0, 0))
                                    self.sc.blit(self.animation_set[i // 12], self.rect)
                                    pg.draw.line(self.sc, (0, 201, 87), (self.H // 2 - 30, self.W // 2 - 30),
                                                 (self.H // 2 + 30, self.W // 2 + 30), 15)
                                    pg.draw.line(self.sc, (0, 201, 87), (self.H // 2 - 30, self.W // 2 + 30),
                                                 (self.H // 2 + 30, self.W // 2 - 30), 15)
                                    pg.display.update()
                                    i += 1
                                    if i == 60:
                                        i = 0
                                    pg.display.flip()
                                    self.clock.tick(60)
                                    cl -= 1
                                    score1 += 1
                            def start_game(self):
                                while 1:
                                    for event in pg.event.get():
                                        if event.type == pg.QUIT:
                                            exit()

                                        elif event.type == pg.MOUSEBUTTONDOWN and not game_over:
                                            x_mouse, y_mouse = pg.mouse.get_pos()
                                            col = x_mouse // (self.size_block + self.margin)
                                            row = y_mouse // (self.size_block + self.margin)
                                            if self.mas[row][col] == 0:
                                                if self.flag % 2 == 0:
                                                    self.mas[row][col] = 'x'
                                                    ixik_nolik.play()
                                                else:
                                                    self.mas[row][col] = 'o'
                                                    ixik_nolik.play()
                                                self.flag += 1
                                    for row in range(3):  # գծում է դաշտը
                                        for col in range(3):
                                            x = col * self.size_block + (col) * self.margin
                                            y = row * self.size_block + (row) * self.margin
                                            pg.draw.rect(self.sc, (230, 230, 250),
                                                         (x, y, self.size_block, self.size_block))
                                            if self.mas[row][col] == 'x':  # գծում է X
                                                pg.draw.line(self.sc, (0, 201, 87), (x + 40, y + 40),
                                                             (x + self.size_block - 40, y + self.size_block - 40), 20)
                                                pg.draw.line(self.sc, (0, 201, 87),
                                                             (x + self.size_block - 40, y + 40),
                                                             (x + 40, y + self.size_block - 40), 20)

                                            elif self.mas[row][col] == 'o':  # գծում է 0
                                                pg.draw.circle(self.sc, (255, 64, 64),
                                                               (x + self.size_block // 2, y + self.size_block // 2),
                                                               self.size_block // 4 + 10, 15)

                                    if (self.flag - 1) % 2 == 0:
                                        game_over = self.check_win('x')
                                    else:
                                        game_over = self.check_win('o')
                                    if game_over:
                                        if game_over == 'x':
                                            ixik_nolik.stop()
                                            gameOver.play()
                                            self.salut_x()
                                            return player2option
                                        elif game_over == 'o':
                                            ixik_nolik.stop()
                                            sound_victory.play()
                                            self.salut_0()
                                            return player2option

                                        else:
                                            ixik_nolik.stop()
                                            sound_victory.play()
                                            self.salut_draw()
                                            return player2option

                                    pg.display.update()

                        two_players_game = Two_players_game()
                        two_players_game.start_game()  # End of the game


                        pygame.display.update()   # End of the loading part

                    mainmenu = pygame_menu.Menu('Select an option', 500, 500, theme=themes.THEME_BLUE)  # Main menu
                    mainmenu.add.table()

                    mainmenu.add.button('1 player', player1)
                    mainmenu.add.button('2 player', player2)
                    mainmenu.add.button('Quit', pygame_menu.events.EXIT)
                    button_sound.play()

                    player1option = pygame_menu.Menu('Select a Difficulty', 500, 500,
                                                     theme=themes.THEME_BLUE)
                    player2option = pygame_menu.Menu('Select a Difficulty', 500, 500,
                                                     theme=themes.THEME_BLUE)
                    player1option = pygame_menu.Menu('Menu', 500, 500,
                                                     theme=themes.THEME_BLUE)
                    player2option = pygame_menu.Menu('Menu', 500, 500,
                                                     theme=themes.THEME_BLUE)
                    player1option.add.button("Restart", player1)
                    player2option.add.button("Restart", player2)
                    player1option.add.button("Score", level_menu)
                    player2option.add.button("Score", level_menu)
                    player1option.add.button("Quit", pygame_menu.events.EXIT)
                    player2option.add.button("Quit", pygame_menu.events.EXIT)
                    arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15))


                    while True:
                        events = pygame.event.get()
                        for event in events:
                            pass

                            if event.type == pygame.QUIT:
                                exit()
                        if mainmenu.is_enabled():
                            mainmenu.update(events)
                            mainmenu.draw(surface)
                            if (mainmenu.get_current().get_selected_widget()):
                                arrow.draw(surface, mainmenu.get_current().get_selected_widget())
                        pygame.display.update()
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = '#00BFFF'

pygame.init()
screen.blit(pygame.transform.scale(imp, (500, 500)), (0, 0))
clock = pygame.time.Clock()
gui_font = pygame.font.Font(None, 35)

button1 = Button(' PLAY ', ' PLAY ', 180, 50, (160, 380), 5)


def buttons_draw():
    for b in buttons:
        b.draw()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    buttons_draw()

    pygame.display.update()
    clock.tick(60)