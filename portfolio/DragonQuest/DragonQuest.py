# Program:                          DragonQuest.py
# Version:                          v2.0.121
# Completed by:                     Anthony Braden on 10/02/2021

import pygame
import random
import sys
import time

TYPINGSPEED = 150
    
def playMusic(track, y, x):
    if y == 1:
        if x == 1:
            try:
                pygame.mixer.init()
                pygame.mixer.music.load(track + ".wav")
                pygame.mixer.music.play(-1)    
            except:
                print("Couldn't find sound file.")
        else:
            try:
                pygame.mixer.init()
                pygame.mixer.music.load(track + ".wav")
                pygame.mixer.music.play()    
            except:
                print("Couldn't find sound file.")
    else:
        try:
            pygame.mixer.music.unload()
            pygame.mixer.music.stop()
        except:
            print("No sound file to stop.")
        if x == 1:
            try:
                pygame.mixer.init()
                pygame.mixer.music.load(track + ".wav")
                pygame.mixer.music.play(-1)    
            except:
                print("Couldn't find sound file.")
                
def typeText(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random() * 10.0 / TYPINGSPEED)

def chooseContinue():
    yesContinue = input("   Press 'Enter' to continue or 'Q' to quit...")
    if yesContinue == "":
        print("")
    elif yesContinue == 'q':
        exit()
    else:
        return chooseContinue()
        
def restartStory(death):
    yesContinue = input("   Press 'Enter' to restart the story or 'Q' to quit...")
    if yesContinue == "":
        if death == True:
            track = "You Die"
            playMusic(track, 1, 0)   
            time.sleep(1)     
            runMain()
        else:
            track = "You Die"
            playMusic(track, 1, 0)   
            time.sleep(1)     
            runMain()            
    elif yesContinue.lower() == 'q':
        exit()
    else:
        return restartStory()
        
def CLICKETYCLACKGAMES():
    text = "   Brought to you by:\n      CLICKETY CLACK GAMES\n"
    typeText(text)
    track = "CLICKETYCLACKGAMES"
    playMusic(track, 1, 0)
    chooseContinue()
        
def printIntro():
    track = "Itty Bitty"
    playMusic(track, 1, 1)
    text = "\n   'Here Ye! Here Ye!\n\n"
    typeText(text)
    text = "\t   The King of Anagua, the Islands of the\n   Great Sea, has proclaimed that Golan, the Great\n   Dragon of the Western Mountains, deserves\n   a slaying. He is terrorizing the countryside,\n   eating nobleman and stealing gold. Any man who\n   feels himself able to slay Golan should report\n   to the castle this afternoon.\n\n"
    typeText(text)
    text = "\t   The King has issued a reward of 5,000\n   gold pieces for the killing of the Dragon and\n   bringing one tooth from his jaws of death,\n   thereby proving that he is dead.'\n\n"
    typeText(text)
    text = "           by decree of His Royal Majesty,\n                  -King Thesium of Anagua\n\n"
    typeText(text)
    chooseContinue()
    
def printIntro2():
    text = "   It's a warm summer day. You, Warrick, an elven\n   warrior of the Great Forest of Anagua, have left\n   your homeland in the trees with the other people\n   to pursue this profitable announcement from the\n   King.\n\n"
    typeText(text)
    text = "   You journey to the castle. As you make your way\n   through the city, you see the other brave men\n   who are willing to accept this challenge also.\n\n"
    typeText(text)
    text = "   You just hope that you will slay the Dragon\n   first.\n"
    typeText(text) 
    chooseContinue()     

def printIntro3():
    text = "   After waiting in line for an hour, the King's\n   squire makes the announcement that the quest is\n   ready to begin.\n\n"
    typeText(text)      
    text = "   He suggests that you go to the peddler's and\n   buy supplies for your journey because the\n   rest of the way will not be easy.\n\n"
    typeText(text) 
    chooseContinue()     
    
def startAdventure():
    print("   Do you:")
    print("   A) Go to the peddler's for supplies?")
    print("   B) Continue without supplies?")
    choice = input("   Which will you choose? \n   (A/B/Q)> ")
    if choice.lower() == "a":
        goToPeddler()
    elif choice.lower() == "b":
        continueWithout()
    elif choice.lower() == 'q':
        exit()
    else:
        return startAdventure()
    
def goToPeddler():
    text = "\n   You've decided that it would be best to go with\n   supplies for you do not know what the wilderness\n   ahead will provide. This will take a little\n   time, but is is worth it.\n\n"
    typeText(text)      
    text = "   At the peddler's, you decide to buy food, a\n   simple earth spellbook, some arrows for your\n   bow, and some matches in case you need to start\n   a fire. The peddler offers you a sword, but you\n   say you already have one forged from the metal\n   of a meteorite that crashed in the Western\n   Mountains years ago.\n\n"
    typeText(text)
    chooseContinue()
    track = "Amber Forest"
    playMusic(track, 0, 1)
    text = "   You leave for the gates heading to the forest\n   and come to a path. The path forks.\n\n"
    typeText(text)      
    chooseFork()
    
def continueWithout():
    text = "\n   You decide to choose the same as the majority\n   of the fighters and go on without supplies. You\n   again make your way through the city towards\n   the gates. You can see the forest of your home\n   up ahead.\n\n"
    typeText(text)      
    text = "   You enter the forest which you have known for\n   so long, but there is something different about\n   it. There is a strange silence in the air. No\n   signs of bird or animal life. You look around\n   and realize you've been surrounded by some of\n   the men that you saw at the castle.\n"
    typeText(text)      
    chooseContinue()
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "   They steal from you what few possessions you\n   have and take your life. The last memory you\n   have is of the men laughing at your lifeless\n   body on the ground...\n\n"
    typeText(text)
    restartStory(True)

def chooseFork():
    print("   Do you:")
    print("   A) Take the right path?")
    print("   B) Take the left path?")
    choice = input("   Which will you choose? \n   (A/B/Q)> ")
    if choice.lower() == "a":
        goRight()
    elif choice.lower() == "b":
        text = "\n   On the left path, you continue your quest."
        typeText(text)
        goLeft()
    elif choice.lower() == 'q':
        exit()
    else:
        return chooseFork()

def goRight():
    text = "\n   You decide to take the right path. You feel\n   that luck has helped you on what you believe\n   is an excellent decision.\n\n"
    typeText(text)
    text = "   As you walk along through the forest, you listen\n   to the sounds of nature and think about your\n   quest ahead. You keep walking and discover that\n   the path ends abruptly and the only way to\n   continue is through the thick underbrush.\n\n"
    typeText(text)
    text = "   You think about what you can do and narrow it\n   down to two choices.\n\n"
    typeText(text)
    chooseUnderbrush()

def chooseUnderbrush():
    print("   Do you:")
    print("   A) Go through the underbrush?")
    print("   B) Walk back and take the left path?")
    choice = input("   Which will you choose? \n   (A/B/Q)> ")
    if choice.lower() == "a":
        goUnderbrush()
    elif choice.lower() == "b":
        goBadLeft()
    elif choice.lower() == 'q':
        exit()
    else:
        return chooseUnderbrush()
    
def goUnderbrush():
    text = "\n   After your long, hard struggle through the\n   underbrush, you finally reach another path.\n   You think it might be the other path you could\n   have taken. You stop and take a rest to eat\n   lunch, but you know...\n\n"
    typeText(text)
    text = "   You must keep going.\n"
    typeText(text)
    chooseContinue()
    goLeft()
    
def goLeft():
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "\n   Night has begun to fall and you know you must\n   be very alert because there are dangers that\n   lurk in the shadows.\n\n"
    typeText(text)
    text = "   You continue walking and hear very strange\n   noises. You look around quickly and realize that\n   there are three small forms following you.\n"
    typeText(text)
    text = "   You turn quickly and make a decision.\n\n"
    typeText(text)
    armSelf()
    
def goBadLeft():
    text = "\n   After you disappoint yourself with your bad\n   decision on the right path and the time you've\n   wasted, you turn and head back.\n\n"
    typeText(text)
    chooseContinue()
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "   After walking several steps, an unknown flying\n   assailant attacks you from the trees. Dazed and\n   amazed, you fall subject to the appetite of a\n   giant raven!\n"
    typeText(text)
    restartStory(True)
    
def armSelf():
    print("   Do you:")
    print("   A) Draw your sword?")
    print("   B) Draw your bow?")
    print("   C) Run!")
    choice = input("   Which will you choose? \n   (A/B/C/Q) > ")
    if choice.lower() == "a":
        drawSword()
    elif choice.lower() == "b":
        drawBow()
    elif choice.lower() == "c":
        run()
    elif choice.lower() == 'q':
        exit()
    else:
        return armSelf()
    
def drawSword():
    text = "\n   Unsheathing your special sword, you prepare\n   yourself for an unknown attack. You find that\n   the forms are really goblin warriors!\n\n"
    typeText(text)
    text = "   You, being a very skill warrior yourself, strike\n   all three down with one swing. The goblins are\n   quickly cut in half by your mighty sword.\n"
    typeText(text)
    chooseContinue()
    track = "Itty Bitty"
    playMusic(track, 0, 1)
    text = "   You are very tired and decide to rest until\n   morning. After you awaken, you decide to continue\n   on the path.\n\n"
    typeText(text)
    continuePath()

def drawBow():
    text = "\n   You take the long wooden bow off your shoulder,\n   pulling three arrows from your quiver and take\n   aim. Launching all the three arrows at once,\n   you take down the three forms quickly.\n\n"
    typeText(text)
    text = "   After you are sure they are dead, you go and\n   inspect the bodies. You discover that they are\n   goblin warriors!\n"
    typeText(text)
    chooseContinue()
    track = "Itty Bitty"
    playMusic(track, 0, 1)
    text = "   You find yourself very tired and decide to rest\n   for the night. After you awaken, you continue\n   on the path.\n\n"
    typeText(text)
    continuePath()

def run():
    text = "\n   Not being sure of the strength of the forms or\n   yourself, you turn cowardly and start to run.\n   As you run, the branches strike against your\n   face. You don't think that you'll make it out\n   alive.\n\n"
    typeText(text)
    text = "   The forms prove to be very quick and catch up\n   with you easily and trip you with long pikes.\n   Before they stab down at you their pikes, you\n   discover that they are goblin warriors!\n"
    typeText(text)
    restartStory(True)
    
def continuePath():
    text = "   After walking for several hours on the thinning\n   path, you see a small mud hut with smoke coming\n   out a hole located on the top of the hut.\n\n"
    typeText(text)
    text = "   You are very tired, but scared of what you might\n   find in the creepy hut.\n\n"
    typeText(text)
    chooseRest()
    
def chooseRest():
    print("   Do you:")
    print("   A) Go to the hut and rest?")
    print("   B) Keep walking?")
    choice = input("   Which do you choose? \n   (A/B/Q) > ")
    if choice.lower() == "a":
        chooseHut()
    elif choice.lower() == "b":
        keepWalking()
    elif choice.lower() == 'q':
        exit()
    else:
        return chooseRest()
    
def chooseHut():
    text = "\n   You stumble over to the mud hut and knock on the small wooden door with no hinges.\n   No one answers. Suddenly, you hear a small voice from behind you. It startles\n   you at first, but then you discover that it is just a hermit, a trusted friend\n   of the elf people. He invites you in to eat and sleep.\n"
    typeText(text)
    chooseContinue()
    track = "Monplaisir"
    playMusic(track, 0, 1)
    text = "   While you are sleeping, you have a vision about the future. You see yourself\n   carrying something in a small sack. People around you are cheering. One last\n   thing you see before awaking is a woman walking, holding your hand.\n\n"
    typeText(text)
    text = "   The hermit wakes you urgently and whispers a verse in your ear, 'You must swing\n   before you fire.' Then he rushes you out the door. You have no clue what it means,\n   but you think it could help you later.\n\n"
    typeText(text)
    chooseWrite() 
    
def keepWalking():
    text = "\n   You decide to skip the hut and keep walking on the never-ending path. You realize\n   you know this part of the woods. You are near your home. You think of your family\n   and your people. You don't want to fail this quest and maybe die because you do\n   not want to lose the ones close to you.\n\n"
    typeText(text)
    text = "   You finally decide that there are no such things as dragons and return home.\n"
    typeText(text)
    restartStory(False)  
    
def chooseWrite():
    print("   Do you:")
    print("   A) Stop to write it down?")
    print("   B) Hurry along and write it later?")
    choice = input("   Which do you choose? \n   (A/B/Q) > ")
    if choice.lower() == "a":
        stopToWrite()
    elif choice.lower() == "b":
        hurryAlong()
    elif choice.lower() == 'q':
        exit()
    else:
        return chooseWrite()
    
def stopToWrite():
    text = "\n   You pull out some leaves and begin sharpening\n  your bark pencil.\n\n"
    typeText(text)
    chooseContinue()
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "   Then you see why the hermit was rushing you.\n   You start to run, but five men also on the quest\n   spot you and take you down.\n\n"
    typeText(text)
    text = "   They steal your belongings and stab you to death.\n"
    typeText(text)
    restartStory(True)
    
def hurryAlong():
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "\n   You start to run, sensing a feeling of danger\n   and only look back once to see five men overtake\n   the hermit's hut and kill your friend.\n"
    typeText(text)
    chooseContinue()
    track = "Itty Bitty"
    playMusic(track, 0, 1)
    text = "   You slip into the forest so as not to be seen\n   and escape safely. You quietly thank the hermit\n   for his kindness to yourself. You will always\n   remember his bravery.\n\n"
    typeText(text)
    text = "   You come to the edge of the forest and see a\n   great, broad river that seems to stretch across\n   for miles. You now know that your journey has\n   just begun.\n\n"
    typeText(text)
    text = "   You come across a boat and get in. You see two\n   choices: go across the river to the scary swamp\   nor go into the dangerous ocean.\n\n"
    typeText(text)
    chooseRiverOrOcean()
    
def chooseRiverOrOcean():
    print("   Do you:")
    print("   A) Choose the river?")
    print("   B) Choose the ocean?")
    choice = input("   Which do you choose? \n   (A/B/Q) >" )
    if choice.lower() == "a":
        goRiver()
    elif choice.lower() == "b":
        text = "   You head out into the ocean and come across a storm."
        typeText(text)
        goOcean()
    elif choice.lower() == 'q':
        exit()
    else:
        return chooseRiverOrOcean()
        
def goRiver():
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "\n   After boating for a while, you notice a school\n   of piranhas! They are swimming too fast to out-\n   paddle them.\n\n"
    typeText(text)
    shootOrZap()
    
def shootOrZap():
    print("   Do you:")
    print("   A) Shoot arrows?")
    print("   B) Zap them?")
    choice = input("   Which do you choose? \n   (A/B/Q) > ")
    if choice.lower() == "a":
        shootArrows()
    elif choice.lower() == "b":
        zapThem()
    elif choice.lower() == 'q':
        exit()
    else:
        return shootOrZap()
    
def shootArrows():
    text = "\n   You try to shoot arrows at them but then wooden\n   arrows float to the top instead. The recoil\n   from the bow sends you over the side of the boat.\n   In your last moments, you see nothing but teeth.\n"
    typeText(text)
    restartStory(True)
    
def zapThem():
    text = "\n   The electricity fills the water and all the\n   piranhas die. You don't like piranhas but\n   remember that they're good for you.\n\n"
    typeText(text)
    eatOrNo()
    
def eatOrNo():
    print("   Do you:")
    print("   A) Choose to eat the piranhas?")
    print("   B) Choose to not eat the piranhas?")
    choice = input("   Which do you choose? \n   (A/B/Q) > ")
    if choice.lower() == "a":
        eat()
    elif choice.lower() == "b":
        dontEat()
    elif choice.lower() == 'q':
        exit()
    else:
        return eatOrNo()
    
def dontEat():
    text = "\n   As you begin to paddle away again, you feel a\n   tugging sensation rock the boat back and forth.\n   Before you can react, you are thrown from the\n   boat and into the water. The fish have turned\n   into zombies! The murky water turns red as the\n   undead piranhas eat you!\n"
    typeText(text)
    restartStory(True)
    
def eat():
    track = "Itty Bitty"
    playMusic(track, 0, 1)
    text = "\n   You fill up on piranhas and are ready to go on.\n"
    typeText(text)
    chooseContinue()
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "\n   There are some rapids up ahead.\n"
    typeText(text)
    fordOrEvaporate()
    
def fordOrEvaporate():
    print("   Do you:")
    print("   A) Try to ford the rapids?")
    print("   B) Try to evaporate some of the water with\nsome fireballs?")
    choice = input("   Which do you choose? \n   (A//B/Q) > ")
    if choice.lower() == "a":
        ford()
    elif choice.lower() == "b":
        evaporate()
    elif choice.lower() == 'q':
        exit()
    else:
        return fordOrEvaporate()
    
def ford():
    text = "\n   The rapids are two powerful! You are crushed\n   against the rocks and die!\n"
    typeText(text)
    restartStory(True)
    
def evaporate():
    text = "\n   After a lot of trying, you manage to evaporate\n   the dangerous part of the water within the brief\n   allotted time. You continue to the swamp.\n"
    typeText(text)
    chooseContinue()
    track = "Underclocked"
    playMusic(track, 0, 1)
    text = "\n   As you enter the dark, green, shadowy swamp,\n   you notice the pungent smell of the scurrying\n   rats and decaying bodies scattered around. You\n   wonder what kind of beast could have done this\n   kind of damage, but are unable to figure it out.\n\n"
    typeText(text)
    text = "   You follow a solitary path for an estimated\n   quarter mile, finding nothing of note. However,\n   you soon come to a river, and are forced to\n   cross somehow.\n\n"
    typeText(text)
    text = "   There is a mud bank to the left of you, but it\n   is very wet and scattered with plants.\n\n"
    typeText(text)
    goMudOrTree()
    
def goMudOrTree():
    print("   Do you:")
    print("   A) Go into the mud?")
    print("   B) Climb the nearby tree and try to jump\nover the stream?")
    choice = input("   Which do you choose? \n   (A/B/Q) > ")
    if choice.lower() == "a":
        goMud()
    elif choice.lower() == "b":
        climbTree()
    elif choice.lower() == 'q':
        exit()
    else:
        return goMudOrTree()
    
def goMud():
    text = "\n   You begin crawling in the mud, almost smothered\n   by the low lying bushes above you...your clothes\n   are soiled and stained, but you took the easy way.\n"
    typeText(text)
    chooseContinue()
    text = "   You barely go over the stream, before you wince\n   as you feel the exhaustion and pain in your legs.\n   Now would you like to rest or journey on?\n\n"
    typeText(text)
    restOrJourney()
    
def climbTree():
    text = "\n   You shimmy your way up the thick trunk and find\n   yourself, once again, stuck with a left and\n   right choice, this time branches.\n\n"
    typeText(text)
    leftOrRightBranch()
    
def leftOrRightBranch():
    print("   Do you:")
    print("   A) Take the left branch?")
    print("   B) Take the right branch?")
    choice = input("   Which do you choose? \n   (A/B/Q) > ")
    if choice.lower() == "a":
        leftBranch()
    elif choice.lower() == "b":
        rightBranch()
    elif choice.lower() == 'q':
        exit()
    else:
        return leftOrRightBranch()  
    
def leftBranch():
    text = "\n   You leap with great grace, almost as if you\n   are flying..."
    typeText(text)
    time.sleep(1)
    text = "wait a minute..."
    typeText(text)
    time.sleep(2)
    text = "\n   You aren't even in the air!\n\n"
    typeText(text)
    time.sleep(1)
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "   You've landed in the snout of an unusually large\n   alligator. He snaps you up quickly, and you are\n   instantly killed.\n"
    typeText(text)
    restartStory(True)     

def rightBranch():
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "\n   You slowly creep onto the right branch, and\n   quickly look down with uneasiness.\n\n"
    typeText(text)
    text = "   Are you getting scared? That's no way for a\n   proud elven warrior like you to go down in\n   history!\n\n"
    typeText(text)
    text = "   I can imagine: Warrick the Great Chicken!\n\n"
    typeText(text)
    jumpOrDown()
    
def jumpOrDown():
    print("   Do you:")
    print("   A) Climb back down?")
    print("   B) Jump?")
    choice = input("   Which do you choose? \n   (A/B/Q) > ")
    if choice.lower() == "a":
        text = "\n   You fall a short way and find yourself once\n   again at the tree trunk. Great. Now what?\n\n"
        typeText(text)
        goMudOrTree()
    elif choice.lower() == "b":
        jumpDown()
    elif choice.lower() == 'q':
        exit()
    else:
        return jumpOrDown()     
    
def jumpDown():
    track = "Underclocked"
    playMusic(track, 0, 1)
    text = "\n   You barely make it over the stream and wince as\n   your legs absorb the shock from your fall. Now,\n   would you like to rest or journey on?\n\n"
    typeText(text)
    restOrJourney() 
    
def restOrJourney():
    print("   Do you:")
    print("   A) Rest?")
    print("   B) Journey on?")
    choice = input("   Which do you choose? \n   (A/B/Q) > ")
    if choice.lower() == "a":
        rest()
    elif choice.lower() == "b":
        journeyOn()
    elif choice.lower() == 'q':
        exit()
    else:
        return restOrJourney()
    
def rest():
    text = "\n   You are too tired to go on, and quickly fall\n   asleep to the lull of the crickets and bullfrogs.\n\n"
    typeText(text)
    text = "   However, the next morning, snickers and giggles\n   are heard as small thieves have stolen all of\n   your goods and clothes.\n\n"
    typeText(text)
    text = "   As you lie in the mud, you realize it is over\n   for you, and you die days later of starvation.\n"
    typeText(text)
    restartStory(True)
    
def journeyOn():
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "\n   You go on, strong as ever, and walk down a\n   straight path until you reach a small, green\n   man wearing a red cloak. He looks somewhat\n   threatening, though he remains still.\n\n"
    typeText(text)
    killOrSpeak()
    
def killOrSpeak():
    print("   Do you:")
    print("   A) Try to kill him?")
    print("   B) Try to speak to him?")
    choice = input("   Which do you choose? \n   (A/B/Q) > ")
    if choice.lower() == "a":
        kill()
    elif choice.lower() == "b":
        speak()
    elif choice.lower() == 'q':
        exit()
    else:
        return killOrSpeak()
    
def kill():
    text = "\n   You lunge at him with your dagger drawn, but\n   are quickly killed as he spins and rakes\n   your eyes out.\n"
    typeText(text)
    restartStory(True)  
    
def speak():
    text = "\n   He speak your language, but only mutters\n   the words, 'Friend...foe...'\n"
    typeText(text)
    friendOrFoe()
    
def friendOrFoe():
    print("   A) Friend?")
    print("   B) Foe!")
    choice = input("   Which do you choose? \n(A/B/Q) > ")
    if choice.lower() == "a":
        chooseFriend()
    elif choice.lower() == "b":
        text = "\n   You shout, 'Foe!' before moving forward to attack."
        typeText(text)
        kill()
    elif choice.lower() == 'q':
        exit()
    else:
        return friendOrFoe()
    
def chooseFriend():  
    text = "\n   You reply, 'Friend.'\n"
    typeText(text)
    text = "   The two of you strike up a conversation, quickly\n   becoming friends, but soon the sun sets, leaving\n   you with another choice.\n\n"
    typeText(text)
    talkOrStay()
    
def talkOrStay():
    print("   Do you:")
    print("   A) Tell him to talk to you later?")
    print("   B) Stay with him?")
    choice = input("   Which do you choose? \n   (A/B/Q) > ")
    if choice.lower() == "a":
        talk()
    elif choice.lower() == "b":
        stay()
    elif choice.lower() == 'q':
        exit()
    else:
        return talkOrStay()

def talk():
    text = "\n   You say, 'I'm terribly sorry, but I must go.\n   Hopefully I will speak to you again soon!'\n\n"
    typeText(text)
    text = "   He replies, 'Yes...dear traveler...\n   come back...soon.'\n\n"
    typeText(text)
    text = "   As you leave, you come to a three-way path.\n\n"
    typeText(text)
    goRightCenterLeft()
    
def stay():
    text = "\n   You say, 'Pardon my intrusion, but may I stay\n   with you for the night? I hope it isn't too\n   much trouble, for I am very weary!'\n\n"
    typeText(text)
    text = "   He answers, 'Oh...sure! Stay...as long as you\n   like...You...are my good friend!'\n\n"
    typeText(text)
    text = "   You go to his house and find his children, all\n   35 of them! You sleep very little, as the kids\n   are talking to you all night. However, in the\n   morning, you quickly steal away while the people\n   are sleeping and return to your adventures.\n\n"
    typeText(text)
    text = "   You come to a three-way path.\n\n"
    typeText(text)
    goRightCenterLeft()
    
def goRightCenterLeft():
    print("   Which way do you take?")
    print("   A) Right path")
    print("   B) Center path")
    print("   C) Left path")
    choice = input("   Which do you choose? \n   (A/B/C/Q) > ")
    if choice.lower() == "a":
        goRightOrCenterPath()
    elif choice.lower() == "b":
        goRightOrCenterPath()
    elif choice.lower() == "c":
        goLeftPath()
    elif choice.lower() == 'q':
        exit()
    else:
        return goRightCenterLeft()    
    
def goRightOrCenterPath():
    text = "\n   You get lost, but are found by the swamp creature's\n   family. They quickly save you from your predicament\n   and lead lead you safely to the edge of the swamp.\n\n"
    typeText(text)
    text = "   Suddenly though, a sacred being comes down\n   from above and rewards you with the following\n   words:\n\n"
    typeText(text)
    text = "   'Let the altitude keep climbing higher...'\n"
    typeText(text)
    chooseContinue()
    continuePlains()

def goLeftPath():
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "\n   You take a single step and quickly fall into\n   the mud, sinking as you go...soon the mud has\n   dried and you are unable to move from the chest\n   up.\n\n"
    typeText(text)
    text = "   You soon die of dehydration.\n"
    typeText(text)
    restartStory(True)
    
def goOcean():
    print("   Do you:")
    print("   A) Brave the Storm?")
    print("   B) Turn back to shore?")
    choice = input("   Which do you choose? \n   (A/B/Q) > ")
    if choice.lower() == "a":
        islandAttack()
    elif choice.lower() == "b":
        backShore()
    elif choice.lower() == 'q':
        exit()
    else:
        return goOcean()
    
def islandAttack():
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "\n   You sail through the storm and come upon an\n   island. As you sail toward it, a group of natives\n   hurl spears at you.\n\n"
    typeText(text)
    retreatFightThrow()
    
def retreatFightThrow():
    print("   Do you:")
    print("   A) Retreat?")
    print("   B) Fight back with jolts of electricity?")
    print("   C) Throw fireballs?")
    choice = input("   Which do you choose? \n   (A/B/C/Q) > ")
    if choice.lower() == "a":
        backShore()
    elif choice.lower() == "b":
        fight()
    elif choice.lower() == "c":
        throwFireballs()
    elif choice.lower() == "q":
        exit()
    else:
        return retreatFightThrow()
    
def fight():
    text = "\n   There are too many spears! You die!\n"
    typeText(text)
    restartStory(True)
    
def throwFireballs():
    text = "\n   You set spears on fire, one by one. Some falling\n   spears hit other spears and ignite them. The\n   natives retreat to another island.\n\n"
    typeText(text)
    retreatFollow()
    
def retreatFollow():
    print("   Do you:")
    print("   A) Retreat?")
    print("   B) Follow them back to their island?")
    choice = input("   Which do you choose? \n   (A/B/Q) > ")
    if choice.lower() == "a":
        backShore()
    elif choice.lower() == "b":
        followBack()
    elif choice.lower() == "q":
        exit()
    else:
        return retreatFightThrow()    
    
def followBack():
    track = "Itty Bitty"
    playMusic(track, 0, 1)
    text = "\n   You get to the island and are greeted by another\n   tribe. They won't let you leave. You live happily\n   ever after with them.\n"
    typeText(text)
    restartStory(False)
    
def backShore():
    track = "Monplaisir"
    playMusic(track, 0, 1)
    text = "\n   On your way back to shore, you come upon the\n   Vhwortyzaxisnghkepqublcfdjm! One head always\n   lies and the other always tells the truth.\n\n"
    typeText(text)
    text = "   'One path leads to certain death, the other\n   leads to freedom,' the heads intone. You can\n   only ask one question to determine the path to\n   take.\n\n"
    typeText(text)
    heads()
    print("")
    paths()
    
def heads():
    print("   Do you:")
    print("   A) Ask the first head a question?")
    print("   B) Ask the second head a question?")
    choice = input("   Which do you choose? \n   (A/B/Q) > ")
    if choice.lower() == "a":
        print("")
        head(1)
    elif choice.lower() == "b":
        print("")
        head(2)
    elif choice.lower() == "q":
        exit()
    else:
        return heads()    
    
def head(x):
    print("   A) Which path do I take?")
    print("   B) Which path would your other head say to take?")
    print("   C) Do you lie or tell the truth?")
    if x == 1:
        choice = input("   What do you ask the first head? \n   (A/B/C/Q) > ")
    else:
        choice = input("   What do you ask the second head? \n   (A/B/C/Q) > ")
    if choice.lower() == "a":
        if x == 1:
            text = "\n   Take the second path.\n"
            typeText(text)
        else:
            text = "\n   Take the first path.\n"
            typeText(text)
    elif choice.lower() == "b":
        text = "\n   The head says, 'My counterpart would say to take the first path.\n"
        typeText(text)
    elif choice.lower() == "c":
        text = "\n   The head replies, 'I only speak the truth.'\n"
        typeText(text)
    elif choice.lower() == "q":
        exit()
    else:
        return head(x)
    
def paths():
    print("   Do you:")
    print("   A) Choose the first path?")
    print("   B) Choose the second path?")
    choice = input("   Which do you choose? \n   (A/B\Q) > ")
    if choice.lower() == "a":
        pathOne()
    elif choice.lower() == "b":
        pathTwo()
    elif choice.lower() == "q":
        exit()
    else:
        return paths()
    
def pathOne():
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "\n   'You chose the wrong path!' the Vhwortyzaxisnghkepqublcfdjm\n   screams. And you die. Just like that.\n"
    typeText(text)
    restartStory(True)
    
def pathTwo():
    track = "Itty Bitty"
    playMusic(track, 0, 1)
    text = "\n   'You chose the correct path.'\n\n"
    typeText(text)
    text = "   As you land on the shore, you see that you have passed the swamp and are going\n   to enter the plains. However, a bottle that has washed ashore catches your eye.\n   You pick it up and notice that a rolled up paper is inside of it. You manage to\n   get the paper out and open it. It has a message written on it that says...\n\n"
    typeText(text)
    text = "   'Let the altitude keep climbing higher'\n\n"
    typeText(text)
    text = "   You continue on to the plains.\n"                    
    typeText(text)
    chooseContinue()
    continuePlains()
    
def continuePlains():
    text = "As you enter the wide open plains you feel a\nsudden gust of wind as you realize just how\nfar you have to go before you reach your final\ndestination.\n\n"
    typeText(text)
    text = "The grass is slightly higher than your waist\nand is so thick you can hardly see your feet.\n\n"
    typeText(text)
    text = "Knowing you have limited time, you try to\nlogically think out the course you should take.\n\n"
    typeText(text)
    trailOrPath()
    
def trailOrPath():
    print("   Do you:")
    print("   A) Choose the old, weed-covered trail to the left\n   over the grassy knoll?")
    print("   B) Choose the dirt path to the right. The\n   path seems to have small footprints of an unknown\n   origin.")
    choice = input("   Which do you choose? \n   (A/B/Q) > ")
    if choice.lower() == "a":
        trail()
    elif choice.lower() == "b":
        dirtPath()
    elif choice.lower() == "q":
        exit()
    else:
        return trailOrPath()    
        
def trail():
    text = "\n   You decide to take the less beaten path to the\n   left. As you start walking, the grass is becoming\n   too tall for your short body so you take your\n   sword from its sheath and begin to slash down\n   the weeds in your path.\n\n"
    typeText(text)
    text = "   You're hoping to have found a shortcut, but\n   instead it only leads into a small creek that\n   winds and bends through dense weeds.\n\n"
    typeText(text)
    creekOrShortcut()
    
def dirtPath():
    text = "\n   The dirt path appeals to you despite the fear that the footprints may lead to\n   something you may not like. Everything is going fine until you hear faint\n   screeching coming closer and closer through the surrounding brush.\n"
    typeText(text)
    chooseContinue()
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "   You pull out your spellbook and try to cast a protective spell before whatever\n   is making the sound is upon you. Minutes turn into seconds and the sounds are so\n   close you can hear the footsteps. The spell is almost complete, but before you\n   can finish it,small, green wretched-looking monsters leap out of the bush. They\n   are even more hideous than you could ever have imagined. Their mouths are seeping\n   oozing saliva and they are staring at you with red, devil-like eyes.\n\n"
    typeText(text)
    speakOrBanish()
    
def speakOrBanish():
    print("   Do you:")
    print("   A) Speak with them and try to become friends?")
    print("   B) Try to banish them to another time and place\n   with a fast activating spell, and be on your\n   way?")
    choice = input("   Which do you choose? \n   (A/B/Q) > ")
    if choice.lower() == "a":
        speakFriend()
    elif choice.lower() == "b":
        banish()
    elif choice.lower() == "q":
        exit()
    else:
        return speakOrBanish() 
        
def speakFriend():
    text = "\n   You try to reason with yourself on what to do, and you decide to try to talk to\n   the monsters. You think they might know a shortcut, considering that they live\n   on the plains. You pick out the largest creature and being to talk to it in every\n   language you know. As you grow tired of trying, the whole band of animals start\n   to chirp in a high-pitched sound. You become alarmed and begin to slowly ease\n   your way to the safety of a nearby tree just large enough to support your weight.\n\n"
    typeText(text)
    text = "   Then comes the screeching from behind you as you bump into a slimy, grotesque-\n   looking monster! You are now so frightened that you forget all logic and take\n   off running. You soon find out how bad of an idea running is as the screeching\n   becomes louder and encircle you completely. Monsters from all sides leap onto\n   you with teeth bared.\n"
    typeText(text)
    restartStory(True)
    
def banish():
    text = "\n   You are fed up with things stopping you from reaching your final destination,\n   so you decide to banish the wretched creatures standing before you to another\n   time and another place with a spell. You pull out your spellbook very slowly as\n   the monsters stare at you with a cross-eyed look. Page by page you turn until\n   you find the spell you want. Wasting no time you begin chanting the words of the\n   spell out loud.\n"
    typeText(text)
    text = "   The monsters seem amused at first, but they stop chirping and begin to screech.\n   They start to leap at you just as you are mid-sentence of your last chant.\n   Instinctively you grab for your sword and lash out at the first one you see.\n   The monsters are somehow stopped by the powerful blows and as a result, several\n   are now lying around you in a morbid mess of blood and decapitated limbs.\n"
    typeText(text)
    chooseContinue()
    text = "   You initial success appears to anger the remaining creatures and they increase\n   the intensity of their attacks. Soon you are no match for them as you fall victim\n   to their superior numbers. You slowly and painfully die as you are devoured whole.\n"
    typeText(text)
    restartStory(True)
    
def creekOrShortcut():
    print("   Do you:")
    print("   A) Follow the creek so that if you come upon\n   the desert you'll have water before entering?")
    print("   B) Follow the shortcut branching off of the creek\n   to the desert?")
    choice = input("   Which do you choose? \n   (A/B/Q) > ")
    if choice.lower() == "a":
        creek()
    elif choice.lower() == "b":
        shortcut()
    elif choice.lower() == "q":
        exit()
    else:
        return creekOrShortcut()    
    
def shortcut():
    text = "\n   You decide to save a tremendous amount of much-\n   needed time and take the shortcut. It makes more\n   sense to take the shortcut, because it's so much\n   easier to walk through the shorter grass than\n   to continue through the long grass.\n"
    typeText(text)
    chooseContinue()
    text = "   You walk.\n"
    typeText(text)
    chooseContinue()
    text = "   And walk...\n"
    typeText(text)
    chooseContinue()
    text = "   And walk...\n"
    typeText(text)
    chooseContinue()
    text = "   It becomes so tiresome that you cannot continue\n   any longer and you have to stop.\n\n"
    typeText(text)
    text = "   You reach for your pouch for a drink of water,\n   but instead of water there is only air. You\n   throw the pouch down in disgust, and as you\n   throw it down you notice a hole in the bottom.\n   You become angered that you didn't notice that\n   when you put the water in the pouch.\n\n"
    typeText(text)
    digOrGiveUp()
    
def digOrGiveUp():
    print("   Do you:")
    print("   A) Try to dig for life-saving water and then once\n   you find it you can continue?")
    print("   B) Give up because you know you will die even if\n   you find water?")
    choice = input("   Which do you choose? \n   (A/B/Q) > ")
    if choice.lower() == "a":
        dig()
    elif choice.lower() == "b":
        giveUp()
    elif choice.lower() == "q":
        exit()
    else:
        return digOrGiveUp()
    
def dig():
    text = "\n   You decide that you would rather try to preserve\n   your life as long as possible, so you dig for\n   water. You choose a place right under the closest\n   tree and begin to dig as fast as humanly possible.\n   Your decision to dig has paid off because you\n   found an underground stream!\n\n"
    typeText(text)
    text = "   You drink the water in huge gulps, barely\n   stopping for air. After you have your fill of\n   the ice-cold water, you lie down to rest.\n\n"
    typeText(text)
    text = "   Your sleep is interrupted by an indescribable\n   pain in your stomach. It feels as though a knife\n   is tearing through your entire body. As you\n   lose consciousness, you figure out that the\n   cause of your pain is the bad water. Thinking\n   only of your mistake, you let death come.\n"
    typeText(text)
    restartStory(True)
    
def giveUp():
    text = "\n   You decide not to even attempt to find water\n   because you know you will die anyway.\n\n"
    typeText(text)
    text = "   As you drift away into unconsciousness, you\n   think of everything you will be leaving behind\n   you. It all depresses you very much, but at\n   least you die in peace and without suffering.\n"
    typeText(text)
    restartStory(True) 
    
def creek():
    text = "\n   You fill your small rawhide pouch with the creek water, and then continue alongside\n   the small creek. It is taking a long time to walk to the desert. You begin to\n   wonder if the other choice had been a better one, but soon dismiss the thought\n   as the tall grass stops. You can see the desert once more, and you still have\n   your pouch full. After you take a small drink of water and sit down slowly to\n   rest, you notice the ten-foot wide gap in front of you. You curse out at yourself\n   for not seeing it earlier, because now you have one more problem to add to your\n   ever-increasing list of troubles.\n\n"
    typeText(text)
    jumpOrMagic()
    
def jumpOrMagic():
    print("   Do you:")
    print("   A) Get up and try to jump across the gap, and prove\n   to yourself you don't always need the aid of\n   magic?")
    print("   B) Use your magic to float across the gap and save\n   some of the energy you may need along your trek?")
    choice = input("   Which do you choose? \n   (A/B/Q) > ")
    if choice.lower() == "a":
        jump()
    elif choice.lower() == "b":
        magic()
    elif choice.lower() == "q":
        exit()
    else:
        return digOrGiveUp()  
    
def magic():
    text = "\n   You think using your magic is the better choice, so you carefully take out the\n   old spellbook and begin to cast the spell. As you start, a whirling wind seems\n   to form out of nowhere and beings to slowly pick you up off of the sandy ground.\n   It has a calming effect on you, so you close your eyes and just let the spell\n   carry you over the gap.\n\n"
    typeText(text)
    text = "   As you are floating, you notice that it is taking forever to get across a mere\n   ten feet. Cautiously you open your eyes.\n"
    typeText(text)
    chooseContinue()
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "   All you see around you are dirt walls that are quickly speeding by.\n\n"  
    typeText(text)
    text = "   You suddenly panic and look down to see your fate. Twenty giant spikes are\n   awaiting you at the bottom of the pit. In seconds you will be impaled by at least\n   three spikes. Your life flashes before your eyes and you know you have failed.\n   You die a death of dishonor.\n"
    typeText(text)
    restartStory(True)
    
def jump():
    text = "\n   You choose to try and jump across the ten feet of space by yourself. In\n   preparation, you judge the distance and the amount of strides you will\n   need to take in order to make it. You are ready after a long and fearful\n   preparation. Once more you look down at the sandy and worn-looking ground and\n   say an old elven prayer your mother once told you for good luck. Then you know\n   it's time.\n\n"
    typeText(text)
    text = "   You take off as fast as your tiny legs can take you. You approach the edge\n   thinking only of making it, and then you finally jump.\n"
    typeText(text)
    chooseContinue()
    text = "   It seems to take forever for something to happen. Suddenly you open your eyes\n   to see that you might not make it. You kick your legs in one last desperate\n   attempt to make it and, to your surprise, you do.\n\n"
    typeText(text)
    text = "   The shock makes your legs give way and you fall, but you don't notice because\n   you're kissing the ground and looking back at how far you actually jumped. You\n   rest once more and then try to decide what to do.\n\n"
    typeText(text)
    summonOrWalk()

def summonOrWalk():
    print("   Do you:")
    print("   A) Try to summon a beast to carry you to the desert?")
    print("   B) Try to walk the 5+ miles on foot without aid?")
    choice = input("   Which do you choose? \n   (A/B/Q) > ")
    if choice.lower() == "a":
        summon()
    elif choice.lower() == "b":
        walk()
    elif choice.lower() == "q":
        exit()
    else:
        return summonOrWalk()    
        
def walk():
    text = "\n   You evaluate the amount of strength you have\n   left and you decide to on by yourself.\n"
    typeText(text)
    chooseContinue()
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "   You have not walked more than a mile when the\n   sky turns a deathly black, the clouds swirl in\n   a threatening wind, and the grass of the plains\n   grab hold of you with its long, waving blades.\n\n"
    typeText(text)
    text = "   You shiver in fear as the brilliant yellow flash\n   of lightning consumes your body, rendering you\n   helpless under its power, and finally as the\n   lightning is gone you fall limp and die.\n"
    typeText(text)
    restartStory(True)
    
def summon():
    text = "\n   You once again decide to take the easy way and summon a beast to carry you the\n   rest of the way to the desert. Before you can even attempt to summon anything\n   you need to collect certain materials, all of which can be easily obtained from\n   the area around you.\n\n"
    typeText(text)
    text = "   You first pick up a handful of sand, then mix it with some water from the earth,\n   and finally you begin to mix that concoction together with your very own blood\n   from a cut your make with your sword. As the ingredients mix together, a beast\n   starts to appear before you. It has a dark brown, shaggy coat like a buffalo,\n   beady eyes like a rat, and a massive body like an elephant.\n"
    typeText(text)
    chooseContinue()
    text = "   You're a little intimidated at first, as the animal only stares at you and snorts,\n   but you soon come to realize it's a gentle creature and you climb on its back.\n\n"
    typeText(text)
    text = "   It lurches forward at a blinding speed, and in a matter of a few seconds you are\n   at the edge of the desert. You blink and slowly dismount the giant beast. As you\n   do, the animal slowly disappears into the air around you.\n\n"
    typeText(text)
    text = "   As the beast fades, a raspy voice, barely audible tells you, 'That which falls\n   upon his head.'\n\n"
    typeText(text)
    text = "   You take your first step on the blistering hot sand of the desert, try to breathe\n   through the heat, and begin perhaps the most grueling walk you have ever attempted.\n"
    typeText(text)
    chooseContinue()
    desert()
    
def desert():
    track = ""
    playMusic(track, 0, 1)
    text = "\n   You enter the Moseekan Desert on the island of\n   Anagua. The temperatures in the desert are\n   extremely hot. The temperatures sometimes reach\n   125 degrees. Beware! Many strange creatures\n   live in the Moseekan.\n\n"
    typeText(text)
    text = "   You initially take a westerly course. You soon\n   come to an enormous rock in the middle of your\n   path. It has a distinctive column of rock that\n   juts straight up into the air. You go around\n   the rock and continue on your way.\n"
    typeText(text)
    chooseContinue()
    text = "   After about two miles, you come upon a giant\n   sand dune that disrupts your path.\n\n"
    typeText(text)
    northwestWestSouthwest()
    
def northwestWestSouthwest():
    print("   Do you:")
    print("   A) Go northwest around the dune?")
    print("   B) Continue west over the dune?")
    print("   C) Travel southwest around the dune?")
    choice = input("   Which do you choose? \n   (A/B/C/Q) > ")
    if choice.lower() == "a":
        northwest()
    elif choice.lower() == "b":
        west()
    elif choice.lower() == "c":
        southwest()
    elif choice.lower() == "q":
        exit()
    else:
        return northwestWestSouthwest()    

def west():
    text = "\n   You start the long climb up the giant sand dune.\n   Your climb up the dune is easy at first but soon\n   gets steeper. Your easy climb is now very\n   difficult.\n"
    typeText(text)
    chooseContinue()
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "\n   All of a sudden you slip and grab onto a vine.\n   The vine turns out to be a snake! It bites you\n   and injects its deadly venom.\n\n"
    typeText(text)
    text = "   He then eats you for dinner.\n"
    typeText(text)
    restartStory(True)
    
def northwest():
    text = "\n   You continue your treacherous walk around the\n   north side of the dune.\n\n"
    typeText(text)
    text = "   As you go, your mouth begins to feel like\n   sandpaper. Each step you take makes it worse.\n\n"
    typeText(text)
    turnEndure()
    
def turnEndure():
    print("   Do you:")
    print("   A) Turn back?")
    print("   B) Endure the heat and continue in the hope of\n   finding water?")
    choice = input("   Which do you choose? \n   (A/B/Q) > ")
    if choice.lower() == "a":
        turnBack()
    elif choice.lower() == "b":
        endure()
    elif choice.lower() == "q":
        exit()
    else:
        return turnEndure()
    
def turnBack():
    text = "\n   You decide to turn back and try to get back to\n   the rock.\n\n"
    typeText(text)
    text = "   You see a row of cacti and decide to follow\n   along the row. You come to a break in the row.\n\n"
    typeText(text)
    straightRight()
    
def straightRight():
    print("   Do you:")
    print("   A) Keep going straight?")
    print("   B) Turn to the right?")
    choice = input("   Which do you choose? \n   (A/B/Q) > ")
    if choice.lower() == "a":
        keepStraight()
    elif choice.lower() == "b":
        turnRight()
    elif choice.lower() == "q":
        exit()
    else:
        return straightRight()     
    
def keepStraight():
    text = "\n   You keep going along the cactus row. Eventually\n   it ends.\n\n"
    typeText(text)
    text = "   By now you are really lost and can't find your\n   way back.\n\n"
    typeText(text)
    text = "   You soon become thirsty and die slowly in the\n   hot heat of the desert.\n"
    typeText(text)
    restartStory(True)
    
def turnRight():
    text = "\n   Turning right, you wander in the extreme heat\n   trying to find a familiar object. You soon see\n   the distinctive rock in front of you.\n\n"
    typeText(text)
    text = "   You continue toward the rock and are at the\n   spot from which you started. You go around the rock\n   and continue on your way.\n\n"
    typeText(text)
    text = "   After about two miles, you come upon the giant\n   sand dune that disrupts your path.\n\n"
    typeText(text)
    northwestWestSouthwest()         
    
def endure():
    text = "\n   You are walking aimlessly in the scorching\n   desert. You are becoming very thirsty.\n   You come upon a large cactus.\n\n"
    typeText(text)
    cactus()
    
def cactus():
    print("   Do you:")
    print("   A) Try to get water from the cactus?")
    print("   B) Leave it alone and continue?")
    choice = input("   Which do you choose? \n   (A/B/Q) > ")
    if choice.lower() == "a":
        getWater()
    elif choice.lower() == "b":
        leaveAlone()
    elif choice.lower() == "q":
        exit()
    else:
        return cactus()  
    
def getWater():
    track = "Monplaisir"
    playMusic(track, 0, 1)
    text = "\n   You are intelligent enough to know there is a\n   refreshing liquid in cacti.\n\n"
    typeText(text)
    text = "   You pull out your trusty sword and slice off a\n   piece. You hold it over your mouth and let\n   the liquid drip into your mouth.\n\n"
    typeText(text)
    text = "   What you didn't know was that some cactus juice\n   is poisonous.\n"
    typeText(text)
    restartStory(True)  
    
def leaveAlone():
    track = "Monplaisir"
    playMusic(track, 0, 1)
    text = "\n   You leave the cactus alone. You continue on\n   your path through the desert.\n\n"
    typeText(text)
    text = "   You see an oasis and go towards it in search\n   of water.\n"
    typeText(text)
    chooseContinue()
    oasis()
    
def southwest():
    text = "\n   You choose to go southwest around the giant\n   sand dune.\n\n"
    typeText(text)
    text = "   When you round the southern tip of the dune,\n   you come upon a sandworm. It is thirty feet\n   long and has rough brown skin.\n\n"
    typeText(text)
    runOrFight()
    
def runOrFight():
    print("   Do you:")
    print("   A) Run back?")
    print("   B) Stay and fight it with your sword?")
    choice = input("   Which do you choose? \n   (A/B/Q) > ")
    if choice.lower() == "a":
        print("")
        northwestWestSouthwest()
    elif choice.lower() == "b":
        worm()
    elif choice.lower() == "q":
        exit()
    else:
        return runOrFight()
    
def worm():
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "\n   You choose to stay and fight the sandworm. You\n   pull out your sword. It glimmers in the bright\n   sun.\n\n"
    typeText(text)
    heartOrHead()
    
def heartOrHead():
    print("   Do you:")
    print("   A) Stab at the heart?")
    print("   B) Swipe at the head?")
    choice = input("   Which do you choose? \n   (A/B/Q) > ")
    if choice.lower() == "a":
        stabHeart()
    elif choice.lower() == "b":
        swipeHead()
    elif choice.lower() == "q":
        exit()
    else:
        return heartOrHead()   
    
def swipeHead():
    text = "\n   You swipe at the sandworm's head. He ducks\n   and your sword makes a 'wiff' sound in the air.\n\n"
    typeText(text)
    text = "   It is furious and is slithering directly at you\n   as fast as a speeding train.\n\n"
    typeText(text)
    text = "   You close your eyes. Goodbye!\n"
    typeText(text)
    restartStory(True)
    
def stabHeart():
    text = "\n   Your stab at the sandworm's heart and the sharp\n   blade of your sword pierces it. The creature\n   falls down, dying in great pain.\n\n"
    typeText(text)
    text = "   You see an oasis and you decide to walk towards\n   it.\n"
    typeText(text)
    chooseContinue()
    oasis()
    
def oasis():
    track = "Monplaisir"
    playMusic(track, 0, 1)
    text = "\n   You walk into the green oasis. You haven't seen\n   this color for a long time. You sit down on the\n   edge of the pond. You take a long refreshing\n   drink. Feeling tired, you fall asleep in the\n   shade of a palm tree.\n\n"
    typeText(text)
    text = "   In the middle of your long nap you feel a blow\n   to your head. On the ground at your side is a\n   coconut. You pick it up and it breaks in two.\n   Inside you find a mysterious piece of paper\n   stating, 'Will strike him down, forever dead\n\n"
    typeText(text)
    text = "   Rubbing your head, you look up to see the\n   mountains before you. You know they hold the\n   lair of the dragon and the end of your quest...\n   but hopefully not the end of you.\n\n"
    typeText(text)
    text = "   Gathering your supplies, you move on.\n"
    typeText(text)
    chooseContinue()
    mountains()
    
def mountains():
    text = "   You finally make it out of the barren desert.\n   You look before you and see the vast\n   mountain lair of the Great Dragon. You make the hike up\n   and enter the twisted caves.\n\n"
    typeText(text)
    text = "   You hear the sound of dripping water throughout\n   the cavern and a stingy mist is in the air. All\n   of a sudden you hear it. Heavy breathing\n   coming from one of the paths. You follow the sound to\n   a large cavernous room.\n\n"
    typeText(text)
    text = "\t   THE LAIR OF THE DRAGON!\n"
    typeText(text)
    chooseContinue()
    theLair()
    
def theLair():
    text = "   You look around quickly and see huge piles of\n   gold...his hoard.\n\n"
    typeText(text)
    text = "   Sitting between piles is a huge dark form. A\n   loud echoing roar erupts from behind the piles.\n\n"
    typeText(text)
    text = "   You move closer to investigate. Seeing all the\n   gold, you are tempted to take some and flee.\n\n"
    typeText(text)
    text = "   You reach forward, and just before you grab\n   some of the gold, you are suddenly face-to-face\n   with Golan..."
    typeText(text)
    chooseContinue()
    theFight()
    
def theFight():
    track = "Dungeon Boss"
    playMusic(track, 0, 1)
    text = "\n   You quickly jump aside before being roasted with\n   an enormous gout of fire. Thinking back, you\n   remember the poem. 'This must be the secret,'\n   you think, but you don't quite understand it.\n   Now it's time for you to make your final decision.\n   What will you use to fight the dragon?\n\n"
    typeText(text)
    text = "   'I can use anything around me,' you think as\n   you notice spears, swords, and battleaxes among\n   the massive piles of gold. You also have everything\n   you currently carry.\n"
    typeText(text)
    recitePoem()
    
def recitePoem():
    text = "\n\t      You must swing before you fire"
    typeText(text)
    text = "\n\t   Let the altitude keep climbing higher"
    typeText(text)
    text = "\n\t      That which falls upon his head"
    typeText(text)
    text = "\n\t    Will strike him down, forever dead\n"
    typeText(text)
    text = "\n    1) Use your sword            \t 2) Use your bow      \t 3) Use your spellbook   \t 4) Use a mace   \t 5) Use a dagger"
    typeText(text)
    text = "\n    6) Say the poem aloud        \t 7) Use a rock        \t 8) Use a handful of dirt\t 9) Sing a song \t10) Fight with your fists"
    typeText(text)
    text = "\n   11) Use a torch              \t12) Use your own blood\t13) Use an axe          \t14) Use a whip  \t15) Use a feather"
    typeText(text)
    text = "\n   16) Use water from your pouch\t17) Use a sling       \t18) Use a club          \t19) Use a mirror\t20) Use a large diamond"
    typeText(text)
    choice = input("\n\n   What shalt thou use to slay the fearsome beast? \n   ( 1/ 2/ 3/ 4/ 5)\n   ( 6/ 7/ 8/ 9/10)\n   (11/12/13/14/15)\n   (16/17/18/19/20) > ")
    if int(choice) == 17:
        youWin()
    elif int(choice) <= 16 or int(choice) >= 18:  
        youLose()
    else:
        return recitePoem()
    
def youLose():
    text = "\n   You have made your choice.\n\n"
    typeText(text)
    text = "   It has no effect on Golan other than to give\n   him a slight chuckle at your foolish and worthless\n   attempt to slay him.\n\n"
    typeText(text)
    text = "   You frantically try to remember the poem more\n   clearly. What hidden meaning did it hold? What\n   have you missed?\n\n"
    typeText(text)
    text = "   Unfortunately, Golan does not miss the opportunity\n   as he releases another blast of fire.\n"
    typeText(text)
    restartStory(True)
    
def youWin():
    track = "Mountain Trials"
    playMusic(track, 0, 1)
    text = "\n   You think back to the lines of the poem you\n   have received throughout your quest. As you\n   pull your sling from your holster resting on\n   your belt. You are hoping this was the best\n   choice. You run behind a vast pile of gold and\n   take careful aim. Round and round you swing the\n   sling until...\n"
    typeText(text)
    chooseContinue()
    text = "   WOOOOOOSH!!!!!!!!!\n"
    typeText(text)
    chooseContinue()
    text = "   The small round stone punctures the area right\n   between the dragon's eyes! The stunned beast\n   falls hard to the ground, shaking the whole\n   cavern. Could it be true the Great Golan has\n   been slain?\n"
    typeText(text)
    chooseContinue()
    text = "   Yes! You finally recall it after studying the\n   motionless dragon. You remember the squire's\n   words from the beginning of your quest. You\n   walk calmly over to the dragon and pry one of\n   his blade-like teeth from his jaws of death.\n   Now that the hard part is over, you must return\n   to the castle with the good word!\n"
    typeText(text)
    chooseContinue()
    toTheCastle()
    
def toTheCastle():
    track = "8 Bit Win!"
    playMusic(track, 0, 1)
    text = "   The King is sitting in his throneroom when you\n   walk into His presence. You speak up nervously\n   of your news and hold up the dragon tooth. The\n   King slowly looks up with a broad smile on his\n   face. He congratulates you and announces a\n   celebration in your honor. For the first time\n   on your long and grueling quest, you feel a true\n   sense of joy. You go right to the town tailor\n   with your gold and buy his finest cloak. Your\n   quest is finally over!\n\n"
    typeText(text)
    chooseContinue()
    text = "\n   You are the new hero of Anagua.\n\n"
    typeText(text)
    text = "   Warrick the Elf!\n"
    typeText(text)
    runCredits()
    restartStory(False)  
    
def runCredits():
    track = "Itty Bitty"
    playMusic(track, 1, 1)
    text = "\n\t   Presented By:\n        CLICKETYCLACKGAMES"
    typeText(text)
    time.sleep(1)
    text = "\n\n\t   Game Design:\n          Anthony Braden\n            Eric Curts"
    typeText(text)
    time.sleep(1)
    text = "\n\n     Music and Special Effects:\n\n   '8-Bit Music' (Dry Times) by Gaming Waffle!\n   https://www.youtube.com/channel/UC0XkDR1cqAA0V-DbKaP8luA/about"
    typeText(text)
    text = "\n\n\t   '8 Bit Summer!' by HeatleyBros\n   https://youtu.be/TiE9Vvmlxew"
    typeText(text)
    text = "\n\n\t   'Amber Forest' by Tad on\n   https://www.youtube.com/channel/UCdGkcznHDqE1BcgTDVJ5aWQ"
    typeText(text)
    text = "\n\n\t   'Boss Fight' by Sibsonic\n   https://www.youtube.com/channel/UCfzvR7945wuSdLAGzKkmZ8w"
    typeText(text)
    text = "\n\n\t   'The Final Battle' by RedStone128\n   https://www.youtube.com/channel/UC8A1oMG8Fga-xKNwOmmQV6Q"
    typeText(text)
    text = "\n\n\t   'Itty Bitty' by Kevin MacLeod\n   https://www.youtube.com/c/kmmusic"
    typeText(text)
    text = "\n\n\t   'Monplaisir' (originally 'Soundtrack') by Monplaisir\n   https://www.youtube.com/user/M0nplaisir"
    typeText(text)
    text = "\n\n\t   'Mountain Trials' by Joshua McLelan\n   mrjoshuamclean.com"
    typeText(text)
    text = "\n\n\t   'Operatic 3' by Vibe Mountain\n   https://vibemountain.com/"
    typeText(text)
    text = "\n\n\t   'Peractorum' by Tad on\n   https://www.youtube.com/channel/UCdGkcznHDqE1BcgTDVJ5aWQ"
    typeText(text)
    text = "\n\n\t   'Underclocked' by Erik Skiff\n   http://ericskiff.com/music/"
    typeText(text)
    text = "\n\n\t   'Scream Of Dying Man Sound Effect HD' (You Die) by CoolSoundFX\n   https://www.youtube.com/channel/UC5c-X5yZaecNv9sr83NWcqA"
    typeText(text)
    time.sleep(1)
    text = "\n\n\t   Software Engineer:\n             Anthony Braden"
    typeText(text)
    time.sleep(1)
    text = "\n\n\t   Sound Engineering:\n   Music and sound effects were edited using mp3cut.net"
    typeText(text)
    time.sleep(1)
    text = "\n\n\t   Playtesters:\n\t  Kitana Mayzik\n\n"
    typeText(text)
    time.sleep(1)
    print("   Want to learn more about how technology can transform education?\n   Visit https://www.controlaltachieve.com/")
    
def runMain():
    CLICKETYCLACKGAMES()
    printIntro()
    chooseContinue()
    printIntro2()
    chooseContinue()
    printIntro3()
    startAdventure()
    
if __name__ == '__main__':    
    runMain()