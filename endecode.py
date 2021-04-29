import base64
from time import sleep

#colors
red = "\033[1;91m"
grean = "\033[1;92m"
yellow = "\033[1;93m"
blue = "\033[1;94m"
white = "\033[1;97m"


txt = """


 ██████╗ ██╗     ██╗████████╗ ██████╗██╗  ██╗
██╔════╝ ██║     ██║╚══██╔══╝██╔════╝██║  ██║
██║  ███╗██║     ██║   ██║   ██║     ███████║
██║   ██║██║     ██║   ██║   ██║     ██╔══██║
╚██████╔╝███████╗██║   ██║   ╚██████╗██║  ██║
 ╚═════╝ ╚══════╝╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝

"""

num = """

  _______________
 |               |
 | 1- Encode     |
 |               |
 | 2- Decode     |
 |_______________|


"""

print(grean)
print(txt)

print(blue)
print(num)

def endecode():
    try:
        while True:
            choose = int(input("\033[1;93m\n Choose Number: " +white))

            if choose == 1:
                sleep(0.2)
                encodeinput = input("\033[1;93m\nEnter Text To Encoding: " +white)

                encode = base64.b64encode(encodeinput.encode('UTF-8')).decode('ascii')
                sleep(1)
                print(white)
                print("\033[1;91m\nEncoding : " +white +encode)

            elif choose == 2:
                sleep(0.2)
                decodeinput = input("\033[1;93m\nEnter Text To Decoding: " +white)
                decode = decode_hash = base64.b64decode(decodeinput)
                decodeit = decode.decode('UTF-8')
                sleep(1)
                print("\033[1;91m\nDecoding : " +white +decodeit)

            else:
                endecode()
    except:
        sleep(1)
        print("\n\033[1;91m#Please Just Choose 1 Or 2")
        endecode()
endecode()
