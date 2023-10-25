# The password encoder should take in an 8-digit password in string format containing only integers.
# After passing the password into the encoder, the encoder stores the encoded password to a new
# variable, with each digit being shifted up by 3 numbers.
# Examples:
# “12345555” will become “45678888” after encoding.
# “00009962” will become “33332295” after encoding.

def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def main():

    continue_program = True
    
    while continue_program:
        print_menu()
        user_input = int(input("Please enter an option: "))
        
        if user_input == 1:
            # example is 12345555 and encode to 45678888
            encoded_password = ''
            my_dict = {"1": "4", "2": "5", "3": "6", "4": "7", "5": "8", "6": "9", "7": "1", "8": "2", "9": "3"}
            to_decode = input("Please enter your password to encode: ")
            for element in to_decode:
                encoded_password += my_dict[element]
        elif user_input == 2:
            pass
        elif user_input == 3:
            continue_program = False

    print(encoded_password)

if __name__ == "__main__":
    main()