def encrypt(x):

    new_passwd = ""
    vacant_list = []
    vacant_list = list(x)
    alpha_caps = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    alpha_small= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alpha_encrypt_c = ['N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M']
    alpha_encrypt_s = ['n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m']
    num_list = ["1","2","3","4","5","6","7","8","9","0"]
    num_encrypt = ["6","7","8","9","0","1","2","3","4","5"]

    for i in vacant_list:
        if i in alpha_caps:
            indx = alpha_caps.index(i)
            new_passwd+=alpha_encrypt_c[indx]
            x = new_passwd
        elif i in alpha_small:
            indx = alpha_small.index(i)
            new_passwd+=alpha_encrypt_s[indx]
            x = new_passwd
        elif i in num_list:
            indx = num_list.index(i)
            new_passwd+=num_encrypt[indx]
            x = new_passwd
        else:
            new_passwd+=i
            x=new_passwd

    return new_passwd

def decrypt(x):
    true_passwd = ''
    vacant_list = []
    vacant_list = list(x)
    alpha_caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']
    alpha_small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
    alpha_encrypt_c = ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F',
                       'G', 'H', 'I', 'J', 'K', 'L', 'M']
    alpha_encrypt_s = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f',
                       'g', 'h', 'i', 'j', 'k', 'l', 'm']
    num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    num_encrypt = ["6", "7", "8", "9", "0", "1", "2", "3", "4", "5"]

    for i in vacant_list:
        if i in alpha_encrypt_c:
            indx = alpha_encrypt_c.index(i)
            true_passwd += alpha_caps[indx]
        elif i in alpha_encrypt_s:
            indx = alpha_encrypt_s.index(i)
            true_passwd +=alpha_small[indx]
        elif i in num_encrypt:
            indx = num_encrypt.index(i)
            true_passwd+=num_list[indx]
        else:
            true_passwd+=i

    return true_passwd


user_password = str(input("Create your password. : "))
user_password = str(user_password)
print("USER PASSWORD  : ->",user_password)
x = encrypt(user_password)

print("encrypted password = ",x)

x = decrypt("Funaxre@6493")

print("Decrypted Password : ",x)
