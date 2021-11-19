from cloud import cloud_fighting
from cloud import cloud_stats
from aerith import aerith_fighting
from aerith import aerith_stats
from easymonster import e_monster_stats
from tqdm import tqdm



def main_menu():
    print("🗡  WELCOME TO TEXT FF7 🗡")
    choices = choice_val()

    if choices == "1":
        print("Wise choice...Alright Everybody, Let's Mosey!")
        for i in tqdm (range (100), desc="Loading..."):
            pass
        encounter()

    elif choices == "2":
        print("I just want to do everything in my power to help.")
        for i in tqdm (range (100), desc="Loading..."):
            pass
        encounter_2()

    elif choices == "3":
        exit()
    else:
        print("fatal error: something went really wrong lol.")
        exit()

def choice_val():
    while True:
        choices = input("""Who would you like to start as?
    1. Cloud
    2. Aerith
    3. Exit
    : """)
        if choices == "1" or choices == "2" or choices == "3":
            return choices
        else:
            print("Invalid input. Please try again!")


def encounter():
# display flavor text (doesnt need to be hard code)
     while e_monster_stats["HP"] > 0:
        print("Survival can be a matter of luck or skill. And you can't rely on luck. Aerith, let's hit it where it hurts!")
        cloud_menu = input("""What will it be?
        1. Attack
        2. Heal
        3. Limit
        4. Swap Character
        : """)
        # swap character
# and wait for user input
#based on the user input, 
        if cloud_menu == "1":
             e_monster_stats["HP"] -= 50
             cloud_stats["MP"] += 20
             print(f"Monster Stats: {e_monster_stats}")
             print("Monster hit for 50!")
        #give user feedback on status
        elif cloud_menu == "2":
            cloud_stats["HP"] += 100
            print(f" Cloud Stats: {cloud_stats}")
            print("Healed for 100!")
        elif cloud_menu == "3" and cloud_stats["MP"] > 50:
                e_monster_stats["HP"] -= 10000
                print("Go beyond the limits... Limit Break")
                print("YOU WON!!! GAME OVER! THANKS FOR PLAYING")
                exit()
        elif cloud_menu == "4":
            encounter_2()
            # print("idk how to fix this yet")
            # e_monster_stats["HP"]
        else:
            print("you cant do that.. yet. try again 🗿🗿🗿")
        choices = input("""What will it be?
        1. Attack
        2. Heal
        3. Limit!
        4. Swap Character
        : """)

        if cloud_stats["HP"] == 0 or e_monster_stats["HP"] == 0:
            print("GAME OVER. THANKS FOR PLAYING!!!")
            break
        print("move blocked! the enemy has attacked! You've been hit for 15!")
        cloud_stats["HP"] -= 15
        print(f"Cloud Stats: {cloud_stats}")



def encounter_2():

    while e_monster_stats["HP"] > 0:
        print("Hey, you asked for it.. Cloud, let's get 'em!")
        aerith_menu = input("""What will it be?
    1. Attack
    2. Heal
    3. Limit
    4. Swap Character
    : """)
    # swap character
# and wait for user input
#based on the user input, 
        if aerith_menu == "1":
            e_monster_stats["HP"] -= 35
            aerith_stats["MP"] += 20
            print(f"Monster Stats: {e_monster_stats}")
            print("Monster hit for 40!")
    #give user feedback on status
        elif aerith_menu == "2":
            aerith_stats["HP"] += 100
            print(f"Aerith Stats: {aerith_stats}")
            print("Healed for 100!")

        elif aerith_menu == "3" and aerith_stats["MP"] > 40:
                e_monster_stats["HP"] -= 10000
                print("Lend me your strength!")
                print("YOU WON!!! GAME OVER! THANKS FOR PLAYING")
                exit()

        elif aerith_menu == "4":
            encounter()
        # print("idk how to fix this yet")
        # e_monster_stats["HP"]
        else:
            print("you cant do that.. yet. try again 🗿🗿🗿")
        choices = input("""What will it be?
        1. Attack
        2. Heal
        3. Limit!
        4. Swap characters
        : """)

        if aerith_stats["HP"] == 0 or e_monster_stats["HP"] == 0:
            print("GAME OVER. THANKS FOR PLAYING!!!")
            break
        print("move blocked! the enemy has attacked! You've been hit for 15!")
        cloud_stats["HP"] -= 15
        print(f"Aerith Stats: {aerith_stats}")
        
    
main_menu()
