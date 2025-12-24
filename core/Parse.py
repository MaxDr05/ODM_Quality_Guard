from Loader import FileLoader
from typing import Generator

class LogParse():
    def __init__(self,rules:list = None):
        self.rules = rules
        if self.rules is None:
            self.rules = [
            {
                "pattern": "FATAL EXCEPTION",
                "level": "CRITICAL",
                "category": "Crash"
            },
            {
                "pattern": "memory leak",
                "level": "HIGH",
                "category": "Performance"
            },
            {
                "pattern": "Connection unstable",
                "level": "WARNING",
                "category": "Network"
            }
        ]
    def parse(self,filepath) -> Generator:
        log_lines = FileLoader.loader(filepath=filepath)
        for num,line in enumerate(log_lines):
            line = line.strip()
            for rule in self.rules:
                if rule["pattern"] in line.strip():
                    mes_dict = {
                        "line_content": line,
                        "level": rule["level"],
                        "category": rule["category"],
                        "line_no": num + 1
                    }
                    yield mes_dict

