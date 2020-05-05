#cython: language_level=3
import stdbase64 as base64

def Encrypt(byte, loopTime, debug = False):
    result = byte
    if debug:
        for time in range(1, loopTime + 1):
            result = base64.b64encode(result)
            print("Current loop time:", time)
    else: 
        for time in range(1, loopTime + 1):
            result = base64.b64encode(result)

    return result

def Decrypt(byte, loopTime, debug = False):
    result = byte
    if debug:
        for time in range(1, loopTime + 1):
            result = base64.b64decode(result, validate = True)
            print("Current loop time:", time)
    else: 
        for time in range(1, loopTime + 1):
            result = base64.b64decode(result, validate = True)

    return result

def TryDecrypt(byte, decryptLastTime = False, debug = False):
    result = byte
    try:
        if debug:
            loopTimes = 0
            while True:
                result = base64.b64decode(result, validate = True)
                loopTimes += 1
                print("Current loop time:", loopTimes)
                print(result)
        else:
            while True:
                result = base64.b64decode(result, validate = True)
    except:
        if not decryptLastTime:
            result = base64.b64encode(result)
        return result

def EncryptToFile(byte, loopTime, path, debug = False):
    file = open(path, "wb")
    file.write(Encrypt(byte, loopTime, debug))
    file.close()

def DecryptToFile(byte, loopTime, path, debug = False):
    file = open(path, "wb")
    file.write(Decrypt(byte, loopTime, debug))
    file.close()

def DecryptFromFile(fileObj, loopTime, debug = False):
    return Decrypt(fileObj.read(), loopTime, debug)

def EncryptFromFile(fileObj, loopTime, debug = False):
    return Encrypt(fileObj.read(), loopTime, debug)
