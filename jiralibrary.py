import time
from datetime import date
import requests
from requests.auth import HTTPBasicAuth
import json
import pandas as pd

def test_func(name):
  print("My name is " + name + ".")
  print(date.today())

class DoFilter:
    url = "https://test.atlassian.net/rest/api/2/search"
    auth = ""
    headers = {
       "Accept": "application/json"
    }

    def __init__(self, jsonJiraAccess):
        self.url = jsonJiraAccess['url']
        self.auth = HTTPBasicAuth(jsonJiraAccess['user'], jsonJiraAccess['key'])

    def GetNumOfJiraFilter(self, filter):
        query = {
           #'jql': 'project = GDP AND issuetype in (Epic, Story, Task) AND created >= 2020-07-01 AND created <= 2020-07-31'
           'jql': filter
        }
        response = requests.request(
           "GET",
           self.url,
           headers = self.headers,
           params = query,
           auth = self.auth
        )
        json_load = json.loads(response.text)
        return(json_load ['total'])
