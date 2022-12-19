import string


class Output:
    def print(self, data_base):
        print("  ===========")
        print(" | " , end='')
        for enum, item in enumerate(data_base.values()):
            if enum < 3:
                print(item, end=" | ")
                if enum==2:
                    print()
                    print("  -----------")
                    print(" | ", end='')

            elif 2 < enum < 6:
                print(item, end=" | ")
                if enum==5:
                    print()
                    print("  -----------")
                    print(" | ", end='')

            elif 5 < enum < 9:
                print(item, end=" | ")
                if enum==8:
                    print()

        print("  ===========")