# Passworder - simple password generator
#
# made by crwave1
#  
# 08.2025
#



import string
import random

print()
print("=============================<{ pasworder }>=============================")
print()

pw = ""

# picking pw complexity

#charlist = string.ascii_letters
#charlist2 = charlist + string.digits
#charlist3 = charlist2 + string.punctuation

#pick = int(input("Please enter desired password complexity (from 1 to 3): "))
#if pick == 1:
#   pickedlist = charlist
#elif pick == 2:
#   pickedlist = charlist2
#elif pick == 3:
#   pickedlist = charlist3

chlist = ""

if input("Would you like to provide a specific character set? (y/n) ") == "y":
   chlist = input("Please input the characters you want in your password: ")

elif input("Would you like numbers in your password? (y/n) ") == "y":
   chlist = string.digits

   if input("Would you like lowercase letters in your password? (y/n) ") == "y":
      chlist += string.ascii_lowercase

   if input("Would you like uppercase letters in your password? (y/n) ") == "y":
      chlist += string.ascii_uppercase

   if input("Would you like basic symbols (!, ?, .) in your password? (y/n) ") == "y":
      chlist += "!?."

   if input("Would you like an extreme password, disregarding previous choices? (y/n) ") == "y":
      chlist = string.digits + string.ascii_letters + string.punctuation

pwlength = int(input("Please enter desired password length: "))

# might add try block for 'int(input())' lines

print()

i = 0

while i < pwlength:
   pw = pw + random.choice(chlist)
  # print(pw)                                         # FOR SEEING THE PASSWORD CREATION PROCESS ONLY. REMOVE LATER
   i = i+1

print(f"Password generated: \n {pw} \n")

input("Press Enter to exit.")