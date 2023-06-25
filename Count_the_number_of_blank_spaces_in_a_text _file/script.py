file = open("myfile.txt", "r")
  
count = 0
while True:
    
    # this will read each character
    # and store in char
    char = file.read(1)
      
    if char.isspace():
        count += 1
    if not char:
        break
  
print(count)
