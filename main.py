import sys
from core import runner

if __name__ == "__main__":
    runner = runner.TestRunner()
    if len(sys.argv) == 1:
        sys.exit(runner.run("./tests","./report",None))
    else:
        sys.exit(runner.run("./tests","./report",sys.argv[1]))