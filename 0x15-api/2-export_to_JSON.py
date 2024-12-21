#!/usr/bin/python3
"""fetches information from JSONplaceholder API and exports to JSON"""

from json import dump
from sys import argv
from security import safe_requests


if __name__ == '__main__':
    main_url = 'https://jsonplaceholder.typicode.com'
    todo_url = main_url + f"/user/{argv[1]}/todos"
    name_url = main_url + f"/users/{argv[1]}"
    todo_result = safe_requests.get(todo_url).json()
    name_result = safe_requests.get(name_url).json()

    todo_list = []
    for todo in todo_result:
        todo_dict = {}
        todo_dict.update({"username": name_result.get(
            "username"), "completed": todo.get("completed"),
                          "task": todo.get("title")})
        todo_list.append(todo_dict)
    with open(f"{argv[1]}.json", 'w') as f:
        dump({argv[1]: todo_list}, f)
