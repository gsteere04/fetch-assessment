# Fetch Assessment - Receipt Processor API

The **Receipt Processor API** is a FastAPI-based web service that processes receipts (provided as JSON objects), assigns a unique identifier (UUID) to each receipt, and calculates points based on a predefined set of rules. The points for a specific receipt can be retrieved using the generated UUID.

## Instructions to Run
- **Clone the Repository**
  ```
  git clone <repository_url>
  cd <repository_directory>
  ```

- **Build the Docker Image**
  Build the application Docker image using the DockerFile
  ```
  docker build -t fetch-assessment .
  ```

  -**Run the Application Container**
  ```
  docker run -d -p 8000:8000 --name fetch-assessment fetch-assessment
  ```
  This maps port 8000 in the container to port 8000 on your local machine.

  -**Verify the Application is running**
  1.  Base URL: http://127.0.0.1:8000
  2.  Interactive Docs: http://127.0.0.1:8000/docs
  3.  Redoc Docs: http://127.0.0.1:8000/redoc
  
## Key Features
- **Receipt Submission**: Accepts receipts in JSON format via a POST endpoint.
- **Unique Receipt ID**: Assigns a UUID to each receipt for later retrieval.
- **Points Calculation**: Automatically calculates points based on specific criteria from the receipt data.
- **Points Retrieval**: Allows retrieval of the calculated points for a specific receipt via a GET endpoint.

## Points Calculation Rules
The points are awarded based on the following criteria:
1. **Retailer Name**: One point for every alphanumeric character in the retailer's name.
2. **Round Dollar Total**: 50 points if the total amount is a round dollar value (e.g., `$10.00`).
3. **Multiples of $0.25**: 25 points if the total amount is a multiple of $0.25.
4. **Item Count**: 5 points for every two items on the receipt.
5. **Item Description Length**: For items with a description length that is a multiple of 3, points equal to 20% of the item's price are awarded (rounded up).
6. **Purchase Date**: 6 points if the day of the purchase date is an odd number.
7. **Purchase Time**: 10 points if the purchase time is between 2:00 PM and 4:00 PM.

## API Endpoints

### 1. Process Receipt
**POST** `/receipts/process`

- **Request Body**: JSON representation of the receipt.
- **Response**: A JSON object containing the UUID of the processed receipt.
- **Example Response**:
  ```json
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
  }

### 2. Retrieve Points
**GET** `/receipts/{id}/points`

- **Path Parameter**: The UUID of the receipt.
- **Response**: A JSON object containing the points awarded for the receipt.
- **Example Response**:
  ```json
  {
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6" 
  }

### Usage
1. Submit a receipt using the /receipts/process endpoint to generate a UUID.
2. Use the UUID with the /receipt/{id}/points endpoint to retrieve the points.

### Technologies Used
**Backend**: FastAPI, Python
**Storage**: In-memory dictionary (for simplicity, but can be extended to a database)
**Unique ID**: UUID for receipt identification

This API is designed to demonstrate robust receipt processing and point calculation functionality while maintaining simplicity and efficiency.
