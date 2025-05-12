# Assignment4
Project: File Handling in Python (Read & Write with Exception Handling)
This project demonstrates the use of file handling in Python with a focus on safe practices like exception handling, clean formatting, and input processing. It includes two main functionalities:

File Reading from sample.txt
This part of the project attempts to open and read a file named sample.txt. If the file is not found or an I/O error occurs, appropriate error messages are displayed. It is useful for reading and displaying the contents of a text file while ensuring the program doesn’t crash due to common file-related issues.

Writing and Reading with output.txt
The second part of the project allows the user to input multiple lines of text, which are appended to a file named output.txt. After the input, the program reads and displays the entire content of the file in a clean, line-by-line format.

During the input phase, the script uses a loop to collect text from the user multiple times. Specifically, the line that controls this loop runs the input process three times. The use of a placeholder variable (_) in the loop signifies that the loop index is not needed, and only the number of repetitions matters.

Each input is cleaned to ensure extra spaces are removed, making the data more readable. The file is safely opened and managed using Python’s context manager, and all errors (like file not found or write failures) are gracefully handled.

Key Features
File Handling Modes: Demonstrates reading, appending, and updating files.

Exception Handling: Catches common file errors to prevent crashes.

Input Cleaning: Ensures consistent formatting by removing unnecessary spaces.

Efficient File Access: Uses file pointer control to re-read the file after writing.

Repetitive Input: Accepts three lines of user input using a loop for multiple entries.

User Interaction: Collects and displays user-generated content with formatting.
