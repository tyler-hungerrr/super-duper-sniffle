def input_num(number): #validating the input as a number
    try:
        number = int(number)
    except ZeroDivisionError as err:
        print(err)
    except NameError as err:
        print(err)
    except ValueError as err:
        print(err)
    except KeyboardInterrupt as err:
        print(err)
    except Exception as err:
        print(err)
    return number
def input_word(word): #validating the input as a word
    try:
        word = str(word)
    except NameError as err:
        print(err)
    except KeyboardInterrupt as err:
        print(err)
    except Exception as err:
        print(err)
    return word
#input_num(hr)

print("Welcome to my Fallout Quiz")
play = input("Do you want to play? ") #play game or quit
if play.lower() != "yes":
    quit()
print("Alright! Let's play!")

correct = 0
answer = input("When did the great war begin? ") #first question
input_num(answer) #validating input
if answer == "2077":
    print("You are Correct!")
    correct += 1
else:
    print("You are Incorrect")

answer = input("When did the US annex Canada? ") #second question
input_num(answer)  #validating input
if answer == "2072":
    print("You are Correct!")
    correct += 1
else:
    print("You are Incorrect")

answer = input("What is the name of the wars the brought about the end of the UN? ") #third question
input_word(answer) #validating input
if answer.lower() == "resource wars":
    print("You are Correct!")
    correct += 1
else:
    print("You are Incorrect")

answer = input("Who fought the US in the Sino-American War? ") #forth question
input_word(answer) #validating input
if answer.lower() == "china":
    print("You are Correct!")
    correct += 1
else:
    print("You are Incorrect")

print("You got " + str((correct / 4) * 100) + "% of questions correct.") #% of questions correct