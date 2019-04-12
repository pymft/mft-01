import re


text = """user@domain.com
user_nAme@anotherdomain.net
info@9gag.com
"""

pat = "\w+@\w+\.\w+"

result = re.findall(pat, text)

print(result)

