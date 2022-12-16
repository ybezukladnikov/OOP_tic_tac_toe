from player import Player
from view.view import View


printer = View()
first_player = Player(printer.get_name('first'))
second_player = Player(printer.get_name('second'))


printer.print(first_player.name)
printer.print(second_player.name)




