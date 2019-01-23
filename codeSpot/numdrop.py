
# Ask user for input number
print("Gimmie a number")
height = int(input("Number: "))

# Accept user input up to a point...
while (height < 0 or height > 10):
    height = int(input("Number: "))

for i in range(height):
    print("" *(height - (i + 1)) + '#' * (i + 2) )