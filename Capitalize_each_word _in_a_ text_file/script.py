totContent = ""
print(end="Enter the Name of File: ")
fileName = str(input())

try:
    fileHandle = open(fileName, "r")
    for content in fileHandle:
        newContent = content.title()
        totContent = totContent + newContent
    fileHandle.close()
	
    try:
        fileHandle = open(fileName, "w")
        fileHandle.write(totContent)
        print("\nAll Words in \"" + fileName + "\" Capitalized Successfully!")
        print(end="\nWant to see the Content of File (y/n): ")
        ch = input()
        if ch=='y':
            fileHandle = open(fileName, "r")
            for content in fileHandle:
                print(end=content)
        else:
            print("Exiting...")
        fileHandle.close()
        print()
    except IOError:
        print("Error Occurred!")
		
except IOError:
    print("\nThe \"" + fileName + "\" is not Exist!")
    print("Exiting...")
