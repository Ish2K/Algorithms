s = input()
freq = dict()
def get_codes(node,curr_code):
    global codes
    if(node[-2]==None and node[-1]==None):
        codes[node[-3]] = curr_code
    else:
        get_codes(node[-2],curr_code+'0')
        get_codes(node[-1],curr_code+'1')
def code_to_string(code):
    global cod
    s = ''
    i = 0
    while(i<len(code)):
        b_s = ''
        while(i<len(code) and b_s not in cod):
            b_s+=code[i]
            i+=1
        s+=cod[b_s]
    return s
for x in s:
    if(x in freq):
        freq[x]+=1
    else:
        freq[x] = 1
heap = []
# print(freq)
for x in freq:
    heap.append((freq[x],x,None,None))
# print(heap)
heapq.heapify(heap)
while(len(heap)!=1):
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)
    top = (left[0]+right[0],left[1]+right[1],left,right)
    heapq.heappush(heap,top)
codes = dict()
get_codes(heap[0],'')
# print(codes)
print(codes)
ans = ''
for x in s:
    ans+=codes[x]
print("Original String : ",s)
print("Coded String : ",ans)
cod = dict()

for x in codes:
    cod[codes[x]] = x

print("Original String : ",code_to_string(ans))