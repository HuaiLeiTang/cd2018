#!/usr/bin/python3
'''
with open("2018cd.txt") as fh:
    lines = fh.readlines()
    #print(len(lines))
    print(lines)
'''    
'''
try:
    f = open('2018cd.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()
'''
"""
['40523115\t40523108\t40523116\t40523144\t40523111\t40523141\t40523104\t40523102\t40523123\n'
, '40523137\t40523117\t40523135\t40523147\t40523146\t40523145\t40523122\t40523136\t40523132\n'
, '40523127\t40523126\t40523125\t40523124\t40523118\t40523131\t40523121\t40523120\t40523119\n'
, '40523105\t40523106\t40523107\t40523143\t40523128\t40523129\t40523130\t40523139\t40523133\n'
, '40523142\t40523148\t40523140\t40523113\t40523138\t40523134\t\t']
"""
'''
40523115	40523108	40523116	40523144	40523111	40523141	40523104	40523102	40523123
40523137	40523117	40523135	40523147	40523146	40523145	40523122	40523136	40523132
40523127	40523126	40523125	40523124	40523118	40523131	40523121	40523120	40523119
40523105	40523106	40523107	40523143	40523128	40523129	40523130	40523139	40523133
40523142	40523148	40523140	40523113	40523138	40523134	
'''
with open("2018cd.txt") as fh:
    # 逐行讀出檔案資料, 並放入數列中
    lines = fh.readlines()
    # 設法用迴圈逐數列內容取出字串
    # 組序變數 g 起始值設為 0
    g = 0
    for i in range(len(lines)):
        # 利用 strip() 去除各行字串最末端的跳行符號
        #print(lines[i].strip())
        line = lines[i].strip()
        # 利用 split() 將以 \t 區隔的字串資料分離後納入 groups 字串
        groups = line.split("\t")
        #print(groups)
        for i in range(len(groups)):
            # 每組有三名組員
            if i%3 == 0:
                # 每三位組員組序增量 1
                g += 1
                print()
                print("第" + str(g) + "組:")
                print(groups[i])
            else:
               print(groups[i])    
                