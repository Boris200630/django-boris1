from django.http import HttpResponse

def index(request, name, age):
    return HttpResponse(f'''
    <h2> Пользователь </h2>
    <p> Имя: {name}</p>
    <p> Возраст: {age}</p>  
''')
def about(request, where, study, love_study):
    return HttpResponse(f'''
    <h> О пользователе </h>
    <p> Живёт: {where}</p>
    <p> Успеваемость: {study}</p>
    <p> Отношение к школе: {love_study} </p>
''')

def contact(request,github, tg, number):
    return HttpResponse(f'''
    <h> Контакты пользователя </h>
    <p> Github: {github}</p>
    <p> telegramm: {tg}</p>
    <p> Телефон: {number} </p>
''')