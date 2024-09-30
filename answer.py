import random


def format_key(string):
    new_string = ""
    if len(string) == 8:
        new_string = string[2:6]
        return new_string
    elif len(string) == 9:
        new_string = string[2:7]
        return new_string
    elif len(string) == 12:
        new_string = string[2:10]
        return new_string

class Answer:
    """
    Class for RPS answers, is expecting:
        1 - Rock\n
        2 - Paper\n
        3 - Scissors
    """
    def __init__(self,option):
        self.option = option
        self.name = ''
        self.number = 0
        self.valid = False
        self.options_dict = {'rock' : 1, 'paper' : 2, 'scissors' : 3}
        if option in range(1,4):
            self.option_int = int(option)

        if self.option.lower() in self.options_dict.keys():
            self.name = self.option.lower()
            self.number = self.options_dict.get(self.name)
            self.valid = True
        if self.option_int in self.options_dict.values():
            self.number = self.option_int
            key = {i for i in self.options_dict if self.options_dict[i]==self.number}
            key_str = format_key(str(key))
            self.name = key_str
            self.valid = True
        else:
            self.valid = False


    def generate_answer(self):
        self.number = random.randint(1, 3)
        key = {i for i in self.options_dict if self.options_dict[i]==self.number}
        key_str = format_key(str(key))
        self.name = key_str
        self.valid = True
