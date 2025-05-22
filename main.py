from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Order(BaseModel):
    order_id: str
    item: str
    quantity: int
    customer: Optional[str] = None

@app.post("/order")
def create_order(order: Order):
    return {
        "status": "received",
        "order_ref": order.order_id,
        "details": order
    }