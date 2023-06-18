import requests

def get_github_files(github_link):
    # Extracting username and repository name from the GitHub link
    _, _, _, username, repository = github_link.rstrip('/').split('/')

    # Making a request to the GitHub API to retrieve the repository contents
    api_url = f"https://api.github.com/repos/{username}/{repository}/contents"
    response = requests.get(api_url)
    response.raise_for_status()

    # Initializing variables to store file contents
    python_files_content = []
    json_files_content = []

    # Parsing the response and filtering files by extension
    for file_info in response.json():
        if file_info['type'] == 'file':
            filename = file_info['name']
            download_url = file_info['download_url']

            if filename.endswith('.py'):
                # Downloading and loading Python file content
                file_content = requests.get(download_url).text
                python_files_content.append(file_content)
            elif filename.endswith('.json'):
                # Downloading and loading JSON file content
                file_content = requests.get(download_url).json()
                json_files_content.append(file_content)

    return python_files_content, json_files_content
