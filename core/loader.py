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

        if not file_list:
            print(f"[WARN] No .log files found in {logdir}")
            return

        for filepath in file_list:
            print(f"[FileLoader] Reading: {filepath}")
            with open(filepath,"r",encoding="utf-8",errors="ignore") as f:
                for line in f:
                    yield line
