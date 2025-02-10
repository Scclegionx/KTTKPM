from fastapi import FastAPI
from apigateway.book_api import router as book_router
from apigateway.customer_api import router as customer_router
from apigateway.cart_api import router as cart_router

app = FastAPI()

# Đăng ký các router theo từng module
app.include_router(book_router, prefix="/api")
app.include_router(customer_router, prefix="/api")
app.include_router(cart_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "API Gateway is running!"}
