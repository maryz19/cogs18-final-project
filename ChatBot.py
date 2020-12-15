import random

class ChatBot(object):
    def __init__(self, name):
        self.name = name
        self.input_chat = None
        self.reponse = None
        self.calculation_symbols = ["plus","minus","mult","div", "*", 
                                                        "+", "-" , "/", "^"]
        self.knowledge_base = dict()
        self.knowledge_base["python"] = "Python is a coding Language."
        self.python_modules = []
        self.words = []
        self.agree = ["I think so!", "Yeah!!", "Sounds good!", 
        "Your are right."]
        self.disagree = ["Nahh.", "I don't think so", 
        "I can hardly agree with you."]
        self.agree_word = []
        self.disagree_word = []
        self.good_bye = ["bye", "Bye", "See you", "exit", "quit", "end"]

    def add_module(self, module):
        self.python_modules.append(module)
        self.knowledge_base[module] = "a python module."

    def add_knowledge(self, knowledge, description):
        self.knowledge_base[knowledge] = description

    def add_agree_disagree(self, word, agree = None):
        self.words.append(word)
        if agree is not None:
            if agree:
                self.agree_word.append(word)
            else:
                self.disagree_word.append(word)

    def oneline_response(self, input_val):
        self.input_chat = input_val
        return self.response()

    def response(self):
        for bye in self.good_bye:
            if bye in self.input_chat:
                return False

        calculation = False
        for symbol in self.calculation_symbols:
            if symbol in self.input_chat:
                calculation = True
                break
        if calculation:
            formula = self.clear_calculation_input(self.input_chat)
            valid, result = self.calculate(formula)
            if not valid:
                print(f"ChatBot {self.name}: I cannot understand you. If you"\
                    f" want me to do calculation, you can use the following "\
                    f"expressions: {self.calculation_symbols} and "\
                    f"use paranthesis to organize the calculation, be sure to"\
                    f" enter a valid formula")
            else:
                print(f"ChatBot {self.name}: your formula equals to {result}")
            return True

        for key in self.knowledge_base:
            if key in self.input_chat:
                print(f"ChatBot {self.name}: Are you asking"\
                f" 'What is {key}?'. Y/n")
                conf = input("User Input: ")
                if conf in ["Y", "y", "yes", "Yes"]:
                    print(f"ChatBot {self.name}: {key} is"\
                    f" {self.knowledge_base[key]}")
                return True

        for word in self.words:
            if word in self.input_chat:
                if word in self.agree_word:
                    msg = self.agree[random.randint(0, 
                                        len(self.agree) - 1)]
                    print(f"ChatBot {self.name}: {msg}")
                elif word in self.disagree_word:
                    msg = self.disagree[random.randint(0, 
                                        len(self.disagree) - 1)]
                    print(f"ChatBot {self.name}: {msg}")
                else:
                    if random.random() > 0.6:
                        msg = self.disagree[random.randint(0, 
                                            len(self.disagree) - 1)]
                        self.disagree_word.append(word)
                        print(f"ChatBot {self.name}: {msg}")
                    else:
                        msg = self.agree[random.randint(0, 
                                            len(self.agree) - 1)]
                        self.agree_word.append(word)
                        print(f"ChatBot {self.name}: {msg}")
                return True

        
        if random.random() > 0.7:
            print(f"ChatBot {self.name}: Sorry I cannot understand you.")
            self.add_knowledge_base()
        else:
            print(f"ChatBot {self.name}: I cannot understand you. However,"\
                    f" I can do a lot of calculations. Use the following "\
                    f"expressions: {self.calculation_symbols} and "\
                    f"use paranthesis to organize the calculation, be sure to"\
                    f" enter a valid formula")
        return True



    def add_knowledge_base(self):
        print(f"ChatBot {self.name}: Can you add any other information "\
            f"to my knowledge base?")
        module = input("User Input: ")
        print(f"ChatBot {self.name}: So {module} is a python module right?"\
                                f" Please type Y/n to confirm.")
        conf = input("User Input: ")
        if conf in ["Y", "y", "yes", "Yes"]:
            knowledge_base[module] =  f"{module} is a python module."
        else:
            print(f"ChatBot {self.name}: Can you provide any description " \
                "for {module}")
            description = input("User Input: ")
            knowledge_base[module] =  description
            print(f"ChatBot {self.name}: Thank you.")


    def clear_calculation_input(self, input_chat):
        formula_start = False
        start_index = -1
        end_index = -1
        i = 0
        while i < len(input_chat):
            if input_chat[i]!=" ":
                if input_chat[i] in "0123456789().":
                    if not formula_start:
                        formula_start = True
                        start_index = i
                else:
                    tmp_formula_start = False
                    for j in range(1, min(len(input_chat) - i + 1, 6)):
                        if input_chat[i:i+j] in self.calculation_symbols:
                            tmp_formula_start = True
                            i += j
                            if not formula_start:
                                start_index = i
                                formula_start = True
                            break
                    if formula_start and not tmp_formula_start:
                        end_index = i
                        break
            i += 1
        if end_index < 0:
            end_index = len(input_chat) 
        return input_chat[start_index:end_index]
                

    def calculate(self, formula):
        formula = formula.replace("plus", "+")
        formula = formula.replace("minus", "-")
        formula = formula.replace("mult", "*")
        formula = formula.replace("div", "/")
        formula = formula.replace(" ", "")
        i = 0
        while i < len(formula):
            if (formula[i] == "(" and i > 0 and 
                formula[i-1] in "0123456789"):
                formula = formula[:i] + "*"+formula[i:]
                i += 1
            if (formula[i] == ")" and i < len(formula)-1 and
                formula[i+1] in "0123456789("):
                formula = formula[:i+1] + "*" +formula[i+1:]
            i += 1

        count = 0
        start_index = -1
        end_index = -1

        for i in range(len(formula)):
            if formula[i] == "(":
                count += 1
                if start_index < 0:
                    start_index = i
            elif formula[i] == ")":
                count -= 1
                if count < 0:
                    return False, None
                elif count == 0 and end_index < 0: 
                    end_index = i
       
        if count != 0:
            return False, None

        

        if end_index > 0:
            valid, value = self.calculate(formula[start_index + 1:end_index])
            if not valid:
                return False, None

            formula=formula[:start_index] + str(value) + formula[end_index+1:]
            return self.calculate(formula)
        else:

            def base_case_calculation(symbols, formula):
                symbol1, symbol2 = "?", "?"
                if len(symbols) == 1:
                    symbol2 = symbols[0]
                else:
                    symbol1 = symbols[0]
                    symbol2 = symbols[1]
                if symbol1 == "+" and symbol2 == "-":
                    formula = formula.replace("+-", "-")
                    formula = formula.replace("--", "+")

                while symbol1 in formula or symbol2 in formula:
                    index = len(formula)
                    symbol = symbol1
                    if symbol1 in formula:
                        index = formula.index(symbol1)

                    if symbol2 in formula and formula.index(symbol2) < index:
                        if symbol2 == "-" and formula.index(symbol2) == 0:
                            if symbol2 in formula[1:]:
                                new_ind = formula[1:].index(symbol2) + 1
                                if new_ind < index:
                                    index = formula.index(symbol2)
                                    symbol = symbol2
                            elif symbol1 not in formula[1:]:
                                break
                        else:
                            index = formula.index(symbol2)
                            symbol = symbol2


                    after, before = "", ""
                    i1 = index - 1
                    while i1 >= 0 and formula[i1] in "0123456789." :
                        before = formula[i1] + before
                        i1 -=1
                    if formula[i1] == "-":
                        before = "-" + before
                        i1 -= 1

                    i2 = index + 1
                    if formula[i2] == "-":
                        after = "-"
                        i2 += 1
                    while i2 < len(formula) and formula[i2] in "0123456789.":
                        after += formula[i2]
                        i2 += 1
                    before = float(before)
                    after = float(after)
                    res = 0
                    if symbol == "^":
                        res = before**after
                    elif symbol == "*":
                        res = before * after
                    elif symbol == "/":
                        res = before/after
                    elif symbol == "+":
                        res = before + after
                    elif symbol == "-":
                        res = before - after
                    formula = formula[:i1 + 1] + str(res) + formula[i2:]
                        
                return formula

            formula = base_case_calculation(["^"], formula)
            formula = base_case_calculation(["*", "/"], formula)
            formula = base_case_calculation(["+", "-"], formula)

            return True, float(formula)





    def chat(self):
        self.input_chat = input("User Input: ")
        while self.response():
            self.input_chat = input("User Input: ")
        print(f"ChatBot {self.name}: See you next time!")
        

# Jupyter

"""
bot = ChatBot("bob")
for module in  ["numpy", "math", "random", "calander", "pandas"]:
    bot.add_module(module)

for word in ["i am good", "fine", "great", "amazing", "nice", "hot",
        "cold", "warm", "rainy", "sunny", "easy", "hard"]:
    bot.add_agree_disagree(word)

bot.add_agree_disagree("watermellon is sweet", True)
bot.chat()
"""
###################################################################
import pytest
""" Test calculate:
    There are five tests total. 
    Use to test that chatbot will calculate in the right order,
    so that it will show up the right answer."""
bot = ChatBot("testbot")
epislon = 1e-5
def test_calculate1():
    formula = "1 + 2 * 3"
    valid, value = bot.calculate(formula)
    assert valid, f"calculate {formula} fails, expect formula to"\
                                 f" be True, however returns {valid}"
    assert abs(value-7.0) < epislon, f"calculate {formula} fails, "\
                                 f"expect value to be 7.0, however "\
                                 f"returns {value}"

def test_calculate2():
    formula = "(34*-12+3*(2+5))/7^2+(3*4)"
    valid, value = bot.calculate(formula)
    assert valid, f"calculate {formula} fails, expect formula to"\
                                 f" be True, however returns {valid}"
    assert abs(value -4.10204) < epislon, f"calculate {formula} fails, "\
                                 f"expect value to be 4.10204, however "\
                                 f"returns {value}"

def test_calculate3():
    formula = "(90+5 plus 5)(2 minus 2 + 2 (1 plus 2))"
    valid, value = bot.calculate(formula)
    assert valid, f"calculate {formula} fails, expect formula to"\
                                 f" be True, however returns {valid}"
    assert abs(value -600) < epislon, f"calculate {formula} fails, "\
                                 f"expect value to be 600, however "\
                                 f"returns {value}"

def test_calculate4():
    formula = "(1+2)/3"
    valid, value = bot.calculate(formula)
    assert valid, f"calculate {formula} fails, expect formula to"\
                                 f" be True, however returns {valid}"
    assert abs(value -1) < epislon, f"calculate {formula} fails, "\
                                 f"expect value to be 1, however "\
                                 f"returns {value}"

def test_calculate5():
    formula = "(5 plus 5 mult 3)/4 div 5"
    valid, value = bot.calculate(formula)
    assert valid, f"calculate {formula} fails, expect formula to"\
                                 f" be True, however returns {valid}"
    assert abs(value -1) < epislon, f"calculate {formula} fails, "\
                                 f"expect value to be 1, however "\
                                 f"returns {value}"
    
#test clear_calculation_input
""" Test clear calculation input:
    There are five tests total. 
    Use to test that chatbot will extracting numbers 
    and calculating symbols from random code."""

def test_clear_calculation_input1():
    input = "lsakjdklpapsj 3 * 4 + 9 /1"
    output = bot.clear_calculation_input(input)
    res = "3 * 4 + 9 /1"
    assert output== res, f"expect {res} get {output}"
    

def test_clear_calculation_input2():
    input = "lsakjfhjosnw 5+8"
    output = bot.clear_calculation_input(input)
    res = "5+8"
    assert output== res, f"expect {res} get {output}"
    
    
def test_clear_calculation_input3():
    input = "dbjkbfksbchfkbv? 35/5 +10"
    output = bot.clear_calculation_input(input)
    res = "35/5 +10"
    assert output== res, f"expect {res} get {output}"  
    
    
def test_clear_calculation_input4():
    input = "otgbihtfnb88-90+(5/20)"
    output = bot.clear_calculation_input(input)
    res = "88-90+(5/20)"
    assert output== res, f"expect {res} get {output}"
   
    
def test_clear_calculation_input5():
    input = "qwwertyuryty88/8+90/9"
    output = bot.clear_calculation_input(input)
    res = "88/8+90/9"
    assert output== res, f"expect {res} get {output}"
#test response true/false 
""" Test response true/false:
    There are five tests total. 
    Use to test that chatbot is one time response or not."""
def test_response_true_false1():
    input_val = "Goodbye"
    output = bot.oneline_response(input_val)
    assert not output, f"expect False get {output}"

def test_response_true_false2():
    input_val = "1 minus 2"
    output = bot.oneline_response(input_val)
    assert output, f"expect True get {output}"