# BookBot

🤖 BookBot is a Python-based command-line tool that performs a deep dive into your favorite literary classics. It parses text files to generate a comprehensive report on word density and character frequency.

📊 Features
Total Word Count: Quickly calculate the total number of words in any .txt document.

Character Analysis: Breaks down the frequency of every character found in the text.

Sorted Reporting: Automatically sorts character data by frequency (most common to least common) for easy analysis.

🚀 How to Run
BookBot uses command-line arguments to locate your books.

1. Prerequisites
Ensure you have Python 3.10+ installed on your system.

2. Execution
Run the script by passing the path to your text file as an argument:

Bash
python3 main.py books/frankenstein.txt
📂 Project Structure
main.py: The entry point that handles user input and coordinates the analysis report.

stats.py: The "brains" of the operation containing the logic for splitting strings and counting characters.

books/: A directory for storing your .txt files (e.g., Frankenstein, The Time Machine, etc.).

📝 Example Output
When you run BookBot, you'll get a clean report printed straight to your terminal:

Plaintext
=========== BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75918 total words
--------- Character Count -------
e: 46043
t: 30365
a: 26743
i: 24613
...
---------------------------------
💡 Technical Highlights
The logic in stats.py ensures that:

All text is converted to lowercase to prevent duplicate counts for capital letters.

Data is transformed into a list of dictionaries to allow for custom sorting using Python’s .sort() method and a helper key function.