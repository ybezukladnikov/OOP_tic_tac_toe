class Check:
    def check_win(self, dictionary):
        if dictionary['1'] == dictionary['2'] == dictionary['3'] or \
                dictionary['4'] == dictionary['5'] == dictionary['6'] or \
                dictionary['7'] == dictionary['8'] == dictionary['9'] or \
                dictionary['1'] == dictionary['4'] == dictionary['7'] or \
                dictionary['2'] == dictionary['5'] == dictionary['8'] or \
                dictionary['3'] == dictionary['6'] == dictionary['9'] or \
                dictionary['1'] == dictionary['5'] == dictionary['9'] or \
                dictionary['3'] == dictionary['5'] == dictionary['7']:
            return True
        else:
            return False

    def check_draw(self, dictionary):
        count = 0
        for value in dictionary.values():
            if value in ('X', 'O'):
                count += 1

        if count==9:

            return True
        else:
            return False

