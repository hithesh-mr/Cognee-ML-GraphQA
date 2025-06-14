# Cognee ML Knowledge Graph Q&A

This project demonstrates the power of the `cognee` library to build a sophisticated Knowledge Graph from a collection of Machine Learning textbooks. It provides a web-based interface to visually explore the interconnected concepts and ask complex questions in natural language, receiving answers synthesized directly from the source texts.

The application can render complex mathematical equations and markdown formatting for a clean and readable user experience.

## Demo

![Cognee ML Knowledge Graph Demo](https://github.com/user-attachments/assets/0deb3b53-a25a-437f-9cc3-be9a956e1070)

## Project Architecture

The project follows a simple client-server architecture:

-   **Backend**: A Python server built with **FastAPI** that handles the core logic. It uses the `cognee` library to interact with the pre-built knowledge graph.
-   **Frontend**: A vanilla JavaScript, HTML, and CSS single-page application that provides the user interface for querying the knowledge graph.
-   **Knowledge Graph**: The graph is generated offline by the `knowledge_graph.py` script, which processes PDF textbooks from the `ML-Textbooks` directory.

### File Interaction Diagram

Here is a simple diagram illustrating how the components interact:

```
[User] <--> [Browser: index.html, scripts.js, styles.css]
   |
   |-- (1) Asks question --> [FastAPI Server: app.py]
   |                                  |
   |                                  |-- (2) Calls cognee.search() --> [Knowledge Graph]
   |                                  |
   |-- (4) Receives formatted answer <-|-- (3) Returns results -------- [FastAPI Server: app.py]
```

## Key Technologies & Libraries

### Backend (Python)
-   **[Cognee](https://github.com/cognee-ai/cognee)**: The core engine for building and querying the knowledge graph from unstructured text.
-   **FastAPI**: A modern, high-performance web framework for building APIs.
-   **Uvicorn**: A lightning-fast ASGI server, used to run the FastAPI application.
-   **python-dotenv**: For managing environment variables (like API keys).

### Frontend
-   **HTML/CSS/JavaScript**: The standard trio for building the web interface.
-   **[KaTeX](https://katex.org/)**: A fast, easy-to-use JavaScript library for TeX math rendering on the web.

## Setup and Installation

Follow these steps to get the project up and running on your local machine.

### 1. Prerequisites
-   Python 3.8+
-   `pip` for package management

### 2. Clone the Repository
```bash
git clone <your-repository-url>
cd <repository-directory>
```

### 3. Set Up a Virtual Environment
It's highly recommended to use a virtual environment to manage project dependencies.
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
Create a `requirements.txt` file with the following content:
```txt
cognee
fastapi
uvicorn[standard]
python-dotenv
```
Then, install the packages:
```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables
The `cognee` library requires an OpenAI API key to function. Create a file named `.env` in the root of the project directory and add your key:
```
OPENAI_API_KEY="your-openai-api-key-here"
```

### 6. Add Textbooks
Place your PDF textbooks into the `ML-Textbooks` directory. The project currently uses:
-   `Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf`
-   `Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron.pdf`
-   `Elements of Statistical Learning.pdf`
-   `Deep Learning by Ian Goodfellow, Yoshua Bengio, Aaron Courville (z-lib.org).pdf`

### 7. Build the Knowledge Graph
This is a one-time step to process the textbooks and build the graph. Run the script from the root directory:
```bash
python knowledge_graph.py
```
This process may take some time depending on the size of your documents. Upon completion, it will generate a `graph_visualization.html` file in the `artifacts` directory.

### 8. Run the Application
Start the FastAPI server:
```bash
python app.py
```
Once the server is running, open your web browser and navigate to:
[http://localhost:8000](http://localhost:8000)

You should now see the application interface and be able to ask questions!

## How It Works

1.  **Data Ingestion (Offline)**: The `knowledge_graph.py` script reads the PDFs from the `ML-Textbooks` folder, uses `cognee` to extract concepts and relationships, and builds the knowledge graph.
2.  **Serving the Frontend**: When you access the root URL, `app.py` serves the `index.html` file.
3.  **Fetching Textbooks**: The frontend `scripts.js` makes a call to the `/textbooks` endpoint to list the source documents.
4.  **User Query**: The user types a question and clicks "Search."
5.  **Backend Processing**: The frontend sends the query to the `/search` endpoint. The FastAPI server receives this, passes it to `cognee.search()`, and gets the relevant information from the knowledge graph.
6.  **Displaying Results**: The results are sent back to the frontend, where `scripts.js` formats the text—handling markdown for headings, bold text, and using KaTeX to render any LaTeX equations—before displaying it to the user.
