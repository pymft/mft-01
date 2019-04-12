import re

text = """
04/12/19
04/25/19
4/11/19
1/12/19
12/01/2019
"""

find_pat = "(\d+)/(\d+)/(\d+)"
repl_pat = r"\2-\1-\3"     # "\\2-\\1-\\3"

result = re.sub(find_pat, repl_pat, text)

print(result)
