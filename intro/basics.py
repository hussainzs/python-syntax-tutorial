#
import requests
from requests.models import Response

url = "https://jsonplaceholder.typicode.com/todos/"
api_response: Response = requests.get(url)

if api_response.status_code == 200:
    todos = api_response.json()
    print(todos)
else:
    print(f"Failed to retrieve data: {api_response.status_code}")


# write to a file
with open(file="todos.json", mode='a') as file:
    file.write(api_response.text)









