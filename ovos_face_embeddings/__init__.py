import face_recognition
import numpy as np
from ovos_chromadb_embeddings import ChromaEmbeddingsDB
from ovos_plugin_manager.templates.embeddings import FaceEmbeddingsRecognizer


class FaceEmbeddingsRecognitionPlugin(FaceEmbeddingsRecognizer):
    def __init__(self, thresh: float = 0.75):
        path = "/tmp/face_db"  # TODO
        db = ChromaEmbeddingsDB(path)
        super().__init__(db, thresh)

    def get_face_embeddings(self, frame: np.ndarray) -> np.ndarray:
        return face_recognition.face_encodings(frame)[0]


if __name__ == "__main__":
    # Example usage:
    a = "/home/miro/PycharmProjects/ovos-user-id/a1.jpg"
    a2 = "/home/miro/PycharmProjects/ovos-user-id/a2.jpg"
    b = "/home/miro/PycharmProjects/ovos-user-id/b.jpg"

    f = FaceEmbeddingsRecognitionPlugin()

    e1 = face_recognition.load_image_file(a)
    e2 = face_recognition.load_image_file(a2)
    b = face_recognition.load_image_file(b)

    f.add_face("arnold", e1)
    f.add_face("silvester", b)
    print(f.query(e1))
    print(f.query(e2))
    print(f.query(b))

