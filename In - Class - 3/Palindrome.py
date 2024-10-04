# Names : Rohith Yerragunta, Sandeep Dulam
# Group - 12
# date : 4th oct, 2024
# Sandeep Dulam git link : https://github.com/sandeepdulam19/scripting-cosc1104
# Rohith Yerragunta git link: https://github.com/rohithYerraguntA/scripting-1104/tree/main

'''
Code for checking the given string is palindrome or not
'''

# importing regular expressions module
import re

class newstring:


    # function for finding the string is palindrome 
    def is_palindrome(p):

        # removing special characters and modifing the string to lower cases
        modified = re.sub(r'[^A-Za-z0-9]', '', p).lower()
        return modified == modified[::-1]
    



if __name__ == "__main__":

    # test cases for checking the string is palindrome or not
    print(newstring.is_palindrome("racecar"))
    print(newstring.is_palindrome("what is my name ? "))
    print(newstring.is_palindrome("Mr.Owl ate my metal worm"))
    print(newstring.is_palindrome("Durham college cloud computing"))
