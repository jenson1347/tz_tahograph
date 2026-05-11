import faiss
import pickle
import numpy as np

from intents import INTENTS
from model import model


texts = [
    intent["description"]
    for intent in INTENTS
]

embeddings = model.encode(texts)

embeddings = np.array(
    embeddings
).astype("float32")


dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)


faiss.write_index(
    index,
    "faiss.index"
)


mapping = {
    i: intent["intent"]
    for i, intent in enumerate(INTENTS)
}

with open(
    "mapping.pkl",
    "wb"
) as f:

    pickle.dump(mapping, f)

print("INDEX CREATED")