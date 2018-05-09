# Flask-DashboardStats

Useful statistics for the [Flask-MonitoringDashboard](https://github.com/flask-dashboard/Flask-MonitoringDashboard) project.

Saves the number of **Github stars** and **Pypi downloads** into
_stats.csv_. The file has the format (stars, downloads, time).

The Python script can be run using a Linux cronjob as described [here](https://kvz.io/blog/2007/07/29/schedule-tasks-on-linux-using-crontab/).
For instance to run it every 6 hours, I added the following _cronjob_:
```
0 */6 * * * python3 /home/bogdan/statistics_flask/statistics.py >/dev/null 2>&1
```
