from typing import Generator


class FileLoader():
    def __init__(self):
        pass

    # 目的是逐行吐出日志文件，具体解析操作交给parse
    @staticmethod
    def loader(filepath:str) -> Generator:
        with open(filepath,"r",encoding="utf-8",errors="ignore") as f:
            for line in f:
                yield line
