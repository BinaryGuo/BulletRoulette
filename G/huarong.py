from numpy import array as arr, where as wr
from random import random as rdm
from json import dump as dp, load as ld
from time import sleep as slp
from os import remove as rm
import pygame
import copy
class Tcountry:
    def __init__(self):
        self.board = arr([
            [1, 2, 2, 3],
            [1, 2, 2, 3],
            [4, 5, 5, 6],
            [4, 8, 9, 6],
            [7, 0, 0, 10],
        ])
        self.log = [(None, self.board.tolist())]
    
    def __chkpsb(self):
        self.possible = []
        x0, y0 = wr(self.board==0)
        blank_tuples = [(x0[i], y0[i]) for i in range(len(x0))]
        for i in range(1, 11):
            x, y = wr(self.board==i)
            current_tuples = [(x[i], y[i]) for i in range(len(x))]
            # move up
            x_pretend_move = [p-1 for p in x if p-1>=0]
            pretend_tuples = [(x_pretend_move[i], y[i]) for i in range(len(x_pretend_move))]
            movables = [w for w in pretend_tuples if w in current_tuples or w in blank_tuples]
            if len(movables)==len(current_tuples): self.possible.append((i, "up")) 
            # move down
            x_pretend_move = [p+1 for p in x if p+1<=4]
            pretend_tuples = [(x_pretend_move[i], y[i]) for i in range(len(x_pretend_move))]
            movables = [w for w in pretend_tuples if w in current_tuples or w in blank_tuples]
            if len(movables)==len(current_tuples): self.possible.append((i, "down")) 
            # move left
            y_pretend_move = [p-1 for p in y if p-1>=0]
            pretend_tuples = [(x[i], y_pretend_move[i]) for i in range(len(y_pretend_move))]
            movables = [w for w in pretend_tuples if w in current_tuples or w in blank_tuples]
            if len(movables)==len(current_tuples): self.possible.append((i, "left"))
            # move right
            y_pretend_move = [p+1 for p in y if p+1<=3]
            pretend_tuples = [(x[i], y_pretend_move[i]) for i in range(len(y_pretend_move))]
            movables = [w for w in pretend_tuples if w in current_tuples or w in blank_tuples]
            if len(movables)==len(current_tuples): self.possible.append((i, "right"))

    def __mv(self, i, direction):
        x, y = wr(self.board==i)
        current_tuples = [(x[i], y[i]) for i in range(len(x))]
        for pos_x, pos_y in current_tuples: self.board[pos_x][pos_y] = 0
        if direction=="left":
            for pos_x, pos_y in current_tuples: self.board[pos_x][pos_y-1] = i
        elif direction=="right":
            for pos_x, pos_y in current_tuples: self.board[pos_x][pos_y+1] = i
        elif direction=="up":
            for pos_x, pos_y in current_tuples: self.board[pos_x-1][pos_y] = i
        elif direction=="down":
            for pos_x, pos_y in current_tuples: self.board[pos_x+1][pos_y] = i
        self.possible = []
        self.log.append(self.board.tolist())

    def __fuzzy(self,board):
        b = arr(board)
        b[b==3]=1
        b[b==7]=3
        b[b==8]=3
        b[b==9]=3
        b[b==10]=3
        b[b==4]=1
        b[b==5]=4
        b[b==6]=1
        return b.tolist()

    def simplify(self):
        try: chain = ld(open("log.json", "r"))
        except:
            print("Please encode first!")
            return
        chain = [self.__fuzzy(w) for w in chain]
        offset = -2
        while True:
            i = offset+len(chain)
            if i>1:
                fuzzy_board = chain[i]
                for j in range(0, i):
                    j_fuzzyboard = chain[j]
                    if fuzzy_board == j_fuzzyboard:
                        del chain[j+1:i+1]
                        break
                print(len(chain))
                offset-=1
            else:
                break
        dp(chain, open("spflog.json", "w", encoding="utf-8"), indent=2)

    def encode(self):
        for round in range(10000000):
            if round % 50000 == 0:print(round)
            self.__chkpsb()
            i, direction = self.possible[int(len(self.possible)*rd())]
            self.__mv(i, direction)
            if self.board[4][1]==2 and self.board[4][2]==2:break
        self.log[0] = self.log[0][1]
        dp(self.log, open("log.json", "w", encoding="utf-8"), indent=1)

    def viewmethod(self,chain = []):
        pygame.init()
        screen = pygame.display.set_mode([640, 800])
        pygame.display.set_caption('hua rong')
        colors = ['white','green', 'red', 'black', 'grey']
        if chain == []:
            try:chain = ld(open("spflog.json", "r"))
            except:
                try:chain = ld(open("edtlog.json", "r"))
                except:
                    try:
                        num = input("Enter number: ")
                        chain = ld(open(f"methods/method{num}.json", "r"))
                    except:
                        print("Please simplify, edit or save method first!")
                        return
        for i in range(len(chain)):
            board = chain[i]
            pygame.draw.rect(screen, 'white', [0, 0, 640, 800])
            for i in range(5):
                for j in range(4):
                    v = board[i][j]
                    c = colors[v]
                    try:
                        if v == 3:pygame.draw.rect(screen, c, [j*160+5, i*160+5, 150, 150])
                        elif v == 4:
                            if board[i][j+1] == 4:pygame.draw.rect(screen, c, [j*160+5, i*160+5, 155, 150])
                            else:pygame.draw.rect(screen, c, [j*160, i*160+5, 155, 150])
                        elif v == 2:
                            if board[i+1][j] == 2 and board[i][j+1] == 2 and board[i+1][j+1]:pygame.draw.rect(screen, c, [j*160+5, i*160+5, 155, 155])
                            elif board[i+1][j] == 2 and board[i][j-1] == 2 and board[i+1][j-1]:pygame.draw.rect(screen, c, [(j+1)*160-5, i*160+5, -155, 155])
                            elif board[i-1][j] == 2 and board[i][j+1] == 2 and board[i-1][j+1]:pygame.draw.rect(screen, c, [j*160+5, (i+1)*160+5, 155, -155])
                            else: pygame.draw.rect(screen,c,[j*160+5, (i+1)*160+5, 155, -155])
                        else:pygame.draw.rect(screen, c, [(j+1)*160-5, (i+1)*160-5, -155, -155])
                    except IndexError:
                        pass
            slp(0.25)
            pygame.display.flip()

    def editmethod(self): # TODO
        try:f = ld(open("spflog.json","r"))
        except:
            try:f = ld(open("edtlog.json","r"))
            except:
                print("Please simplify first!")
                return
        while True:
            pt = input("Enter operation:")
            #try:
            if pt == "exit": break
            elif pt[:4] == "view":
                pt = list(pt)
                del pt[:5]
                tmp = ''
                while pt[0] != ' ':
                    tmp += pt[0]
                    del pt[0]
                del pt[0]
                t1 = ''
                t2 = ''
                for w in tmp:t1 += w
                for w in pt:t2 += w
                self.viewmethod(f[int(t1) - 1:int(t2)])
            else:
                ptl = pt.split(' ')
                ptl[0] = int(ptl[0]) - 1
                ptl[1] = eval(ptl[1])
                f[ptl[0]] = ptl[1]
            #except:
             #   print("OPERATION ERR")
        dp(f,open("edtlog.json","w",encoding='utf-8'),indent=1)
    
    def savemethod(self):
        num = input("Enter number:")
        a = open(f"methods/method{num}.json","w")
        try:b = open("edtlog.json","r")
        except:
            try:b = open("spflog.json","r")
            except:
                print("Please simplify or edit first!")
                return
        a.write(b.read())
        rm("log.json")
        rm("spflog.json")
        try:rm("edtlog.json")
        except:pass

class Number:

    def __init__(self):
        self.board = arr([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0],
        ])
        self.history_chain = [(None, None, self.board.tolist())]
        self.goal = arr([
            [0, 15, 14, 13],
            [12, 11, 10, 9],
            [8, 7, 6, 5],
            [4, 3, 2, 1],
        ])
        self.WIDTH = 4
        self.RANGE_MAX = 16
        self.history_set = set()  # 这个是用来去重，记录历史经历的棋局
        self.history_set.add(str(self.board.tolist()))
    
    def check_possible(self):
        self.possible = []
        x0, y0 = wr(self.board==0)
        blank_tuples = [(x0[i], y0[i]) for i in range(len(x0))]
        for i in range(1, self.RANGE_MAX):
            x, y = wr(self.board==i)
            current_tuples = [(x[i], y[i]) for i in range(len(x))]

            # move up
            x_pretend_move = [p-1 for p in x if p-1>=0]
            pretend_tuples = [(x_pretend_move[i], y[i]) for i in range(len(x_pretend_move))]
            movables = [w for w in pretend_tuples if w in current_tuples or w in blank_tuples]
            if len(movables)==len(current_tuples): self.possible.append((i, "up")) 
        
            # move down
            x_pretend_move = [p+1 for p in x if p+1<=self.WIDTH-1]
            pretend_tuples = [(x_pretend_move[i], y[i]) for i in range(len(x_pretend_move))]
            movables = [w for w in pretend_tuples if w in current_tuples or w in blank_tuples]
            if len(movables)==len(current_tuples): self.possible.append((i, "down")) 

            # move left
            y_pretend_move = [p-1 for p in y if p-1>=0]
            pretend_tuples = [(x[i], y_pretend_move[i]) for i in range(len(y_pretend_move))]
            movables = [w for w in pretend_tuples if w in current_tuples or w in blank_tuples]
            if len(movables)==len(current_tuples): self.possible.append((i, "left"))

            # move right
            y_pretend_move = [p+1 for p in y if p+1<=self.WIDTH-1]
            pretend_tuples = [(x[i], y_pretend_move[i]) for i in range(len(y_pretend_move))]
            movables = [w for w in pretend_tuples if w in current_tuples or w in blank_tuples]
            if len(movables)==len(current_tuples): self.possible.append((i, "right"))
        print("all posiible choice", self.possible)
        
    def __move_action(self, board, i, direction):
        x, y = wr(board==i)
        current_tuples = [(x[i], y[i]) for i in range(len(x))]
        for pos_x, pos_y in current_tuples: board[pos_x][pos_y] = 0
        if direction=="left":
            for pos_x, pos_y in current_tuples: board[pos_x][pos_y-1] = i
        elif direction=="right":
            for pos_x, pos_y in current_tuples: board[pos_x][pos_y+1] = i
        elif direction=="up":
            for pos_x, pos_y in current_tuples: board[pos_x-1][pos_y] = i
        elif direction=="down":
            for pos_x, pos_y in current_tuples: board[pos_x+1][pos_y] = i
        
    def move(self):
        distance_list = []
        for i, direction in self.possible: # 计算各种可能的走法，和终点之间的距离
            board = copy.deepcopy(self.board)
            self.__move_action(board, i, direction)

            if str(board.tolist()) in self.history_set:   # 如果这个走法，在历史上出现过，那么这个距离就算无穷远
                distance_list.append((i, direction, 10000))
            else:
                distance = 0   
                for k in range(1, self.RANGE_MAX):
                    x1, y1 = wr(board==k)
                    x2, y2 = wr(self.goal==k)
                    k_distance = abs(x1[0]-x2[0])+abs(y1[0]-y2[0])
                    distance+=k_distance
                distance_list.append((i, direction ,distance))
        
        distance_list = sorted(distance_list, key = lambda x:x[2]) # 按照距离对可能的走法进行排序
        print(distance_list)

        min_list = [w for w in distance_list if w[2]==distance_list[0][2]]
        if len(min_list)==1: # 如果只有一个候选的话
            i, direction, _ = min_list[0]
        else: # 如果有多个候选，就随机选择一个
            idx = int(rdm()*len(min_list))
            i, direction, _  = min_list[idx]
        print("select move %d %s"%(i, direction))
        self.__move_action(self.board, i, direction)
        print()
        print(self.board)
        self.possible = []
        self.history_chain.append((i, direction, self.board.tolist()))
        self.history_set.add(str(self.board.tolist()))


    def run(self):
        for round in range(10000):
            print("No. %d round"%round)
            self.check_possible()
            self.move()
            print()

            if (self.board == self.goal).all():
                print("SUCCESS GO OUT FINALLY")
                dp(self.history_chain, open("history_chain_math.json", "w", encoding="utf-8"), indent=2)
                break

    def draw(self):
        import pygame, json, time
        pygame.init()

        WIDTH = 640
        HEIGHT = 640

        screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption('hua rong road')

        print(len(self.history_chain))
        font = pygame.font.SysFont("Arial", 100)
        font.bold = True
        for i, direction, board in self.history_chain:
            pygame.draw.rect(screen, 'white', [0, 0, WIDTH, HEIGHT])            
            for j in range(self.WIDTH):    
                for k in range(self.WIDTH):        
                    text = str(board[k][j])
                    if text !="0":
                        pygame.draw.rect(screen, 'black', [j*160+5, k*160+5, 150, 150])
                        textSurface = font.render(text, True, (255, 255, 255),(0,0,0))
                        width, height = font.size(text)
                        screen.blit(textSurface, (j*160+25,  k*160+25))
            time.sleep(0.5)
            pygame.display.flip()

while True:
    mode = input("Enter class(Tcountry:1,Number:2):")
    if mode == '1':
        b = Tcountry()
        while True:
            mode = input("Enter mode(Encode:1,Simplify:2,View-method:3,Edit-method:4,Save-method:5,Exit:6): ") #1256
            if mode == '1': b.encode()
            elif mode == '2': b.simplify()
            elif mode == '3': b.viewmethod()
            elif mode == '4': b.editmethod()
            elif mode == '5': b.savemethod()
            elif mode == '6': exit()
            else : print("MODE ERR")
    elif md == '2':
        b = Number()
        while True:
            mode
    print("CLASS ERR")