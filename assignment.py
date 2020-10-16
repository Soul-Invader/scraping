from bs4 import BeautifulSoup
import requests
import pandas

url='https://www.programmableweb.com/category/tools/api'

jobs={}
job_no=0

while True:
    response=requests.get(url)
    source_code=response.text
    data=BeautifulSoup(source_code,'html.parser')

    table=data.find('tbody')
    rows=table.find_all('tr')
    for row in rows:
        name_and_link_tag=row.find('td',{'class':'views-field views-field-title'})
        name_and_link=name_and_link_tag.find('a')
        name=name_and_link.text
        link='https://www.programmableweb.com'+name_and_link.get('href')
        category_tag=row.find('td',{'class':'views-field views-field-field-article-primary-category'})
        category=category_tag.find('a').text
        description=row.find('td',{'class':'views-field views-field-field-api-description'}).text
        job_no+=1
        jobs[job_no]=[name,link,category,description]
        
        print(name,'\n',link,'\n',category,'\n',description,'\n....')

    next_page=data.find('a',{'id':'pager_id_apis_all'})
    if next_page:
        if next_page.get('href'):
            url='https://www.programmableweb.com'+next_page.get('href')
            print(url)
    else:
        break
    
print(job_no)
jobs_df=pandas.DataFrame.from_dict(jobs,orient='index',columns=['Name','Link','Category','Description'])
jobs_df.to_csv('assignment.csv')
                                   
    
