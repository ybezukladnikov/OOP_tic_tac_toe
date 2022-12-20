from model.Check import Check
from model.Player import Player
from view.Input import Input
from view.Output import Output
from model.Data_Base import Data_Base


class Presenter:

    dictionary = Data_Base()
    my_output = Output()
    my_input = Input()
    my_check = Check()


    dictionary.set_dict({'1': '1', '2': '2', '3': '3',
                        '4': '4', '5': '5', '6': '6',
                        '7': '7', '8': '8', '9': '9'})



    def start(self):
        player1 = Player(self.my_input.get_name('first'))
        player2 = Player(self.my_input.get_name('second'))
        my_dict = self.dictionary.get_dict()

        while True:
            self.my_output.print(my_dict)
            step_first_pl = self.my_input.get_step(player1.name)
            player1.make_step(my_dict, step_first_pl, 'X')
            if self.my_check.check_win(my_dict):
                self.my_output.print_name_win(player1.name)
                self.my_output.print(my_dict)
                break
            elif self.my_check.check_draw(my_dict):
                self.my_output.print_draw()
                self.my_output.print(my_dict)
                break


            self.my_output.print(my_dict)
            step_second_pl = self.my_input.get_step(player2.name)
            player2.make_step(my_dict, step_second_pl, 'O')
            if self.my_check.check_win(my_dict):
                self.my_output.print_name_win(player2.name)
                self.my_output.print(my_dict)
                break
            elif self.my_check.check_draw(my_dict):
                self.my_output.print_draw()
                self.my_output.print(my_dict)
                break








