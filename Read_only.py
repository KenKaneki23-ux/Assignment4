try:
  with open('sample.txt','r') as file1:
    reading_file = file1.read()
    print(reading_file)

except FileNotFoundError:
    print("Error: The file sample.txt was not found.")
except IOError:
  print("Error: An I/O error occurred while working with the file.")