from django.shortcuts import render
import torch
import json
import random
import numpy as np
from django.http import JsonResponse
from rest_framework.decorators import api_view
from chatbot.nltk_utils import bag_of_words, tokenize
from chatbot.model1 import NeuralNet
from django.shortcuts import render

def chatbot_page(request):
    return render(request, "chat.html")  # Make sure chat.html exists


def chatbot_page(request):
    return render(request, "chat.html")

import os

# Get the absolute path of the `intents.json` file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INTENTS_FILE = os.path.join(BASE_DIR, "intents.json")

# Load intents file
with open(INTENTS_FILE, 'r', encoding='utf-8') as f:
    intents = json.load(f)

import os

# Get absolute path of `data.pth`
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_FILE = os.path.join(BASE_DIR, "data.pth")

# Load trained model
data = torch.load(MODEL_FILE)



# Load intents file
#with open('intents.json', 'r') as f:
    #intents = json.load(f)

# Load trained model
#FILE = "data.pth"
#data = torch.load(FILE)

# Extract model parameters
input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

# Initialize model
model = NeuralNet(input_size, hidden_size, output_size)
model.load_state_dict(model_state)
model.eval()

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

@api_view(["POST"])
def chatbot_response(request):
    user_message = request.data.get("message", "")

    if not user_message:
        return JsonResponse({"response": "Please enter a message."})

    # Tokenize and create bag of words
    sentence = tokenize(user_message)
    X = bag_of_words(sentence, all_words)
    X = torch.from_numpy(X).to(device)

    # Predict intent
    output = model(X)
    _, predicted = torch.max(output, dim=0)
    tag = tags[predicted.item()]

    # Get response
    response = "I don't understand."
    for intent in intents["intents"]:
        if tag == intent["tag"]:
            response = random.choice(intent["responses"])
            break

    return JsonResponse({"response": response})

