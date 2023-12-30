import pickle
import random

with open('translated_words.pkl', 'rb') as f:
    translated_dict = pickle.load(f)

correct_answers = 0
incorrect_answers = 0

while True:
    word = min(translated_dict, key=lambda x: translated_dict[x]['correct_count'])
    correct_translation = translated_dict[word]['translation']

    options = [correct_translation]
    translations = [item['translation'] for item in translated_dict.values()]
    while len(options) < 4:
        option = random.choice(translations)
        if option not in options:
            options.append(option)

    random.shuffle(options)

    print(f"\nКак переводится слово '{word}' на русский?")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    answer = input("Введите номер ответа, 'q' для выхода, 'e' для редактирования или 'd' для удаления: ")
    if answer.lower() == 'q':
        break
    elif answer.lower() == 'e':
        new_translation = input("Введите правильный перевод: ")
        translated_dict[word]['translation'] = new_translation
        print(f"Перевод слова '{word}' обновлен на '{new_translation}'")
    elif answer.lower() == 'd':
        del translated_dict[word]
        print(f"Слово '{word}' удалено из словаря")
    elif int(answer) == options.index(correct_translation) + 1:
        print("\nПравильно!")
        correct_answers += 1
        translated_dict[word]['correct_count'] += 1
    else:
        print(f"\nНеправильно. Правильный ответ: {correct_translation}")
        incorrect_answers += 1
        translated_dict[word]['correct_count'] -= 1

    translated_dict = dict(sorted(translated_dict.items(), key=lambda item: item[1]['correct_count']))

print(f"\nОбщее количество правильных ответов: {correct_answers}")
print(f"Общее количество неправильных ответов: {incorrect_answers}")

with open('translated_words.pkl', 'wb') as f:
    pickle.dump(translated_dict, f)

with open('translated_words.txt', 'w', encoding='utf-8') as f:
    for word, data in translated_dict.items():
        f.write(f"{word}        {data['translation']}        {data['correct_count']}\n")
