from google.adk.agents import Agent
from google.adk.tools.retrieval.vertex_ai_rag_retrieval import VertexAiRagRetrieval
from vertexai.preview import rag

rag_retrieval = VertexAiRagRetrieval(
    name="retrieve_documents",
    description="Retrieve relevant documents from the knowledge base to answer the user's question.",
    rag_resources=[
        rag.RagResource(
            rag_corpus="projects/your-project-id/locations/us-central1/ragCorpora/1234567890"
#replace this 
        )
    ],
    similarity_top_k=10,
    vector_distance_threshold=0.6,
)

root_agent = Agent(
    name="rag_agent",
    model="gemini-2.5-flash",
    description="Answers questions using a private knowledge base.",
    instruction=(
        "You are a helpful assistant. Use the 'retrieve_documents' tool to search "
        "the knowledge base before answering. If the retrieved content doesn't "
        "answer the question, say so rather than guessing."
    ),
    tools=[rag_retrieval],
)
