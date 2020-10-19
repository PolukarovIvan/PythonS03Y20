def div(x, y):
    try:
        x / y
    except TypeError:
        print("Type Error ;(")


div(10, str())
div(10, {})
div(10, [123, 2, 2, 2])

try:
    div(10, 0)
except ZeroDivisionError:
    print("Zero division error :(")


def div2(x, y):
    try:
        return x / y
    except (TypeError, ZeroDivisionError):
        print("Error ;(")


div2(10, 0)
div2(10, [])


def div3(x, y):
    try:
        return x / y
    except (TypeError, ZeroDivisionError) as e:
        print(type(e))
        print(e)
        print(e.args)


div3(10, 0)
div3(10, [])

print(ZeroDivisionError.mro())


def div3(x, y):
    try:
        return x / y
    except ArithmeticError as ae:
        print(ae.args)


div3(3, 0)


def div4(x, y):
    try:
        result = x / y
    except ZeroDivisionError as zde:
        print(zde.args)
    else:
        print(result)
    finally:
        print("finally")

    div4(3, 3)
    div4(3, 0)
    div4(3, [])
