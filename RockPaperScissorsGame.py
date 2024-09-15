from enum import Enum
import sys
import random


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("")
playerschoice = input(
    "Enter.....\n1 for rock\n2 for Paper, or\n3 for scissors:\n\n")

player = int(playerschoice)
if player < 1 or player > 3:
    sys.exit("You must Enter 1,2 or 3.")

computerchoice = random.choice("123")
computer = int(computerchoice)

print("")
print("You Choose " + str(RPS(player)).replace('RPS.', '') + ".")
print("Python Choose " + str(RPS(computer)).replace('RPS.', '') + ".")
print("")

if player == 1 and computer == 3:
    print("🥳You Win!")
elif player == 2 and computer == 1:
    print("🥳You Win!")
elif player == 3 and computer == 2:
    print("🥳You Win!")
elif player == computer:
    print("😲Tie Game!")
else:
    print("🐍Python Wins!")
