import re
import json

text = open('mbg_presentation.tex', encoding='utf-8').read()

def nums(line):
    line = line.replace('$-$', '-')
    return [float(x) for x in re.findall(r'-?\d+\.\d+', line)]

blocks = re.findall(r'\\multicolumn\{13\}\{l\}.*?\\\\\n(.*?)\\bottomrule', text, re.S)
print("num table blocks found:", len(blocks))

rows = {}
for b in blocks:
    for line in b.split('\\\\'):
        line = line.strip()
        if not line or 'multicolumn' in line:
            continue
        m = re.match(r'^(?:\\rowcolor\{[^}]*\}\s*)?([A-Za-z]+)\s*&(.*)$', line)
        if m:
            name = m.group(1).strip()
            vals = nums(m.group(2))
            if len(vals) == 12:
                rows[name] = vals

print("num provinces parsed:", len(rows))
for k, v in list(rows.items())[:3]:
    print(k, v)

json.dump(rows, open('mapdata/table4_data.json', 'w'), indent=0)
