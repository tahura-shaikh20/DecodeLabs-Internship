from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load dataset
data = load_iris()
X = data.data
y = data.target

print("Dataset loaded successfully")
print("Total samples:", len(X))
print("Features:", data.feature_names)
print("Target classes:", data.target_names)
print("-" * 50)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))
print("-" * 50)

# Create model
model = DecisionTreeClassifier()

# Train model
model.fit(X_train, y_train)
print("Model training completed")
print("-" * 50)

# Make predictions
y_pred = model.predict(X_test)

# Show sample predictions
print("Sample Predictions vs Actual:")
for i in range(5):
    print(f"Predicted: {y_pred[i]}, Actual: {y_test[i]}")
print("-" * 50)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)
print("-" * 50)

# Confusion Matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("-" * 50)

# Classification Report
print("Classification Report:")
print(classification_report(y_test, y_pred))