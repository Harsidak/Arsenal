x,y = map(int, input().split())
seq = input().strip()

li = [seq[i] for i in range(0,len(seq))]

li[x-1],li[y-1] = li[y-1],li[x-1]
final_seq = ''.join(li)
print(final_seq)