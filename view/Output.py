from colorama import Fore, Back, Style, init
init(autoreset=True)


class Output:
    def print(self, data_base):
        print(Fore.GREEN +"  ===========")
        print(" | " , end='')
        for enum, item in enumerate(data_base.values()):
            if enum < 3:
                if item == 'X':
                    print(Fore.BLUE + item, end=" | ")
                elif item == 'O':
                    print(Fore.RED + item, end=" | ")
                else:
                    print(item, end=" | ")
                if enum==2:
                    print()
                    print("  -----------")
                    print(" | ", end='')

            elif 2 < enum < 6:
                if item == 'X':
                    print(Fore.BLUE + item, end=" | ")
                elif item == 'O':
                    print(Fore.RED + item, end=" | ")
                else:
                    print(item, end=" | ")
                if enum==5:
                    print()
                    print("  -----------")
                    print(" | ", end='')

            elif 5 < enum < 9:
                if item == 'X':
                    print(Fore.BLUE + item, end=" | ")
                elif item == 'O':
                    print(Fore.RED + item, end=" | ")
                else:
                    print(item, end=" | ")
                if enum==8:
                    print()

        print(Fore.GREEN +"  ===========")

    def print_name(self, name_player):
        print(name_player)

    def print_name_win(self,name_player):
        print(f"Congratulate! {name_player} win.")

    def print_draw(self):
        print("Draw.")