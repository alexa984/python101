
def is_credit_card_valid(number):
    number_digits = len(str(number))
    if number_digits%2 == 0:
        return False
    else:
        number_as_arr = to_digits(number)
        for i in range (1,number_digits, 2):
            number_as_arr[i] *= 2 
        number = to_number(number_as_arr)
        if sum_of_digits(number)%10 == 0:
            return True
        else:
            return False