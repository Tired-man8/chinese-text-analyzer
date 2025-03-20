# 🇨🇳 Chinese Text Analysis API 

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

## **🚀 Installation & Setup**
### **1️⃣ Clone the Repository**

## **Dependencies**
Python:
pip install flask jieba

Go:
go get -u github.com/gin-gonic/gin

## Running Project
start_servers.sh

http://127.0.0.1:5000

```sh
git clone https://github.com/your-username/chinese-text-analysis.git
cd chinese-text-analysis

