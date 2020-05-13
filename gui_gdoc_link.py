#use tkinter to create a gui addition
#to our google doc link program
from tkinter import *
import requests as req, bs4, webbrowser as browser

#gui: root, Entry point for input, textarea for output
#button_read_link to analyze the link
#button_auth to sign in to google and ensure
# that public sharing priviledges
#are on.
# 3 buttons:

#gui
#main window
root = Tk()
root.title("Google Doc Reader")
root.geometry("600x400")
root.columnconfigure(0, weight=1)
root.rowconfigure((0,1,2,4), weight=1)

'''clean the entry and text area'''
def clean_text_areas():
    user_link_input.delete(0, 'end')
    text_area.delete('1.0', 'end')


#methods for data collection and analysis.
#accept input from user: insert link and go to where the link leads
#google verification
user_link_label = Label(root, text="Insert Link here:")
user_link_input = Entry(root, width=50, borderwidth=5)
#place it on the window using grids
user_link_label.grid(row=0, column=0)
user_link_input.grid(row=1, column=0)


#text area for returned text
text_are_label = Label(root, text="Your Google Doc Text:").grid(row=2, column=0)
text_area = Text(root, height=12, width=70, wrap=WORD, bg= "white", borderwidth=5)
#pack it on window
text_area.grid(row=5,column=0)


#methods for data collection and analysis.
'''----------------'''
def analyse_Text(simpleText):
    simple_txt1 = simpleText.split('s":')
    #get text from index 1
    if (len(simple_txt1) >= 2):
        simple_txt2 = simple_txt1[1]
    #split text  from \n"}
        simple_txt3 = simple_txt2.split('}')
        if(len(simple_txt3) >= 1):
            simple_txt4 = simple_txt3[0]
            return simple_txt4
    return " "
#method for getting text from user through Entry
def Show_Text():
    #get the text from input
    link_ = user_link_input.get()
    res2 = req.get(link_)
    res2. raise_for_status()
    text_html = bs4.BeautifulSoup(res2.text, "html.parser")
    inputelements = text_html.select('script[type="text/javascript"]')
    for inp_element in inputelements:
        stringinput = str(inp_element)
        text_area.insert(END, analyse_Text(stringinput))



#method for display text in the textarea so user can see it.
def Reset_Text():
    clean_text_areas()
    show_Text()


#buttons: Show Text, Reset
button_show_text = Button(root, text="Show Text", bg="cyan", command=Show_Text).grid(row=3, column=0)
button_reset = Button(root, text="Reset", bg="cyan", command=Reset_Text).grid(row=4, column=0)
button_exit = Button(root, text="Exit", bg="cyan", command=root.destroy).grid(row=6, column=0)

#make window  resizable
root.resizable(True, True)

#run mainloop
root.mainloop()
