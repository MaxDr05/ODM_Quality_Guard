import sys
from core import runner

if __name__ == "__main__":
    runner = runner.TestRunner()
    sys.exit(runner.run("./tests","./output"))