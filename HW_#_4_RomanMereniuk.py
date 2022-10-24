"""
1. Створіть клас Vehicle з атрибутами екземпляра max_speed і mileage та методами increase_speed, break_speed, mileage_info
2. Створіть дочірній клас Bus, який успадкує всі змінні та методи класу Vehicle і матиме власний метод seating_capacity
3. Визначте, від якого класу успадковується клас Bus (перевірте issubclass)
4. Створіть екземпляр Bus під назвою school_bus і визначте, чи є school_bus об'єктом класу Vehicle/Bus
5. Створіть новий клас School з атрибутами екземпляра get_school_id і number_of_students та методами school_address, main_subject
6*. Створіть новий клас SchoolBus, який успадкує всі методи від School і Bus і матиме власний - bus_school_color
7. Поліморфізм: Створіть два класи: Bear, Wolf. Обидва вони повинні мати метод eat. Створіть два екземпляри: від Ведмідь і від Вовк,
створіть із нього кортеж і використовуючи спільну змінну, викличте метод eat.
Магічні методи:
Додатково: 8*. Створіть клас City з атрибутами екземпляра name i population, сторіть новий екземпляр цього класу, лише коли population > 1500,
інакше повертається повідомлення: "Your city is too small". Підказка: використовуєте для цього завдання магічні методи
"""
#task_20
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
sorted(lst_to_sort)
print(sorted(lst_to_sort))

#task_21
sorted(lst_to_sort, reverse=True)
print(sorted(lst_to_sort, reverse=True))