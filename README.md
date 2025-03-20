# NLP-ChatBot
# 🤖 AI Chatbot with Django & PyTorch

This is  AI chatbot built using **Python, PyTorch, Django, and JavaScript**.

---

## **🚀 Installation & Setup**

### **1️⃣ Create and Activate a Virtual Environment**
- `venv/` *(Virtual Environment Folder)*

### **2️⃣ Install Dependencies**
- pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install django djangorestframework nltk numpy

### **3️⃣ Train the Chatbot**
- `train.py` *(Generates `data.pth` file)*

### **4️⃣ Django Backend Setup**
- `chatbot_project/` *(Django Project Folder)*
  - `manage.py` *(Django Command-Line Utility)*
  - `chatbot/` *(Django App)*
    - `views.py` *(Handles API & Chatbot Logic)*
    - `urls.py` *(URL Routing)*
    - `nltk_utils.py` *(Tokenization & NLP Helpers)*
    - `model1.py` *(Neural Network Model)*
    - `intents.json` *(Chatbot Responses & Training Data)*
    - `data.pth` *(Trained Model File)*
    - `templates/chat.html` *(Frontend UI File)*

### **5️⃣ Run the Django Server**
```sh
python manage.py runserver
