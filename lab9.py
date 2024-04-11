def encode_number(num):
    num_str = str(num)
    encoded_num_str = ''
    for digit in num_str:
        encoded_digit = str(int(digit) + 3)
        encoded_num_str += encoded_digit
    encoded_num = int(encoded_num_str)
    return encoded_num

