score = int(input("Enter your score\n"))
if 90 <= score <= 100:
    print("Your grade is A")
elif 80 <= score <= 89:
    print("Your score is B")
elif 70 <= score <= 79:
    print("Your grade is C")
elif 70 <= score <= 79:
    print("Your grade is D")
elif 60 <= score <= 69:
    print("Your grade is E")
elif 50 <= score <= 59:
    print("Your grade is F")
elif score>100:
    print("Please enter a valid number")
else:
    print("You are failed")

