class Robot():
    #FACING:
    #right = 0
    #up = 1
    #left = 2
    #down = 3
    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.facing = facing
    def updatePos(self, x, y, facing):
        self.x = x
        self.y = y
        self.facing = facing

def returnCommandList(commands):
    running = ""
    cmdList = []
    commands=commands
    for k, i in enumerate(commands):
        if (k%2==0 and k != 0):
            if (running[0] == "F" or running[0] == "B"):
                for i in range(0, int(running[1])):
                    cmdList.append(str(running[0])+"1")
            else:
                cmdList.append(running)
            running = ""
        running += commands[k]
    if (running[0] == "F" or running[0] == "B"):
        for i in range(0, int(running[1])):
            cmdList.append(str(running[0])+"1")
    else:
        cmdList.append(running)
    return cmdList

def findThing(char, string):
    array = []
    if (string.find(char) == -1):
        return []
    for k,c in enumerate(string):
        if (c == char):
            array.append(k)
    return array

def findInitialDir(entry, dim):
    if (entry[0][1] == dim-1):
        return 1
    if (entry[0][1] == 0):
        return 3
    if (entry[0][0] == 0):
        return 0
    if (entry[0][0] == dim-1):
        return 2

def isIn(rbt, thing):
    if (thing == "W"):
        for p in walls:
            if (p[0] == rbt.x and p[1] == rbt.y):
                return True
    if (thing == "X"):
        for p in exitt:
            if (p[0] == rbt.x and p[1] == rbt.y):
                return True
    if (thing == "T"):
        for p in traps:
            if (p[0] == rbt.x and p[1] == rbt.y):
                return True
    if (thing == "P"):
        for p in pits:
            if (p[0] == rbt.x and p[1] == rbt.y):
                return True
    return False

def runCommand(cmd, rbt):
    if (cmd[0] == "F"):
        if (rbt.facing == 0):
            rbt.x += int(cmd[1])
        if (rbt.facing == 1):
            rbt.y -= int(cmd[1])
        if (rbt.facing == 2):
            rbt.x -= int(cmd[1])
        if (rbt.facing == 3):
            rbt.y += int(cmd[1])
        if (isIn(rbt, "W")):
            if (rbt.facing == 0):
                rbt.x -= int(cmd[1])
            if (rbt.facing == 1):
                rbt.y += int(cmd[1])
            if (rbt.facing == 2):
                rbt.x += int(cmd[1])
            if (rbt.facing == 3):
                rbt.y -= int(cmd[1])
            print "Ow!"
    if (cmd[0] == "B"):
        if (rbt.facing == 0):
            rbt.x -= int(cmd[1])
        if (rbt.facing == 1):
            rbt.y += int(cmd[1])
        if (rbt.facing == 2):
            rbt.x += int(cmd[1])
        if (rbt.facing == 3):
            rbt.y -= int(cmd[1])
        if (isIn(rbt, "W")):
            if (rbt.facing == 0):
                rbt.x += int(cmd[1])
            if (rbt.facing == 1):
                rbt.y -= int(cmd[1])
            if (rbt.facing == 2):
                rbt.x -= int(cmd[1])
            if (rbt.facing == 3):
                rbt.y += int(cmd[1])
            print "Ow!"
    if (cmd[0] == "L"):
            rbt.facing += int(cmd[1])
            while (rbt.facing >= 4):
                rbt.facing -= 4
    if (cmd[0] == "R"):
            rbt.facing -= int(cmd[1])
            while (rbt.facing <= -1):
                rbt.facing += 4
    return rbt

dim = int(raw_input())
maze = []

for i in range(0,dim):
    maze.append(raw_input().upper())

#maze = ["WWWWWWXWWW", "W    W W W", "W      WWW", "W        W", "WTTT     W", "W        W", "W  PWWWWWW", "W T      W", "WW       W", "WWWEWWWWWW"]
'''mazee = raw_input().upper()
running = ""
for c in mazee:
    if (c == "\n"):
        maze.append(running.lstrip("\n"))
        running = ""
    running += c
maze.append(running.lstrip("\n"))'''

pgrm = raw_input().upper()
#pgrm = "F2L1F1R1F3R1F3L1F5R1F1L1F2"

traps = []
entry = []
pits = []
exitt = []
walls = []
for y,line in enumerate(maze):
    for x,c in enumerate(line):
        if (c == "T"):
            traps.append([x, y])
        if (c == "E"):
            entry.append([x, y])
        if (c == "P"):
            pits.append([x, y])
        if (c == "X"):
            exitt.append([x, y])
        if (c == "W"):
            walls.append([x, y])

robot = Robot(entry[0][0], entry[0][1], findInitialDir(entry, dim))

pgrm = returnCommandList(pgrm)

lastx = robot.x
lasty = robot.y
skip = False
i = 0
for k in pgrm:
    try:
        #print robot.x, robot.y, robot.facing, pgrm[i]
        robot = runCommand(pgrm[i], robot)
        #print robot.x, robot.y, robot.facing
        if (isIn(robot, "X")):
            print "Aww yeah!"
            break
        if (isIn(robot, "P")):
            print "Well, I'm boned"
            break
        if (isIn(robot, "T") and (pgrm[i][0] == "F" or pgrm[i][0] == "B")):
            print "Bite my shiny metal ass!"
        
        i += 1
    except:
        pass

















