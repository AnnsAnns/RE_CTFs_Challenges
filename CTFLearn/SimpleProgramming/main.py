file = open("data.dat")
lines = file.readlines()
total = 0

for line in lines:
    if line.count("0") % 3 == 0 or line.count("1") % 2 == 0:
        total += 1
        
print(total)