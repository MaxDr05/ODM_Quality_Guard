import json
import pytest
import allure
from core.parse import LogParser

@allure.feature("Log Analysis Module")
class TestMTBF():
    @allure.story("stability")
    @allure.title("crash")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_crash_detection(self,device_log_path):
        parser = LogParser()
        error_logs = list(parser.parse_file(device_log_path))
        with allure.step(f"scan log:{device_log_path}"):
            for msg in error_logs:
                if "Crash" == msg["category"]:
                    allure.attach(json.dumps(msg),"error msg",attachment_type=allure.attachment_type.JSON)
                    pytest.fail(f"Crash detected! Pattern:{msg['pattern']}")
            # 拓展写法
            # assert not any(msg["category"] == "Crash" for msg in logparse),"found Crash log!"

    @allure.story("Performance")
    @allure.title("memory leak")
    @allure.severity(allure.severity_level.NORMAL)
    def test_memory_leak(self,device_log_path):
        parser = LogParser()
        error_logs = list(parser.parse_file(device_log_path))
        with allure.step(f"scan log:{device_log_path}"):
            for msg in error_logs:
                if "memory leak" == msg["category"]:
                    allure.attach(json.dumps(msg),"error msg",attachment_type=allure.attachment_type.JSON)
                    pytest.fail(f"memory leak detected! Pattern:{msg['pattern']}")