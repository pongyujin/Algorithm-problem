rd1,rd2,rd3 = input("").split()
rd1= int(rd1)
rd2 = int(rd2)
rd3 = int(rd3)
result = 0

# 모두 같을때 
if (rd1 == rd2 == rd3):
    result += 10000+(rd1*1000)

# 두개 같을떄 
if(rd1 == rd2 !=rd3):
    result += 1000+(rd1*100)
elif(rd1==rd3 !=rd2):
    result += 1000+(rd1*100)
elif(rd2==rd3 != rd1):
    result += 1000+(rd2*100)

# 모두 다를때 
if(rd1 != rd2 and rd1 != rd3 and rd2 != rd3):

    if(rd1>rd2 and rd1>rd3):
        result += rd1*100
    elif(rd2>rd1 and rd2>rd3):
        result += rd2*100
    elif(rd3>rd1 and rd3>rd2):
        result += rd3*100


print(result)

