import requests
from bs4 import BeautifulSoup
import csv
import datetime

stars = ''
downloads = ''

req_github = requests.get('https://api.github.com/repos/flask-dashboard/Flask-MonitoringDashboard')

if req_github.status_code != 200:
    print('Request to Github failed with code %d' %(req_github.status_code))

else:
    stars = req_github.json()['stargazers_count']
    print('Number of stars: %s' %(stars))


req_pepy = requests.get('http://pepy.tech/count/Flask-MonitoringDashboard')
if req_pepy.status_code != 200:
    print('Request to Pepy failed with code %d' % (req_pepy.status_code))
else:
    html_doc = req_pepy.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    downloads = soup.body.div.div.p.b.string
    print('Number of downloads: %s' %(downloads))

timestamp = datetime.datetime.now()
with open('stats.csv', 'a') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerow([stars, downloads, timestamp.strftime("%Y-%m-%d %H:%M:%S")])



