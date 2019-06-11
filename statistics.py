import requests
import csv
import datetime
import sys
import os

stars = ''
downloads = ''

req_github = requests.get('https://api.github.com/repos/flask-dashboard/Flask-MonitoringDashboard')

if req_github.status_code != 200:
    print('Request to Github failed with code %d' % (req_github.status_code))

else:
    stars = req_github.json()['stargazers_count']
    print('Number of stars: %s' % stars)

req_pepy = requests.get('https://api.pepy.tech/api/projects/Flask-MonitoringDashboard')
if req_pepy.status_code != 200:
    print('Request to Pepy failed with code %d' % (req_pepy.status_code))
else:
    stats = req_pepy.json()
    downloads = stats['total_downloads']
    print('Total downloads: %s' % downloads)

timestamp = datetime.datetime.now()
with open(os.path.join(sys.path[0], 'stats.csv'), 'a') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerow([timestamp.strftime("%Y-%m-%d %H:%M:%S"), stars, downloads])
