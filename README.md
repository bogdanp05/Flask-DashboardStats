# Flask-DashboardStats

Useful statistics for the [Flask-MonitoringDashboard](https://github.com/flask-dashboard/Flask-MonitoringDashboard) project.

Saves the number of **Github stars** and **Pypi downloads** into
_stats.csv_. The file has the format (stars, downloads, time).

This repository contains a make file with the following commands:

- Fetching stats: `make stats`
- Viewing a graph: `make graph`
- Auto committing: `make commit`

The `make stats` and `make commit` can be run using a Linux cronjob as described [here](https://kvz.io/blog/2007/07/29/schedule-tasks-on-linux-using-crontab/).
For instance to run it every hour, add the following _cronjob_:
```
@hourly cd <REPO FOLDER> && make stats >/dev/null 2>&1 && make commit >/dev/null 2>&1 
```
