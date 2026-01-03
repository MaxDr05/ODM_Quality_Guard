from typing import Generator
import os,glob

class FileLoader():
    def __init__(self):
        pass

    # 目的是逐行吐出日志文件，具体解析操作交给parse
    @staticmethod
    def load(logdir:str) -> Generator:
        search_pattern = os.path.join(logdir,'*.log')
        file_list = glob.glob(search_pattern)

        print(f"[FileLoader] Scanning directory: {logdir}")
        print(f"[FileLoader] Found files: {file_list}")

        # 避免无文件造成的异常通过
        if not file_list:
            print(f"[WARN] No .log files found in {logdir}")
            raise FileNotFoundError(f"No .log files found in {logdir}. Did the Runner fail?")

        for filepath in file_list:
            print(f"[FileLoader] Reading: {filepath}")

            # 避免空文件造成的异常通过
            if os.path.getsize(filepath) == 0:
                raise ValueError(f"Log file is empty: {filepath}. Test execution might have failed silently.")
            with open(filepath,"r",encoding="utf-8",errors="ignore") as f:
                for line in f:
                    yield line
