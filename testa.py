
# weight = input('Enter weight in Kg: ')
# Pounds = int(weight) * 2.2
# print("Your weight in pounds is " + str(Pounds))



# Age = int(input("Enter your age; "))
# if Age >= 18:
#     print("I can drive")
# else:
#     print("I cannot drive")



# color = input("Enter color ")
# if color == "red":
#     print("Danger")
# elif color == "green":
#     print("get ready")
# else:
#     print("You can now go")



# score = int(input("Enter test score for Phyics "))
# if score >= 80:
#     print("Grade A")
# elif score >= 70:
#     print("Grade B")
# elif score >= 60:
#     print("Grade C")
# elif score >= 50:
#     print("Grade D")
# else:
#     print("Fail")



# from curses.ascii import isdigit
# number = input("Enter a digit ")
# if number.isdigit(): you can use either of this methods they work
# if number.isdigit()==True:

#     print("You have entered a number")
# else:
#     print("Yoh have not entered a number")



# age = int(input("Enter your age "))
# if age % 2 == 0:
#     print("Your age is an even number")
# else:
#     print("Your age is an odd number")


# Sorting order
# first = [7,50,89]
# second = [45,67,20]
# total = sorted(first + second)
# print(total)


# v = input("Enter a letter ")

# if v == 'a' or v=='A' or v=='e'or v=='E'or v=='O'or v=='O'or v=='u'or v=='U'or v=='i'or v=='I':
#     print(v + " is a vowel")
# else:
#     print(v + " is a consonant")



# vowel = 0
# consonant = 0
# test = input("Enter a vowel ")

# for v in test:
#     if v == 'a' or v=='A' or v=='e'or v=='E'or v=='O'or v=='O'or v=='u'or v=='U'or v=='i'or v=='I':
#         vowel = vowel + 1
#         print(vowel)
#     else:
#         print(consonant)
#         consonant = consonant + 1
# print(consonant)



# vowel = ['a', 'e', 'i', 'o', 'u']
# Sentence = input("Enter a phrase: ")
# count = 0
# for letter in Sentence:
#     if letter in vowel:
#         count += 1
# print(count)


# Finding the maximum value in the list
# list = [41, 4, 20, 21, 14, 72]
# large = max(list)
# print(large)




# v = input("Enter letter ")
# vowels = ['a','e','i','o','u','A', 'E', 'I','O','U']
# if v in vowels:
#     print("Vowel")
# else:
#     print("consonant")



## Determining total number of odd and even numbers
# num = [1,30,56,13,17,89,90]
# # num = input("Enter value ")
# odd = 0
# even = 0
# prime = 0

# for n in num:
#     if n % 2 == 0:
#         even = even +1
        
#     elif n % 2 != 0:
#         odd = odd + 1
        
    
# print("even numbers are " + str(even))
# print("Odd number are "+ str(odd))



####Determining prime numbers
# # taking input from user
# number = int(input("Enter any number: "))

# # prime number is always greater than 1
# if number > 1:
#     for i in range(2, number):
#         if (number % i) == 0:
#             print(number, "is not a prime number")
#             break
#     else:
#         print(number, "is a prime number")

# # if the entered number is less than or equal to 1
# # then it is not prime number
# else:
#     print(number, "is not a prime number")

