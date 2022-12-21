from view.Abstract_Input import Abstract_Input


class Input(Abstract_Input):

    def get_name(self, order):
        return input(f"Input name {order} player => ")

    def get_step(self, name):
        return input(f"{name} enter the cell number => ")



