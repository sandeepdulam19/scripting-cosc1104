# Names : Rohith Yerragunta, Sandeep Dulam
# Group - 12
# date : 4th oct, 2024
# Sandeep Dulam git link : https://github.com/sandeepdulam19/scripting-cosc1104
# Rohith Yerragunta git link: https://github.com/rohithYerraguntA/scripting-1104/tree/main


'''
code for checking whether the number is positive float number or not
'''

class number():

    # function for finding the number is positive or not
    def positive(is_number):
        return isinstance(is_number,float) and is_number > 0
    



if __name__ == "__main__":

    # test cases for finding positive number
    print(number.positive(60.5))
    print(number.positive(-5.9))
    print(number.positive(80))
    print(number.positive(0.0))