from cloud import cloud_fighting
from aerith import aerith_fighting


def main_menu():
    print("🗡  WELCOME TO TEXT FF7 🗡")
    choices = input("""Who would you like to start as?
    1. Cloud
    2. Aerith
    3. Exit
    : """)
    if choices == "1":
        print("Wise choice...Alright Everybody, Let's Mosey!")
        print("🔺.....loading.....🔺")
        print("  🔺..loading...🔺")
        print("🔺.....loading.....🔺")
        print("  🔺..loading..🔺")
        print("🔺.....loading.....🔺")
        print("  🔺..loading..🔺")
        cloud_fighting()
    elif choices == "2":
        print("I just want to do everything in my power to help.")
        print("🔺.....loading.....🔺")
        print("🔺.....loading.....🔺")
        print("🔺.....loading.....🔺")
        print("🔺.....loading.....🔺")
        print("🔺.....loading.....🔺")
        print("🔺.....loading.....🔺")
        aerith_fighting()
    elif choices == "3":
        exit()
    else:
        print("ERROR: try again 🗿🗿🗿")
        choices = input("""Who would you like to start as?
    1. Cloud
    2. Aerith
    3. Exit
    : """)




main_menu()
