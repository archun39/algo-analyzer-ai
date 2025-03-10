from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router
from dotenv import load_dotenv
import os

app = FastAPI(title="Algorithm Analyzer AI")

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Spring Boot 서버
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 루트 경로 핸들러 추가
@app.get("/")
async def root():
    return {"message": "Algorithm Analyzer AI API"}

# API 라우터 등록
app.include_router(router, prefix="/api")
