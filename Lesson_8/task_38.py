#Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
#Пользователь также может ввести имя или фамилию
#Вы должны реализовать функционал для изменения и удаления данных

#записывает 
with open('phonebook.csv', 'w') as data:
    phones = ['1;Vasya Pupkin;8-999-88-77\n', '2;Grisha Dubkin;8-111-55-22\n', '3;Alyosha Zatupkin;8-555-44-65\n']
    data.writelines(phones)

#редактирует
with open('phonebook.csv', 'w') as data:
    phones = ['1;Vasya Pupkin;8-999-88-77\n', '2;Vova Dubkin;8-111-55-22\n', '3;Sasha Zatupkin;8-555-44-65\n']
    data.writelines(phones)


#удаляет
with open('phonebook.csv', 'w') as data:
    phones = ['1;Vasya Pupkin;8-999-88-77\n', '3;Alyosha Zatupkin;8-555-44-65\n']
    data.writelines(phones)