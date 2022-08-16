from api.repositories.repos import Repos


class Github():
    def __init__(self, **kwargs):
        self.api_root_url = "http://api.github.com"
        self.repos = Repos(self.api_root_url, **kwargs)


if __name__ == '__main__':
    r = Github(token="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")
    data = {"visibility": "all", "affiliation": "collaborator,organization_member", "sort": "updated"}
    x = r.repos.list_your_repos(params=data)
    print(x.text)
    print("---------------分割---------------")

    r = Github(token="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")
    data = {"type": "all", "sort": "updated", "direction": "desc"}
    x = r.repos.list_a_user_repos(username="bluetech", params=data)
    print(x.text)
    print("---------------分割---------------")

    r = Github(token="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")
    x = r.repos.list_public_repos()
    print(x.text)
    print("---------------分割---------------")
