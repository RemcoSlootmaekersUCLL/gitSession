import time

def calculate_tablet_area_based_on_ingame_sens(sens, display_ratio, tablet_width):
    tablet_height = tablet_width / display_ratio
    
    area_width = tablet_width / sens
    area_height = tablet_height / sens

    return f"Area width: {area_width:.3f}\nArea height: {area_height:.3f}"


def main():
    run = True
    while run:
        print("1. Calculate area based on osu! sensitivity and screen ratio.")
        print("0. Quit")
        choice = input("Enter the number of the option you want.\n")

        match choice:
            case "0":
                print("~ Quitting script, Bye :) ~")
                run = False
                time.sleep(2)

            case "1":        
                ingame_sens = float(input("What is your in-game osu! sensitivity?\n"))
                display_width = int(input("Enter your display (monitor) width (in px).\n"))
                display_height = int(input("Enter your display (monitor) height (in px).\n"))
                tablet_width = int(input("Enter your tablet width (in mm).\n"))

                tablet_area = calculate_tablet_area_based_on_ingame_sens(ingame_sens, display_width / display_height, tablet_width)
                print(tablet_area)
                print("-" * 30)
                time.sleep(4)

            case _:
                print("Not a valid choice.")
                time.sleep(1)

if __name__ == "__main__":
    main()