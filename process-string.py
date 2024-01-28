# Application 1
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
a = "String"
for x in a:
    result = ''.join(x * 2)
    print(result, end = "")

# * "Hello World" -> "HHeelllloo  WWoorrlldd"
b = "Hello World"
for y in b:
    result = ''.join(y * 2)
    print(result, end = "")

# * "1234!_ "     -> "11223344!!__  "
c = "1234!_"
for z in c:
    result = ''.join(z * 2)
    print(result, end = "")


# Application 2
#  Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes A hyphen will separate the two letters in the string.



# write down all of the alphabet total range
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ"
# ask user to input letter from one - another using split
user_input = input('Enter a range of letters (e.g., a-z): ')
# analyze start and end point by getting the user input range e.g. a-m so, start = a
start, end = user_input.split("-")
# using index function to find the position of the start point e.g. a = 0
start_num = alphabet.index(start)
# using index function to find the position of the end point e.g. m = 13
end_num = alphabet.index(end)
# using range alphabet[num1:num2] which means the position of num1 to num2
range = alphabet [start_num: end_num + 1]
# e.g. alphabet[0:13] which means in alphabet variable, it displays from letter in 0 position to 13 position
# note: variable[:] only works with number, not string and that's why we have to find the number of position in the string
print(range)