def create_list(user_input):

    str_list = str(user_input)
    digits = list()

    for index in range(len(str_list) - 1):
        if str_list[index] == str_list[index + 1]:
            digits.append(int(str_list[index]))
    
    if str_list[-1] == str_list[0]:
        digits.append(int(str_list[-1]))
    
    return digits


def main():

    ui = input('Enter digits: ')

    digits = create_list(ui)

    total_amount = sum(digits)
    print(total_amount)
    

if __name__ == "__main__":
    main()