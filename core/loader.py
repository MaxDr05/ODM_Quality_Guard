from typing import Generator
import os,glob

class FileLoader():
    def __init__(self):
        pass

    # 返回文件名列表
    @staticmethod
    def get_log_files(logdir:str) -> list:
        search_pattern = os.path.join(logdir,'*.log')
        file_list = glob.glob(search_pattern)

        # 校验无日志情况-直接报错
        if not file_list:
            error_msg = f"[FATAL] No log files found in {logdir}!"
            print(error_msg)
            raise RuntimeError(error_msg)

        return sorted(file_list)

    # 读取单个文件，给具体的测试用例用
    @staticmethod
    def load_single_file(filepath):
        if os.path.getsize(filepath) == 0:
            return

        with open(filepath,"r",encoding="utf-8",errors="ignore") as f:
            for line in f:
                yield line