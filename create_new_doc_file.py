#python file to create new dropbox txt files
#get a link from dropbox, get the html from  iframe element
#show the elements in <pre><span>....</span></pre>
#paste the element from the html
#using requests and other modules.
#can we access gcloud and add files to it.
import requests as req, bs4, webbrowser as browser


#use requests to get link status.
link_zero = input("enter a dropbox link: ")
#link_one = str(link_zero)
res = req.get(link_zero)
res.raise_for_status()
print(res)
#create a beautiful soup contain
object_soup =bs4.BeautifulSoup(res.text, 'html.parser')
