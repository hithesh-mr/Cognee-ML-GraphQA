import cognee
from cognee.api.v1.visualize import visualize_graph
from dotenv import load_dotenv
import asyncio
import pathlib

load_dotenv()

input_text = ["ML-Textbooks/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf", "ML-Textbooks/Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron.pdf", "ML-Textbooks/Elements of Statistical Learning.pdf", "ML-Textbooks/Deep Learning by Ian Goodfellow, Yoshua Bengio, Aaron Courville (z-lib.org).pdf"]


async def main():
    # First we'll clean any old data and resets system metadata so we start from a blank slate.
    await cognee.prune.prune_data()
    await cognee.prune.prune_system(metadata=True)

    # Add text to cognee
    await cognee.add(input_text)

    # Generate the knowledge graph
    await cognee.cognify()

    # Visualize the knowledge graph
    output_dir = pathlib.Path("artifacts")
    output_dir.mkdir(parents=True, exist_ok=True)
    graph_file_path = (output_dir / "graph_visualization.html").resolve()

    print(f"Saving graph visualization to: {graph_file_path}")
    await visualize_graph(str(graph_file_path))
    print("Graph visualization saved successfully.")


if __name__ == '__main__':
    asyncio.run(main())

