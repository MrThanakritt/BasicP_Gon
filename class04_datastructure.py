'''
x = ["A", "B"]

print(x)
#print(x(type))

x[0] = "C"

print(x[0])

x.append("D")

print(x)

x.pop()

print(x)





x = ["a","b","c","d","e"]

print(len(x))


for i in range(len(x)):
    print(x[i])


for speaker in x:
    print(speaker)



score = [99, 40, 30, 64, 52]
sum = 0

for i in range(len(score)):
    print(sum)
    sum += score[i]

    print("total : ",sum)


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in num:
   if (number % 2 == 0):
    print("Even : " , number) 
   else:
      print("Odd", number)



x = {
    "AA" : "BB",
     "DD" : "EE"
     }
print(x["AA"])

x["SSS"] = 100
x["AA"] = "ZZ"

print(x)
'''

students =  [
    {"name" : "T" , "id" : "1" , "score" : 90},
    {"name" : "A" , "id" : "2" , "score" : 85},
    {"name" : "G" , "id" : "3" , "score" : 60},
    {"name" : "B" , "id" : "4" , "score" : 50}
]

#print(students[0]["name"])

for student in students:
   if ("score" >= 90):
      print("Score : A",students["score"])
if("score" > 70):
      print("Score : B",students["score"])
elif("score" > 50):
    print("Score : C",students["score"])
else:
    print("Score : F",students["score"])

    print(students)