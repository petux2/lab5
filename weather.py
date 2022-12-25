import requests

print(requests.get('http://google.com')) #первое задание

appid = '7d9300ddd5a8b4c19e0dea2e24284324'

#ввод города и обращение к api
while True:
    city = input('Введите имя города: ')
    r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={appid}').json()
    if int(r['cod']) == 404:
        print('Город не найден')
        continue
    break

#вывод информации
print(f"Город: {r['name']}, {r['sys']['country']}")
print(f"Погода: {r['weather'][0]['description']}")
print(f"Влажность: {r['main']['humidity']}%")
print(f"Давление: {r['main']['pressure']*10**2} Па")

