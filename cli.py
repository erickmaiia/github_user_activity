import requests

class CLI:

    def list_activity(self, user):
        url = f"https://api.github.com/users/{user}/events"

        try:
            # Making a GET request
            response = requests.get(url)

            # Check if the request was successful
            if response.status_code == 200:
                events = response.json()

                print(f"Latest activities for user '{user}':")
                for event in events[:3]:  # Limit to the last 3 events
                    event_type = event.get("type", "Unknown Event")
                    repo_name = event.get("repo", {}).get(
                        "name", "Unknown Repository")

                    if event_type == "PushEvent":
                        commits = event.get("payload", {}).get("commits", [])
                        print(f"- [PUSH] {len(commits)
                                          } commit(s) pushed to {repo_name}.")
                    elif event_type == "IssuesEvent":
                        action = event.get("payload", {}).get(
                            "action", "unknown action")
                        issue_title = event.get("payload", {}).get(
                            "issue", {}).get("title", "Unknown Title")
                        print(
                            f"- [ISSUE] '{issue_title}' was {action} in {repo_name}.")
                    elif event_type == "WatchEvent":
                        print(f"- [STAR] Starred the repository {repo_name}.")
                    else:
                        print(f"- [{event_type}] Action in {repo_name}.")
            else:
                print(f"Request failed with status code: {
                      response.status_code}")
        except requests.RequestException as e:
            print(f"Error while making the request: {e}")
