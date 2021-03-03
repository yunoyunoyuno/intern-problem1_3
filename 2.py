import random;

def pow_mod(base,k,m):
    if(k == 0): return 1;
    x = pow_mod(base,k//2,m);
    x *= x;
    if(k % 2 == 1): x *= base;
    return x % m;
    
def miller_rabin(n, k):

    # Implementation uses the Miller-Rabin Primality Test
    # The optimal number of rounds for this test is 40
    # See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    # for justification

    # If number is even, it's a composite number

    if n == 2: return True
    if n % 2 == 0 or n <= 1: return False
    r, s = 0, n - 1
    
    while s % 2 == 0:
        r += 1; s //= 2
        
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow_mod(a, s, n);
        if x == 1 or x == n - 1: continue
        for _ in range(r - 1):
            x = pow_mod(x, 2, n)
            if x == n - 1: break
        else: return False
    return True

ans = False;
while(True):
    num = "".join(input().split("."));
    if(num == "00"): break
    for end in range(2,13):
        ans = miller_rabin(int(num[:end]),40);
        if(ans == True): break;
    print(ans);

# ก่อนอื่นต้องขอยอมรับว่า ไม่ทราบอัลกอริทึมของคุณ Miller–Rabin ขั้นตอนต่าง ๆ มาอย่างไร
# แต่ทราบว่าควรใช้วิธีดังกล่าวเช็คจำนวนเฉพาะที่มีขนาดใหญ่ ( ในกรณีแย่สุด )
# หาอัลกอริทึมคร่าว ๆ จาก https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test
# แต่ก้ยังไม่เข้าใจว่าจะต้องใช้ k เท่าไหร่ จึงใช้ประกอบกับ https://gist.github.com/Ayrx/5884790
# เมื่อพอเข้าใจจึงปรับแต่ง code เล็กน้อย เพราะไม่แน่ใจว่า built in power mod หาค่าตรง ๆ หรือไม่
# จึงปรับประสิทธิภาพเผื่อกรณี built in power mod หาค่าตรง ๆ ( แต่คาดว่าน่าจะไม่ได้หาตรง ๆ )


# ปล. ในปี 4 หากผมได้เรียน Number Theory ผมอาจจะเข้าใจมันมากขึ้นครับ
    
