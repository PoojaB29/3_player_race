"""
Racing between 3 players 
Three player : Sita Ram Sham
Winner rank  :  1     2    3
Write a function that given persons name return his/her place as winner
Also
Write a fuction that given the place returns his/her name
"""

def choice_to_number(choice):
    dict1 = {"Sita":2, "Ram": 1, "Sham": 3}
    return dict1[choice]

def number_to_choice(choice):
    dict2 = {1:"Sita", 2: "Ram", 3: "Sham"}
    return dict2[choice]

def test_choice_to_number():
    assert choice_to_number("Sita") == 1
    assert choice_to_number("Ram") == 2
    assert choice_to_number("Sham") == 3

def test_number_to_choice():
    assert number_to_choice(1) == "Sita"
    assert number_to_choice(2) == "Ram"
    assert number_to_choice(3) == "Sham"

def test_all():
    try:
        test_choice_to_number()
        test_number_to_choice()
    except AssertionError:
        import wrong
    else:
        import success

test_all()
