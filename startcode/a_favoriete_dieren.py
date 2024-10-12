lijst= []
input_dier = ""
input_dier = input("Kies je 3 favoriete dieren, 1 per keer:")
for i in range(3):
    input_dier = input("dier " + str(i+1) + ":")
lijst.append(input_dier)
print(lijst)

