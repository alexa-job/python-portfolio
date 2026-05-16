          
import os
import json

print ("Приветствую тебя, дорогой читатель! Это программа создана для введения статистики чтения книг.")
print ("Список комманд: добавить, список, автор, прочитано, статистика, выход")

if os.path.exists("books.json"):
    with open ("books.json", 'r', encoding='utf-8') as f:
        books = json.load(f) # чтение данных если список словарей books.json существует
else:
    books = [] # либо создание пустого списока для словарей

while True: # бесконечный цикл
    com=input ("Введите команду:")
    
    # выход из цикла 
    if com.lower() == "выход":
        with open ("books.json", 'w', encoding='utf-8') as f:
            json.dump(books, f, ensure_ascii=False, indent=4)  
            break 
     
    # добавление полученных данных в список словарей books[{"полученные данные"}]   
    elif com.lower() == "добавить":
         title = input ("Введите название книги?: ")
         year = input ("В каком году написана книга?: ")
         author  = input ("Кто автор?: ")
         books.append({"title":title, "year":year, "author":author, "read":False}) 
        
    # список сохраненых книг ([v] - отметка о прочтении)      
    elif com.lower() == "список":
        for index, book in enumerate(books, start=1):
            if not book["read"]:
                print (f"{index}. [ ] {book['title']} {book['author']} {book['year']}")
            else:
                print (f"{index}. [V] {book['title']} {book['author']} {book['year']}")
    
    # поиск книг по автору
    elif  com.lower() == "автор":
        author = input ("Введите автора: ")
        for index, book in enumerate(books, start=1):
            if book["author"] == author:
                print (f"{index}. [ ] {book['title']} {book['author']} {book['year']}")
    
    # отметка о прочтении
    elif com.lower() == "прочитано":
        title = input ("Введите название книги: ")
        for book in books:
            if book['title']==title:
                if not book['read']:
                    book['read']=True
                    
    # получение статистики
    elif com.lower()=="статистика":
        no_read =0
        yes_read =0
        for book in books:
            if not book['read']:
               no_read +=1
            else:
                yes_read+=1 
        print (f"Общее количество книг: {no_read+yes_read}")
        print (f"Прочитано: {yes_read}")    
        print (f"Запланировано к чтению: {no_read}")