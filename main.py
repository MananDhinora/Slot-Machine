MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

def deposite():
    """ New method to take input from the user to set a deposite value 

    Returns: deposite amount by the user
        _type_: int
    """
    while True:
        deposite_amount = input("Enter deposite amount $: ")
        if not deposite_amount.isdigit():
            print("Please Enter a number.")
            continue
        deposite_amount = int(deposite_amount)
        if not deposite_amount > 0:
            print("Enter amount greater than 0.")
            continue
        break    
    return deposite_amount


def get_number_of_lines():
    """ New method to take input from the user to set the number or lines 

    Returns: number of lines selected by the user
        _type_: int
    """
    while True:
        number_of_lines = input("Enter number of lines $: ")
        if not number_of_lines.isdigit():
            print("Please Enter the number of lines. (1-"+ str(MAX_LINES) +") ")
            continue
        number_of_lines = int(number_of_lines)
        if not 1 <= number_of_lines <= 3:
            print("Enter amount valid number of lines.")
            continue
        break    
    return number_of_lines


def get_bet():
    
    """ New method to take input from the user to set the bet ammount 

    Returns: bet amount set by the user
        _type_: int
    """
    while True:
        number_of_lines = input("Enter the bet value $: ")
        if not number_of_lines.isdigit():
            print(f"Please Enter the bet ammount. (${MIN_BET}-${MAX_BET})")
            continue
        number_of_lines = int(number_of_lines)
        if not MIN_BET <= number_of_lines <= MAX_BET:
            print("Enter a bet ammount between the upper and lower bet limits.")
            continue
        break    
    return number_of_lines
    
    
def user_input():
    #TODO create a generic method for the above 3 methods
    pass
    
def main():
    player_balance = deposite()
    selcted_lines = get_number_of_lines()
    player_bet = get_bet()
    print(player_balance, selcted_lines, player_bet)
    
main()