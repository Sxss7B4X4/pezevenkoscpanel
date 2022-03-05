import time
import os
##################################################
# Bu Program Time Ve Os sistemini kullanmaktadir #
# Tum Haklari TGT ye ve Alyx e Aittir            #
##################################################
os.system("color a")
print("""####################################
# PezevenkOS Kontrol Paneli        # 
# 1 - Cmd yi acar                  #
# 2 - Regedit i acar               #
# 3 - Aygit Yoneticisini Acar      #
####################################""")
secim=input("Seciminiz Nedir 1-2-3 : ")


if secim =='1':
    os.system("start cmd")


if secim =='2':
    os.system("start regedit")


if secim =='3':
    os.system("start devmgmt.msc")

print("Bu Sekme 5SN Icinde Kapanacak")
time.sleep(5)
