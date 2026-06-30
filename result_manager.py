# project ; students result managment 
print("================================================")
print("===========STUDENTS RESULT MANAGMENT============")
print("================================================")

print("\n======= STUDENT INFORMATION ========")
name=input("*NAME->")
grade=int(input("*CLASS->"))
age=int(input("*AGE->"))

print ("\n========== STUDENT MARKS ========== ")
a=int(input("MATHEMATIS (1-20) :-"))
b=int(input("COMPUTER (1-20) :-"))
c=int(input("ENGLISH (1-20) :-"))
d=int(input("PHYYSICS (1-20) :-"))
e=int(input("CHEMISTRY (1-20) :-"))

print("====== STUDENT RESULT ======")
sum = a+b+c+d+e
print("\n MARKS OBTAINED =>",sum )
per = sum/100*100
print("\n percentage =>", per)
average = a+b+c+d+e/5
print("\n average =>", average)

if per > 90 :
    print("grade => A+")
    print("PASS")
elif per > 80 and per < 90 :
    print(" grade => A")
    print("PASS") 
elif per>70 and per < 80 :
    print("grade => B")
elif per>65 and per < 70 :
    print("grade => D")
    print("PASS")
else:
    print("FAIL")

print("====== STUDENT PROGRESS ======")
            
