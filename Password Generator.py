#Ne yepacağınızı bilemem ancak proje yok :)


import random

lower = "abcçdefgğhıijklmnoöprsştuüvyz"
upper = lower.upper()
number = "123456789"
mark = "*!_"


total = lower + upper + number + mark

password = random.choices(total , k=10)
print(password)

password = ''.join(password)
print(password)
