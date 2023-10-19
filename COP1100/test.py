'''
#1

result = 0
for n in range(5):
    result = n - 3
    if (result % 2) != 0:
        print('-', end=' ')
        continue
    print(result, end=' ')
print('done')

#2

a = int(input())
b = int(input())
c = int(input())
result = 0
while a < b:
    result = a * 2
    print(result)
    if result > c:
        break
    a += 3

#3

stop = int(input())
result = 0
for a in range(3):
    for b in range(5):
        result += a * b
    print(result)
    if result > stop:
        break


stop = int(input())
result = 0
for a in range(3):
    print(a, end=': ')
    for b in range(2):
        result += a + b
        if result > stop:
            print('-', end=' ')
            continue
        print(result, end=' ')
    print()

user_score = 0
simon_pattern = input()
user_pattern  = input()

for i in simon_pattern:
   if user_pattern[user_score] == simon_pattern[user_score]:
      user_score += 1
   else:
      break
  
print(f'User score: {user_score}')

'''


numbers = [3, -10, 5, 0, -9]
for position, number in enumerate(numbers):
    if number < 0:
        print(f'{position} {number}')
    else:
        print(f'{position} x')