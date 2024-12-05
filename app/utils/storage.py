import uuid
from models.receipt import Receipt


storage = {}

def store_receipt(receipt: Receipt, points=None):
    receipt_id = str(uuid.uuid4())
    storage[receipt_id] = {"receipt": receipt.model_dump(), "points": points}
    return receipt_id

def get_points(receipt_id):
    if receipt_id in storage:
        return storage[receipt_id]["points"]
    return None