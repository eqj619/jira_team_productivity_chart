import requests
from requests.auth import HTTPBasicAuth
import json
import pandas as pd
import datetime
import openpyxl

#
# Get the number of refult of search with filter
#
class jiraTrendFilter:
    url = "https://test.atlassian.net/rest/api/2/search"
    auth = ""
    headers = {
       "Accept": "application/json"
    }

    def __init__(self, jsonJiraAccess):
        self.url = jsonJiraAccess['url']
        self.auth = HTTPBasicAuth(jsonJiraAccess['user'], jsonJiraAccess['key'])

    def GetNumOfJiraFilter(self, JiraFilter):
        query = {
           #'jql': 'project = GDP AND issuetype in (Epic, Story, Task) AND created >= 2020-07-01 AND created <= 2020-07-31'
           'jql': JiraFilter
        }
        response = requests.request(
           "GET",
           self.url,
           headers = self.headers,
           params = query,
           auth = self.auth
        )

        df = pd.read_json(response.text)
        return(len(df))

def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
    return next_month - datetime.timedelta(days=next_month.day)

def createDaysList(daysList, monthList):
    import time
    from datetime import date

    today = date.today()
    for y in range(today.year-2, today.year):
        for m in range(today.month, today.month+12):
            mm = m%12
            if mm == 0:
                mm = 12
                y += 1
            firstday = datetime.date(y, mm, 1)
            lastday = last_day_of_month(firstday)
            daysList.append([firstday.strftime("%Y-%m-%d"), lastday.strftime("%Y-%m-%d")])
            monthList.append(firstday.strftime("%Y-%m"))

# main
import time
from datetime import date

wb = openpyxl.load_workbook("jira_team_productivity_template.xlsx")
ws = wb.active

daysList = []
monthList = []
createDaysList(daysList, monthList)

json_open = open('jira_filter.json', 'r')
json_load = json.load(json_open)

tf = jiraTrendFilter(json_load['jiraAccess'])

projectName = json_load['input']['project']
i = 0
for day in daysList:
    f = 'project in (' + projectName + ') AND issuetype in (Epic, Story, Task) AND created >= ' \
        + day[0] +  ' AND created <= ' + day[1]
    ws.cell(row = i+2, column = 2).value = tf.GetNumOfJiraFilter(f)
    print(" >>> ", f)

    f = 'project in (' + projectName + ') AND issuetype in (Epic, Story, Task) AND resolved >= ' \
        + day[0] +  ' AND resolved <= ' + day[1]
    ws.cell(row = i+2, column = 4).value = tf.GetNumOfJiraFilter(f)
    print(" >>> ", f)
    i += 1

i = 0
for ym in monthList:
    ws.cell(row = i+2, column = 1).value = ym
    i += 1

wb.save("jira_" + projectName + "-team_performance-" + date.today().strftime("%Y-%m-%d") + ".xlsx")
