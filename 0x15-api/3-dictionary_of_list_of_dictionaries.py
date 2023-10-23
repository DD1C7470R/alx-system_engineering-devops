#!/usr/bin/python3
"""fetches information from JSONplaceholder API and exports to JSON"""

from json import dump
from requests import get
from sys import argv


if __name__ == '__main__':
    main_url = 'https://jsonplaceholder.typicode.com'
    users_result = get(main_url + '/users').json()

    employees_data = {}
    for user in users_result:
        todo_list = []
        todo_url = main_url + f"/user/{user.get('id')}/todos"
        name_url = main_url + f"/users/{user.get('id')}"
        todo_result = get(todo_url).json()
        name_result = get(name_url).json()

        todo_list = []
        for todo in todo_result:
            todo_dict = {}
            todo_dict.update(
                    {
                        "username": name_result.get("username"),
                        "completed": todo.get("completed"),
                        "task": todo.get("title")
                    })
            todo_list.append(todo_dict)

        employees_data.update({user.get("id"): todo_list})
    with open("todo_all_employees.json", 'w') as f:
        dump(employees_data, f)
