# region while-else
# WHILE döngüsü BREAK satırı ÇALIŞARAK biterse, else içerisine GİRMEZ
# WHILE döngüsü BREAK satırı ÇALIŞMADAN biterse, else içerisine GİRER
"""
i = 1
while i <= 10:
    print(i, end=" ")
    if i == 2:
        break
    i += 1
else:
    print("şu an else içerisine girdim")
print("while döngüsü bitti")"""


"""
for i in range(10, 1, -1):
    print(i, end=" ")
    if i == 9:
        break
else:
    print("şu an for elsedeyim")

    """