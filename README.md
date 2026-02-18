# Claim Processing Pipeline Assignment

Sample PDF to process: final.pdf

## Goal
Build a FastAPI service that processes PDF claims using LangGraph to orchestrate document segregation and multi-agent extraction.

## Features
- FastAPI endpoint for PDF claim processing
- LangGraph workflow with an AI-powered segregator and three extraction agents
- Structured extraction using Pydantic schemas
- Request ID middleware and JSON logging
- Docker support for containerized runs

## Tech Stack
- FastAPI
- LangGraph
- LangChain (OpenAI)
- pdfplumber

## API
Endpoint:
- POST /api/process-claim

Input (form-data):
- claim_id (string)
- file (PDF)

Output:
- JSON with extracted data (identity, discharge summary, itemized bill)

Example curl:
```bash
curl -X POST "http://localhost:8000/api/process-claim" \
  -F "claim_id=CLAIM-001" \
  -F "file=@final.pdf"
```

## LangGraph Workflow
Flow:
START -> [Segregator Agent (AI)] -> [ID Agent] -> [Aggregator] -> END
             |                        ^
             |-> [Discharge Summary] -|
             |-> [Itemized Bill] -----|

Nodes:
- Segregator Agent: classifies pages into document types and routes pages to the right agent
- ID Agent: extracts patient identity info
- Discharge Summary Agent: extracts diagnosis, dates, physician details
- Itemized Bill Agent: extracts line items and totals
- Aggregator: combines all agent results into final JSON

Key rule: the segregator routes pages, and only the 3 extraction agents process their assigned pages.

## Project Structure
- app/main.py: FastAPI app setup
- app/api/routes.py: API endpoint
- app/graph/workflow.py: LangGraph workflow definition
- app/agents/: segregator and extraction agents
- app/services/pdf_reader.py: PDF text extraction
- app/services/aggregator.py: final response composer
- app/core/: config, logging, middleware, LLM setup
- app/schemas/: Pydantic schemas for structured outputs

## Configuration
Create a .env file in the project root:
```
OPENAI_API_KEY=your_api_key
LLM_PROVIDER=openai
```

## Run Locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## Run with Docker
```bash
docker build -t claimgraph-ai .
docker run -p 8000:8000 --env-file .env claimgraph-ai
```

## Notes
- Middleware adds X-Request-ID to responses and binds request-scoped logs.
- The segregator uses an LLM with structured output to classify pages.


