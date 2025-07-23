# for i in range(5) :
#    print("H")

# for i in range(5) :
#    print("H")

'''
for i in range(10) :
    if(i % 2) == 0:
        print("")
'''

'''

num1 = int(input(""))

for i in range(12) :
    print(num1,(i+1,num1*(i+1))) 

'''


''' 
start = True
while start :
    print("เลือกข้อที่ต้องการเล่น")
    print("ข้อที่ [1] โจทย์แรก")
    print("ข้อที่ [2] โจทย์สอง")
    x = int(input("กรุณากรอกเลข : "))
    if (x == 1):
        print("")
    elif(x == 2):
        print("")
    else :
        print("")

'''

monster = 110
weapon1 = 50
weapon2 = 45
weapon3 = 10

game_start = True

while game_start :
    print("WELCOME")
    print("-----<>-----")
    print("เลือกข้อที่ต้องการเล่น")
    print("ข้อที่ [1] เล่น")
    print("ข้อที่ [2] ไม่เล่น")
    option = int(input("1 or 2"))
    if (option == 1) :
        attack_m = int(input("How many Attack"))
        for i in range(attack_m):
            print("เลือด = " ,monster)
            print("อาวุธชนิดที่ 1 Damage :",weapon1)
            print("อาวุธชนิดที่ 2 Damage :",weapon2)
            print("อาวุธชนิดที่ 3 Damage :",weapon3)
            
            print("Monster health")
            print("เหลือโอกาสตีอยู่", i - 1)
            weapon = int(input(""))
            print("",weapon)
            if (weapon == 1) :
                print()
    else :
        print("Bye Bye")
        break
    