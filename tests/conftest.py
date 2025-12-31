import pytest,os
from core import parse

def pytest_addoption(parser):
    parser.addoption(
        "--logpath",
        action="store",
        default=None,
        help="input a logpath to analyze"
    )


@pytest.fixture(scope="session")
def logexport(request):
    log_path = request.config.getoption("--logpath")
    if log_path is None:
        with open("app.log",'w',encoding='utf-8') as f:
            f.write('FATAL EXCEPTION:1\n')
            f.write('memory leak:2\n')
        dummy_logs = "./app.log"
        yield dummy_logs
        os.remove(dummy_logs)
    else:
        yield log_path

@pytest.fixture(scope="session")
def logparse(logexport):
    parser = parse.LogParser()
    log_path = logexport
    error_log = parser.parse(log_path)
    yield list(error_log)
    # 清理现场