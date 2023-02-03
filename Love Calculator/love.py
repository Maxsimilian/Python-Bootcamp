print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# lowering the names
lower_name1 = name1.lower()
lower_name2 = name2.lower()
# adding the names 
Couple_names = lower_name1+lower_name2
# counting the number of times the letters in the word love and true occurs.
true = str(Couple_names.count("t")) + str(Couple_names.count("r")) + str(Couple_names.count("u")) + str(Couple_names.count("e"))
sum_true = int(true[0]) + int(true[1]) + int(true[2]) + int(true[3])
love = str(Couple_names.count("l")) + str(Couple_names.count("o")) + str(Couple_names.count("v")) + str(Couple_names.count("e"))
sum_love = int(love[0]) + int(love[1]) + int(love[2]) + int(love[3])
# adding the two results
total = str(sum_true) + str(sum_love)
# converting the str to int.
love_score = int(total)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")





