# 2.	Perform Following on Python Shell Window
print(5 ** 9)

print(5 // 2)

print(7 // 3)

print(7 / 3)

print(6 == 6)

a = 20
a += 30
a %= 3
print(a)

print(True * False)
print(True & False)
print(True and False)
print(((6 > 3) and (7 < 4) or (18 == 3)) and (9 > 3))
print(True is False)
# print(False in 'False')  # IT WILL GIVE ERROR SO COMMENTED
print(((True == False) or (False > True) and (False <= True)))
# ==============================================================================================================

# 3) Try to get following output from two python strings s1 = “Nice to have it”   s2= “here”

s1 = "Nice to have it"
s2 = "here"
p = print(s1 + ' ' + s2)
# =============================================================================================================

# 4) Given this nested list, use indexing to grab the word "hello"
a = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]

# print(len(a))

print(a[-3][-3][-1][0])
# =================================================================================================================

#  5): Try to insert above strings s1 and s2 in the list ‘a’ mentioned in
#  que 4, in the beginning and end of it respectively
s1 = "Nice to have it"
s2 = "here"
a = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]  # Given list
a.insert(0, s1)
a.append(s2)
print(a)
# =================================================================================================================

# 6) Write a Python program to print out a set containing all the colours
# from color_list_1 which are not present in color_list_2. Test Data:
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output:
# {'Black', 'White'}


color_list_1 = {"White", "Black", "Red"}
color_list_2 = {"Red", "Green"}

print(color_list_1 - color_list_2)

# ================================================================================================================

# Pangram

inp = str(input('Enter a string: '))
s_inp = set(inp.lower())  # it will give unique values in lower case

s_alphabets = 'abcdefghijklmnopqrstuvwxyz'

if len(s_inp) >= len(s_alphabets):
    print('String is pangram')
else:
    print('String is not pangram')

# 8. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

""".format ::: It is mathod of string which passes the input to the string"""
# Mathod 1
i = int(input("Enter a no:"))
n = (i + ((i * 10) + i) + ((i * 100) + (i * 10) + i))
print(n)
#########################################################################################
# #Mathod 2
#
# n = int(input("Enter a no:"))
# e = eval('{0}+{0}{0}+{0}{0}{0}'.format(n))
# print(e)

######################################################################################
# Mathod 3
# n = eval('{0}+{0}{0}+{0}{0}{0}'.format(input("Enter a no:")))
# print(n)

######################################################################################################
# 9) Write a program that accepts a comma separated sequence of words
# as input and prints the words in a comma-separated sequence after
# sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

seq = input("Enter a string: ")
seq = sorted(seq.split(","))
print(",".join(seq))


######################################################################################################


# 10) Write a Python function to find the name of person obtained
# highest marks in exam from given dictionary
# Example dictionary
# d = {‘Student’: [‘Rahul’, ‘Kishore’, ‘Vidhya’, ‘Raakhi’],
# ‘Marks’: [57,87,67,79]}
# Output: Kishore


def dict(n):
    print('name of student who got high mark is:', d['student'][m])
    return


d = {'student': ['Rahul', 'Kishore', 'Vidya', 'Raakhi'], 'marks': [57, 87, 67, 79]}
print('Marks of student are', d['marks'])
v = max(d['marks'])
m = d['marks'].index(v)

dict(m)
