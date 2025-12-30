import json
import pytest
import allure

@allure.feature("Log Analysis Module")
class TestMTBF():
    @allure.story("stability")
    @allure.title("crash")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_crash_detection(self,logparse):
        with allure.step("scan crash in log"):
            for msg in logparse:
                if "Crash" == msg["category"]:
                    allure.attach(json.dumps(msg),"error msg",attachment_type=allure.attachment_type.JSON)
                    assert False
            assert True
            # 拓展写法
            # assert not any(msg["category"] == "Crash" for msg in logparse),"found Crash log!"

    @allure.story("Performance")
    @allure.title("memory leak")
    @allure.severity(allure.severity_level.NORMAL)
    def test_memory_leak(self,logparse):
        with allure.step("scan memory leak in log"):
            for msg in logparse:
                if "Performance" == msg["category"] and "memory leak" == msg["pattern"]:
                    allure.attach(json.dumps(msg), "error msg", attachment_type=allure.attachment_type.JSON)
                    assert False
            assert True
            # 拓展写法
            # assert not any(msg["category"] == "Performance" and msg["pattern"] == "memory leak" for msg in logparse),"found memory leak log!"