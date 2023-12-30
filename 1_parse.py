import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter
import re
from deep_translator import GoogleTranslator
import pickle

nltk.download('punkt')  # токенизатор предложений
nltk.download('averaged_perceptron_tagger')  # используется для частеречной разметки
nltk.download('wordnet')  # база данных лексических отношений англ.языка
nltk.download('stopwords')  # набор стоп-слов для нескольких языков
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

try:
    with open('MachineLearning.txt', 'r') as file:
        text = file.read().replace('\n', '')
except FileNotFoundError:
    print("Файл не найден")
    exit()

words = word_tokenize(text)

words = [word for word in words if word.isalpha()]

lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

filtered_words = [word for word in lemmatized_words if word not in stop_words]

translated_dict = {}
for word in filtered_words:
    translation = GoogleTranslator(source='auto', target='russian').translate(word)
    translated_dict[word] = {'translation': translation, 'correct_count': 0}

with open('translated_words.pkl', 'wb') as f:
    pickle.dump(translated_dict, f)
