num_list = [ int(e) for e in input().split(" ")];
show = ["_" for i in range(12)];
sort_num = num_list[:];
DB = {};
sort_num.sort();
count = 0;
score = 0;
wrong_ans = ""


for i in range(1,len(sort_num)):
    if(sort_num[i] == sort_num[i-1]):
        count += 1;
    else:
        DB[str(sort_num[i-1])] = count + 1;
        count = 0;
    if(i == len(sort_num)-1):
        DB[str(sort_num[i])] = count + 1;

max_score = sum(DB.values());
        
def check(n):
    for i,e in enumerate(num_list):
        if(str(e) == n):
            show[i] = n;

for i in range(5):
    g = input();
    check(g);
    if (g in DB and score < max_score): score += DB[g];
    else: wrong_ans += g + " "
    print(" ".join(show),wrong_ans);

print(score);

    
