#
# out = "poem: |{text:^50}|".format(text="que largo es el mundo!")
# print(out)

line1 = "que largo es el mundo!"
line2 = "es infinito!"
out = f"p oem: \n|{line1:^50}|\n|{line2:.>50}|"

print(out)