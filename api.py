import os
from fastapi import APIRouter, UploadFile, BackgroundTasks, Request
from fastapi.concurrency import run_in_threadpool

from ingest import ingest_document
from rag import answer_question
from schemas import QuestionRequest
from rate_limiter import limiter

router = APIRouter()

UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
@limiter.limit("5/minute")
async def upload_file(
    request: Request,                
    file: UploadFile,
    background_tasks: BackgroundTasks
):
    filename = os.path.basename(file.filename)
    file_path = os.path.join(UPLOAD_DIR, filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    background_tasks.add_task(ingest_document, file_path)

    return {"message": "Document uploaded and processing started"}


@router.post("/ask")
@limiter.limit("10/minute")
async def ask_question(
    request: Request,                # 👈 REQUIRED
    body: QuestionRequest
):
    answer = await run_in_threadpool(
        answer_question,
        body.question
    )

    return {"answer": answer}
