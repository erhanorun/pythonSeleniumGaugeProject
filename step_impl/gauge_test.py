from getgauge.python import step

from BasePackage.base_test import BaseTest


@step('test for the case which has wanted by Keytorc')
def test_method():
    # BaseTest.case_page.login()
    BaseTest.case_page.add_favourite()
