from plugin import Plugin
import requests
from generalMethods import write_to_json_file

# Implementation for the dummyapi.io specific plugin


class DummyIOConfig(Plugin):
    # Initialing the configuration with the specific info
    def __init__(self,key):
        self.key = key
        self.check_connection_endpoint = "https://dummyapi.io/data/v1/user"
        self.post_list_endpoint = "https://dummyapi.io/data/v1/post?limit=50"


class DummyIOPlugin(Plugin):
    def __init__(self, key):
        super().__init__(DummyIOConfig(key))

    # Collect the list of all users in the system
    def user_list(self, limit, page):
        print(f"Getting all users from API, page {page}")
        # TODO: for that fetch 5 pages and returns the list of users
        response = requests.get(f"{self.config.check_connection_endpoint}?page={page}&limit={limit}",
                                headers={"app-id": self.config.key})
        write_to_json_file(response.json(), "user_list", 'w')

    # Collect a List of all posts, including each post’s comments
    def post_list(self):

        pos_data = requests.get("https://dummyapi.io/data/v1/post?limit=50", headers={"app-id": self.config.key})
        post_comments = []
        posts_data = pos_data.json()
        # Organize comments data by post_id
        for post in posts_data["data"]:
            write_to_json_file("The post:", "posts_list", "a")
            write_to_json_file(post, "posts_list", "a")
            post_id = post["id"]
            url_comments_endpoint = "https://dummyapi.io/data/v1/post/" + post_id + "/comment"
            comments = requests.get(url_comments_endpoint, headers={"app-id": self.config.key})
            comments_data = comments.json()
            # Collecting the relevant comments
            for comment in comments_data["data"]:
                post_comments += [comment["message"]]
            write_to_json_file("The comments:", "posts_list", "a")
            write_to_json_file(post_comments, "posts_list", "a")


