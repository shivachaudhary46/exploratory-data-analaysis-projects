firstNum = int(input("get me a first number: "));
secondNum = int(input("get me a second number: "));
operator = input("there are 7 operator +, *, -, /, //, **, % : ");

if(operator == "+"):
    print("addition: ", firstNum+secondNum);
elif(operator == "-"):
    print("subtraction: ", firstNum-secondNum);
elif(operator == "*"):
    print("multiplication: ",firstNum*secondNum);
elif(operator == "/"):
    print("divide: ", secondNum/firstNum);
elif(operator == "//"):
    print("floor division: ", secondNum//firstNum);
elif(operator == "**"):
    print("power: ", firstNum**secondNum);
elif(operator == "%"):
    print("modules: ", firstNum%secondNum);
else:
    print("please use one operator which are given: ");



