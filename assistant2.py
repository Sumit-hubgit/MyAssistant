import speech_recognition as sr
import pyttsx3
import pyaudio#with pyaudio  we can eaily use python2 play and record audio 
import pywhatkit
import datetime
import wikipedia
from playsound import playsound
import datetime
import requests
from search_web import *
from bs4 import BeautifulSoup
from tkinter import *

#recognises your voice(recording) (creating instance)

listener=sr.Recognizer()

#initialization of pyttsx3(setup)

engine=pyttsx3.init()

#get all the voices available.

voices=engine.getProperty("voices")

#selected 2ns voice out of all the voice present.

engine.setProperty("voice",voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
talk("how may i help you sir")

def take_command():    
    try:
        with sr.Microphone() as source:   #using Microphone as a source for input.
            print("listening you.....")
            voice=listener.listen(source) #calling speech Recognizer() to listen to source.
            command=listener.recognize_google(voice) #converts ourvoice to text.
            command=command.lower() #converting command to lower case.
            if 'python' in command:
                command=command.replace('python','')
            if 'hey' in command:
                command.replace('hey','')
            print(command)
    except:
        pass
    return command
def run_alexa():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif ('write' or 'right')in command:
        print("please speak")
        talk("please speak, sir!")
        print(command)
    elif "time" in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk("current time is: "+time)
    elif 'who is'in command:
        person=command.replace('who is','')
        info=wikipedia.summary(person,10)
        print(info)
        talk(info)
    elif 'alarm' in command:
        talk("Enter the  time sir")
        alarmHour=int(input("Enter Hour: "))
        alarmMin=int(input("Enter Minutes: "))
        alarmAm=input("am/pm")
        talk(f"setting alarm of,{alarmHour}")
        if alarmAm=="pm":
            alarmHour+=12
        while True:
            if(alarmHour==datetime.datetime.now().hour and alarmMin==datetime.datetime.now().minute):
                print("playing: ")
                playsound("C:\\Python310\\jarvis.mp3")
                talk("wake up sir")
                break
    elif 'whatsapp' in command:
            talk("opening whatsapp")
            pywhatkit.sendwhatmsg("+916307628236","hello",11,8)
    elif 'who are you' in command:
        talk("hello sir i am python a backend program and a smart assistant , who can do various predefined tasks on your single command . I am designed by mister sumit") 

    elif 'temprature' in command:
        search="temprature in delhi"
        url=f"https://www.google.com/search?q={search}"
        r=request.get(url)#The requests module allows you to send HTTP requests using Python.
        data=BeautifulSoup(r.text,"html.parser")#beautifulsoup:-taking only text form of data by parsing.
        tem=data.find("div",class_="BNeawe").text
        talk(f"current {search} is {temp}")
            








































































    elif 'calculator' in command:
            def press(num):
                # point out the global expression variable
                #global expression
                # concatenation of string
                expression = expression + str(num)

                # update the expression by using set method
                equation.set(expression)
                # Function to evaluate the final expression                
            def equalpress():
            # Try and except statement is used
            # for handling the errors like zero
            # division error etc.

            # Put that code inside the try block
            # which may generate the error
                try:
                    global expression

                    # eval function evaluate the expression
                    # and str function convert the result
                    # into string
                    total = str(eval(expression))

                    equation.set(total)

                    # initialize the expression variable
                    # by empty string
                    expression = ""

	# if error is generate then handle
	# by the except block
                except:
                    equation.set(" error ")
                    expression = ""
    # Function to clear the contents
    # of text entry box
            def clear():
                global expression
                expression = ""
                equation.set("")


    # Driver code
            if __name__ == "__main__":
                # create a GUI window
                gui = Tk()

                # set the background colour of GUI window
                gui.configure(background="light green")
    
                # set the title of GUI window
                gui.title("Simple Calculator")

                # set the configuration of GUI window
                gui.geometry("270x150")

                # StringVar() is the variable class
                # we create an instance of this class
                equation = StringVar()

                # create the text entry box for
                # showing the expression .
                expression_field = Entry(gui, textvariable=equation)

                # grid method is used for placing
                # the widgets at respective positions
                # in table like structure .
                expression_field.grid(columnspan=4, ipadx=70)

                # create a Buttons and place at a particular
                # location inside the root window .
                # when user press the button, the command or
                # function affiliated to that button is executed .
                button1 = Button(gui, text=' 1 ', fg='black', bg='red',
                                                command=lambda: press(1), height=1, width=7)
                button1.grid(row=2, column=0)

                button2 = Button(gui, text=' 2 ', fg='black', bg='red',
                                                command=lambda: press(2), height=1, width=7)
                button2.grid(row=2, column=1)

                button3 = Button(gui, text=' 3 ', fg='black', bg='red',
                                                command=lambda: press(3), height=1, width=7)
                button3.grid(row=2, column=2)

                button4 = Button(gui, text=' 4 ', fg='black', bg='red',
                                                command=lambda: press(4), height=1, width=7)
                button4.grid(row=3, column=0)

                button5 = Button(gui, text=' 5 ', fg='black', bg='red',
                                                command=lambda: press(5), height=1, width=7)
                button5.grid(row=3, column=1)

                button6 = Button(gui, text=' 6 ', fg='black', bg='red',
                                                command=lambda: press(6), height=1, width=7)
                button6.grid(row=3, column=2)

                button7 = Button(gui, text=' 7 ', fg='black', bg='red',
                                                command=lambda: press(7), height=1, width=7)
                button7.grid(row=4, column=0)

                button8 = Button(gui, text=' 8 ', fg='black', bg='red',
                                                command=lambda: press(8), height=1, width=7)
                button8.grid(row=4, column=1)

                button9 = Button(gui, text=' 9 ', fg='black', bg='red',
                                                command=lambda: press(9), height=1, width=7)
                button9.grid(row=4, column=2)

                button0 = Button(gui, text=' 0 ', fg='black', bg='red',
                                                command=lambda: press(0), height=1, width=7)
                button0.grid(row=5, column=0)

                plus = Button(gui, text=' + ', fg='black', bg='red',
                                        command=lambda: press("+"), height=1, width=7)
                plus.grid(row=2, column=3)

                minus = Button(gui, text=' - ', fg='black', bg='red',
                                        command=lambda: press("-"), height=1, width=7)
                minus.grid(row=3, column=3)

                multiply = Button(gui, text=' * ', fg='black', bg='red',
                                                command=lambda: press("*"), height=1, width=7)
                multiply.grid(row=4, column=3)

                divide = Button(gui, text=' / ', fg='black', bg='red',
                                                command=lambda: press("/"), height=1, width=7)
                divide.grid(row=5, column=3)

                equal = Button(gui, text=' = ', fg='black', bg='red',
                                        command=equalpress, height=1, width=7)
                equal.grid(row=5, column=2)

                clear = Button(gui, text='Clear', fg='black', bg='red',
                                        command=clear, height=1, width=7)
                clear.grid(row=5, column='1')

                Decimal= Button(gui, text='.', fg='black', bg='red',
                                                command=lambda: press('.'), height=1, width=7)
                Decimal.grid(row=6, column=0)
                # start the GUI
                gui.mainloop()

            
run_alexa()
