### MASTER MIND
### by Marage


### Variables
code = ''                                                   ###     Default code variable
number = ''                                                 ###     Testing code variable
code_arr = []                                               ###     An array of the numbers in the "code" variable to help with value comparison
combination_arr = []                                        ###     An array of the numbers in the "number" variable to help with value comparison
shownCode = []                                              ###     An array of the code to show; show the good numbers and hide the wrong one with a "X". Eg : code : "1234"; testing code : "1243"; shownCode : [1],[2],[X],[X]
combHints = []                                              ###     An array of the numbers which are present in the code. Eg : the code is "1234" and the other player enter the code "4321", this will tells that the numbers 1,2,3 and 4 are presents in the final code


### Functions
def askCode ():                                             ###     Ask to the player the code to find ( needs to be a 4 digits code)
    global code
    code = input('Enter a 4 digit code :\n- ')
    print('The code is : '+code)
def verifyCode ():                                          ###     Check code's length, and maybe some other features in the future
    global code
    if len(code) != 4:                                      # Target code's length
        print('Code must contains 4 digits')
        return False;
    else:
        return True;
def clearConsoleLogs():                                     ###     "Clear" the console by skipping 100 lines
    print("\n"*100)
def verifyNumber (number):                                  ###     NOT USED
    global code
    lookingfor = str(number)
    print('! Verifying code : ')
    for c in range(0, len(code)):
        if code[c] == lookingfor:
            print(str(c) + " " + code[c]);
def askNumber():                                            ###     Ask to the player the code to test
    global number
    number = input('Enter a code to test :\n- ')
def comp():                                                 ###     Comparison logic
    ##  Refer the global variables
    global code
    global number
    
    global code_arr
    global combination_arr
    
    global shownCode
    global combHints

    ## Clear the variables array to avoid to have wrong arrays. Eg : each turns, the code_arr will be "1234"*turn without tha, so "123412341234" at the third turn
    combination_arr.clear()
    code_arr.clear()
    shownCode.clear()
    combHints.clear()

    ## Add the numbers entered by the players in the variables array, the code and the testing code
    for x in range(0,len(code)):
        code_arr.append(code[x])
    for x in range(0,len(number)):
        combination_arr.append(number[x])
    ## Compare the values
    for x in range(0,len(code)):
        # Check the the tested number of the tested code is at the same index as the one of the final code
        if code_arr[x] == combination_arr[x]:
            shownCode.append(code_arr[x])               ###     If it is at the right place, add it in the "shownCode" array
        else:
            shownCode.append('X')                       #        Otherwise, add a "X" in the "shownCode" array
    ## Check for all the numbers in the code if it correspond to any of the numbers present in the target code
    for x in range(0,len(code)):
        for i in range(0,len(number)):
            if str(code_arr[i]) in combination_arr[x]:
                combHints.append(combination_arr[x])        #       If it is contained in the code, add it in the "combHints" variable ( the hints )
    
    ## Transform the arrays to string to make it clearer
    formatedCode = ' '.join(shownCode)
    formatedHints = ' '.join(combHints)

    print(formatedCode)                                     #       Print the code entered by the player trying to find the code with the numbers and the "X". Eg : "12X4" or "X73X"
    if len(combHints) != 0:                                 #       Print the hints
        print('The code contains : '+ formatedHints)
    else :                                                  #       If there's no hint in the variable, says that the code entered doesn't contain those numbers
        print("The code doesn't contain any numbers you've tested")

    ## Wining condition
    if code_arr == combination_arr:                         #       Check if the code entered is the same as the final one, and if yes return True ( which is going to be used in the wining condition in run() )      
        return True;    
    else:
        return False;                                       #       Else return False ( which is going to be used in run() to keep doing the loop )

def run ():                                                 ###     The function called to run the file
    tries = 5                                               # Set the number of tries allowed
    clearConsoleLogs()                                      # Clear the console
    askCode()                                               # Ask the code to the player
    if verifyCode() == True:                                # Check if the code use a correct format ( 4 digits )
        clearConsoleLogs()                                  # Clear the console to avoid the other player to see the final code
        for x in range(tries):                              # Loop until the "tries" variable is equal to 0
            askNumber()                                     # Ask to the other player a code to test
            if comp() == True:                              # Run the comparison logic and see if it's returning True ( Win ) or False ( Continue )
                print("You've found the code, good work ! ")
                break;                                      # Stop the tries loop
            else:
                tries -= 1                                  # Decrease the amount of tries
                print("\nYou have "+str(tries)+" tries left\n")   # Print the number of tries left

run()                                                       ###     Run the game