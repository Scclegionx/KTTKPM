from fastapi import APIRouter
import httpx

router = APIRouter()
BOOK_SERVICE_URL = "http://127.0.0.1:8000/api/book"

@router.get("/books/")
async def get_books():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BOOK_SERVICE_URL}/books/")
    return response.json()
