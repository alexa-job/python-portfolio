import json
import os

if os.path.exists("notebook.json"):
    with open ("notebook.json", 'r', encoding='utf-8') as f:
        notebook=json.load(f)  # загрузить
else:
    notebook = {}# пустой словарь


while True:
     com=input ("введите команду (добавить, список, поиск, выход): ")
     if (com.lower()=="выход"):
         with open ("notebook.json", 'w', encoding='utf-8') as f:
          json.dump(notebook, f, ensure_ascii=False, indent=4)  
         break
     elif (com.lower()=="добавить"):
         name_inp = input ("Введите имя контакта: ").strip()
         phone_inp = input ("Введите телефонный номер: ").strip()
         notebook[name_inp]=phone_inp
         print (f"Имя: {name_inp}")
         print (f"Номер: {phone_inp}")
         print ("Контакт добавлен!")
         with open ("notebook.json", 'w', encoding='utf-8') as f:
          json.dump(notebook, f, ensure_ascii=False, indent=4)  
  
     elif (com.lower()=="список"): 
            for name, phone in notebook.items():
             print(f"{name}: {phone}")
     elif (com.lower()=="поиск"):
            name_inp = input ("Введите имя контакта: ").strip()
            phone = notebook.get(name_inp, "Контакт не найден")
            print (f"Поиск по имени {name_inp}: {phone}")