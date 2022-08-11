Q1
class Myclass:
    def __init__(self):
        pass
    def removrchar(self):
        s = "i love pets"
        s2 = s.replace("o", "")
        print("string after removing",s2)
        print("string before removing",s)
obj=Myclass()
obj.removrchar()
Q2
min = int(input("Enter the min : "))
max = int(input("Enter the max : "))
for n in range(min,max + 1):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n)
  Q3
  sentence = 'you are my sunshine'
count = 0
for i in sentence:
    if i == "e":
        count = count + 1
print(count)
