def add(num1, num2):
    result = num1 + num2
    return result

def meinus(num1, num2):
    result = num1 - num2
    return result
     
def mutiple(num1, num2):
    result = num1 * num2
    return result

def divide(num1, num2):
    result = num1 / num2
    return result

def is_even(num):
    result = num % 2
    return result

num1 = 1
num2 = 2


def main():
    num1 = int(input("กรอกข้อมูลตัวที่ 1"))
    num2 =  int(input("กรอกข้อมูลตัวที่ 2"))
    print("---?---")
    print(" [1] ")
    print(" [2] ")
    print(" [3] ")
    print(" [4] ")
    print(" [5] ")

operation = input("เลือกสักอัน")

if (operation == 1):
        result = add(num1, num2)
        print("ผลบวกคือ" ,result)
elif (operation == 2):
        result = meinus(num1, num2)
        print = ("ผลลบคือ ",result)

elif (operation == 3):
        result = mutiple(num1, num2)
        print = ("ผลคูณคือ ",result)

elif (operation == 4):
        result = divide(num1, num2)
        print = ("ผลหารคือ ",result)

elif (operation == 5):
        result = is_even(num1, num2)
        print = ("ผลคือ ",result)
    
        print(is_even(result))

main()