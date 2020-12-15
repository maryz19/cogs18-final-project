import pytest
from ChatBot import ChatBot
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
    There are two tests total. 
    Use to test that chatbot is one time response or not."""
def test_response_true_false1():
    input_val = "Goodbye"
    output = bot.oneline_response(input_val)
    assert not output
    #f"expect False get {output}"

def test_response_true_false2():
    input_val = "1 minus 2"
    output = bot.oneline_response(input_val)
    assert output
    #, f"expect True get {output}"
    