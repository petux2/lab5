import requests

apikey = '0618c5c4abd44728a9190078ca8a1553'

#ввод информации для поиска
keyword = input('Введите ключевое слово: ')

while True:
    searchIn0 = input('Введите тип поиска(0 - в заголовке, 1 - в описании, 2 - в содержании, можно комбинировать): ')
    searchIn = ''
    if '0' in searchIn0: searchIn += 'title,'
    if '1' in searchIn0: searchIn += 'description,'
    if '2' in searchIn0: searchIn += 'content,'
    searchIn = searchIn[0:-1]
    if searchIn == '': print('Ошибка ввода')
    else: break

while True:
    sortBy = input('Введите тип сортировки(0 - релевантность, 1 - популярность, 2 - дата публикации): ')
    if sortBy == '0': sortBy = 'relevancy'; break
    elif sortBy == '1': sortBy = 'popularity'; break
    elif sortBy == '2': sortBy = 'publishedAt'; break
    else: print('Ошибка ввода')

while True:
    try:
        num_of_res = int(input('Введите количество результатов для вывода: '))
        break
    except ValueError:
        print('Ошибка ввода')

#обращение к api
url = f'https://newsapi.org/v2/everything?q={keyword}&searchIn={searchIn}&sortBy={sortBy}&apiKey={apikey}'
r = requests.get(url).json()
if r['status'] == 'error':
    print(f"Ошибка: {r['message']}")
    exit()

#вывод кол-ва результатов
print()
print(f"Найдено результатов: {r['totalResults']}" + (f" ({num_of_res} будет выведено)" if r['totalResults'] > num_of_res else ""))
num_of_res = min(num_of_res, r['totalResults'])

#т.к. одна страница запроса содержит только до 100 результатов, то обращение происходит к каждой странице
for j in range((num_of_res//100 if num_of_res%100!=0 else num_of_res//100 - 1) + 1):
    #обращение к текущей странице
    url = f'https://newsapi.org/v2/everything?q={keyword}&searchIn={searchIn}&sortBy={sortBy}&page={j+1}&apiKey={apikey}'
    r = requests.get(url).json()
    if r['status'] == 'error':
        print(f"Ошибка: {r['message']}")
        exit()

    #количество результатов на странице
    num = 100
    if j == (num_of_res//100 if num_of_res%100!=0 else num_of_res//100 - 1): num = num_of_res % 100

    for i in range(num):
        #вывод информации
        rr = r['articles'][i]
        print()
        print('-'*25 + f' Результат №{j*100+i+1} ' + '-'*25)
        print(f"Источник: {rr['source']['name']}")
        print(f"Автор: {rr['author']}")
        print(f"Заголовок: {rr['title']}")
        print(f"Описание: {rr['description']}")
        print(f"Ссылка: {rr['url']}")
        print(f"Дата публикации: {rr['publishedAt'].split('T')[0]} {rr['publishedAt'].split('T')[1][0:-1]}")