import requests
import os

def extract_files_from_github(repo_url, extension):
    repo_api_url = repo_url.replace("github.com", "api.github.com/repos")
    response = requests.get(repo_api_url)
    if response.status_code == 200:
        repo_data = response.json()
        repo_name = repo_data["name"]
        repo_owner = repo_data["owner"]["login"]
        files_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents"
        response = requests.get(files_url)
        if response.status_code == 200:
            files_data = response.json()
            for file in files_data:
                if file["type"] == "file" and file["name"].endswith(extension):
                    file_url = file["download_url"]
                    file_content = requests.get(file_url).text
                    # Process the file content or save it to a local file
                    print(file_content)
        else:
            print("Error occurred while retrieving repository files.")
    else:
        print("Error occurred while retrieving repository information.")

# Example usage
repo_url = "https://github.com/openai/gpt-3.5-turbo"
extension = ".txt"
extract_files_from_github(repo_url, extension)
