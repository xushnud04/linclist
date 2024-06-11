import PyPDF2
from gtts import gTTS


"""def speak(audio):
    tts = gTTS(text=audio, lang='en')
    tts.save('audio.mp3')"""


def convert(pdf_path, audio_path):
    """with open(pdf_path, "rb") as audio_file:
        pdf = PyPDF2.PdfFileReader(audio_file)
        pages = pdf.getNumPages
        speak(pages)
        text = pdf.getPage(0).extractText()"""


tts = gTTS(text=" Hello jon", lang='en')
ts = gTTS(text="hello jon", lang='en')
ts.save("F:\\uy\\audio_1.mp3")

