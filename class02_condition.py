#age = int(input("Enter your age:"))

#if (age > 20):
#    print("you Pass")
#elif (age > 18) :
 #   print("Bring parent")
#else:
  #  print("you didnt pass")



eps = int(input("กรุณากรอกระยะทาง :"))

if (eps < 50):
    print(eps,"ค่าบริการ 10 บาท")
elif (eps >= 51  and eps <= 100) :
    print(eps, "ค่าบริการ 15 บาท")
elif (eps >= 101  and eps <= 300) :
    print(eps, "ค่าบริการ 25 บาท")
elif (eps >= 301  and eps <= 500) :
    print(eps,"ค่าบริการ 35 บาท")
elif (eps >= 501) :
    print(eps,"ค่าบริการ 45 บาท")
else :
    print(eps,"ไม่มีบริการจัดส่ง")
