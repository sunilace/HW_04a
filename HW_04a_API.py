import requests
import json

def details(name):
    repo_name = requests.get(f'https://api.github.com/users/{name}/repos')
    if repo_name.status_code == 200:
        repos = json.loads(repo_name.text)

        repositories = [repo["name"] for repo in repos]

        comment_total = []
        for repo in repositories:
            response = requests.get(f'https://api.github.com/repos/{name}/{repo}/commits?per_page=100')
            if response.status_code == 200:
                commit = json.loads(response.text)
                commits = 0
                for comment in commit:
                    if "comments_url" in comment:
                        #comment_url = comment["comments_url"]
                        #print('Commit value: ', comment_url)
                        commits += 1
                comment_total.append(commits)
                #print(f"Repository name: {repo}, Commits: {commits}")
            else:
                print(f"Cannot find comment value for repository {repo}. \nStatus Code: {response.status_code}")
                return f"Status Code: {response.status_code}"
        stri = ''
        for i in range (len(repositories)):
            stri += f"Repository name: {repositories[i]}, Commits: {comment_total[i]}\n"
        return stri
    else:
        print(f"Cannot find details for given ID. \nStatus Code: {repo_name.status_code}")
        return f"Status Code: {repo_name.status_code}"

if __name__ == "__main__":
    id = "richkempinski"

    data = details(id)