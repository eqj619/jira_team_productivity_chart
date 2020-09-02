# jira_team_productivity_chart
This is python3 script which create team KPI from JIRA.
Retrieve the number of resolved tickets at target project in JIRA to see team KPI per 12 month time range.
this KPI focus on the number of resolved tickets within 12 months to measure team productivity to avoid seasonable variable at productivity (holidays, sickoff, event). increasing the number of resolved ticket encourage team staff to break down story and large ticket to 1-2 days task. and, paying attention to WIP to close the ticket effectively.
ideally in case of 2 weeks sprint, a staff have 9 working days. so that, 2 days and less volume of task can be resolved 4.5 tickets within a sprint. a company executes 20 sprints in annual, 90 tickets per person are resolved. this is example of reference number of resolved ticket.
manager is able to setup target number based on current team performance. then, address approach how to increase team KPI. Line chart created by this script show the monthly trend of annual resolved tickets.


## install:
      1. checkout this repository
      2. modify json file for your JIRA project
            JIRA URL
            user name
            jira Token
            target project(s) names
## Usage:
      $ python3 jira_team_productivity.py jsonInpufile
      Result, you can get updated excel file and be able to see the line chart and table in this excel file.

### Tested python version
      3.7.7
      3.8.5

### Required module:
      $pip3 install pandas
      $pip3 install openpyxl
      $pip3 requests

### Files:
      jira_team_productivity.py  ... main script file
      jiralibrary.py             ... library file
      jira_team_productivity_template.xlsx ... an excel template file
      jira_filter_template.json   ... json input file, jira_filter_template


### Input json file format
      {
            "jiraAccess":{
                "url":"https://<own_jira_url>.atlassian.net/rest/api/2/search",
                "user":"your jira username",
                "key":"your jira api token"
            },

            "input":{
                "project":"GDP, CLI, SVR", ... list of JIRA short project name
                "startWeek":"2019-12-30" ... not use for this scrypt
            }
      }

### note:
      You can find how to get JIRA API token in this link.
      https://confluence.atlassian.com/cloud/api-tokens-938839638.html

### output:
      Fill team KPI information and Line chart into an excel file.
      note: this script does not support fill out the head count at team(s). please input these number by manual, now.
