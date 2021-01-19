# -*- coding: gbk -*-
from lib.send_email import send_email  # �޸ĵ���·��
from config.config import *
import unittest
from lib.HTMLTestReportCN import HTMLTestRunner

logging.info("================================== ���Կ�ʼ ==================================")
suite = unittest.defaultTestLoader.discover(test_path)  # �������ļ��ж�ȡ

with open(report_file, 'wb') as f:  # �������ļ��ж�ȡ
    HTMLTestRunner(stream=f, title="Api Test", description="��������").run(suite)

if send_email_after_run:
    send_email(report_file)  # �������ļ��ж�ȡ
logging.info("================================== ���Խ��� ==================================")