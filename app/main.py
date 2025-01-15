from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur la démo de Nexora !"}

@app.post("/chatbot/")
def create_chatbot(name: str, description: str):
    return {"chatbot_name": name, "description": description}
