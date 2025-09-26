try:
    fileRead = open('Sample.txt', 'r')
    fileContent = fileRead.read()
    print(fileContent)
    fileRead.close()

except FileNotFoundError:
    print("Error: The file Sample.txt not found")

    