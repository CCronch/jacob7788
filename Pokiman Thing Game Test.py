import sys
from random import seed
from random import randint
from random import random
import time

seedNum = random()
print(seedNum)
seed(seedNum)


def randomnum(rangenum, firstnum, lastnum):
    for _ in range(rangenum):
        value = randint(firstnum, lastnum)
        return value


def rewitem():
    item_give = randomnum(1, 1, 100)
    if 1 <= item_give <= 40:
        print("\nYou got a Red Stone!")
        time.sleep(2)
        tr = input("Use Red Stone or throw Red Stone? (U or T)")
        if tr == "U":
            time.sleep(1)
            print("\nYou used Red Stone on " + starter[0] + "\n")
            print(starter[0] + "'s Stats:")
            print("ATK: " + repr(starter[1]) + " -->" + repr(starter[1] + 35))
            starter[1] = starter[1] + 35
            print("HP: " + repr(starter[2]) + " of " + repr(starter[4]))
            print("BLK: " + repr(starter[3]))
        else:
            time.sleep(1)
            print("Ouch!")
            starter[2] = starter[2] - 15
            time.sleep(3)
            if starter[2] <= 0:
                print("\n\n\n\n\n\n\n\n\n\n\n" + starter[0] + " fainted...")
    elif 41 <= item_give <= 65:
        print("\nYou got a Green Stone!")
        time.sleep(2)
        tr = input("Use Green Stone or throw Green Stone? (U or T)")
        if tr == "U":
            time.sleep(1)
            print("\nYou used Green Stone on " + starter[0] + "\n")
            print(starter[0] + "'s Stats:")
            print("ATK: " + repr(starter[1]))
            print("HP: " + repr(starter[2]) + " of " + repr(starter[4]) + " -->" + repr(starter[4] + 35))
            starter[4] = starter[4] + 35
            starter[2] = starter[2] + 35
            print("BLK: " + repr(starter[3]))
        else:
            time.sleep(1)
            print("Ouch!")
            starter[2] = starter[2] - 15
            time.sleep(3)
            if starter[2] <= 0:
                print("\n\n\n\n\n\n\n\n\n\n\n" + starter[0] + " fainted...")
    elif 66 <= item_give <= 90:
        print("\nYou got a Yellow Stone!")
        time.sleep(2)
        tr = input("Use Yellow Stone or throw Yellow Stone? (U or T)")
        if tr == "U":
            if starter[3] >= 170:
                print("Nothing happened... \n")
            else:
                time.sleep(1)
                print("\nYou used Yellow Stone on " + starter[0] + "\n")
                print(starter[0] + "'s Stats:")
                print("ATK: " + repr(starter[1]))
                print("HP: " + repr(starter[2]) + " of " + repr(starter[4]))
                print("BLK: " + repr(starter[3]) + " -->" + repr(starter[3] + 20))
                starter[3] = starter[3] + 20
        else:
            time.sleep(1)
            print("Ouch!")
            starter[2] = starter[2] - 15
            time.sleep(3)
            if starter[2] <= 0:
                print("\n\n\n\n\n\n\n\n\n\n\n" + starter[0] + " fainted...")
    elif 91 <= item_give <= 95:
        print("\nYou got a Rainbow Stone!")
        time.sleep(2)
        tr = input("Use Rainbow Stone or throw Rainbow Stone? (U or T)")
        if tr == "U":
            time.sleep(1)
            print("\nYou used Rainbow Stone on " + starter[0] + "\n")
            starter[2] = starter[4]
            print(starter[0] + "'s Stats:")
            print("ATK: " + repr(starter[1]) + " -->" + repr(starter[1] + 15))
            starter[1] = starter[1] + 15
            print("HP: " + repr(starter[2]) + " of " + repr(starter[4]) + " -->" + repr(starter[4] + 15))
            starter[4] = starter[4] + 15
            starter[2] = starter[4]
            if starter[3] >= 170:
                print("BLK: " + repr(starter[3]) + "MAX")
            else:
                print("BLK: " + repr(starter[3]) + " -->" + repr(starter[3] + 15))
                starter[3] = starter[3] + 15
        else:
            time.sleep(1)
            print("Oh!")
            starter[2] = starter[2] + 50
            time.sleep(3)
    elif 96 <= item_give <= 100:
        print("\nYou got a Stone!")
        time.sleep(2)
        tr = input("Use Stone or throw Stone? (U or T)")
        if tr == "U":
            time.sleep(1)
            print("\nYou used Stone on " + starter[0] + "\n")
            print("Why?\n")
            print(starter[0] + "'s Stats:")
            print("ATK: " + repr(starter[1]))
            print("HP: " + repr(starter[2]) + " of " + repr(starter[4]))
            print("BLK: " + repr(starter[3]))
        else:
            time.sleep(1)
            print("Ouch!")
            starter[2] = starter[2] - 30
            time.sleep(3)
            if starter[2] <= 0:
                print("\n\n\n\n\n\n\n\n\n\n\n" + starter[0] + " fainted...")


print("\nHello young Pokiman trainer my name is Prof. Sap, I am going to start your Pokiman journey.")

name = input("\nFirst off what is your name?")
bready = 0

print("\nHello " + name + "! Welcome to Little Trunk your new home town.")

time.sleep(3)

starternum = randomnum(1, 1, 3)

if starternum == 1:
    starter = ["Sunbeamtiger", randomnum(1, 50, 100), randomnum(1, 175, 225), randomnum(1, 25, 75)]
elif starternum == 2:
    starter = ["Sunlightcorpion", randomnum(1, 75, 125), randomnum(1, 125, 175), randomnum(1, 50, 100)]
else:
    starter = ["LilPup", randomnum(1, 50, 75), randomnum(1, 150, 200), randomnum(1, 75, 125)]
# add print(starter) here to see stats
starter.append(starter[2])

print("\nFor your first Pokiman I have chosen " + starter[0] + "!" + "\nHe shall serve you well\n")

time.sleep(3)

print(starter[0] + "'s Stats:")
print("ATK: " + repr(starter[1]))
print("HP: " + repr(starter[2]))
print("BLK: " + repr(starter[3]))

opPokinum = randomnum(1, 1, 3)

if opPokinum == 1:
    opPoki = ["Moonlighttiger", randomnum(1, 50, 100), randomnum(1, 175, 225), randomnum(1, 25, 75)]
elif opPokinum == 2:
    opPoki = ["Darkcorpion", randomnum(1, 75, 125), randomnum(1, 125, 175), randomnum(1, 50, 100)]
else:
    opPoki = ["LilKit", randomnum(1, 50, 75), randomnum(1, 150, 200), randomnum(1, 75, 125)]
# add print(opPoki) here to see stats
opPoki.append(opPoki[2])

print("Here have this.\n")
rewitem()

print("\nMy grandchild Dave wants to fight you with his Pokiman " + opPoki[0] + ", Good luck!")
time.sleep(1)
fightB = input("\nDo you accept my grandchild's request? (Y or N)")

if fightB == "Y":
    print("\nGood luck!\n")
else:
    print("\nThat's not very cash money of you.\n")

time.sleep(2)

print("3\n")
time.sleep(1)
print("2\n")
time.sleep(1)
print("1\n")
time.sleep(1)
print("Fight\n\n\n\n\n\n\n\n\n")

global econfused
econfused = 0
global pconfused
pconfused = 0


def playerfight():
    global pconfused
    global econfused
    if pconfused < 1:
        option = input("Attack(1) Confuse(2) Heal(3)\n")
        if option == "1":
            print("\n" + starter[0] + " Attacked " + opPoki[0] + "\n")
            time.sleep(2)
            crit = randomnum(1, 1, 20)
            if crit == 1:
                print(starter[0] + " did a critical hit and dealt")
                pdam = randomnum(1, 60, 90) / 100
                print(round(starter[1] * pdam))
                print("damage!\n")
                opPoki[2] -= starter[1] * pdam
                time.sleep(2)
                if opPoki[2] <= 0:
                    print(opPoki[0] + " has fainted\n")
                    time.sleep(3)
                else:
                    print(opPoki[0] + " has")
                    print(round(opPoki[2]))
                    print("out of")
                    print(opPoki[4])
                    print("HP left \n\n\n")
                    opfight()
            else:
                print(starter[0] + " did")
                pdam = randomnum(1, 30, 60) / 100
                print(round(starter[1] * pdam))
                print("damage!\n")
                opPoki[2] -= starter[1] * pdam
                time.sleep(2)
                if opPoki[2] <= 0:
                    print(opPoki[0] + " has fainted\n")
                else:
                    print(opPoki[0] + " has")
                    print(round(opPoki[2]))
                    print("out of")
                    print(opPoki[4])
                    print("HP left \n\n\n")
                    opfight()
        elif option == "2":
            print(starter[0] + " is trying to confuse " + opPoki[0] + "\n")
            time.sleep(2)
            bchance = randomnum(1, 1, 200)
            if 0 <= bchance <= starter[3]:
                print(starter[0] + " confused " + opPoki[0] + "\n")
                econfused = randomnum(1, 1, 3)
                opfight()
            else:
                print(starter[0] + " failed to confuse " + opPoki[0] + "\n")
                opfight()
        elif option == "3":
            if starter[2] < starter[4]:
                healnum = randomnum(1, 20, 35) / 100
                heal = starter[1] * healnum
                print(starter[0] + " healed himself by " + repr(heal) + " HP\n")
                starter[2] += heal
                print("ATK: " + repr(starter[1]))
                print("HP: " + repr(round(starter[2])) + " of " + repr(starter[4]))
                print("BLK: " + repr(starter[3]))
                opfight()
            else:
                print("\n" + starter[0] + "is already healthy.\n")
                playerfight()
        else:
            print("That's not an option silly!" + "\n\n\n\n")
            playerfight()
    elif pconfused >= 1:
        print(starter[0] + " is confused\n")
        pconfused = - 1
        opfight()


def opfight():
    time.sleep(2)
    opoption = randomnum(1, 1, 100)
    float(opoption)
    global econfused
    global pconfused
    if econfused < 1:
        if 1 <= opoption <= 69:
            print("\n" + opPoki[0] + " Attacked " + starter[0] + "\n")
            time.sleep(2)
            crit = randomnum(1, 1, 20)
            if crit == 1:
                print(opPoki[0] + " did a critical hit and dealt")
                pdam = randomnum(1, 60, 90) / 100
                print(round(opPoki[1] * pdam))
                print("damage!\n")
                starter[2] -= opPoki[1] * pdam
                time.sleep(2)
                if starter[2] <= 0:
                    print(starter[0] + " has fainted\n")
                    time.sleep(3)
                else:
                    print(starter[0] + " has")
                    print(round(starter[2]))
                    print("out of")
                    print(starter[4])
                    print("HP left \n\n\n")
                    playerfight()
            else:
                print(opPoki[0] + " did")
                pdam = randomnum(1, 30, 60) / 100
                print(round(opPoki[1] * pdam))
                print("damage!\n")
                starter[2] -= opPoki[1] * pdam
                time.sleep(2)
                if starter[2] <= 0:
                    print(starter[0] + " has fainted\n")
                    time.sleep(3)
                else:
                    print(starter[0] + " has")
                    print(round(starter[2]))
                    print("out of")
                    print(starter[4])
                    print("HP left \n\n\n")
                    playerfight()
        elif 70 <= opoption <= 98:
            print(opPoki[0] + " is ready to confuse " + starter[0] + "\n")
            time.sleep(2)
            bchance = randomnum(1, 1, 200)
            if 0 <= bchance <= opPoki[3]:
                print(opPoki[0] + " confused " + starter[0] + "\n")
                pconfused = randomnum(1, 1, 3)
                playerfight()
            else:
                print(opPoki[0] + " failed to confuse " + starter[0] + "\n")
                playerfight()
        else:
            print(opPoki[0] + " stood still..." + "\n")
            playerfight()
    elif econfused >= 1:
        print(opPoki[0] + " is confused\n")
        econfused = econfused - 1
        playerfight()


playerfight()

if starter[2] >= 1:
    time.sleep(2)
    print('\n\n\n\n\n\n\n\nWow that\'s surprising here I\'ll heal your Pokiman and take this.')
    starter[2] = starter[4]
    rewitem()
    opPoki.clear()
    opPokinum = randomnum(1, 1, 4)
    if opPokinum == 1:
        opPoki = ["Goldenpike", randomnum(1, 70, 120), randomnum(1, 185, 220), randomnum(1, 70, 125)]
    elif opPokinum == 2:
        opPoki = ["Stageleft", randomnum(1, 90, 140), randomnum(1, 100, 140), randomnum(1, 50, 100)]
    elif opPokinum == 3:
        opPoki = ["Brokiman", randomnum(1, 90, 95), randomnum(1, 145, 150), randomnum(1, 100, 150)]
    else:
        opPoki = ["Stageright", randomnum(1, 30, 55), randomnum(1, 240, 285), randomnum(1, 50, 100)]
    # add print(opPoki) here to see stats
    opPoki.append(opPoki[2])
    print("\nNow it it time to face the wraith of my other grandson John with his " + opPoki[0] + "!\n")
    time.sleep(2)
    print("3\n")
    time.sleep(1)
    print("2\n")
    time.sleep(1)
    print("1\n")
    time.sleep(1)
    print("Fight\n\n\n\n\n\n\n\n\n")
    playerfight()
    rewitem()

if starter[2] >= 1:
    time.sleep(2)
    print('\n\n\n\n\n\n\n\nOh you did it again...')
    time.sleep(1)
    print("Well, here I'll heal your Pokiman.")
    time.sleep(3)
    print("I bet you can't beat the top Pokiman trainer in my class, Jared!")
    time.sleep(1)
    starter[2] = starter[4]
    opPoki.clear()
    opPokinum = randomnum(1, 1, 5)
    if opPokinum == 1:
        opPoki = ["Lapiscat", randomnum(1, 70, 90), randomnum(1, 190, 210), randomnum(1, 150, 170)]
    elif opPokinum == 2:
        opPoki = ["Friemon", randomnum(1, 100, 120), randomnum(1, 125, 175), randomnum(1, 50, 100)]
    elif opPokinum == 3:
        opPoki = ["Scarymonster", randomnum(1, 150, 175), randomnum(1, 75, 100), randomnum(1, 10, 40)]
    elif opPokinum == 4:
        opPoki = ["Cloakedkend", randomnum(1, 100, 100), randomnum(1, 200, 200), randomnum(1, 50, 50)]
    else:
        opPoki = ["Metalion", randomnum(1, 45, 55), randomnum(1, 270, 310), randomnum(1, 10, 40)]
    # add print(opPoki) here to see stats
    opPoki.append(opPoki[2])
    print("He has over 100 wins with his " + opPoki[0] + "!")
    print("Good luck, you'll need it!\n")
    time.sleep(2)
    print("3\n")
    time.sleep(1)
    print("2\n")
    time.sleep(1)
    print("1\n")
    time.sleep(1)
    print("Fight\n\n\n\n\n\n\n\n\n")
    playerfight()
    rewitem()
    rewitem()

if starter[2] >= 1:
    time.sleep(2)
    print('\n\n\n\n\n\n\n\nHow! You are a child but you swept the floor with Jared')
    time.sleep(1)
    print("Well here, I'll heal your Pokiman.")
    time.sleep(3)
    print("If you are that good I want to fight you.")
    time.sleep(1)
    starter[2] = starter[4]
    opPoki.clear()
    opPoki = ["BigLilKit", randomnum(1, 170, 190), randomnum(1, 280, 300), randomnum(1, 130, 150)]
    # add print(opPoki) here to see stats
    opPoki.append(opPoki[2])
    print("I will use my genetically modified " + opPoki[0] + "!")
    print("No good luck this time.\n")
    time.sleep(2)
    print("3\n")
    time.sleep(1)
    print("2\n")
    time.sleep(1)
    print("1\n")
    time.sleep(1)
    print("Fight\n\n\n\n\n\n\n\n\n")
    playerfight()
    rewitem()
    rewitem()
    rewitem()

if starter[2] > 1:
    time.sleep(2)
    print('\n\n\n\n\n\n\n\nHow is this possible? I have been training Pokimans for over 40 years')
    time.sleep(1)
    print("Well here, I'll heal your Pokiman.")
    time.sleep(3)
    print("I must summon one of the Pokiman gods to judge you and your " + starter[0] + ".\n")
    time.sleep(1)
    starter[2] = starter[4]
    opPoki.clear()
    opPokinum = randomnum(1, 1, 3)
    if opPokinum == 1:
        opPoki = ["GodKit", randomnum(1, 130, 130), randomnum(1, 250, 250), randomnum(1, 199, 199)]
    elif opPokinum == 2:
        opPoki = ["GodStage", randomnum(1, 130, 130), randomnum(1, 400, 400), randomnum(1, 100, 100)]
    else:
        opPoki = ["GodCorpion", randomnum(1, 225, 225), randomnum(1, 250, 250), randomnum(1, 100, 100)]
    # add print(opPoki) here to see stats
    opPoki.append(opPoki[2])
    print("*" + opPoki[0] + " is summoned*")
    print("Now fight him and he will decide your fate.\n")
    time.sleep(2)
    print("3\n")
    time.sleep(1)
    print("2\n")
    time.sleep(1)
    print("1\n")
    time.sleep(1)
    print("Go\n\n\n\n\n\n\n\n\n")
    playerfight()

time.sleep(3)
print("Wow you made" + opPoki[0] + "faint.")
time.sleep(2)
print("Congrats I think you win.")
time.sleep(2)
print("I will now test your abilities in the endless Pokiman Trainer Simulation Director, Aka PTSD.")
print("A whole hearted good luck from me.")

levelnum = 1
loopnum = 1
while starter[2] > 1:
    print("\n\n\n\n\nLevel: " + repr(levelnum))
    rewitem()
    rewitem()
    loopnum += 0.1
    Names = ["Yeasus", "Magimap", "Likerhoe", "Jixen", "Flixen", "loped", "toddles", "quacker", "kakely", "zebrahorn",
             "captianmunch", "captiancrunch", "Gampo", "Topuga", "pepagerus", "retary", "yotop", "botalnek",
             "sunstridar", "YesNoMabye", "Jifgy", "Kigfy", "ligmaBalls", "Joe", "mumma", "Alaric", "Hyeplume",
             "Scorpisaur", "Hippopeat", "Dinosow", "Steelwhale", "Stunhopper", "Aquatacle", "Gothuito", "Charachnid",
             "Goath", "Scorpipod", "Elecoon", "Lobstuna", "Salamaid", "Skeleling", "Charpie", "Chilloda", "Bellecta",
             "Yetiger", "Turtoro", "Crocodily", "Koatle", "Bisius", "Flamama", "Elecraffe", "Whirlray", "Sandopotamus",
             "Kinetacuda", "Magmeleon", "Dolphire", "Coyoloon", "Chimpalix", "Rhinithe", "Panthora", "Quickkey",
             "Blastpion", "Dewander", "Earthypus", "Viperil", "Caesardine", "Alligacross", "Swactric", "Barracoke",
             "Chimpath", "Voltraffe", "Charroach", "Wintorb", "Whirlilla", "Quaileaf", "Yetiger", "Crodos", "Falconyte",
             "Termyle", "Hippopuzz", "Chimepion", "Fiepie", "Elecoceros", "Charatee", "Boaris", "Bumble", "Beetle",
             "Kangalow", "Salamasion", "Pengola", "Turtia", "Doombat", "Gromeleon", "Silvering", "Slowadger",
             "Lemonster", "Raccocoon", "Scorpipip", "Alligaphy", "Pandord", "Salamevoir", "Gladiaroach", "Ashbat",
             "Slowing", "Specodo", "Falcondor", "Twilightingale", "Flamiplume", "Toadrill", "Vulturitar", "Pandora",
             "Quiroach", "Magiraffe", "Steelosaur", "Skelalo", "Camouse", "Camoose", "Wolvecoon", "Allibyss",
             "Pelicyss", "Salamyss", "Quickray", "Elecpecker", "Carnelope", "Fluffaby", "Antethereal", "Troutlaw",
             "Kangaslash", "Catefree", "Dinosita", "Parrory", "Crazehawk", "Crazeroach", "Earthapi", "Gotharos",
             "Vanillama", "Fearkat", "Kangamite", "Albalite", "Donkops", "Crocodaring", "Venohopper", "Fierkey",
             "Mountela", "Oddabura", "Pandarkness", "Raccoconut", "Alliron", "Jaguabyss", "Caterpion", "Pelicoss",
             "Spizelle", "Fiewhale", "Magicossum", "Starypus", "Squidle", "Termitis", "Barracross", "Wolvebyss",
             "Flamita", "Alligyss", "Quilpecker", "Crazemite", "Quickey", "Steelida", "Vaporc", "Dinoscythe", "Koatric",
             "Antezel", "Kangaraid", "Cobroom", "Flubat", "Ashron", "Shelida", "Magmaby", "Autoad", "Clovertex",
             "Hyecoon", "Flamire", "Turtepi", "Parrena", "Quiray", "Venobug", "Terrigator", "Glasilla", "Thortoise",
             "Rhinova"]
    ename = Names[randomnum(1, 1, 187)]
    opPoki = [ename, randomnum(1, 100, 150) * loopnum, randomnum(1, 200, 300) * loopnum,
              randomnum(1, 50, 150) * loopnum]
    opPoki.append(opPoki[2])
    print("A Simulated " + opPoki[0] + " appeared\n\n")
    time.sleep(2)
    print("3\n")
    time.sleep(1)
    print("2\n")
    time.sleep(1)
    print("1\n")
    time.sleep(1)
    print("Fight\n\n\n\n\n\n\n\n\n")
    playerfight()
    print("Congrats")
    levelnum += 1

if starter[2] <= 1:
    time.sleep(3)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n               You Lose :(\n\n\n\n\n\n\n")
    time.sleep(10)
sys.exit()
