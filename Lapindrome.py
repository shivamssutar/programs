print("Lapindrome Program :")
s=input("Enter a String : ")
n=len(s)
m=n//2
if n%2==0:
    if s[0:m]==s[m:n]:
        print("Sting is Lapindrome")
    else:
        print("String is not lapindrome")
else:
    if s[0:m]==s[m+1:n]:
        print("Sting is Lapindrome")
    else:
        print("String is not lapindrome")
