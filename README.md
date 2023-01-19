# Grading Server

This is a way to ease grading when students are in groups. On a server, deploy the `server/` code. On graders' machines, run `client/` code.

# Adapting to your course

* In `server/server.py`, change the value of `GRADES_FILE`. Line 15 assumes your assignments start on the 8th column, with 2 columns assigned to each assignment (one for the grade, one for the feedback).
* In `server/server.py`, change the value of `GROUPS_FILE` to your spreadsheet with groups. This assumes a column named "Group", and additional columns named "Member 1" through "Member 4". You can add more to that if needed.
* Deploy the server code to a central server, and in `.env`, add in the server URL like so:

```
SERVER_URL=<URL>
``` 
