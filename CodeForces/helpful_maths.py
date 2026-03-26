s = input().strip()
s_clean = sorted(list(map(int,s.split('+'))))
s_final = []
for i in range(len(s_clean)):
    if i > 0:
        s_final.append('+'+str(s_clean[i]))
    else:
        s_final.append(str(s_clean[i]))
S = ''.join(s_final)
print(S)