import os
from whoosh.fields import Schema, TEXT, ID
from whoosh.index import create_in
from whoosh.qparser import QueryParser

# Define the schema
schema = Schema(
    title=TEXT(stored=True),  # Title field (stored for retrieval)
    content=TEXT,            # Content field (searchable)
    path=ID(stored=True)     # Path field (stored for retrieval)
)

# Create index directory
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

# Create the index
ix = create_in("indexdir", schema)

# Add documents to the index
writer = ix.writer()

# Example documents
writer.add_document(title="Whoosh Intro", content="Whoosh is a fast library for indexing and searching text.", path="/intro")
writer.add_document(title="Search Engines", content="Search engines retrieve information from a dataset.", path="/search")
writer.add_document(title="Python Programming", content="Python is a versatile programming language.", path="/python")

writer.commit()  # Save changes

# Open the index for searching
with ix.searcher() as searcher:
    # Parse a search query
    query = QueryParser("content", ix.schema).parse("programming")
    
    # Perform the search
    results = searcher.search(query)
    
    # Display results
    for result in results:
        print(f"Title: {result['title']}, Path: {result['path']}")
