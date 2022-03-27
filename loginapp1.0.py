print("Hallo this is a login basic program that made by Marvin XI SIJA")
name = (input("Would you like to give your name?: "))

print (f"Hallo {name} glad to see you")

#This is an input program 
kelas = (input("Masukkan jenis jurusan anda [IT / TEKNIK: "))
#if else statement 
if kelas == "IT":
    jurusan = (input("Masukkan Jurusan kamu [TKJ/RPL/SIJA]: "))
else: 
    jurusan = (input("Masukkan Jurusan kamu [TFLM/TOI/TKRO/TP]: "))
#else-if statement 
if jurusan == "SIJA": 
    mapel = (input("Masukkan jenis mapel kamu hari ini [SIOT/SKJ/PAAS]: "))
    print("Silahkan masuk ke LAB SIJA gedung E ")
elif jurusan == "TKJ": 
    mapel = (input("Masukkan jenis mapel kamu hari ini [ASJ/ISJ]: "))
    print("Silahkan masuk ke LAB TKJ gedung F")
else: 
    mapel = (input("Masukkan jenis mapel kamu hari ini [PBO/WEB]: "))
    print("Silahkan masuk ke ruang RPL 2 gedung G")

