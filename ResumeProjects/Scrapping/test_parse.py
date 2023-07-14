'''1.  Bring HTML DAtA'''
import requests

#Function
def fetch_and_save_To_File(url,path):
    r = requests.get(url)
    with open(path,"w") as f:
        f.write(r.text)
url = " https://www.computerhope.com/jargon/w/website.htm"

#calling

fetch_and_save_To_File(url, "PycharmProjects/pythonProject/ResumeProjects/Scrapping/news.html")