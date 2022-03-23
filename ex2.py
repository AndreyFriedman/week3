lastCall = ""


def lastcall (func):

    def wrapper (*args,**kwargs):
        value = func(*args,*kwargs)
        global lastCall

        if type(value) == type(lastCall):
            if value != lastCall:
                print(value)
                lastCall = value
            else:
                print("I already told you that the answer is ", str(value) + "!")
        else:
            lastCall = value
            print(value)
        return value

    return wrapper


@lastcall
def int_ex(num: int) -> int:
    return num


if __name__ == '__main__':
    num = 1
    int_ex(num)
    int_ex(num)
    num = 10
    int_ex(num)
    int_ex(num)
