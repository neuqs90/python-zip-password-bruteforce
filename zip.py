import pyzipper
import itertools

zip_file_path = input("\nEnter ZIP File Path : ")

combinations = []

numconfirm = input("\nIs The Password Contains Numbers ? ( if dont know , enter 'yes') ( yes / no ) : ")

charconfirm = input("\nIs The Password Contains Characters ? ( if dont know , enter 'yes') ( yes / no ) : ")

specialcharconfirm = input("\nIs The Password Contains Special Characters ? ( if dont know , enter 'yes') ( yes / no ) : ")

if charconfirm.lower() == "yes" or charconfirm.lower() == "y":
    combinations.append("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

if specialcharconfirm.lower() == "yes" or specialcharconfirm.lower() == "y":
    combinations.append("!@#$%^&*()?/<>.,;':\"|\\")

if numconfirm.lower() == "yes" or numconfirm.lower() == "y":
    combinations.append("0123456789")

password_length = input("\nEnter Maximun Guessed Password Length (eg . 6 numbers or 9 characters ) : ")

password_found = False

file_name = zip_file_path.split(".")[0]
if "/" in file_name:
    file_name = file_name[file_name.rfind("/")+1:]

for r in range(1, int(password_length)+1):  
    if password_found:
        break  
    for combo in itertools.product(*combinations, repeat=r):
        password = ''.join(combo)
        print("Trying : " + password)
        try:
            with pyzipper.AESZipFile(zip_file_path) as zf:
                zf.extractall(path=file_name + "/", pwd=password.encode())
                print("Password Found:", password)
                password_found = True
                break
        except:
            continue
    
    
if not password_found:
    print("Password not found.")
