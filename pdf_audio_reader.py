# Import the PyPDF2 module for working with PDF files
import PyPDF2

# Import the pyttsx3 module for text-to-speech functionality
import pyttsx3

# Open a PDF file in binary mode for reading
pdfFileObj = open(r"C:\Users\Lenovo\Desktop\Sample.pdf", "rb")

# Create a PdfReader object to read the PDF file
pdfReader = PyPDF2.PdfReader(pdfFileObj)

# Initialize an empty string to store extracted text
myText = ""

# Iterate through each page of the PDF
for page_num in range(len(pdfReader.pages)):
    # Get the page object for the current page
    pageObj = pdfReader.pages[page_num]

    # Extract text from the page and append it to the myText string
    myText += pageObj.extract_text()

# Close the PDF file
pdfFileObj.close()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the speech rate (words per minute)
engine.setProperty('rate', 175)

# Set the voice for speech synthesis (in this case, English male voice)
engine.setProperty('voice', 'en+m5')

# Use the text-to-speech engine to speak the extracted text
engine.say(myText)

# Wait for the speech to finish
engine.runAndWait()