# Passworder - simple password generator
#
# made by crwave1
#  
# 08.2025
#



import string
import random

print()
print("============== pasworder ==============")
print()

pw = ""
charlist = string.ascii_letters
charlist2 = charlist + string.digits
charlist3 = charlist2 + string.punctuation
pwlength = int(input("Please enter desired password length: "))

# picking pw complexity

pick = int(input("Please enter desired password complexity (from 1 to 3): "))

if pick == 1:
   pickedlist = charlist
elif pick == 2:
   pickedlist = charlist2
elif pick == 3:
   pickedlist = charlist3

# will add try block for 'int(input())' lines

print()

i = 0

while i < pwlength:
   pw = pw + random.choice(pickedlist)
  # print(pw)                                         # FOR SEEING THE PASSWORD CREATION PROCESS ONLY. REMOVE LATER
   i = i+1

print(f"Password generated: \n {pw} \n")

input("Press Enter to exit.")