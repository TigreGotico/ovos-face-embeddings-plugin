# FaceEmbeddingsRecognitionPlugin

The `FaceEmbeddingsRecognitionPlugin` is a plugin designed for recognizing and managing face embeddings. It extends the `FaceEmbeddingsRecognizer` class from the `ovos_plugin_manager` template and integrates with the `ChromaEmbeddingsDB` for storing and retrieving face embeddings. The plugin utilizes the `face_recognition` library to generate face embeddings from image frames.

## Features

- **Face Embeddings Extraction**: Converts images into face embeddings using the `face_recognition` library.
- **Face Data Storage**: Stores and retrieves face embeddings using `ChromaEmbeddingsDB`.
- **Face Data Management**: Provides methods to add, query, and delete face embeddings associated with user IDs.

**Note:** `face_recognition` also requires `dlib`, which may require additional setup. Please refer to the [face_recognition installation instructions](https://github.com/ageitgey/face_recognition#installation) for detailed steps.

## Usage

Here is a quick example of how to use the `FaceEmbeddingsRecognitionPlugin`:

```python
from ovos_face_embeddings import FaceEmbeddingsRecognitionPlugin
import face_recognition

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
```
