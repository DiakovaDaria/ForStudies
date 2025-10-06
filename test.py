print ('This is a simple test! Lets test your knowledge')
print()

res1 = False
res2 = False
res3 = False

print('Question one: what language are we studing?')
ans1 = input(str('Your answer: '))
if ans1 == 'Python':
    res1 = True
print(res1)
print()

print('Question two: Who is the creator of Python?')
print('Choose the correct option and type the letter of the answer')
print('a - Guido van Rossum')
print('b - Niklaus Emil Wirth')
print('c - Brendan Eich')
ans2 = input(str('Your answer: '))
if ans2 == 'a':
    res2 = True
print(res2)
print()

print('Question three: how many on the following types are basic ones?')
print('String, lists, sets, dictionaries, booleans')
ans3 = input(int('Your answer: '))
if ans3 == '2':
    res3 = True
print(res3)
print()

print ('Test is completed! Number of correct answers: ', res1+res2+res3)
