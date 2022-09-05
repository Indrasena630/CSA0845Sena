def reverse(s):
    str = " "
    for i in s:
        str = i + str
    return str
s = "1234"
print("the string is : " ,end=" ")
print(s)
print("the reversed string(using loop) is : ",end=" ")
print(reverse(s))
