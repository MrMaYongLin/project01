def test02():
    print("uuuu")

def error():
    num = 1
    try:
        print(num)
    except Exception as msg:
        print(msg)
    else:
        print("na meiuco")
    finally:
        print("bixu zhixing")
error()