from bs4 import BeautifulSoup
import requests
import pandas as pd

site = requests.get("https://en.wikipedia.org/wiki/List_of_companies_of_Nepal").text
soup = BeautifulSoup(site, 'lxml')

site_table = soup.find('table')
thead = site_table.find_all('th')
thead_txt = [title.text.strip() for title in thead]
df=pd.DataFrame(columns = thead_txt)

column_data = site_table.find_all('tr')
for row in column_data[1:]:
    row_data = row.find_all('td')
    tbody_txt = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = tbody_txt

df.to_csv(r'companies.csv')