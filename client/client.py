import requests
import cutie


URL = 'http://localhost:5000'


def get_assignments():
    response = requests.get(URL + '/assignments/get')
    response = response.json()['assignments']

    print('Select an assignment:')
    assignment = response[cutie.select(response)]

    while True:
        group = cutie.get_number('Enter the group number: ')
        grade = cutie.get_number('Enter the grade (0-100): ')
        feedback = input('Enter feedback: ')

        response = requests.post(URL + '/assignments/submit', json={ 
            'assignment': assignment,
            'group': group,
            'grade': grade,
            'feedback': feedback 
        })

        if not cutie.prompt_yes_or_no('Submit another grade?'):
            break