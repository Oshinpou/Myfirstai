=============================

AI WEBSITE USING PYTHON (FLASK)

Includes UI/UX with HTML + CSS

=============================

from flask import Flask, render_template, request, jsonify import random

app = Flask(name)

-----------------------------

SIMPLE AI RESPONSE FUNCTION

-----------------------------

def ai_response(user_input): responses = [ "That's interesting! Tell me more.", "I understand. Here's a smart suggestion.", "Let me think about that for you.", "Great question! Here's something useful.", "I can help you build something amazing." ] return random.choice(responses)

-----------------------------

ROUTES

-----------------------------

@app.route('/') def home(): return render_template('index.html')

@app.route('/chat', methods=['POST']) def chat(): user_input = request.json.get("message") reply = ai_response(user_input) return jsonify({"reply": reply})

-----------------------------

RUN SERVER

-----------------------------

if name == 'main': app.run(debug=True)

=============================

HTML TEMPLATE (templates/index.html)

=============================

"""

<!DOCTYPE html><html>
<head>
    <title>AI Website</title>
    <style>
        body {
            font-family: Arial;
            background: linear-gradient(135deg, #1e1e2f, #2a2a40);
            color: white;
            text-align: center;
        }
        .chat-box {
            width: 60%;
            margin: auto;
            background: #333;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 0 20px rgba(0,0,0,0.5);
        }
        input {
            width: 70%;
            padding: 10px;
            border-radius: 10px;
            border: none;
        }
        button {
            padding: 10px 20px;
            border: none;
            border-radius: 10px;
            background: #ff4b2b;
            color: white;
            cursor: pointer;
        }
        .messages {
            margin-top: 20px;
            text-align: left;
        }
        .user { color: #00ffcc; }
        .ai { color: #ffcc00; }
    </style>
</head>
<body><h1>AI Chat Website</h1><div class="chat-box">
    <input id="message" placeholder="Type your message...">
    <button onclick="sendMessage()">Send</button><div class="messages" id="messages"></div>

</div><script>
function sendMessage() {
    let message = document.getElementById("message").value;

    fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {
        let chat = document.getElementById("messages");
        chat.innerHTML += `<p class='user'>You: ${message}</p>`;
        chat.innerHTML += `<p class='ai'>AI: ${data.reply}</p>`;
    });
}
</script></body>
</html>
"""=============================

HOW TO RUN

=============================

1. Install Flask: pip install flask

2. Create folder 'templates'

3. Save HTML inside templates/index.html

4. Run: python main.py
