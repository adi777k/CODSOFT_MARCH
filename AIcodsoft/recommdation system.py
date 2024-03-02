import tkinter as tk
from tkinter import messagebox

# Sample user-item ratings matrix (can be replaced with real data)
user_item_ratings = {
    'user1': {'The Great Gatsby': 5, 'To Kill a Mockingbird': 4, '1984': 0, 'The Godfather': 5, 'Pulp Fiction': 4},
    'user2': {'The Catcher in the Rye': 4, 'To Kill a Mockingbird': 0, 'Fahrenheit 451': 0, 'The Godfather': 4, 'Pulp Fiction': 5},
    'user3': {'The Great Gatsby': 0, '1984': 4, 'Animal Farm': 5, 'The Godfather': 4, 'Pulp Fiction': 3},
    'user4': {'The Catcher in the Rye': 0, 'Fahrenheit 451': 0, 'Brave New World': 4, 'Pulp Fiction': 3, 'The Shawshank Redemption': 4}
}



# Function to calculate similarity between users using cosine similarity
def cosine_similarity(user1_ratings, user2_ratings):
    common_items = set(user1_ratings.keys()) & set(user2_ratings.keys())
    if len(common_items) == 0:
        return 0
    numerator = sum(user1_ratings[item] * user2_ratings[item] for item in common_items)
    denominator1 = sum(user1_ratings[item] ** 2 for item in user1_ratings)
    denominator2 = sum(user2_ratings[item] ** 2 for item in user2_ratings)
    return numerator / (denominator1 ** 0.5 * denominator2 ** 0.5)

# Function to recommend items to a target user
def recommend_items(target_user, user_item_ratings, num_recommendations=3):
    if target_user not in user_item_ratings:
        return []  # Return an empty list if the target user is not found

    target_ratings = user_item_ratings[target_user]
    similarities = {}
    for user, ratings in user_item_ratings.items():
        if user != target_user:
            similarity = cosine_similarity(target_ratings, ratings)
            similarities[user] = similarity
    
    recommendations = []
    for item in target_ratings:
        if target_ratings[item] == 0:
            # Predict ratings for unrated items
            predicted_rating = sum(user_item_ratings[user].get(item, 0) * similarities[user] for user in user_item_ratings if user != target_user) / sum(similarities.values())
            recommendations.append((item, predicted_rating))
    
    # Sort recommendations by predicted rating in descending order
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations[:num_recommendations]


# Function to display recommendations
def display_recommendations():
    target_user = user_entry.get().strip()
    if not target_user:
        messagebox.showerror("Error", "Please enter a user.")
        return
    
    if target_user not in user_item_ratings:
        messagebox.showerror("Error", f"User '{target_user}' not found.")
        return
    
    recommendations = recommend_items(target_user, user_item_ratings)
    if not recommendations:
        messagebox.showinfo("Info", f"No recommendations found for user '{target_user}'.")
        return
    
    recommendation_text.delete('1.0', tk.END)
    for item, rating in recommendations:
        recommendation_text.insert(tk.END, f"{item}: Predicted Rating - {rating:.2f}\n")

# Create Tkinter window
window = tk.Tk()
window.title("Recommendation System")

# GUI elements
user_label = tk.Label(window, text="Enter User:")
user_label.grid(row=0, column=0, padx=10, pady=10)

user_entry = tk.Entry(window)
user_entry.grid(row=0, column=1, padx=10, pady=10)

recommend_button = tk.Button(window, text="Get Recommendations", command=display_recommendations)
recommend_button.grid(row=1, columnspan=2, padx=10, pady=10)

recommendation_text = tk.Text(window, width=40, height=10)
recommendation_text.grid(row=2, columnspan=2, padx=10, pady=10)

# Run the Tkinter event loop
window.mainloop()
