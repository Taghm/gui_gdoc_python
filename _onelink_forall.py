import requests as req, bs4, webbrowser


def check_link(a):
    a_link1 = a.split("href=")
    a_link2 = a_link1[1]
    a_link3 = a_link2.split(">")
    a_link4 = a_link3[0]
    a_link5 = a_link4[1:-1]
    return a_link5

def getText(simpleText):
    simple_txt1 = simpleText.split('s":')
    #get text from index 1
    if (len(simple_txt1) >= 2):
        simple_txt2 = simple_txt1[1]
    #split text  from \n"}
        simple_txt3 = simple_txt2.split('}')
        if(len(simple_txt3) >= 1):
            simple_txt4 = simple_txt3[0]
            return "user typed: " + simple_txt4
    return " "


general_link2 = 'https://accounts.google.com/AccountChooser/identifier?continue=https%3A%2F%2Fdrive.google.com%2F%3Ftab%3Dwo&amp%3Bfollowup=https%3A%2F%2Fdrive.google.com%2F%3Ftab%3Dwo&amp%3Bservice=wise&amp%3Bemr=1&flowName=GlifWebSignIn&flowEntry=AddSession'
#  we have to sign in via cli and then access gdrive's components.

if(webbrowser.open(general_link2) == True):
    #get google doc file
    general_link3 = input("paste a google doc file <link> here: ")
    if (general_link3 != " "):
        print("ChatBox 1.0 Opened")
        #get link of google file
        res2 = req.get(general_link3)
        res2. raise_for_status()
        text_html = bs4.BeautifulSoup(res2.text, "html.parser")
inputelements = text_html.select('script[type="text/javascript"]')
print("number of inputs: ", len(inputelements))
#print(funcsimpletxt2)
#text differentiated by "s": and \n
# go through all inputelements.
stringinput = ''
for inp_element in inputelements:
    stringinput = str(inp_element)
    print(getText(stringinput))

#add permissions
#to do...
