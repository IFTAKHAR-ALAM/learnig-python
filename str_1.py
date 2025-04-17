print("Hello Github World")

print("Hello World & Hello Github World ")

print("I am working with Inurance. \n but I am intersted in IT")

str = ("My name is iftikhat.\n I am working Insurance")

print("My name is IFTIKHAR" + "and I am working with Insurance")

int("20")
x = int(input("Enter your val:" ))

print(type(x), x ) 


name = input("Enter your name:" )
print("Welcoe" , name )


x = "M IFTIKHAR ALAM and working with Insurance"
ch = x
ch = x[4]
print(ch)

x = "M IFTIKHAR ALAM"
print(x[ 2:5 ])

x = "NUSRAT IFTIKHAR"
print(x[ 0:9 ])

x = "ARSAL IFTIKHAR"
print(x[ -1:-5] )

x = "M IFTIKHARALAM"
print(x.endswith("ALAM"))

x = "M IFTIKHAR ALAM"
print(x.endswith("IFT"))

x = "m IFTIKHAR ALAM"
x = (x.capitalize())
print(x)

x = (x.capitalize())
print(x)

x = "M IFTIKHAR ALAM"
print(x.replace("I", "A"))

x = "M IFTIKHAR ALAM"
print(x.replace("ALAM", "AHMED"))

x = "m IFTIKHAR ALAM"
x = (x.upper())
print(x)

x = "M IFTIKHAR ALAM"
print(x.lower())
print(x)

x = "M IFTIKHAR ALAM"
print(x.find("IFT"))

x = "I am M IFTIKHAR ALAM fron Karachi but you are fron Lahore"
print(x.find("from"))

x = "NUSRAT IFRIKHAR"
print(x.count("I"))


year = 2025
month = 1
print(calendar.month(year, month))

year = 2025
month = 2
print(calendar.month(year, month))

yy = 2024
mm = 2
print(calendar.month(yy, mm))


# CONDITIONA L STATEMENTS

age =23

if(age >= 18): 
    print("You are eligible to NIC")
else:
    print("You are not eligible to NIC")
    
    age = 22
    
    if (age >= 18):
        print("You are eligible to drive a car")
    else:
        print("You are not eligible to drive a car")  
        
age = 5    

if("age >= 18"):
    print("You are eligible to admission nursery")
else:
    print("You are not eligible to admission nursery")    
    
    
    marks = 75
    
if(marks >= 90):
    print("Grade A")
elif(marks >= 80):   
    print("Grade B") 
elif(marks >= 70):    
    print("Grade C")
elif(marks >= 60):    
    print("Grade D")
elif(marks >= 50):    
    print("Grade E")
    
    
    marks =int(input("Enter your marks: "))
    marks = 75
    
    if(marks >= 90):
        Grade = "A"
    elif(maiks >= 90):
        Grade = "A"
    elif(marks >= 80 and marks < 90):
        Grade = "B"
    elif(marks >= 70 and marks < 80):
        Grade = "C"
    else:    
        Grade = "D"
    ptint("Grade of the student -> ", Grade)  
    
    
    marks1 = 90.1
    marks2 = 80.1
    marks3 = 70.1  
    marks4 = 60.1
    marks5 = 50.1
    # marks = (marks1 + marks2 + marks3 + marks4 + marks5) / 5
    
    marks = [80.1, 90.1, 70.1, 60.1, 50.1]
    print(marks)
    print(marks[0])
    print(marks[1])
    print(marks[2])
    print(marks[3])
    priny(type(marks))
    print(len(marks))
    
    student = ["IFTIKHAR", 90.6, 40, "Karachi, Pakistan"] 
    print(student)
    student[0] = "ARSAL IFTIKHAR"
    print(student)
    
    marks = [80.1, 90.1, 70.1, 60.1, 50.1]
    print(marks[1:3])
    print(marks[0:4])
    print(marks[0:5])
    print(marks[ :5])
    print(marks[ :4])
    print(marks[ 2: ])
    print(marks[-3:-1 ])
    print(marks[-4:-1])
    print(marks[-5:-2 ])
    
    list =  ["IFTIKHAR", "ARSAL", "Karachi, Pakistan"]
    print(list)
    print(list.append("Pakistan"))
    print(list.reverse())
    print(list.sort())
    print(list)
    
    list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list.append(11)
    list.insert(0, 12)
    print(list.sort())
    list.remove()
    print(list)
    
    list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list.remove(1)
    list.pop(4)
    print(list)
    
    tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(type(tup))
    
    
    tup = ()
    print(tup)
    print(type(tup))
    
    tup = (1,)
    print(tup)
    print(type(tup))
    
    tup = (1)
    print(tup)
    print(type(tup))
    
    tup = (2.0)
    print(tup)
    print(type(tup))
    
    tup = "IFTIKHAR"
    print(tup)
    print(type(tup))
    
    tup = ("IFTIKHAR", )
    tup = (2.0)
    print(tup)
    print(type(tup))
    
    
    tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(tup.index(1))
    print(tup.index(2))
    print(tup.index(3))
    print(tup.index(4))
    print(tup.count(2))
    print(tup.count(3))
    print(tup.count(4))
          
    
    
    
    
    
    
    
    
        