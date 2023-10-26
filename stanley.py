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


def encode(to_encode):
    encoded_password = ''
    my_dict = {"1": "4", "2": "5", "3": "6", "4": "7", "5": "8", "6": "9", "7": "1", "8": "2", "9": "3"}
    for element in to_encode:
        encoded_password += my_dict[element]
    return encoded_password

def decode(to_decode):
    decoded_password = ''
    for i in range(len(to_decode)):

        if int(to_decode[i]) >= 3:
            decoded_password += str(int(to_decode[i]) - 3)
        else:
            decoded_password += str(int(to_decode[i]) + 7)

    return decoded_password

def main():
    continue_program = True

    while continue_program:
        print_menu()
        user_input = int(input("Please enter an option: "))
        if user_input == 1:
            # example is 12345555 and encode to 45678888
            to_encode = input("Please enter your password to encode: ")
            encoded_password = encode(to_encode)
            print("Your password has been encoded and stored!")
        elif user_input == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
        elif user_input == 3:
            continue_program = False


if __name__ == "__main__":
    main()
