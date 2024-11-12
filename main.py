import sys
from manage.cache import delete_pycaches
from games.pok.game import main as pok_main

def display_menu():
    print("\n===== Game Menu =====")
    print("1. Pok")
    print("2. Siku")
    print("3. Ongdu")
    print("4. Exit")
    print("=====================")

def main():
    while True:
        display_menu()
        choice = input("\nSelect a game (1-4): ")
        
        if choice == "1":
            print("\nStarting Pok...\n")
            pok_main()
        elif choice == "2":
            print("\nSiku is not yet available.")
        elif choice == "3":
            print("\nOngdu is not yet available.")
        elif choice == "4":
            print("\nThanks for playing!")
            delete_pycaches()
            sys.exit()
        else:
            print("\nInvalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
