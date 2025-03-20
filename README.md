# 🇨🇳 Chinese Text Analysis API 

Website -> https://chinese-text-analyzer-production.up.railway.app/

This is a personal project to practice programming while improving my Chinese. Hopefully it helps you too.

A hybrid **Go + Python** API that analyzes Chinese text, categorizes words (verbs, nouns, adjectives, etc.), and provides **HSK level** classification. The project uses:
- **Go (Gin)** for the primary API
- **Flask (Python)** for text processing with `jieba`
- **HTML + JavaScript** for the frontend

## **Features**
✔️ Categorizes words into **verbs, nouns, adjectives, adverbs, prepositions, and conjunctions**  
✔️ **HSK level classification** (if the word is in an HSK vocabulary list)  
✔️ **Sorts words by occurrence**  
✔️ **Filters results by HSK level**  
✔️ **Web interface** to analyze text interactively  
✔️ **Go API calls the Python NLP processor**  

---

## **Tech Stack**
| Component  | Technology  |
|------------|------------|
| **Backend (API)** | Go (Gin) + Python (Flask) |
| **Text Processing** | Jieba (Chinese NLP) |
| **Frontend** | HTML + JavaScript |
| **Data** | HSK JSON Vocabulary |

---

## **Future Improvements**
- Add HSK 7-9 vocabulary
- Add feature to export vocabulary to anki
- Other feedback I receive :)
