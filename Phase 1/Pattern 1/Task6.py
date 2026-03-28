'''class Address(BaseModel):
    city: str
    country: str

class Person(BaseModel):
    name: str
    address: Address    # Address is nested inside Person
```
When you do this, Pydantic validates the nested object too — automatically, all the way down.
---
## Exercise
Build this structure for a RAG pipeline context — you'll actually use something like this in Phase 5:
```
ChunkMetadata
    - source: str
    - page_number: int
    - is_verified: bool = False
Document
    - doc_id: str
    - title: str
    - content: str
    - metadata: ChunkMetadata        ← nested model
    - tags: list[str] = []'''

from pydantic import BaseModel
from typing import Optional

class ChunkMetadata(BaseModel):
    source: str
    page_number: int
    is_verified: bool = False
class Document(BaseModel):
    doc_id: str
    title: str
    content: str
    metadata: ChunkMetadata
    tags: list[str] = []

data = {"doc_id": "170x",
        "title": "Physics",
        "content": "Physics is the science of the world",
        "metadata": {"source": "HC Verma",
                        "page_number": 104,
                        "is_verified": True},
        "tags": ['Physics', 'Science']
                        }
D = Document.model_validate(data)
print(D)

# Test 1 — passing nested object directly
meta = ChunkMetadata(source="textbook.pdf", page_number=5)
doc = Document(doc_id="001", title="AI Basics", content="Neural networks...", metadata=meta)
print(doc.model_dump())

# Test 2 — passing nested dict via model_validate (this is the real world case)
data = {
    "doc_id": "002",
    "title": "RAG Systems",
    "content": "Retrieval augmented...",
    "metadata": {"source": "paper.pdf", "page_number": 12, "is_verified": True}
}
doc2 = Document.model_validate(data)
print(doc2.metadata.source)      # should print: paper.pdf
print(doc2.metadata.page_number) # should print: 12

             
             
