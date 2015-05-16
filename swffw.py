import pdb
commands = "F2L1F1R1F3R1F3L1F5R1F1L1F2"

running = ""
cmdList = []
commands=commands
for k, i in enumerate(commands):
    if (k%2==0 and k != 0):
        print running[0], running[1]
        if (running[0] == "F" or running[0] == "B"):
            for i in range(0, int(running[1])):
                cmdList.append(str(running[0])+"1")
        else:
            cmdList.append(running)
        running = ""
    running += commands[k]
cmdList.append(running)
print cmdList
