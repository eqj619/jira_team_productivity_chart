# jira_team_productivity_chart
This is python3 script which create team KPI from JIRA.
Retrieve the number of resolved tickets at target project in JIRA

usage:

<code>$ python3 jira_team_productivity.py <json file> </code>

python version 3.7


files:

      jira_team_productivity.py  ... main script file
      jiralibrary.py             ... library file
      jira_team_productivity_template.xlsx ... an excel template file
      jira_filter_template.json   ... json input file, jira_filter_template


input json file format

      {
            "jiraAccess":{
                "url":"https://own jira url.atlassian.net/rest/api/2/search",
                "user":"your jira username",
                "key":"your jira access token"
            },

            "input":{
                "project":"list of JIRA short project name",
                "startWeek":"2019-12-30" ... not use for this scrypt
            }
      }

output:

Fill team KPI information and Line chart into an excel file.
