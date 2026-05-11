from pathlib import Path

import faiss
import pickle
import numpy as np

from router.model import model


BASE_DIR = Path(__file__).resolve().parent


INDEX_PATH = BASE_DIR / "faiss.index"
MAPPING_PATH = BASE_DIR / "mapping.pkl"


index = faiss.read_index(
    str(INDEX_PATH)
)


with open(MAPPING_PATH, "rb") as f:
    mapping = pickle.load(f)


def route(text: str):

    emb = model.encode([text])

    emb = np.array(
        emb
    ).astype("float32")

    distances, indices = index.search(
        emb,
        k=1
    )

    best_idx = indices[0][0]

    best_intent = mapping[best_idx]

    confidence = float(
        1 / (1 + distances[0][0])
    )

    return {
        "intent": best_intent,
        "confidence": confidence
    }