import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

app = FastAPI()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

class QuestionRequest(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "Groq FastAPI server is running"}

@app.post("/ask")
def ask_question(request: QuestionRequest):
    try:
        chat_completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": request.question
                }
            ],
        )

        answer = chat_completion.choices[0].message.content

        return {"answer": answer}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))