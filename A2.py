try:
    num1=int(input("enter a number: "))
    num2=int(input("enter a number: "))
    result= num1/num2
    print("result is: ", result)
    print("result is: ", result1)
except ZeroDivisionError:
    print("division by 0 isn't allowed!")
except ValueError:
    print("please enter a number!")
except NameError as ex:
    print("the exception is: ", ex)
except:
    print("some error occured!")
finally:
    print("I will excecute no matter what happens!")