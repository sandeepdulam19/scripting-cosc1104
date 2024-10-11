# function for finding prime number
def prime_no(n):

    # checking the number is prime
    if n <=1:
        return False
    
    # checking for factors from 2 to square root of n 
    # we use this to reduce number of iterations and quick calculations
    # we can also use (n/2) instead of (n**0.5) but it will have lot of unnecessary iterations for larger values.
    for i in range(2, int(n**0.5)+1):
    
        # if n is divisible by i it is not prime
        if n % i == 0:
            return False
    return True


# function for finding previous prime number
def previous_prime(n):
    
    # from n-1 to 2
    for j in range(n-1, 1, -1):

        # checking if j is prime or not
        if prime_no(j):
            return j
    return None



# function for finding next prime number
def next_prime(n):

    # starting from n+1 to n*2
    for i in range(n+1, n*2):

        # checking if i is prime ot not
        if prime_no(i):
            return i
    return None



# function for finding factors for non-prime numbers
def get_divisors(n):
    divisors = []

    # checking all the numbers from 1 to n
    for i in range(1, n+1):

        # if i divides n appending i to list
        if n % i == 0:
            divisors.append(i)
        
    return divisors


def main():
    while True:
        user_input = input("Please enter the number to check: ")

        # checking if the input value is digit and converting to integer
        if user_input.isdigit():
            number = int(user_input)

            # checking the number is positive or not
            if number > 0:
                break
            else:
                print("This is not a positive whole number. Please try again: ")
        else:
            print("Invalid input. Please enter a positive whole number. Try again")


    # special condition for number 1
    if number == 1:
        print("1 is not a prime number")
        print("There are no prime numbers before 1")
        print("Prime number after 1 is 2")
        return




    # finding the previous prime number
    prev_prime = previous_prime(number)
    if prev_prime:
        print(f"The prime number before {number} is {prev_prime}")
    else:
        print(f"There is no prime number before {number}")

    


    # checking the number is prime or not
    if prime_no(number):
        print(f"{number} is a prime number")

    # getting the factors if number is not a prime    
    else:
        print(f"{number} is not a prime number")
        print(f"The factors of {number} are {get_divisors(number)}")



    # finding the next prime number
    next_p = next_prime(number)
    print(f"The prime number after {number} is {next_p}")




# main function for script execution
if __name__ == "__main__":
    main()

    
    