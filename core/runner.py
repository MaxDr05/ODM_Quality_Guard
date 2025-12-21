import pytest

class TestRunner:
    def run(self, test_path: str, report_path: str) -> int:
        """
        :param test_path: 测试用例的目录，比如 "./tests"
        :param report_path: allure报告的数据存放目录，比如 "./output/report_data"
        :return: exit_code (0=Pass, other=Fail)
        """
        # 你的任务：
        # 1. 组装参数列表 args = [...]
        #    你需要包含：test_path, '-s', '-v', 还有 '--alluredir=xxx'
        # 2. 调用 pytest.main(args)
        # 3. 返回 main 的执行结果
        args = ["-v","-s","--clean-alluredir",f"--alluredir={report_path}",test_path]
        return pytest.main(args)