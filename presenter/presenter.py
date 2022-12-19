from model.player import Player
from view.view import View
from view.Output import Output
from model.Data_Base import Data_Base


class Presenter:
    dictionary = Data_Base()

    my_output = Output()

    def start(self):
        my_dict = self.dictionary.dictionary
        # my_dict['01'] = 99
        self.my_output.print(my_dict)
