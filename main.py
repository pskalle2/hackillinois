import pandas as pd
def recommend_classes(user_input):
    classes_recommendations = {
        "programming": ["Introduction to Programming", "Advanced Python", "Java Basics"],
        "web development": ["HTML/CSS Basics", "JavaScript Fundamentals", "Full-Stack Web Development"],
        "data science": ["Introduction to Data Science", "Machine Learning Fundamentals", "Data Visualization"],
        "AI/ML": ["Networking Basics", "Cisco Certified Network Associate (CCNA)"],
        "cybersecurity": ["Cybersecurity Fundamentals", "Ethical Hacking", "Security+ Certification"],
    }

    recommended_classes = []
    
    for preference in user_input:
        if preference.lower() in classes_recommendations:
            recommended_classes.extend(classes_recommendations[preference.lower()])
    
    return recommended_classes

def main():
    print("Welcome to the Computer Classes Recommender!")
    print("Available preferences: programming, web development, data science, AI/ML, cybersecurity")

    user_input = input("Enter your preferences (comma-separated): ").split(',')

    recommendations = recommend_classes(user_input)

    if recommendations:
        print("\nRecommended Classes:")
        for class_name in recommendations:
            print(f"- {class_name}")
    else:
        print("Sorry, no recommendations for the given preferences.")

if __name__ == "__main__":
    main()
