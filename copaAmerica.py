out = ""
s=""
out1 = ""
n = " "
cont = 0
s = input()

s=s.replace(" ", "")
n=s[0]
for i in s:
    if i == n:
        cont += 1
    else:
        out += str(cont)+" "
        out1 += n+" "
        cont = 1
        n = i
out += str(cont)+" "
out1 += n+" "
print(out1+"\n"+out)
print("no hay risa")