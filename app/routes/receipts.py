from fastapi import APIRouter, HTTPException
from models.receipt import Receipt
from services.points_calculator import calculate_points
from utils.storage import store_receipt, get_points, storage

router = APIRouter()

@router.post("/receipts/process")
async def process_receipt(receipt: Receipt):
    try:
        # Store the receipt and generate an ID
        receipt_id = store_receipt(receipt)

        # Calculate points for the receipt
        points = calculate_points(receipt)

        # Update the entry in storage with the calculated points
        if receipt_id in storage:
            storage[receipt_id]["points"] = points
        else:
            raise HTTPException(
                status_code=500, 
                detail="Internal storage error: Receipt ID not found after storage"
            )

        return {"id": receipt_id}

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=f"Invalid data format: {ve}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")

@router.get("/receipt/{id}/points")
async def get_receipt_points(id: str):
    try:
        # Fetch the points for the given receipt ID
        points = get_points(id)

        if points is None:
            raise HTTPException(
                status_code=404, 
                detail=f"Receipt with ID {id} not found"
            )

        return {"points": points}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")
