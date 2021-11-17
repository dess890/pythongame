cloud_stats = {
    "HP":"400",
    "LV":"5",
    "Strength":"50"
}
def cloud_fighting():
    print("Survival can be a matter of luck or skill. And you can't rely on luck. Aerith, let's hit it where it hurts!")
    cloud_menu = input("""1. Attack
    2. Heal
    3. Limit!""")
    if cloud_menu == "1":
        print("Monster hit for 40!")
    elif cloud_menu == "2":
        print("Healed for 20+ HP")
    elif cloud_menu == "3":
        print("Limit break!!")
    else:
        print("Cmon, what do you want me to do! Pick one!")
        cloud_menu = input("""1. Attack
    2. Heal
    3. Limit!""")

    #make a menu prompting fight and what the user wants to do
    #make a while loop?