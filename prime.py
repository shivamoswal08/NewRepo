num=13
count=2
while count!=num:
     if num%count==0:
       break
else:
     count+=1

if count==num:
   print "Number",num,"is prime"
else:
  print "Number",num,"is not prime"