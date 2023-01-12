a = int(input("enter yours marks:"))
if a > 0:
    if 25 >= a >= 0:
        print("GRADE:F")
    elif 25 <= a < 45:
        print("GRADE:E")
    elif 45 <= a < 50:
        print("GRADE:D")
    elif 50 <= a < 60:
        print("GRADE:C")
    elif 60 <= a < 80:
        print("GRADE:B")
    else:
        print("GRADE:A")
else:
    print("Negative marks not allowed")
