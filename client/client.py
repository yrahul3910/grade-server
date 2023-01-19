import os
import sys
import requests
import cutie


if not os.path.exists('.env'):
    URL = 'http://localhost:5000'
else:
    with open('.env', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        url_line = [line for line in lines if line.startswith('SERVER_URL')]

        if len(url_line) == 0:
            print('Error: Missing SERVER_URL parameter in .env')
            sys.exit(1)

        URL = url_line[0].split('=')[1][:-1]


def main():
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
        }, timeout=3000)

        response = response.json()
        if response['status'] != 'success':
            print('Error:', response['error'])

        if not cutie.prompt_yes_or_no('Submit another grade?'):
            break


if __name__ == '__main__':
    main()
