from fastapi import FastAPI

app = FastAPI()

@app.get("/api/python")
def hello_world():
    return {"message": "Hello from Python on Vercel!"}

@app.get("/api/chat")
def chat(prompt: str):
    # Put your AI logic here
    return {"response": f"AI says: I received {prompt}"}
