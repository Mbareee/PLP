
with open("my_file.txt", "w") as file:
    file.write("Hello, everybbody.\n")
    file.write("1232423\n" )
    file.write("Final line here, with a mix of characters and numbers: a1b2c3\n")



with open("my_file.txt","a")as file_app:
    file_app.write("What it do what it do\n")
    file_app.write("My names Borat\n")
    file_app.write("aaahh help I'm in the void")

def read_contents():
    try:
        file2 = open("my_files.txt","r")
        contents = file2.read()
       
    except FileNotFoundError:
        return "The file is not available. Please try again."
    
    else:
        return print(contents)
    finally:
        if 'file2' in locals():
            file2.close()     

read_contents()








    





