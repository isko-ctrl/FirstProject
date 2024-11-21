x = 10
while True:
    san = int(input("sandy engiz: "))
    if san == x:
        print("Sen taptyn!")
        break
    elif san > x:
        print("Engizilgen san ulken")
    elif san < x:
        print("Engizilgen san kishi")
    else:
        print("Durys emes, kaitadan engiz")
x = 50
while True:
    ban = int(input("sandy engiz: "))
    if ban == x:
        break
    elif ban > x:
        print("Engizilgen san ulken")
    elif ban < x:
        print("Engizilgen san kishi")
    else:
        print("Durys emes, kaitadan engiz")