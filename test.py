# 1
a = int(input('Write the num'))
print(a+a*2)

# 2
a = 46
b = "lol"
print(a * 5,b)

# 3
a = 5,"f","privet",90.2
b = 62
print(b,"privet")

# 4
num = str(input("give me a num"))
num = list(str(num))
print(num)

# 5
a = input("give me a name")
b = input("give me a surename")
z = input("give me a age")
print(" привет " + a,b + " тебе уже " + z + " лет ")


# 6
a = int(input("give a num"))
b = int(input("give a num"))
c = int(input("give a num"))
print( a + b + c)

# 7
a = 1
b = "1"
c = 1.1
print(int(a) + int(b) + int(c))

# 8
a = int(input('дайте мне первое целое число: '))
b = int(input('дайте мне второе целое число: '))
c = int(input('дайте мне третью целое число: '))
print(a+b+c)


# 9
a = input('write a pin: ')
b = input('write again: ')
if a == b:
    print("your pin was accepted")
else:
    print('you write incorrect pin')