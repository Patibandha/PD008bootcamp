import logging


def main():
    p_string = input("Enter a string: ")
    rem_spe_chr = ""
    for character in p_string:
        if character.isalnum():
            rem_spe_chr += character
    logging.warning(msg="after removing special character final output:" + rem_spe_chr)
    obj_pali.palstr(rem_spe_chr)


class Pali:

    def palstr(self, rem_spe_chr):
        if rem_spe_chr == rem_spe_chr[::-1]:
            msg = "The string is a palindrome"
        else:
            msg = "Not a palindrome"
        logging.warning(msg)


obj_pali = Pali()

if __name__ == '__main__':
    main()
