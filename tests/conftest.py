import pytest
import os
import json
from core.loader import FileLoader

# 全局变量：用来暂存每个用例的测试结果
results_buffer = []

# 添加命令行参数 --logpath
def pytest_addoption(parser):
    parser.addoption(
        "--logpath",
        action="store",
        default="./logs",
        help="logs directory"
    )

# 动态生成测试用例
def pytest_generate_tests(metafunc):
    if "device_log_path" in metafunc.fixturenames:
        log_dir = metafunc.config.getoption("--logpath")

        # 检查目标日志目录是否存在
        if not os.path.exists(log_dir):
            raise FileNotFoundError(f"Log directory not found:{log_dir}")

        files = FileLoader.get_log_files(log_dir)

        ids = [os.path.basename(f) for f in files]

        metafunc.parametrize("device_log_path",files,ids=ids)

@pytest.hookimpl(tryfirst=True,hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        if 'device_log_path' in item.callspec.params:
            log_path = item.callspec.params['device_log_path']
            filename = os.path.basename(log_path)

            # 简单的解析序列号逻辑
            if filename.startswith("device_") and filename.endswith(".log"):
                serial = filename.replace("device_", "").replace(".log", "")
            else:
                serial = filename

            # 存结果
            results_buffer.append({
                "serial": serial,
                "status": "SUCCESS" if report.passed else "FAIL",
                "log_path": log_path
            })

# 生成 JSON
def pytest_sessionfinish(session,exitstatus):
    report_dir = "/app/report"
    if not os.path.exists(report_dir):
        os.makedirs(report_dir,exist_ok=True)

    output_file = os.path.join(report_dir,"summary.json")

    # 合并结果：一个设备跑了 Crash （pass） 和 内存泄露测试 (fail) ，则应该合并结果逻辑 - fail
    final_summary = {}

    for res in results_buffer:
        serial = res["serial"]

        if serial not in final_summary:
            final_summary[serial] = {
                "serial":serial,
                "status":"SUCCESS", # 创建时默认通过
                "log_path":res["log_path"]
            }

        if res["status"] == "FAIL":
            final_summary[serial]["status"] = "FAIL"

    # 写入
    data = {"device_results":list(final_summary.values())}
    with open(output_file,"w",encoding="utf-8") as f:
        json.dump(data,f,indent=2)
    print(f"\n[Reporter] Summary generated:{output_file}")