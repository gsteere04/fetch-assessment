from math import ceil
from app.models.receipt import Receipt

def calculate_points(receipt: Receipt):
    points = 0

    # add one point for every alphanumeric in receipt retailer name
    points += len([c for c in receipt.retailer if c.isalnum()])

    # add 50 points if receipt is a round dollar amount, with no cents
    if float(receipt.total).is_integer():
        points += 50

    # add 25 points if receipt total is a multiple of 0.25
    if float(receipt.total) % 0.25 == 0:
        points += 25

    # add 5 points for every two items on the receipt 
    points += (len(receipt.items) // 2) * 5
    
    # trim the description length, check if it is a multiple of 3,\
    # if it is, multiply item price by 0.2 and round up to nearest integer using ceil.
    # add to total points
    for item in receipt.items:
        description_length = len(item.shortDescription.strip())
        if description_length % 3 == 0:
            points += ceil(float(item.price) * 0.2)
    
    if int(receipt.purchaseDate.split("-")[2]) % 2 != 0:
        points += 6
    
    # add 10 points if time is between 2:00 PM and 4:00 PM
    time = receipt.purchaseTime.split(":")
    hours, _ = map(int, receipt.purchaseDate.split(":"))
    if 14 <= hours < 16:
        points += 10

    return points