import os

class console():
    def __init__(self, width:int=80):
        self.width = width

    def clear(self, title:str=None):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"{title:-^{self.width}}")

    def draw_box(i:list):
        print(f"   1 2 3\n1 |{i[0][0]}|{i[0][1]}|{i[0][2]}|\n2 |{i[1][0]}|{i[1][1]}|{i[1][2]}|\n3 |{i[2][0]}|{i[2][1]}|{i[2][2]}|\n")

    def syntaxError(self, val:str, val1:str, val2:str, val3:str=None, val4:str=None):
        self.clear("\033[41mERROR:\033[0m")
        input(f"'{val}' is not a valid value.\nOnly '{val1}'{"," if val3 else " and"} '{val2}'{f", '{val3}' and '{val4}'" if val4 else f" and '{val3}'" if val3 else ""} are allowed.\nPress ENTER to continue.")

    def question(self, title:str, question:str, answer1:str, answer2:str, answer3:str=None, answer4:str=None)->int:
            while True:
                try:
                    self.clear(title)
                    inp = input(f"{question}\n>>>").lower()
                    return {answer1:1, answer2:2, answer3:3, answer4:4}[inp]
                except KeyError:
                    self.syntaxError(inp, answer1, answer2, answer3, answer4)