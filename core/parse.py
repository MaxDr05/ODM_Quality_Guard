from .loader import FileLoader
from typing import Generator

class LogParser():
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
        log_lines = FileLoader.load(filepath=filepath)
        for num,line in enumerate(log_lines):
            line = line.strip()
            for rule in self.rules:
                if rule["pattern"] in line.strip():
                    mes_dict = {
                        "line_content": line,
                        "level": rule["level"],
                        "category": rule["category"],
                        "line_no": num + 1,
                        "pattern": rule["pattern"]
                    }
                    yield mes_dict

