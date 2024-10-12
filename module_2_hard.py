def get_password (n):
    pairs = []
    for i in range(1, 21):
        for j in range(i + 1, 21):
            if n % (i + j) == 0:
                pairs.append(f"{i}{j}")

    result = ''.join(pairs)
    return result

n1 = 9
n2 = 11

result1 = get_password(n1)
result2 = get_password(n2)

print(f"{n1} - {result1}")
print(f"{n2} - {result2}")

for n in range(3, 21):
    print(f"{n} - {get_password(n)}")


def password(n):
    pass_ = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                pass_ += str(i) + str(j)
    return pass_

print('Введите число: ')
print(password(int(input())))


Все пароли для чисел от 3 до 20 (для сверки):
# 3 - 12
# 4 - 13
# 5 - 1423
# 6 - 121524
# 7 - 162534
# 8 - 13172635
# 9 - 1218273645
# 10 - 141923283746
# 11 - 11029384756
# 12 - 12131511124210394857
# 13 - 112211310495867
# 14 - 1611325212343114105968
# 15 - 1214114232133124115106978
# 16 - 1317115262143531341251161079
# 17 - 11621531441351261171089
# 18 - 12151811724272163631545414513612711810
# 19 - 118217316415514613712811910
# 20 - 13141911923282183731746416515614713812911