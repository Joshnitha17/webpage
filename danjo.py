


pip install Django
django-admin startproject myproject
cd myproject
pip install Flask
mkdir myproject
cd myproject
touch app.py
from django.http import JsonResponse
import datetime
import os

def htop(request):
    data = {
        "Name": "Your Full Name",
        "Username": os.getenv("USER"),
        "Server Time": datetime.datetime.now().astimezone().isoformat(),
    }
    return JsonResponse(data)
from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/htop')
def htop():
    data = {
        "Name": "Your Full Name",
        "Username": os.getenv("USER"),
        "Server Time": datetime.now().isoformat(),
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)






