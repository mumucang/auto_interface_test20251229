import requests

from config import project_url


class UpdateUserInfo:

    @classmethod
    def update_user_info(cls,token,user_info_data):

        header = {"token": token}
        url = project_url+"/api/user/user_change"
        res = requests.post(url,data=user_info_data,headers=header)
        return res