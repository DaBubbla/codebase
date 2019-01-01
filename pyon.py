# While trying to work with sqlite table data.
# Out put from sqlite3 seems to be a tuple.
# Created a method of outputting sudo-json data

# Sqlite output example
a = [
     ('2018-2-8', .50, .50, "down"),
     ('2018-2-9', .48, .45, "down"),
    ('2018-2-10', .47, .48, "down"),
    ('2018-2-11', .48, .47, "down"),
]

# Create an array
b = []

# Loop through a and add key:value objects
for i in a:
    # print(i[0])
    b.append({
    'date': i[0],
    'open': i[1],
    'close': i[2],
    'x': i[3]
    })
# print(c)# Successfully prints array of objects

# No longer immutable
# isolate close & open
for w in range(len(b)):
    Open = b[w]['open'] # 0.5
    Close= b[w]['close']# 0.5
    u_d  = b[w]["x"]# 'down'
    if Open <= Close:
        b[w]['x']='upper'
    else:
        b[w]['x']='down'
    print(b[w])
