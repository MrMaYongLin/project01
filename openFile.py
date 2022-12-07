import time

def openF():
    try:
        ss = open( 'ss.txt' )
        try:
            while True:
                content = ss.readline()
                if len(content) == 0:
                    break
                time.sleep(3)
                print(content)
        except:
            print("wenjian zhongduanle")
        finally:
            ss.close()
            print("guanbi file")
    except Exception as nsg:
        print(nsg)

openF()

