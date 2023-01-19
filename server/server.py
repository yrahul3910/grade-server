import re
from flask import Flask, request
import pandas as pd

app = Flask(__name__)

GRADES_FILE = 'CSC 591 (021) SPRG 2023 Grades.xlsx'
GROUPS_FILE = 'project/homework groups CSC591/791.xlsx'


@app.route('/assignments/get')
def get_assignments():
    # Read each time so that the server doesn't need to be restarted
    grades_df = pd.read_excel(GRADES_FILE, sheet_name='Grades')
    assignments = grades_df.columns[8:-1:2]
    return { 'assignments': assignments }


@app.route('/assignments/submit', methods=['POST'])
def submit_grade():
    req = request.get_json(force=True)
    assignment, group, grade, feedback = req['assignment'], req['group'], req['grade'], req['feedback']

    # Read each time so that the server doesn't need to be restarted
    groups_df = pd.read_excel(GROUPS_FILE, sheet_name='Sheet1')
    names = groups_df[groups_df['Group'] == group]

    # Write to the grades file
    grades_df = pd.read_excel(GRADES_FILE, sheet_name='Grades')

    for member in ['Member 1', 'Member 2', 'Member 3', 'Member 4']:
        if re.match('^\\s*$', names[member].values[0]):
            continue

        # Get the first and last name
        name = names[member].values[0]
        first, last = name.split(' ')[0], name.split(' ')[-1]

        # Iterate over rows in grades_df
        for index, row in grades_df.iterrows():
            # If the first and last name match, then update the grade
            if first in row['First Name'] and last in row['Last Name']:
                assignment_name = assignment.split(' (Real)')[0]
                grades_df.at[index, req['assignment']] = grade
                grades_df.at[index, assignment_name + ' (Feedback)'] = feedback
