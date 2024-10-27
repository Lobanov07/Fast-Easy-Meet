# Проект Fast-Easy-Meet
____

## Оглавление
- [Проект Fast-Easy-Meet](#проект-fast-easy-meet)
  - [Оглавление](#оглавление)
  - [Стек технологий](#стек-технологий)
  - [Краткое описание проекта](#краткое-описание-проекта)
  - [Установка и запуск](#установка-и-запуск)
  - [Команда разработки](#команда-разработки)

 ## Стек технологий
+ Python 3.12
+ Django
 ## Краткое описание проекта
Fast-Easy-Meet — это инструмент, который помогает организовать встречи в удобное время для всех участников. Приложение позволяет выбрать время, которое подходит или не подходит для определенного человека, и на основе этих данных подбирает оптимальное время для проведения встречи.
 ## Установка и запуск
1.Клонировать репозиторий и перейти к проекту:
   ```
   git clone https://github.com/Lobanov07/Fast-Easy-Meet 
   ```

2.В корневой директории проекта создайте виртуальное окружение, используя команду:
- Если у вас windows:
  
   ```
   python -m venv venv
   ```
    или

    ```
    py -3 -m venv venv
    ```
- Если у вас Linux/macOS:
  ```
  python3 -m venv venv.
  ```

3.Активируйте виртуальное окружение командой:
- Если у вас windows:
  ```
  source venv/Scripts/activate
  ```
- Если у вас Linux/macOS:
  ```
  source venv/bin/activate
  ```
4.Обновите менеджер пакетов:
```
python -m pip install --upgrade pip
```
5.Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
6.Выполнить миграции:
```
python manage.py migrate
```
7.Запустить проект:
```
python manage.py runserver
```
Ваш проект запустился на `http://127.0.0.1:8000/`

С помощью команды pytest вы можете запустить тесты и проверить работу модулей

## Команда разработки

- Lobanov Konstantin
  -  github: [Lobanov07](https://github.com/Lobanov07)

- Sokolov Mark
  -  github: [MarikSmerch](https://github.com/MarikSmerch)

- Ledovskikh Artem
  -  github: [RiverBoy26](https://github.com/RiverBoy26)
  