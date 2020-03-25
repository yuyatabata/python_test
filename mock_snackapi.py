import requests


# 外注が作っている機能を呼び出す
class ThirdPartyMotherRequestSnackApi(object):
    def request_snack(self, child_cry):
        result = requests.get('https://snack/api', child_cry)
        return result.json()['snack']


# 自分たちで作成する機能
class ChildGetSnackApi(object):
    def __init__(self, name, hungry):
        self.mother_request_api = ThirdPartyMotherRequestSnackApi()
        self.name = name
        self.hungry = hungry


    # おやつを取得
    def get_snack(self):
        snack = self.mother_request_api.request_snack(
            child_cry='おなか減った、なんかお菓子ない？'
        )
        return snack