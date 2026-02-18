from fastapi import UploadFile, APIRouter, File, Form
from app.services.pdf_reader import extract_pages
from app.graph.workflow import run_claim_workflow

router = APIRouter(prefix = "/api")

@router.post("/process-claim")
async def process_claim(
    file: UploadFile = File(...),
    claim_id: str = Form(...)
):
    pages = await  extract_pages(file)
    result = await run_claim_workflow(claim_id, pages)

    return result



