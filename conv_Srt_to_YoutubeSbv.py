#!/c/msys64/mingw64/bin/python 
#!/bin/python

import glob
import re

files = glob.glob('./*.srt')
file_pattern = r'\.\/(.+?)\.srt'


time_pattern = r'(\d{2}:\d{2}:\d{2}),(\d+)'
pattern = r'(\d{2}:\d{2}:\d{2},\d+)(\s+)(-->)(\s+)(\d{2}:\d{2}:\d{2},\d+)\n(.+)\n'

def conv_time(value):
    m = re.match(time_pattern, value)
    return f'{m.group(1)}.{m.group(2)[:3]}'


for file in files:
    with open(file, encoding='utf-8', mode='r') as rp:
        all_text = rp.read()
    matches = re.findall(pattern, all_text)

    file_match = re.match(file_pattern, file)
    out_file = file_match.group(1) + '.sbv'
    print(out_file)

    with open(out_file, encoding='utf-8', mode='w') as wp:
        for value in matches:
            (from_time, space1, arrow, space2, to_time, message) = value
            wp.write(f'{conv_time(from_time)},{conv_time(to_time)}\n{message}\n\n')
        