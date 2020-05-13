import requests as req
import bs4
#span class="kix-wordhtmlgenerator-word-node"
r = req.get("https://docs.google.com/document/d/1kB8oQJH4SU_MzbzAYORmkLAjxN4gop7OxVfS4lwQxX4/edit?usp=sharing")
#check status of link
if(r.status_code == req.codes.ok):
    print(">>> OK")
else:
    print(">>> not Ok.")
print("----from link: ", r)
#select an element from which we can see real time changes
#element span = "kix-wordhtmlgenerator-word-node"
#1. save file as txt so to check if it contains the span kix element
#rename it to gcloudwordhtmltext
file_text_gcloud = open("gcloudword3.html", 'wb')
for chunk in r.iter_content(1000000):
    file_text_gcloud.write(chunk)

#2. close file to avoid data leakage
#file_text_gcloud.close()

#parse the html to find the span kix element using bs4.
#file_to_load = open('gcloudword3.html')

file_to_parse = bs4.BeautifulSoup(open('gcloudword3.html'), 'html.parser')
spanElems = file_to_parse.select("span")
print("this is the span element at 0: " + str(spanElems[0]))
#print all span elements
print(str(spanElems))
#find the kix span class element.
'''for element in spanElems:
    if (spanElems.get(element) != "kix-wordhtmlgenerator-word-mode"):
        if (element  == "class"):
            print(element)
    else:
        print("element not found")'''
#continuation later.
