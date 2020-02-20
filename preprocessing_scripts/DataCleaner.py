import spacy
import csv
import re
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
filename_train = r"C:\Users\drewb\PycharmProjects\FirstProject\KegalCompetition\train.csv"
nlp = spacy.load('en_core_web_sm')

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def extract_entities(s):
    doc = nlp(s)
    new_string = s
    for ent in doc.ents:
        new_string = new_string.replace(ent.text, ' ' + ent.label_ +' ')
    return new_string

def lemmatize_text(s):
    new_string = ''
    for word in s.split(' '):
        try:
            new_string += lemmatizer.lemmatize(word) + ' '
        except:
            new_string += word + ' '
    return new_string

keywords = list()
locations = list()
texts = list()
targets = list()
with open(filename_train, encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile)
    itr = 0
    for row in reader:
        keyword, location, text, target = row['keyword'], row['location'], row['text'], row['target']
        keywords.append(keyword)
        locations.append(location)
        text = text.replace("\n", ' ')
        text = text.replace("\'", ' ')
        text = text.replace("\"", ' ')
        text = text.replace('\n', ' ')
        #text = lemmatize_text(text)
        texts.append(extract_entities(text))
        targets.append(target)






new_texts = list()
for text in texts:
    new_string = '<START> '
    for token in text.split(' '):
        if re.match("^((https|http|ftp|file)?:\/\/).*", token):
            new_string += "<LINK> "
            continue
        #need to check for time regex
        if re.match("[0-9]+:[0-9]+(am|AM|pm|PM)?", token):
            new_string += "TIME "
            continue

        temp = token.replace(';', ' ')
        temp = temp.replace('?', ' ')
        temp = temp.replace(':', ' ')
        temp = temp.replace('!', ' ')
        if re.match("^-?\d*\.?\d+$", temp):
            new_string += "<NUM> "
            continue

        temp = temp.replace('-', ' ')
        temp = temp.replace('.', ' ')
        temp = temp.replace('(', ' ')
        temp = temp.replace(')', ' ')
        temp = temp.replace('{', ' ')
        temp = temp.replace('}', ' ')
        temp = temp.replace('[', ' ')
        temp = temp.replace(']', ' ')

        if re.match("^@.*", temp):
            new_string += "<USER>"
        elif re.match("^ @.*", temp):
            new_string += "<USER>"
        elif re.match("^#.*", temp):
            new_string += "<HASH>"
        elif not is_ascii(temp):
            new_string += "<NASCII>"
        else:

            new_string += temp
        new_string += ' '
    new_string += "<STOP>"
    new_string = new_string.replace('*', " * ")
    new_string = new_string.replace('&', ' ')
    new_string = new_string.replace('$', ' ')
    new_string = new_string.replace('#', ' ')
    new_string = new_string.replace('^', ' ')
    new_string = new_string.replace('\\', ' ')
    new_string = new_string.replace('/', ' ')
    new_string = new_string.replace('`', ' ')
    new_string = new_string.replace('~', ' ')
    new_texts.append(' '.join(new_string.split()))
with open("new_train_data.txt", "w") as f:
    for t in new_texts:
        f.write(t + "\n")

print(len(new_texts))