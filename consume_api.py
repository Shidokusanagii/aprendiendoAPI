import requests
animeName = input("Enter anime name:")
url = 'https://api.jikan.moe/v4/anime?q='+animeName+'&sfw'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f'Mensaje de la API: {data}')
else:
    print(f'Error al acceder a la API. Código de estado: {response.status_code}')
