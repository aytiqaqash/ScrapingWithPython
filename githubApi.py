import requests
import pandas as pd
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 OPR/82.0.4227.33"
}
url = "https://api.github.com/users/aytiqaqash/repos"

response = requests.get(url, headers=header).json()

print(response)

pd.DataFrame(response).to_json('aytiqaqashGitHubRepos')
