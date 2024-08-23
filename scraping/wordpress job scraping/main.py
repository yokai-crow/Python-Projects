from bs4 import BeautifulSoup
import requests
import time


def find_jobs():
    print("********************************************************")
    print("|Searching for wordpress developer job in timesjobs.com|")
    print("********************************************************")

    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=wordpress&txtLocation=').text
    soup =BeautifulSoup(html_text,'lxml')
    jobs=soup.find_all('li',class_="clearfix job-bx wht-shd-bx")
    counter = 0
    for job in jobs:
        published_date = job.find('span',class_="sim-posted").span.text
        if 'few' in published_date:
            company_name = job.find('h3',class_="joblist-comp-name").text.replace(' ','')
            skills = job.find('span',class_="srp-skills").text.replace(' ','')
            more_info = job.header.h2.a['href']

            print(f"Company Name: {company_name.strip()}")
            print(f"Skills required: {skills.strip()}")
            print(f"More info: {more_info}")
            print('-----------------------------------------------------------')
            counter = counter+1      
    print(f"{counter} jobs available at the moment.")

if __name__ == '__main__':
    while True:
        find_jobs()
        
        time_wait = 10
        print(f"waiting {time_wait} minutes for next scrap...")
        time.sleep(time_wait*60)
        