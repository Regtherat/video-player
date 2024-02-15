import pywhatkit
import tkinter as tk

print("hi put the link of the video you want to play here if you want to stop watching videos just say stop")
videolink =  input()

pywhatkit.playonyt(videolink)

print("would you like to watch another video? if so put the link here if you want to watching just say ")

another = input()


pywhatkit.playonyt(another)


     
