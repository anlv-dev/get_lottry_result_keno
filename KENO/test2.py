import re
p='\d+'
s = '<span class="bong_tron small">04</span>'

if re.search(p, s) is not None:
    for catch in re.finditer(p, s):
        print(catch[0]) # catch is a match object