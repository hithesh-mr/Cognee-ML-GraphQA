from dotenv import load_dotenv
import os
import cognee
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

@app.get("/textbooks")
async def get_textbooks():
    """Return a list of PDF files from the ML-Textbooks directory."""
    textbook_dir = "ML-Textbooks"
    try:
        files = [f for f in os.listdir(textbook_dir) if f.lower().endswith('.pdf')]
        return {"textbooks": files}
    except FileNotFoundError:
        return {"error": "Textbooks directory not found."}

@app.get("/search")
async def search(query: str):
    """Perform a search using Cognee and return the results."""
    try:
        print(f"Received search query: {query}")
        results = await cognee.search(query)
        print(f"Found {len(results)} results.")
        return {"results": results}
    except Exception as e:
        print(f"An error occurred during search: {e}")
        return {"error": str(e)}

@app.on_event("startup")
async def startup_event():
    """A simple startup event to confirm the server is running."""
    print("FastAPI server started. Cognee is ready for queries.")
    # Assuming cognee is already initialized and the graph is built.

# Mount static files after API routes are defined
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/artifacts", StaticFiles(directory="artifacts"), name="artifacts")

@app.get("/")
async def read_root():
    return FileResponse('index.html')

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)