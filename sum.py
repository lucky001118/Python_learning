#this is normsl addition performing
first = int(input("Enter the first input: "))
second = int(input("Enter the second input: "))
sumResult = first+second
print("The result of the sum is: ",sumResult)
if sumResult<100:
    print("the result is less then the 100")
elif sumResult>100 and sumResult<1000:
    print("result is laying in the second condition.")
else:
    print("result is greater then the all cases.")


discription = "We are inclosing the first input at 0th index and second input at 1st index and thier sum in the 2nd index and 3rd index discription."
theList = [first,second,sumResult,discription]
print(theList)