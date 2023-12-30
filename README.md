## 1. Создаем и активируем виртуальное окружение
> python -m venv .env<br>
> .\\.env\Scripts\Activate.ps1<br>

## 2. Устанавливаем необходимые пакеты
> pip install nltk<br>
> pip install deep_translator<br>

## 3. Создаем переменную среды куда сохранять ресурсы NLTK (необязательно)
> $env:NLTK_DATA="C:\nltk_data"<br>

## 4. Подставляем сюда путь к исходному текстовому файлу
with open('MachineLearning.txt', 'r') as file:

## 5. Запускаем 1_parse.py
> python 1_parse.py<br>

Этот процесс может занять довольно много времени (из-за задержки между запросами к GoogleTranslate)

## 6. Учим слова с помощью 2_learn.py
Это можно запускать не из .env (т.к. нет внешних зависимостей)
