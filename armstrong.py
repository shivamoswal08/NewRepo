num=input("Enter number : ")
ono=num
rem=0
cube=0
sum=0
while num!=0:
  rem=num%10
  cube=rem*rem*rem
  sum=sum+cube
  num=num/10

if sum==ono:
  print "Its an Aremstrong number"
else:
  print "Its not an Armstrong number"