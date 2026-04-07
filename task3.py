# AI Recommendation System using Jaccard Similarity

def jaccard_similarity(user_interests, item_tags):
    intersection = len(set(user_interests) & set(item_tags))
    union = len(set(user_interests) | set(item_tags))
    return intersection / union if union != 0 else 0


# Take user input
user_input = input("Enter your interests (comma separated): ")
user_interests = [i.strip().lower() for i in user_input.split(",")]

print("\nYour Interests:", user_interests)
print("-" * 50)

# Dataset of items
items = [
    {"name": "Machine Learning Course", "tags": ["python", "machine learning", "ai"]},
    {"name": "Web Development Bootcamp", "tags": ["html", "css", "javascript"]},
    {"name": "Data Science with Python", "tags": ["python", "data visualization", "pandas"]},
    {"name": "AI Fundamentals", "tags": ["ai", "machine learning"]},
    {"name": "Frontend Design Course", "tags": ["web design", "css"]},
    {"name": "Deep Learning Specialization", "tags": ["ai", "deep learning", "python"]},
]

# Recommendation logic
recommendations = []

print("Calculating similarity scores...\n")

for item in items:
    score = jaccard_similarity(user_interests, item["tags"])
    recommendations.append((item["name"], score))
    print(f"{item['name']} -> Score: {score:.2f}")

print("-" * 50)

# Sort recommendations (highest score first)
recommendations.sort(key=lambda x: x[1], reverse=True)

# Display filtered recommendations
print("\nTop Recommendations:")

found = False
for name, score in recommendations:
    if score > 0:
        print(f"{name} (Match Score: {score:.2f})")
        found = True

# If no matches found
if not found:
    print("No strong matches found. Try different interests.")

# Best recommendation
print("-" * 50)
print("Best Match:", recommendations[0][0])
