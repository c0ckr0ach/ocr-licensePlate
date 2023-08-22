import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from skimage.feature import hog
import cv2

# Example dataset (images of license plates and their corresponding labels)
# You should replace these with your own dataset
data = [
    {"image": "plate1.jpg", "label": "ABC123"},
    {"image": "plate2.jpg", "label": "XYZ789"},
    # Add more data...
]

# Preprocess images and extract HOG features
def preprocess_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    resized_image = cv2.resize(image, (100, 50))  # Resize to a consistent size
    features = hog(resized_image, pixels_per_cell=(10, 10))  # Extract HOG features
    return features

# Prepare data
X = []
y = []
for item in data:
    features = preprocess_image(item["image"])
    X.append(features)
    y.append(item["label"])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train KNN model
k = 3  # Number of neighbors
knn_model = KNeighborsClassifier(n_neighbors=k)
knn_model.fit(X_train, y_train)

# Predict license plate text using KNN
predictions = knn_model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)

# Example usage: Predict text from a new license plate image
new_image_path = "new_plate.jpg"
new_features = preprocess_image(new_image_path)
predicted_text = knn_model.predict([new_features])[0]
print("Predicted License Plate:", predicted_text)
