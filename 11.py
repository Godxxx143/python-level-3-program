print("takshashila university")
print   ("ongur,tindivanam")
print("----------------------")
print("stunent mark list")
print("----------------------")
pm = int(input("Enter the python mark: "))
dm = int(input("Enter the DBMS mark : "))
im = int(input("Enter the Industry mark : "))
total = pm + dm + im
average = total/3
if average >= 100:
    grade = "O"
elif average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
elif average >= 40:
    grade = "E"
else:
    grade = "F"
result = "pass" if average >= 40 else "fail"
print("Total mark:", total)
print("average mark :", int(average)) 
print("result:", result)
print("Grade :", grade)
