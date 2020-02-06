import pygame,random,sys


 #initialising
def reset():
    global P,sp1,sp2,game,collection,cardno,card,p1,p2,computer
    P,sp1,sp2,game,computer = 1,0,0,1,0
    #suits=('0','hearts','diamond','clubs','spades')
    #values=('0','ace','2','3','4','5','6','7','8','9','10','jack','queen','king')
    screen.fill(color,(250,200,73.077,98))
    collection,cardno,card,p1,p2=['0'],[],[],[],[]
    for i in range(1,5):
        for j in range(1,14):
            card.append((i,j))
    for i in range(52):
        cardno.append(i)
    for i in range(52):
        no=random.choice(cardno)
        if(P):
            p1.append(no)
            P=0
        else:
            p2.append(no)
            P=1
        cardno.remove(no)
    choice()

#data

pygame.init()
screen=pygame.display.set_mode((280*2,200*2))
pygame.display.set_caption('Cards On Cards')
color=[55,255,236]
green = (69, 3, 252)
bcolor=(57,20,204)
rcolor=(252,100,100)
screen.fill(color)
cards=pygame.image.load("data/cards.png")
cardback=pygame.transform.scale(pygame.image.load("data/back.png"),(74,92))

pygame.mixer.music.set_volume(.2)
back=pygame.mixer.music.load('data/back.mp3')
vic=pygame.mixer.Sound("data/victory.wav")
draw=pygame.mixer.Sound("data/draw.wav")
cpm=pygame.mixer.Sound("data/cplay.wav")
vic.set_volume(.2)
draw.set_volume(.2)
font=pygame.font.SysFont('Arial', 22 ,bold=True)
fontc=pygame.font.SysFont('Arial', 12 ,bold=True)
creater=fontc.render('CREATED BY- Rakshit Goel',True,green,color)
center=(170,30)

tp2=font.render('     PLAYER TWO           ',True,green,color)
twp2=font.render('  PLAYER TWO WIN    ',True,green,color)
tep2=font.render('PLAYER TWO EMPTY',True,green,color)

def initi():
    global tp1,twp1,tep1
    if computer:
        tp1=font.render('      COMPUTER           ',True,green,color)
        twp1=font.render('   COMPUTER WIN    ',True,green,color)
        tep1=font.render(' COMPUTER EMPTY',True,green,color)
    else:
        tp1=font.render('     PLAYER 0NE           ',True,green,color)
        twp1=font.render('  PLAYER ONE WIN    ',True,green,color)
        tep1=font.render('PLAYER ONE EMPTY',True,green,color)
    




def display():
    global lenp1,lenp2
    lenp1=len(p1)
    lenp2=len(p2)
    np1=font.render('PLAYER 1-'+str(lenp1)+'  ',True,green,color)
    np2=font.render('PLAYER 2-'+str(lenp2)+'  ',True,green,color)
    coll=font.render('CARDS IN COLLECTION '+str(len(collection)-1)+'    ',True,green,color)
    ssp1=font.render('SCORE-'+str(sp1)+'  ',True,green,color)
    ssp2=font.render('SCORE-'+str(sp2)+'  ',True,green,color)
    screen.blit(np1,[20,15])
    screen.blit(np2,[406,15])
    screen.blit(coll,[150,300])
    screen.blit(ssp1,[20,170])
    screen.blit(ssp2,[406,170])
    pygame.display.update()

def cardprint(x,y):    
    x,y=x-1,y-1
    x,y=x*73.077,y*98
    screen.blit(cards,(250,200),(x,y,73.077,98))
    pygame.display.update()

def mixx(px):
    print('called')
    templ=[]
    for i in range(len(px)):
        temp=random.choice(px)
        templ.append(temp)
        px.remove(temp)
    return(templ)
    


def move():
    global P,collection,p1,p2
    pygame.mixer.Sound.play(cpm)
    try:
        if(P):
            P=0
            temp=p1.pop()
            cardprint(card[temp][1],card[temp][0])          
            screen.blit(tp1,center)            
            if lenp1==1:
                screen.blit(tep1,center)
                screen.fill(color,rect=[50,50,74,92])                
            #print(values[card[temp][1]],' of ',suits[card[temp][0]])
            if(card[temp][1]==card[int(collection[-1])][1]):
                collection.append(temp)
                win()
            else:                
                collection.append(temp)
        else:
            P=1
            temp=p2.pop()
            cardprint(card[temp][1],card[temp][0])
            #print(values[card[temp][1]],' of ',suits[card[temp][0]])
            screen.blit(tp2,center)            
            if lenp2==1:
                screen.blit(tep2,center)
                screen.fill(color,rect=[436,50,74,92])
            if(card[temp][1]==card[int(collection[-1])][1]):
                collection.append(temp)
                win()
            else:                
                collection.append(temp)        
        pygame.display.update()
    except:
        #print('cards empty of player ',P)
        pygame.mixer.Sound.play(draw)
        screen.blit(cardback,(50,50))
        screen.blit(cardback,(436,50))
        pygame.display.update()        
        TP=not P
        for i in collection[1:]:
            if(TP):
                p1.insert(0,i)
            else:
                p2.insert(0,i)
            TP=not TP
        
        P=not P
        collection=['0']

def win():
    global p1,p2,collection,sp1,sp2
    TL=[]
    pygame.mixer.Sound.play(vic)
    if(not P):
        screen.blit(twp1,center)
        TL.extend(collection[1:-1])
        TL.extend(p1)
        p1=TL
        #print(p1)
        sp1=sp1+1        
    else:
        screen.blit(twp2,center)
        TL.extend(collection[1:-1])
        TL.extend(p2)
        p2=TL
        #print(p2)
        sp2=sp2+1        
    pygame.display.update()
    collection=['0',collection[-1]]
    pygame.time.delay(200)
    
    

pygame.mixer.music.play(-1)
#reset()
def start():
    global game, p1 ,p2
    screen.fill(color)
    screen.blit(cardback,(50,50))
    screen.blit(cardback,(436,50))
    screen.fill(bcolor,(406,220,140,35))
    screen.fill(rcolor,(210,342,150,35))
    mix=font.render("Shuffle Cards",True,color,bcolor)
    rset=font.render("RESET GAME",True,color,rcolor)
    if not computer:
        screen.fill(bcolor,(20,220,140,35))
        screen.blit(mix,[20,228])
    screen.blit(mix,[406,228])
    screen.blit(rset,[210,350])
    screen.blit(creater,[10,380])
    pygame.display.update()
    while(game):
        display()
        if computer and P:
            pygame.time.delay(450)
            move()
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    #sys.exit()
                    game=0
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        game=0
                        pygame.quit()
                        #quit()
                        sys.exit()
                    if event.key==pygame.K_SPACE:
                        pygame.event.pump()
                        move()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    if(160 > x >20 and 255 > y >220 and P):
                        p1=mixx(p1)
                        #print("p1")
                    elif(546 > x > 406 and 255 > y > 220):
                        p2=mixx(p2)
                        #print('p2')
                    elif(360>x>210 and 377>y>342):
                        reset()
                    else:
                        #print(p1,'  \n ',p2,' \n ',collection)        
                        move()

#start()
def choice():
    global computer,game
    font=pygame.font.SysFont('Arial', 36 ,bold=True)
    screen.fill(color)
    play1=font.render("vs computer",True,color,bcolor)
    play2=font.render(" 2 players ",True,color,bcolor)
    name=font.render('CARDS ON CARDS',True,bcolor,color)
    screen.blit(play1,[210,130])
    screen.blit(play2,[225,240])
    screen.blit(creater,[10,380])
    screen.blit(name,[170,40])
    pygame.display.update()
    while(game):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                #sys.exit()
                game=0
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    game=0
                    pygame.quit()
                    #quit()
                    sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                #]print(x,'  ',y)
                if( 385>x>210 and 172>y>130):
                    computer=1
                    initi()
                    start()
                elif( 365>x>225 and 280>y>240):
                    computer=0
                    initi()
                    start()
reset()
