num=input("Enter Number :")
ono=num
rem=0
rev=0
while num!=0:
  rem=num%10
  rev=rev*10+rem
  num=num/10
print rev

if rev==ono:
  print "number is palindrome"
else:
  print "number is not palindrome"