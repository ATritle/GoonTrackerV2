import requests


class TarkovAPI:

    URL = "https://api.tarkov.dev/graphql"

    @staticmethod
    def get_status():
        return requests.get("https://api.tarkov.dev").status_code