from core.rest_client import RestClient


class Repos(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Repos, self).__init__(api_root_url, **kwargs)

    def list_your_repos(self, **kwargs):
        """
        https://docs.github.com/en/rest/repos/repos#list-repositories-for-the-authenticated-user
        :param kwargs:
        :return:
        """
        return self.get("/user/repos", **kwargs)

    def list_a_user_repos(self, username, **kwargs):
        """
        https://docs.github.com/en/rest/repos/repos#list-repositories-for-a-user
        :param username: github用户名
        :param kwargs:
        :return:
        """
        return self.get("/users/{}/repos".format(username), **kwargs)

    def list_public_repos(self, **kwargs):
        """
        https://docs.github.com/en/rest/repos/repos#list-public-repositories
        :param kwargs:
        :return:
        """
        return self.get("/repositories", **kwargs)