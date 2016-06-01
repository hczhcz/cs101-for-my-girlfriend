# coding = utf-8

# a = input('temperature?')
# print(a)
# print(int(a) + 273)

# a = input('number?\n')
# b = input('number?\n')
# print(int(a) + int(b))
# print(a + b)

'''
open = ctrl+o
save = ctrl+s
undo = ctrl+z
# = ctrl+/
multi-editing = ctrl+click

ls
cd some_dir
cd ..
cat some_file
less some_file
py.exe some_file.py
echo 'print(1+1)' | py.exe
echo -e 'print(1+1)\r\nhello' | tac
up/down/tab
'''

# print('hell' + 'o')
# print('hello'[2])
# print('hello'[4])
# print('hello'[:4])
# print('hello'[3:] + 'hello'[2])

# print(True)
# print(True or False and False) # and > or, print true
# print(1 + 0 * 0)

# if 1 > 0:
#     print('a')
# else:
#     print('b')

# a = input('')
# b = input('')
# if int(a) > int(b):
#     print(int(a) + 1)
# else:
#     pass # pass = a placeholder

# a = input('')
# b = input('')
# c = input('')
# if int(a) > int(b):
#     if int(a) > int(c):
#         print(a)
#     else:
#         print(c)
# else:
#     if int(b) > int(c):
#         print(b)
#     else:
#         print(c)

# a = input('')
# b = input('')
# c = input('')
# if int(a) > int(b):
#     b = a
# if int(b) > int(c):
#     c = b
# print(c)

# l = [1,3,2,4,6,4,6,8,8,5,3,6,8,9,5,3]
# s = 0
# biggest = -1
# for i in l:
#     s = s + i
#     if i > biggest:
#         biggest = i
# print(s)
# print(biggest)
# print(sum(l))
# print(max(l))

# s = 0
# for i in range(101):
#     s = s + i
# print(s)
# print(list(range(11)))

s = 0 - 21 + 50
t = 0
for x in range(-100, 101):
    y = x**2 - 21*x + 50
    if y <= s:
        s = y
        t = x
print(s)
print(t)

s = 0 - 21 + 50
t = []
for x in range(-100, 101):
    y = x**2 - 21*x + 50
    if y < s:
        s = y
        t = [x]
    elif y == s:
        t = t + [x]
print(s)
print(t)
