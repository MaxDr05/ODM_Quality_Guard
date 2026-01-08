import pytest

class TestRunner:
    def run(self, test_path: str, report_path: str,log_path: str) -> int:
        """
        :param test_path: 测试用例的目录，比如 "./tests"
        :param report_path: allure报告的数据存放目录，比如 "./output/report_data"
        :return: exit_code (0=Pass, other=Fail)
        """
        args = ["-v","-s","--clean-alluredir",f"--alluredir={report_path}",test_path]
        if log_path:
            args.insert(2,f"--logpath={log_path}")
        return pytest.main(args)