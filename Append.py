try:
    with open('output.txt', 'a+') as file1:
        for _ in range(3):
            user_input = input("Enter text to append to the file: ")
            clean_input = ' '.join(user_input.strip().split())
            file1.write('\n' + clean_input)
        file1.seek(0)
        print("\nFile content:")
        for line in file1:
            formatted_line = ' '.join(line.strip().split())
            print(formatted_line)
except FileNotFoundError:
    print("Error: The file was not found.")
except IOError:
    print("Error: An I/O error occurred while working with the file.")
