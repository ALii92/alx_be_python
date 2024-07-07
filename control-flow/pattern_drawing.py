size = int(input("Enter the size of the pattern:"))
rows = size
while size > 0:
    for num in range(0,rows):
        print("*", end="")
    print()
    
    size -= 1