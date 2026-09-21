"""Day 10 - API Data Explorer"""

import json
import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"
FILE_NAME = "saved_posts.json"


class ApiClient:
    def __init__(self, url=API_URL):
        self.url = url

    def get_post(self, post_id):
        try:
            response = requests.get(f"{self.url}/{post_id}", timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.Timeout:
            print("Request timed out. Please try again.")
        except requests.HTTPError as error:
            print("API error:", error)
        except requests.RequestException as error:
            print("Request failed:", error)
        except ValueError:
            print("Invalid JSON response.")
        return None


class PostExplorer:
    def __init__(self):
        self.api = ApiClient()
        self.saved_posts = self.load_saved_posts()

    def load_saved_posts(self):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data if isinstance(data, list) else []
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_posts(self):
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(self.saved_posts, file, indent=4)

    def show_post(self, post):
        print("\n--- Post ---")
        print("ID:", post["id"])
        print("User ID:", post["userId"])
        print("Title:", post["title"])
        print("Body:", post["body"])

    def fetch_and_show(self):
        try:
            post_id = int(input("Enter post ID (1-100): ").strip())
            if not 1 <= post_id <= 100:
                print("Please enter an ID from 1 to 100.")
                return
        except ValueError:
            print("Please enter a valid number.")
            return

        post = self.api.get_post(post_id)

        if post:
            self.show_post(post)

            save = input("Save this post? (y/n): ").strip().lower()
            if save == "y":
                if any(item["id"] == post["id"] for item in self.saved_posts):
                    print("Post is already saved.")
                else:
                    self.saved_posts.append(post)
                    self.save_posts()
                    print("Post saved successfully.")

    def view_saved_posts(self):
        if not self.saved_posts:
            print("No saved posts.")
            return

        print("\n--- Saved Posts ---")
        for post in self.saved_posts:
            print(f"{post['id']}. {post['title']}")


def show_menu():
    print("\n===== API Data Explorer =====")
    print("1. Fetch post")
    print("2. View saved posts")
    print("3. Exit")


def main():
    explorer = PostExplorer()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            explorer.fetch_and_show()
        elif choice == "2":
            explorer.view_saved_posts()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-3.")


if __name__ == "__main__":
    main()
