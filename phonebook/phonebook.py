import json
import os

if os.path.exists("phonebook.json"):
    with open ("phonebook.json", 'r', encoding='utf-8') as f:
        phonebook=json.load(f)  # загрузить
else:
    phonebook = {}# пустой словарь

while True:
     com=input ("введите команду (добавить, список, поиск, удалить, выход): ").strip()
     if com.lower()=="выход":
         with open ("phonebook.json", 'w', encoding='utf-8') as f:
          json.dump(phonebook, f, ensure_ascii=False, indent=4)  
         break
     elif com.lower()=="добавить":
         name_inp = input ("Введите имя контакта: ").strip()
         phone_inp = input ("Введите телефонный номер: ").strip()
         if name_inp not in phonebook:
            phonebook[name_inp]=phone_inp
            print (f"Имя: {name_inp}")
            print (f"Номер: {phone_inp}")
            print ("Контакт добавлен!")
            with open ("phonebook.json", 'w', encoding='utf-8') as f:
                json.dump(phonebook, f, ensure_ascii=False, indent=4)  
         else:
            print ("Контакт был записан ранее!")
  
     elif com.lower()=="список": 
            for name, phone in phonebook.items():
             print(f"{name}: {phone}")
     elif com.lower()=="поиск":
            name_inp = input ("Введите имя контакта: ").strip()
            for name, phone in phonebook.items():
             if name_inp in name:
               print (f"Поиск по имени {name}: {phone}")
     elif com.lower() == "удалить":
          name_inp = input ("Введите имя контакта: ").strip()
          if name_inp in phonebook:
            del phonebook[name_inp]
            print ("Контакт удален!")
            with open ("phonebook.json", 'w', encoding='utf-8') as f:
                json.dump(phonebook, f, ensure_ascii=False, indent=4)  
          else:
            print ("Контакт не найден!")