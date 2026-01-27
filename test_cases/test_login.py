import json
import os

import allure
import pytest
import requests

from apis.login_api import LoginApi
from config import datas_path
from utils.assert_util import AssertUtil
from utils.read_excle import ReadExcel
from utils.str_dict import StrDict

datas = ReadExcel.read_excel(os.path.join(datas_path, "autointerface.xlsx"),"logindata")

@allure.feature("登录模块")
@allure.story("登录功能")
class TestLogin:

    @pytest.mark.parametrize("title,login_data,status_code,code,msg", datas)
    @allure.title("{title}")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_success(self,title,login_data,status_code,code,msg,get_logger):
        get_logger.info(f"开始执行用例：{title}")
        with allure.step("登录"):
            login_data = StrDict.str_to_dict(login_data)
            res = LoginApi.login(login_data)
            get_logger.info(res.text)
        with allure.step("断言结果"):
            AssertUtil.assert_result(res,status_code,code,msg)





