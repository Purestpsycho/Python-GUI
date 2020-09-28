#Disply an empty window
import tkinter
import tkinter.messagebox

class ConvertGUI():
    def __init__(self):

        #Create the main window
        self.main_window = tkinter.Tk()

        #Create 2 frames to group widgets
        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        #Create the widgets for the top frame

        #This creates the text
        self.prompt_label = tkinter.Label(self.top_frame, text ='Enter a number and'\
                                      ' click either button to convert to Celsius or'\
                                      ' Farenheit:')

        #This creates the entry field and assigns it the value unitEntry
        self.unit_entry = tkinter.Entry(self.top_frame, width = 10)

        #Pack the Widgets
        self.prompt_label.pack(side='left')
        self.unit_entry.pack(side='left')

        #Create the widgets for the bottom frame
        
        #Create the convert to fahrenheit button
        self.fahrenheit_button = tkinter.Button(self.bottom_frame,
                                                text = 'FAHRENHEIT',
                                                command =self.convertFahrenheit) 
        self.celsius_button = tkinter.Button(self.bottom_frame,
                                             text ='CELSIUS',
                                             command =self.convertCelsius ) 
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text = 'QUIT',
                                          command = self.main_window.destroy)

        #Pack these stupid buttons
        self.fahrenheit_button.pack(side='left')
        self.celsius_button.pack(side='left')
        self.quit_button.pack(side='left')

        #Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        #Enter the main loop
        tkinter.mainloop()

    def convertFahrenheit(self):
        #callback function to, you guessed it, convert number to fahrenheit


        #Get the value from the user
        fahrenheit = float(self.unit_entry.get())
        fToC = (fahrenheit *9/5) + 32

        #Display the results
        tkinter.messagebox.showinfo('Results ',
                                    str(fahrenheit) +
                                    ' Celsius is equal to ' +
                                    str(fToC) + ' Fahrenheit'+
                                    ' \nMade by Hunter Goodpaster')
    def convertCelsius(self):
        #callback function to convert entry to celsius
        celsius = float(self.unit_entry.get())
        cToF = (celsius - 32) * 5/9

        #display the results
        tkinter.messagebox.showinfo('Results ',
                                    str(celsius) +
                                    ' Fahrenheit is equal to ' +
                                    str(cToF) + ' Celsius' +
                                    ' \nMade by Hunter Goodpaster')

        

#Test the GUI
convTest = ConvertGUI()
