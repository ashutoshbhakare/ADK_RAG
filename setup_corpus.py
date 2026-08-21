import vertexai
from vertexai.preview import rag

vertexai.init(project="your-project-id", location="us-central1")

#either use $GOOGLE_CLOUD_PROJECT variable or change the project and location 

# Create the corpus
corpus = rag.create_corpus(display_name="my_knowledge_base")
print(f"Corpus created: {corpus.name}")

# Import documents from GCS
rag.import_files(
    corpus.name,
    ["gs://your-bucket/docs/"],  #replace the bucket name and path ( may varies) 
    chunk_size=512,
    chunk_overlap=100,
)
print("Documents imported.")
