#gcloud doc CLI
import requests as req, bs4, webbrowser

#function to get we links
def check_link(a):
    a_link1 = a.split("href=")
    a_link2 = a_link1[1]
    a_link3 = a_link2.split(">")
    a_link4 = a_link3[0]
    a_link5 = a_link4[1:-1]
    return a_link5

#get to google.com
res = req.get("https://google.com")

#ask user what they want to do with google.

#get links from google's main page
res.raise_for_status
file_html_google_mainpage = bs4.BeautifulSoup(res.text, "html.parser")
#print(str(file_html_google_mainpage))
link_elements = file_html_google_mainpage.select("a")
#print links
#ask user where he wants to go by passing by google auth
print("number of links: ", len(link_elements))
#print these elements
print("this is your drive link: ")
for link in link_elements:
    s = str(link)
    #print(check_link(s))
    if("drive" in check_link(s)):
        print(check_link(s))


# get input from user on what to do in google (via cli or browser)
'''cli_or_browser = input("Use CLI or a browser to access Google? Type 'cli' or 'web' to access google -> ")
#check input for CLI or browser
if (cli_or_browser == "web"):
    #ask what  the user wants to do in google
    web_input = input("use google to check: 'mail', 'sign in' or 'google doc' -- for chat, type: chat -> ")
    for link in link_elements:
        s = str(link)
        if (web_input == "mail"):
            if("mail" in check_link(s)):
                webbrowser.open(check_link(s))
        elif(web_input == "sign in"):
            if("accounts" in check_link(s)):
                webbrowser.open(check_link(s))
        elif(web_input == "google doc"):
            if("drive" in check_link(s)):
                webbrowser.open(check_link(s))
        elif(web_input == "chat"):
            if("drive" in check_link(s)):
                webbrowser.open(check_link(s))
elif(cli_or_browser == "cli"):
    #ask user what they want to do with cli
    cli_input = input("Your are now using cli commands.'\nSelect by typing: 'mail', 'sign in', or 'google doc' -- for chat, type: chat: -> ")
    for link in link_elements:
        s = str(link)
        if (cli_input == "mail"):
            if ("mail" in check_link(s)):
                #webbrowser.open(check_link(s))
        elif (cli_input == "sign in"):
            if ("sign in" in check_link(s)):
                #webbrowser.open(check_link(s))
        elif (cli_input == "google doc"):
            if ("drive" in check_link(s)):
                #webbrowser.open(check_link(s))
        elif (cli_input == "chat"):
            if ("drive" in check_link(s)):
                #webbrowser.open(check_link(s))'''













