def reverse(s):
    num = " "
    for i in s:
        num = i + num
    return num

s = "1234"
print("the number is : " ,end=" ")
print(s)
print("the reversed number(using loop) is : ",end=" ")
print(reverse(s))
