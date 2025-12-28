import pytest,os
from core import parse

@pytest.fixture(scope="session")
def logexport():
    # 通过adb 命令我估计会用subprocess.run（[adb bugreport]）来导出设备日志，这里用打开创建文件方式mock
    with open("app.log",'w',encoding='utf-8') as f:
        f.write('FATAL EXCEPTION:1\n')
        f.write('memory leak:2\n')
    dummy_logs = "./app.log"
    yield dummy_logs
    # 这里我不确定日志是否清理
    os.remove(dummy_logs)

@pytest.fixture(scope="session")
def logparse(logexport):
    parser = parse.LogParser()
    log_path = logexport
    error_log = parser.parse(log_path)
    yield list(error_log)
    # 清理现场