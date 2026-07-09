s = input()
ans = []
for ch in s:
    if(ch == "A"):
        ans.append("Z")
    elif(ch == "B"):
        ans.append("Y")
    elif(ch == "C"):
        ans.append("X")
    elif(ch == "D"):
        ans.append("W")
    elif(ch == "E"):
        ans.append("V")
    elif(ch == "F"):
        ans.append("U")
    elif(ch == "G"):
        ans.append("T")
    elif(ch == "H"):
        ans.append("S")
    elif(ch == "I"):
        ans.append("R")
    elif(ch == "J"):
        ans.append("Q")
    elif(ch == "K"):
        ans.append("P")
    elif(ch == "L"):
        ans.append("O")
    elif(ch == "M"):
        ans.append("N")
    elif(ch == "N"):
        ans.append("M")
    elif(ch == "O"):
        ans.append("L")
    elif(ch == "P"):
        ans.append("K")
    elif(ch == "Q"):
        ans.append("J")
    elif(ch == "R"):
        ans.append("I")
    elif(ch == "S"):
        ans.append("H")
    elif(ch == "T"):
        ans.append("G")
    elif(ch == "U"):
        ans.append("F")
    elif(ch == "V"):
        ans.append("E")
    elif(ch == "W"):
        ans.append("D")
    elif(ch == "X"):
        ans.append("C")
    elif(ch == "Y"):
        ans.append("B")
    elif(ch == "Z"):
        ans.append("A")
    else:
        ans.append(ch)
res = ["".join(ans)]
for c in res:
    print(c,end="")