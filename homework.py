num=int(input("please enter a number:"))
print("number is: ",num)
namedarr=['zero','one','two','three','four','five','six','seven','eight','nine']
if num>0 and num<10:
    print("num is: ",namedarr[num])

elif num>10 and num<99:
    digit1=num%10
    digit2=num%100/10
    sumdigits=int(digit1+digit2)
    print("has two digits and the digit sum is: ",sumdigits)

elif num>100 and num<999:
    digit1=int(num%10)
    digit2=int(num%100/10)
    digit3=int(num%1000/100)
    multiplydigits=int(digit1*digit2*digit3)
    print("has three digits and the digit multiply is: ",multiplydigits)

elif num>999:
    print("num has more then 3 digits")