from accessify import private
class Data_Base:

    # def __init__(self, dictionary):
    #     self.__dictionary = dictionary

    @private
    @classmethod
    def check_value(cls, dictionary):
        return type(dictionary) is dict

    def set_dict(self, dictionary):
        if self.check_value(dictionary):
            self.__dictionary = dictionary
        else:
            raise ValueError("Wrong type")



    def get_dict(self):
        return self.__dictionary




