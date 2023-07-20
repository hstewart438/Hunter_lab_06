# Hunter Stewart and Joelie Campana (decode)
def encode(password):
    password = [int(num) for num in list(password)]  # password to integer list for iteration
    for idx, num in enumerate(password):
        encoded_num = password[idx] + 3
        if encoded_num > 9:
            remainder = encoded_num - 10  # takes amount over 9
            password[idx] = remainder  # replaces value out of range, with new in value range
        else:
            password[idx] += 3
    encoded_password = ''.join([str(num) for num in password])  # encoded password put back into string
    return encoded_password


def decode(encoded_password):
    decoded_password = ""
    # iterate through decoded pw, subtract 3 from each
    for i in encoded_password:
        subtracted = str((int(i) - 3) % 10)
        # append to string
        decoded_password += subtracted
    return decoded_password



if __name__ == '__main__':
    program_on = True
    print('Welcome to the password encoder and decoder!\n')
    while program_on:
        print('1. Encode password\n'
              '2. Decode password\n'
              '3. Exit program')
        option = int(input('\nPlease select a menu option: '))
        if option == 1:
            user_password = input('Please input a numerical 8-digit password to encode: ')
            encoded_password = encode(user_password)
            print(f'Your password has been encoded and stored.\n')
            continue
        elif option == 2:
            decoded_password = decode(encoded_password)
            print(f'Your encoded password is {encoded_password}, and your original password is {decoded_password}.\n')
            continue
        elif option ==3:
            print('\nGoodbye!')
            program_on = False  # break out and end program
