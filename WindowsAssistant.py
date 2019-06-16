import speech_recognition as speech
from googlesearch import search
import pyttsx3
import webbrowser
import os
def textToSpeech():
	engine=pyttsx3.init()
	voices=engine.getProperty('voices')
	engine.setProperty('voice',voices[1].id)
	volume=engine.getProperty('volume')
	engine.setProperty('volume',10.0)
	rate=engine.getProperty('rate')
	engine.setProperty('rate',rate-25)
	return engine
def openApp():
	engine=textToSpeech()
	r= speech.Recognizer()
	with speech.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		engine.say("Which application to run? ")
		engine.runAndWait()
		audio= r.listen(source)
	try:
	
		text=r.recognize_google(audio)
		print(text)
		if text == "Notepad plus plus" or text == "notepad plus plus" or text == "notepad++" or text=="Notepad++":
			os.system('start Notepad++.exe')
		elif text=="Chalsea" or text== "Calculator" or text=="calculator" or text=="calc":
			os.system('start calc.exe')
		elif text== "outlook" or text=="Outlook":
			os.system("start outlook.exe")
		else:
			os.system('start {}.exe" '.format(text))
		
		
	except Exception as e:
		engine.say("sorry could not hear you")
		engine.runAndWait()
def search():
	engine=textToSpeech()
	r= speech.Recognizer()
	with speech.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		engine.say("Please say what you wanna search for? ")
		engine.runAndWait()
		audio= r.listen(source)
		try:
			text=r.recognize_google(audio)
			print("Searching for : {}".format(text))
			engine.say("Searching for {0} in default browser".format(text))
			engine.runAndWait()
			#results=search(text, tld="co.in",stop=10,pause=2)
			"""for row in results:
				print(row)
				engine.say(row)
				engine.runAndWait()
			
			
			print("ok")
			"""
			chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
			webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
			webbrowser.get('chrome').open("https://www.google.com/search?q={}".format(text))
			
			#webbrowser.open_new(text)
		
		except Exception as e:
			engine.say("sorry could not hear you")
			engine.runAndWait()
			
def main():
	engine=textToSpeech()
	r= speech.Recognizer()
	with speech.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		engine.say("Please say open to run application or search to search online")
		engine.runAndWait()
		audio= r.listen(source)
	try:
		text=r.recognize_google(audio)
		if (text=="open"):
			print("open")
			openApp()
		else:
			search()
	except Exception as e:
		engine.say("sorry could not hear you")
		engine.runAndWait()


if __name__=='__main__':
	main()