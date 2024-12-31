# GitHub User Activity CLI

A simple command-line interface (CLI) application that fetches and displays the recent activity of a GitHub user using the GitHub API. This project is designed to help you practice working with APIs, handling JSON data, and building a user-friendly CLI.

---

## Features

- **Fetch User Activity**: Retrieve and display recent events for a specified GitHub user.
- **Error Handling**: Gracefully manage invalid usernames or API failures.
- **Simple CLI**: Accept GitHub usernames as input and display formatted activity directly in the terminal.

---

## How It Works

1. **Input**: Enter a GitHub username when prompted by the CLI.
2. **Fetch**: The application retrieves the user's recent activity from the GitHub API using the `/users/{username}/events` endpoint.
3. **Output**: Displays the latest events, such as:
   - Push events with commit details.
   - Issues created or updated.
   - Repositories starred.

Link to Project - [https://roadmap.sh/projects/github-user-activity](https://roadmap.sh/projects/github-user-activity)