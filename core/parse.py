from .loader import FileLoader
from typing import Generator
import re

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

        patterns_to_compile = []
        self.pattern_map = {}
        for rule in self.rules:
            # 防御性编程：去除首尾空格，防止配置失误
            origin_pattern = rule["pattern"].strip()

            # 只支持“纯文本匹配”，不支持正则配置（这是为了安全的取舍）
            escaped_pattern = re.escape(origin_pattern)

            patterns_to_compile.append(escaped_pattern)
            self.pattern_map[origin_pattern] = rule

        patterns_to_compile.sort(key=len, reverse=True)
        full_regex_str = "|".join(patterns_to_compile)
        self.regex_obj = re.compile(full_regex_str)


    def parse(self,filepath) -> Generator:
        log_lines = FileLoader.load(logdir=filepath)
        for num,line in enumerate(log_lines):
            line = line.strip()
            # 使用编译好的对象进行搜索
            match = self.regex_obj.search(line)
            if match:
                # 因为使用了 re.escape，match.group() 拿到的就是原文
                matched_text = match.group()
                rule = self.pattern_map.get(matched_text)

                # 双重保险：防止极端的 key 不存在情况
                if rule:
                    yield {
                        "line_content": line,
                        "level": rule["level"],
                        "category": rule["category"],
                        "line_no": num + 1,
                        "pattern": rule["pattern"]
                    }

