import random
from config import p, e


def roll_dice(sides=6, count=1):
    rolls = list()
    total = 0

    p("=== Dice Roll Started ===")

    p(f"Rolling {count} dice with {sides} sides.")

    for i in range(count):
        roll = random.randint(1, sides)
        total += roll
        rolls.append(roll)

        p(f"Rolled {roll} - Total: {total}")
    
    p(f"Total of rolls: {total}")
    if total == 1:
        p("You rolled a lonely 1!")
    elif total == 2:
        p("Snake Eyes! Double 1s rolled!")
    elif total == 3:
        p("Three's company! You rolled 3!")
    elif total == 6:
        p("Half a dozen! You rolled 6!")
    elif total == 7:
        p("Lucky! You rolled 7!")
    elif total == 13:
        p("Unlucky! You rolled 13!")
    elif total == 21:
        p("Blackjack! You rolled 21!")

    p("Returning results to game.")

    p("=== Dice Roll finished ===")

    return rolls, total

def roll3d6stat():
    rolls, total = roll3d6()
    if total < 8:
        total = 8
    return total
    

def roll3d6():
    return roll_dice(sides=6, count=3)

def roll2d10():
    return roll_dice(sides=10, count=2)

def rolld6(count=1):
    return roll_dice(sides=6, count=count)

def rolld4(count=1):
    return roll_dice(sides=4, count=count)



if __name__ == "__main__":
    # This was run directly
    print("Testing...")
    rolls, total = roll_dice(sides=6, count=4)
    print(f"Total: {total}\nRolls: {rolls}")
    
    rolls, total = roll3d6()
    print(f"3d6 Total: {total}\nRolls: {rolls}")




    