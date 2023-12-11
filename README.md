# PDF_text_reader


This is the code for reading the texts that are written in a PDF file.
It may (less chances) give errors for non-ASCII characters.


Follow the steps to run on your windows PC-
1. open CLI
2. RUN pip install PyPDF2
3. Make a PDF or use an already existing one and copy the file location using properties.
4. Open the PDF file in binary mode for reading
5. Visit the official espeak repository on GitHub: [espeak-ng GitHub Releases](https://github.com/espeak-ng/espeak-ng/releases).
   Look for the latest release and download the installer for Windows (usually a file with a .exe extension).
6. Add espeak to your system PATH (optional but recommended)



This was it all.
Below is the line by line explanation of code-


**Import Modules:**
Import the necessary modules, PyPDF2 for working with PDF files and pyttsx3 for text-to-speech functionality.


**Open PDF File:**
Open a PDF file in binary mode for reading using the open function. The file path is specified as an argument.


**Create PdfReader Object:**
Create a PdfReader object from the opened PDF file. This object allows you to read the contents of the PDF.


**Initialize Empty String:**
Initialize an empty string myText to store the extracted text from the PDF.


**Iterate Through PDF Pages:**
Use a loop to iterate through each page of the PDF.
Get the pageObj representing the current page.


**Extract Text:**
Extract text from the current page using the extract_text method of the pageObj.
Append the extracted text to the myText string.


**Close PDF File:**
Close the PDF file using the close method to free up system resources.


**Initialize Text-to-Speech Engine:**
Initialize the pyttsx3 text-to-speech engine.


**Set Speech Rate and Voice:**
Set the speech rate (words per minute) using setProperty.
Set the voice for speech synthesis (in this case, an English male voice).

**Text-to-Speech:**
Use the text-to-speech engine to speak the contents of the myText string.

**Wait for Speech to Finish:**
Use runAndWait to wait until the speech is finished before proceeding.
