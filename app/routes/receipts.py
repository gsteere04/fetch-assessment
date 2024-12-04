from fastapi import APIRouter, HTTPException
from app.models.receipt import Receipt
from app.services.points_calculator import calculate_points
from app.utils.storage import store_receipt, get_points

router = APIRouter()

@router.post("/receipts/process")
async def process_receipt(receipt: Receipt):
    receipt_id = store_receipt(receipt)
    points = calculate_points(receipt)
    store_receipt(receipt, points)
    return {"id": receipt_id}

@router.get("receipt/{id}/points")
async def get_receipt_points(id: str):
    points = get_points(id)
    if points is None:
        raise HTTPException(status_code=404, detail="Receipt not found")
    return {"points": points}