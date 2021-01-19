# -*- coding: gbk -*-
import unittest
import requests
from lib.db import *
from lib.read_excel import *
import json
from config.config import *
import os  # ������һ��os����Ҫ������װ·��
import sys
sys.path.append("../..")  # ����2������Ŀ��Ŀ¼��

class TestUserReg(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list(os.path.join(data_path, "test_user_data.xlsx"), "TestUserReg")  # ��ȡTestUserReg����������������

    def test_user_reg_normal(self):
        case_data = get_test_data(self.data_list, 'test_user_reg_normal')
        if not case_data:
            print("�������ݲ�����")
        url = case_data.get('url')
        data = json.loads(case_data.get('data'))  # תΪ�ֵ䣬��Ҫȡ�����name�������ݿ���
        expect_res = json.loads(case_data.get('expect_res'))  # תΪ�ֵ䣬����ʱֱ�Ӷ��������ֵ��Ƿ����
        name = data.get("name")  # ������
        print(data,expect_res,name)

        # �������
        if check_user(name):
            # ��������
            res = requests.post(url=url, data=data)  # ��data=data ���ַ���Ҳ����
            # ��Ӧ���ԣ�������ԣ�

            self.assertDictEqual(res.text, expect_res)
            # ���ݿ����
            self.assertTrue(check_user(name))
            # ������������ע��ӿ������ݿ�д�����û���Ϣ��




if __name__ == '__main__':    # �Ǳ�Ҫ�����ڲ������ǵĴ���
    unittest.main(verbosity=2)