import asyncio
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
import httpx #async http client for external APIs

app = FastAPI(title = "Internal Operations")

#schemas
class SupportPayload(BaseModel):
    ticket_id: int
    raw_transcript: str = Field(..., min_length=10)

class AutomatedResolution(BaseModel):
    category: str
    priority: str
    suggested_action: str

#auth
async def verify_internal_jwt(token: str = "secure-internal-token"):
    if not token:
        raise HTTPException(status_code=401, detail="Invalid internal credentials")
    return token

#routes
@app.post("/api/v1/operations/triage", response_model=AutomatedResolution)
async def triage_customer_issue(
    payload: SupportPayload,
    token: str = Depends(verify_internal_jwt)
):
    """
    Parses customer transcripts and routes them to the correct internal team.
    Will eventually connect to an LLM API for automated tagging.
    """

    async with httpx.AsyncClient() as client:
        #simulate latency
        await asyncio.sleep(0.1) 
        
        #simple keyword matching for triage fallback
        if "invoice" in payload.raw_transcript.lower():
            return {
                "category": "BILLING",
                "priority": "MEDIUM",
                "suggested_action": "Route to accounts team; flag invoice lock out."
            }
        elif "hack" in payload.raw_transcript.lower() or "malware" in payload.raw_transcript.lower():
            return {
                "category": "MALWARE",
                "priority": "HIGH",
                "suggested_action": "Inform security team, isolate container."
            }
        
        return {
            "category": "TECH_SUPPORT",
            "priority": "LOW",
            "suggested_action": "Assign to regional hosting engineering queue."
        }