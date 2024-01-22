file=open("practical-4.txt",'w')
list=[1,2,3,4,5,6,7,8,9,10,11,12]
sum=0
i=0
while(i<len(list)):
    sum=sum+list[i]
    i=i+1
    avg=int(sum/len(list))
file.write(f"the average is: {str(avg)}")