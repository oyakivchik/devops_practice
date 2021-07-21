n = input('Number of terms ')
acc = 0
for i in range(1,int(n)+1):
    a=input('Term number '+str(int(i))+': ')
    acc += float(a)
print('The average is ',acc/int(n))                                         
