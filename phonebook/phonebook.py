import json
import os

if os.path.exists("notebook.json"):
    with open ("notebook.json", 'r', encoding='utf-8') as f:
        notebook=json.load(f)  # загрузить
else:
    notebook = {}# пустой словарь


while True:
     com=input ("введите команду (добавить, список, поиск, удалить, выход): ").strip()
     if com.lower()=="выход":
         with open ("notebook.json", 'w', encoding='utf-8') as f:
          json.dump(notebook, f, ensure_ascii=False, indent=4)  
         break
     elif com.lower()=="добавить":
         name_inp = input ("Введите имя контакта: ").strip()
         phone_inp = input ("Введите телефонный номер: ").strip()
         if name_inp not in notebook:
            notebook[name_inp]=phone_inp
            print (f"Имя: {name_inp}")
            print (f"Номер: {phone_inp}")
            print ("Контакт добавлен!")
            with open ("notebook.json", 'w', encoding='utf-8') as f:
                json.dump(notebook, f, ensure_ascii=False, indent=4)  
         else:
            print ("Контакт был записан ранее!")
  
     elif com.lower()=="список": 
            for name, phone in notebook.items():
             print(f"{name}: {phone}")
     elif com.lower()=="поиск":
            name_inp = input ("Введите имя контакта: ").strip()
            for name, phone in notebook.items():
             if name_inp in name:
               print (f"Поиск по имени {name}: {phone}")
     elif com.lower() == "удалить":
          name_inp = input ("Введите имя контакта: ").strip()
          if name_inp in notebook:
            del notebook[name_inp]
            print ("Контакт удален!")
            with open ("notebook.json", 'w', encoding='utf-8') as f:
                json.dump(notebook, f, ensure_ascii=False, indent=4)  
          else:
            print ("Контакт не найден!")