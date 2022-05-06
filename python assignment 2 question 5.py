a=int(input("Enter the side 1 of triangle"))
b=int(input("Enter the side 2 of triangle"))
c=int(input("Enter the side 3 of triangle"))
sum1=a+b
sum2=b+c
sum3=c+a
d=(c<=sum1)
i=(a<=sum2)
t=(b<=sum3)
print(d and i and t )


