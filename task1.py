def file_operations():
    filename = input("Enter the filename: ")
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\nFile content:")
            print(content)
    except FileNotFoundError:
        with open(filename, 'w') as file:
            file.write("File is opened in write mode")
        print("File is opened in write mode")

file_operations()