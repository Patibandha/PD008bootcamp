import logging


def main():
    p_string = input("Enter a string: ")
    rem_spe_chr = ""
    for character in p_string:
        if character.isalnum():
            rem_spe_chr += character
    logging.warning(msg="after removing special character final output:" + rem_spe_chr)
    pal_str(rem_spe_chr)


def pal_str(rem_spe_chr):
    if rem_spe_chr == rem_spe_chr[::-1]:
        msg = "The string is a palindrome"
    else:
        msg = "Not a palindrome"
    logging.warning(msg)


if __name__ == '__main__':
    main()


# def check_is_digit(p_str):
#     if p_str.strip().isdigit():
#         logging.warning(msg="You must enter a string. Please try again")
#     else:
#         pal_str(p_str)


