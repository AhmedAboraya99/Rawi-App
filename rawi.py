import pyttsx3
import PyPDF2
book = open('Technology-Trends.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
rate = speaker.getProperty('rate')
speaker.setProperty('rate',120)
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].languages)
for num in range(0, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()