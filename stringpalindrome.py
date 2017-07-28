name=input("Enter name : ")
reverse=name[::-1]
print reverse
if name==reverse:
  print "It is a palindrome"
else:
  print "It is not a palindrome"