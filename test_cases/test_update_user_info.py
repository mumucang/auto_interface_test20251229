import os

import allure
import pytest


from apis.update_user_info import UpdateUserInfo
from config import datas_path
from utils.assert_util import AssertUtil
from utils.read_excle import ReadExcel
from utils.str_dict import StrDict

datas = ReadExcel.read_excel(os.path.join(datas_path, 'autointerface.xlsx'), 'userInfoData')
@allure.feature("用户管理")
@allure.story("更新用户信息")
class TestUpdateUserInfo:

    @pytest.mark.parametrize("title,data,status_code,code,msg", datas)
    @allure.title("{title}")
    @allure.severity(allure.severity_level.NORMAL)
    def test_update_user_info(self,title,data,status_code,code,msg,login):
        with allure.step("更新用户信息"):
            data =StrDict.str_to_dict(data)

            res = UpdateUserInfo.update_user_info(login,data)
        with allure.step("断言结果"):
            AssertUtil.assert_result(res,status_code,code,msg)