# jira_team_productivity_chart
Retrieve the number of resolved tickets at interest JIRA project. 
then, fill these numbers into excel template file "jira_team_productivity_template.xlsx"
to plot trend line chart to see team performance in 12 month time range.

python version 3.7
import
  requests
  pandas
  openpyxl

<code>
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
</code>
