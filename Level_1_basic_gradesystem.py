percent=int(input("Eneter Your total Percentage: "))

if(percent>=90):
    print("Your Percentage is: ",percent)
    print("Your Grage is: A+")
elif(percent<90 and percent>=80):
    print("Your Percentage is: ",percent)
    print("Your Grage is: A")
elif(percent<80 and percent>=70):
    print("Your Percentage is: ",percent)
    print("Your Grage is: B+")
elif(percent<70 and percent>=60):
    print("Your Percentage is: ",percent)
    print("Your Grage is: B")
elif(percent<60):
    print("Your Percentage is: ",percent)
    print("Your Grage is: C")