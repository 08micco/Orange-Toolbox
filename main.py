from code_gen import code_gen
import jigger
import lando


def main():
    correct_info = False
    chosen_mode_str = input(
        "Choose mode:\n1| Generate Coupon Codes\n2| Address Jigger\n3| Zalando Autocheckout\n"
    )
    chosen_mode = int(chosen_mode_str)

    # Code Gen
    if chosen_mode == 1:
        while correct_info == False:
            amount = input("\nHow many codes do you want? ")
            delay = input("\nWhat delay would you like to use? ")

            print(f"Amount of codes: {amount}\nDelay used: {delay}\n")

            info_input = input("Is this the correct info? y/n: \n")

            if info_input == "y":
                if int(amount) >= 0 or int(delay) >= 0:
                    correct_info = True
                    if amount != "1":
                        print(f"\nGenerating {amount} codes with a delay of {delay}.\n")
                    else:
                        print(f"\nGenerating {amount} code with a delay of {delay}.\n")
                    for x in range(1, int(amount) + 1):
                        code_gen.gen(int(x), int(delay))
            else:
                correct_info = False

    # Jigger
    elif chosen_mode == 2:
        print("\nJigger Chosen")
        jigger.main("3", "Road", "Road Num", 25)

    # Zalando ACO
    elif chosen_mode == 3:
        mode = input("\nChoose mode:\n1 Preload Drop\n2 ACO\n")

        if mode == "1":
            lando.main("1")
        elif mode == "2":
            lando.main("2")


if __name__ == "__main__":
    main()
