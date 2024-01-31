try:
    with open('"D:\python\Demo\example.txt.txt"') as file:
        print(file.read())
except:
    print("file not found :(")
    
