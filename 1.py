n = int(input());
print();

class max_heap:
    size = 0;e = [];
    def __greather(self,a,b):
        child = self.e[a]; parent = self.e[b];
        if(child['length'] == parent['length']):
            return child['name'] < parent['name'];
        return child['length'] > parent['length']
        
    def __percolate_up(self,k):
        while(k > 0):
            p = (k-1)// 2 #หาพ่อของปม
            if(not self.__greather(k,p)): break;
            self.e[p],self.e[k] = self.e[k],self.e[p];
            k = p;
    def __percolate_down(self,i):
        c = 2*i+1;
        while( c < self.size): 
            if(c+1 < self.size and self.__greather(c+1,c)): c+= 1 
            if(not self.__greather(c,i)): break;
            self.e[i],self.e[c] = self.e[c],self.e[i];
            i = c;c = 2*i+1
    def show(self): print(self.e);
    def enqueue(self,e):
        self.e.append(e);
        self.__percolate_up(self.size);
        self.size += 1;
    def dequeue(self):
        first = self.e[0];
        self.e[0] = self.e[self.size-1];
        self.e.pop(); self.size -= 1;
        self.__percolate_down(0);
        return first;
                


def transform(c = []):
    s = "";
    alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for e in c:
        if(e[0] in alp): s+= e[0];
    return (s,len(s));

h= max_heap();
for i in range(n):
    c = input().split(' ');
    print();
    n,l = transform(c);
    h.enqueue({"name":n,"length":l});

for i in range(h.size):
    print(h.dequeue()['name']);


    
    
