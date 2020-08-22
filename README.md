# jira_team_productivity_chart
This is python3 script which create team KPI from JIRA.
Retrieve the number of resolved tickets at target project in JIRA to see team KPI per 12 month time range.

Usage:

<code>$ python3 jira_team_productivity.py jsonInpufile </code>

Tested python version

      3.7.7
      3.8.5

Required module:

      $pip3 install pandas
      $pip3 install openpyxl
      $pip3 requests

Files:

      jira_team_productivity.py  ... main script file
      jiralibrary.py             ... library file
      jira_team_productivity_template.xlsx ... an excel template file
      jira_filter_template.json   ... json input file, jira_filter_template


Input json file format

      {
            "jiraAccess":{
                "url":"https://<own_jira_url>.atlassian.net/rest/api/2/search",
                "user":"your jira username",
                "key":"your jira api token"
            },

            "input":{
                "project":"list of JIRA short project name",
                "startWeek":"2019-12-30" ... not use for this scrypt
            }
      }

note:

https://confluence.atlassian.com/cloud/api-tokens-938839638.html

output:

Fill team KPI information and Line chart into an excel file.
