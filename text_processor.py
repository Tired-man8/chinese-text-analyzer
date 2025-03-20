import jieba
import jieba.posseg as pseg
import json

jieba.initialize()

# Open HSK file
with open("HSK.json", 'r', encoding='utf-8') as file:
    hsk_vocab = json.load(file)

# Convert list of dictionaries into one big dictionary
hsk_dict = {entry["Chinese"]: entry for entry in hsk_vocab}

def process_text(text):

    if not text:
        return {
            "verbs": {},
            "nouns": {},
            "adjectives": {},
            "adverbs": {}
        }

    # Convert generator to list
    words = list(pseg.cut(text))

    # words = pseg.cut(text)
    noun_tags = ('n', 'nr', 'ns', 'nt', 'nw', 'nz') # Noun
    verb_tags = ('v', 'vd', 'vn')                   # Verb 
    adj_tags = ('a',)                               # Adj
    adv_tags = ('d',)                               # Adv
    prep_tags = ('p',)                              # Preposition
    conj_tags = ('c',)                              # Conjunction

    verb_occurrence = dict()
    noun_occurrence = dict()
    adj_occurrence = dict()
    adv_occurrence = dict()
    prep_occurrence = dict()
    conj_occurrence = dict()

    # for word, flag in words:
    for token in words:
        word, flag = token.word, token.flag

        word_data = hsk_dict.get(word, {})

        if flag in verb_tags: # If flag is verb
            if word not in verb_occurrence:
                verb_occurrence[word] = {
                    "Chinese": word,
                    "Pinyin": word_data.get("Pinyin", "Not in HSK"),
                    "English": word_data.get("English", "Not in HSK"),
                    "HSK": word_data.get("HSK", "Not in HSK"),
                    "Occurrence": 0
                }
            verb_occurrence[word]["Occurrence"] += 1

        elif flag in noun_tags: # If flag is a noun
            if word not in noun_occurrence:
                noun_occurrence[word] = {
                    "Chinese": word,
                    "Pinyin": word_data.get("Pinyin", "Not in HSK"),
                    "English": word_data.get("English", "Not in HSK"),
                    "HSK": word_data.get("HSK", "Not in HSK"),
                    "Occurrence": 0
                }
            noun_occurrence[word]["Occurrence"] += 1

        elif flag in adj_tags:  # If flag is an adj
            if word not in adj_occurrence:
                adj_occurrence[word] = {
                    "Chinese": word,
                    "Pinyin": word_data.get("Pinyin", "Not in HSK"),
                    "English": word_data.get("English", "Not in HSK"),
                    "HSK": word_data.get("HSK", "Not in HSK"),
                    "Occurrence": 0
                }
            adj_occurrence[word]["Occurrence"] += 1

        elif flag in adv_tags: # If flag is an adv
            if word not in adv_occurrence:
                adv_occurrence[word] = {
                    "Chinese": word,
                    "Pinyin": word_data.get("Pinyin", "Not in HSK"),
                    "English": word_data.get("English", "Not in HSK"),
                    "HSK": word_data.get("HSK", "Not in HSK"),
                    "Occurrence": 0
                }
            adv_occurrence[word]["Occurrence"] += 1

        elif flag in prep_tags: # If flag is a preposition
            if word not in prep_occurrence:
                prep_occurrence[word] = {
                    "Chinese": word,
                    "Pinyin": word_data.get("Pinyin", "Not in HSK"),
                    "English": word_data.get("English", "Not in HSK"),
                    "HSK": word_data.get("HSK", "Not in HSK"),
                    "Occurrence": 0
                }
            prep_occurrence[word]["Occurrence"] += 1

        elif flag in conj_tags: # If flag is a conjunction
            if word not in conj_occurrence:
                conj_occurrence[word] = {
                    "Chinese": word,
                    "Pinyin": word_data.get("Pinyin", "Not in HSK"),
                    "English": word_data.get("English", "Not in HSK"),
                    "HSK": word_data.get("HSK", "Not in HSK"),
                    "Occurrence": 0
                }
            conj_occurrence[word]["Occurrence"] += 1
        else:
            continue

    return {
        "verbs": verb_occurrence,
        "nouns": noun_occurrence,
        "adjectives": adj_occurrence,
        "adverbs": adv_occurrence,
        "prepositions": prep_occurrence,
        "conjunctions": conj_occurrence
    }

# with open("output.txt", 'w', encoding='utf-8') as file:
#     file.write("Verbs:\n")
#     json.dump(verb_occurrence, file, ensure_ascii=False, indent=4)
#     file.write("\nNouns:\n")
#     json.dump(noun_occurrence, file, ensure_ascii=False, indent=4)
#     file.write("\nAdj:\n")
#     json.dump(adj_occurrence, file, ensure_ascii=False, indent=4)
#     file.write("\nAdv:\n")
#     json.dump(adv_occurrence, file, ensure_ascii=False, indent=4)
