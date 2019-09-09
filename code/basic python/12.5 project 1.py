#Take user input of weight in pounds or KG. Then prompt if it's pounds or KGs. Then convert this to other format

weight = input("Weight: ")
p_k = input("(L)bs or [K]g")
conv=0

if p_k.upper()=='L':
    conv=float(weight)*0.45
elif p_k.upper()=='K':
    conv=float(weight)/0.45

print(f"Your weight {conv}")