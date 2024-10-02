import random
import rarfile
import threading

filePath = input('enter file path: ')
extractedPath = filePath.split('.')[0]
tested = []
# def gettingFile():
#     rar_file = rarfile.RarFile(filePath)
#     passWord = random.randint(1000,9999)
#     for i in range(1000,10000):
#     # passWord = random.randint(10000000,99999999)
#     # for i in range(10000000,100000000):
#         if passWord not in tested:
#             try:
#                 rar_file.extractall(path=extractedPath, pwd=str(passWord))
#                 print("Password is correct! File is ready" + str(passWord))
#                 return True
#             except rarfile.BadRarFile:
#                 print("Password is incorrect or the file is corrupted." + str(passWord))
#                 tested.append(passWord)
#                 pass
#         else:
#             passWord = random.randint(1000,9999)
#             # passWord = random.randint(10000000,99999999)
#             pass
#     return False


def gettingFile1():
    rar_file = rarfile.RarFile(filePath)
    passWord = random.randint(1000,9999)
    for i in range(1000,10000):
    # passWord = random.randint(10000000,99999999)
    # for i in range(10000000,100000000):
        if passWord not in tested:
            try:
                rar_file.extractall(path=extractedPath, pwd=str(passWord))
                print("Password is correct! File is ready" + str(passWord))
                t2.stop()
                t3.stop()
                t4.stop()
                return True
            except rarfile.BadRarFile:
                print("Password is incorrect or the file is corrupted." + str(passWord))
                tested.append(passWord)
                pass
        else:
            passWord = random.randint(1000,9999)
            # passWord = random.randint(10000000,99999999)
            pass
    return False

def gettingFile2():
    rar_file = rarfile.RarFile(filePath)
    passWord = random.randint(1000,9999)
    for i in range(1000,10000):
    # passWord = random.randint(10000000,99999999)
    # for i in range(10000000,100000000):
        if passWord not in tested:
            try:
                rar_file.extractall(path=extractedPath, pwd=str(passWord))
                print("Password is correct! File is ready" + str(passWord))
                t1.stop()
                t3.stop()
                t4.stop()
                return True
            except rarfile.BadRarFile:
                print("Password is incorrect or the file is corrupted." + str(passWord))
                tested.append(passWord)
                pass
        else:
            passWord = random.randint(1000,9999)
            # passWord = random.randint(10000000,99999999)
            pass
    return False

def gettingFile3():
    rar_file = rarfile.RarFile(filePath)
    passWord = random.randint(1000,9999)
    for i in range(1000,10000):
    # passWord = random.randint(10000000,99999999)
    # for i in range(10000000,100000000):
        if passWord not in tested:
            try:
                rar_file.extractall(path=extractedPath, pwd=str(passWord))
                print("Password is correct! File is ready" + str(passWord))
                t1.stop()
                t2.stop()
                t4.stop()
                return True
            except rarfile.BadRarFile:
                print("Password is incorrect or the file is corrupted." + str(passWord))
                tested.append(passWord)
                pass
        else:
            passWord = random.randint(1000,9999)
            # passWord = random.randint(10000000,99999999)
            pass
    return False

def gettingFile4():
    rar_file = rarfile.RarFile(filePath)
    passWord = random.randint(1000,9999)
    for i in range(1000,10000):
    # passWord = random.randint(10000000,99999999)
    # for i in range(10000000,100000000):
        if passWord not in tested:
            try:
                rar_file.extractall(path=extractedPath, pwd=str(passWord))
                print("Password is correct! File is ready" + str(passWord))
                t1.stop()
                t2.stop()
                t3.stop()
                return True
            except rarfile.BadRarFile:
                print("Password is incorrect or the file is corrupted." + str(passWord))
                tested.append(passWord)
                pass
        else:
            passWord = random.randint(1000,9999)
            # passWord = random.randint(10000000,99999999)
            pass
    return False


t1 = threading.Thread(target=gettingFile1())
t2 = threading.Thread(target=gettingFile2())
t3 = threading.Thread(target=gettingFile3())
t4 = threading.Thread(target=gettingFile4())


def gettingFile():
    t1.start()
    t2.start()
    t3.start()
    t4.start()


gettingFile()



# import rarfile
# import itertools
# import string


# tested = []
# def crack_rar(file_path, password_length, charset="0123456789"):
#     rar_file = rarfile.RarFile(file_path)
#     for attempt in itertools.product(charset, repeat=password_length):
#         password = attempt
#         try:
#             rar_file.extractall(path=extractedPath, pwd=str(password))
#             print(f"Password found: {password}")
#             return password
#         except rarfile.BadRarFile:
#             print(password)
#             pass
#     print("Password not found")
#     return None

# # Example usage:
# file_path = input('enter file path: ')
# extractedPath = file_path.split('.')[0]
# password_length = 4
# crack_rar(file_path, password_length)