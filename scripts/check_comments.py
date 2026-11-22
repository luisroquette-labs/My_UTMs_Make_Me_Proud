from pathlib import Path
import subprocess
import sys

from pygments import lex
from pygments.lexers import BashLexer, HtmlLexer, PythonLexer, YamlLexer
from pygments.token import Comment


LEXERS = {".py": PythonLexer, ".sh": BashLexer, ".html": HtmlLexer, ".yaml": YamlLexer, ".yml": YamlLexer}


def comment_lines(source: str, suffix: str) -> list[int]:
    lines = []
    line = 1
    for token, value in lex(source, LEXERS[suffix.lower()]()):
        required_directive = (
            suffix.lower() in {".py", ".sh"} and line == 1 and value.startswith("#!")
        ) or (
            suffix.lower() == ".html" and value.lower().startswith("<!doctype")
        )
        if token in Comment and not required_directive:
            lines.append(line)
        line += value.count("\n")
    return lines


def main() -> int:
    tracked = subprocess.check_output(["git", "ls-files", "-z"]).decode().split("\0")
    failures = [
        f"{path}:{line}"
        for path in tracked
        if path and Path(path).suffix.lower() in LEXERS
        for line in comment_lines(Path(path).read_text(), Path(path).suffix)
    ]
    if failures:
        print("Comments are forbidden:\n" + "\n".join(failures), file=sys.stderr)
        return 1
    print("Comment ratchet: zero comments in tracked Python, shell, HTML and YAML files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
