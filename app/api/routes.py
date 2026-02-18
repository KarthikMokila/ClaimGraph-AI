from fastapi import UploadFile, APIRouter, File, Form, HTTPException
from app.services.pdf_reader import extract_pages
from app.graph.workflow import run_claim_workflow

router = APIRouter(prefix = "/api")

@router.post("/process-claim")
async def process_claim(
    file: UploadFile = File(...),
    claim_id: str = Form(...)
):
    
    try:
        if not file.filename.endswith(".pdf"):
            raise HTTPException(status_code=400, detail = "Only pdf files are allowed")
        
        pages = await extract_pages(file)
        if not pages:
            raise HTTPException(status_code=400, detail = "Failed to extract pages from the PDF or PDF is empty")
        
        result = await run_claim_workflow(claim_id, pages)

        return result
     
    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(status_code=500, detail = f"An error occurred while processing the claim: {str(e)}")



