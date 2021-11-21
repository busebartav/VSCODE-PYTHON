#region ornek_1
"""
a=input("Metni giriniz=")
i=int(input("Kaç kere tekrar etmesini istediğinizi giriniz="))
x=0
while x < i:
    print(a)
    x+=1 
"""


#region ornek_2 * * * * * * * * * *
"""
i=1
while i<=10:
    i+=1
    print("*", end=" ")
 """

#region ornek_3 * $ * $ * $ * $ * $
"""
i=0
while i<10:
    i+=1
    if i%2==0:
        print("$", end=" ")
    else:
        print("*", end=" ")

"""

#region ornek_4 

i = 0
j = 0
while i<10:
    while j<10:
        print("hayat çk zor", end=" ")
        j+=1
    i+=1
    j=0
    print()