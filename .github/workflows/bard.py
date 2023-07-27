import requests
def pull_files(repo_url, directory):
  """Pulls all files from the specified GitHub repository into the specified directory.

  Args:
    repo_url: The URL of the GitHub repository.
    directory: The directory to store the files in.
  """

  response = requests.get(repo_url + "/contents/")
  if response.status_code != 200:
    if response.status_code == 403:
      raise Exception("Failed to get contents of repository. The repository is not public.")
    else:
      raise Exception("Failed to get contents of repository.")

  contents = response.json()
  for item in contents:
    filename = item["name"]
    filepath = os.path.join(directory, filename)
    if item["type"] == "file":
      with open(filepath, "wb") as f:
        f.write(requests.get(item["url"]).content)
    elif item["type"] == "dir":
      if not os.path.exists(filepath):
        os.mkdir(filepath)
      pull_files(item["url"], filepath)

if __name__ == "__main__":
  repo_url = "https://github.com/Hackerash008/devsecops-jenkins-k8s-tf-sast-sca-sonarcloud-snyk-repo/blob/main/Dockerfile"
  directory = "C:\\Users\\HP"
  pull_files(repo_url, directory)
