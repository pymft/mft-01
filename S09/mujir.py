import re



with open('mujir.txt') as f:
    text = f.read()

pat = "Glory be to You O (.+?)![\., ]+Exalted are You O (.+?)!"
result = re.findall(pat, text)


for a, b in result:
    print(f"{a:>50}|{b}")

