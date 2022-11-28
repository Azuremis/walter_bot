import os
import re
import pandas as pd

data = {
    'character': [],
    'line': []
}
pattern = '([a-zA-Z|\s]+): (.+)'

os.chdir("./data")

for i in range(1, 6):
    filename = f'breaking_bad_s{i}_transcript.txt'

    with open(filename) as file:
        for line in file.readlines():
            match = re.findall(pattern, line)
            if match:
                character, line = match[0]
                data['character'].append(character)
                data['line'].append(line)
        print(len(data['line']))

df = pd.DataFrame(data)

df.to_csv('breaking_bad.csv', index=False)







