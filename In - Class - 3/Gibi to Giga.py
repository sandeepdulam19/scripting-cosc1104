# Names : Rohith Yerragunta, Sandeep Dulam
# Group - 12
# date : 4th oct, 2024
# Sandeep Dulam git link : https://github.com/sandeepdulam19/scripting-cosc1104
# Rohith Yerragunta git link: https://github.com/rohithYerraguntA/scripting-1104/tree/main

'''
code for converting gibi bytes to giga bytes and also vice-versa

'''



class number:

    #function for converting Gibi bytes to Giga bytes
    
    def gibi_to_giga(gibi):
        return gibi*(1.073741824/1.00000000)
    

    #function for converting Giga bytes to Gibi bytes
    
    def giga_to_gibi(giga):
        return giga * (1.00000000/1.073741824)
    





if __name__ == "__main__":

    # test cases for gibi to giga
    
    print(f'Gibi to Giga: {number.gibi_to_giga(4)}')
    print(f'Gibi to Giga: {number.gibi_to_giga(10)}')
    print(f'Gibi to Giga: {number.gibi_to_giga(1)}')


    # test cases for giga to gibi

    print(f'Giga to Gibi: {number.giga_to_gibi(1)}')
    print(f'Giga to Gibi: {number.giga_to_gibi(8)}')
    print(f'Giga to Gibi: {number.giga_to_gibi(10)}')

