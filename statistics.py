import requests
from bs4 import BeautifulSoup

req_github = requests.get('https://api.github.com/repos/flask-dashboard/Flask-MonitoringDashboard')

if req_github.status_code != 200:
    print('Request to Github failed with code %d' %(req_github.status_code))

else:
    print('Number of stars:')
    print(req_github.json()['stargazers_count'])


req_pepy = requests.get('http://pepy.tech/count/Flask-MonitoringDashboard')
if req_pepy.status_code != 200:
    print('Request to Pepy failed with code %d' % (req_pepy.status_code))
else:
    html_doc = req_pepy.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    print('Number of downloads:')
    print(soup.body.div.div.p.b.string)



