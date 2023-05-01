# (F14) Mendefinisikan Fungsi Save
from util import *
import os.path
from load_data import *

def save(username_arr,password_arr,role_arr,data_candi,data_bahan_bangunan):
#Fungsi ini menyimpan data 
    folder=input("\nMasukkan nama folder: ")
    print("\nSaving...")
    if not os.path.isdir("save"):
        print("\nMembuat folder save...")
        os.mkdir("save")
    if not os.path.isdir("save/"+folder):
        print("Membuat folder save/"+folder)
        os.mkdir("save/"+folder)

    #memasukkan array username, password, dan role ke satu array data_user
    data_user=["%" for i in range (103)]
    data_user[0]=["username","password","role"]
    for i in range (1, 103):
        if username_arr[i-1]!="%":
            temparr=["%" for i in range (3)]
            temparr[0]=username_arr[i-1]
            temparr[1]=password_arr[i-1]
            temparr[2]=role_arr[i-1]
            data_user[i]=temparr

    #menulis data di data_user ke user.csv
    user=open("save/"+folder+"/user.csv",'w+')
    line=data_user[0][0]
    for j in range (1,3):
        line+=";"+data_user[0][j]
    user.write(line)
    for i in range (1,cariindeksterakhir(data_user,103)+1):
        user.write('\n')
        if data_user[i]!="%":
            line=data_user[i][0]
            for j in range (1,3):
                line+=";"+data_user[i][j]
            user.write(line)
    user.close()

    #menulis data di data_candi ke candi.csv
    candi=open("save/"+folder+"/candi.csv",'w+')
    line=data_candi[0][0]
    for j in range (1,5):
        line+=";"+data_candi[0][j]
    candi.write(line)
    for i in range (1,cariindeksterakhir(data_candi,101)+1):
        candi.write('\n')
        if data_candi[i]!="%":
            line=data_candi[i][0]
            for j in range (1,5):
                line+=";"+str(data_candi[i][j])
            candi.write(line)
    candi.close()

    #menulis data di data_bahan_bangunan ke bahan_bangunan.csv
    bahan=open("save/"+folder+"/bahan_bangunan.csv",'w+')
    line=data_bahan_bangunan[0][0]
    for j in range (1,3):
        line+=";"+data_bahan_bangunan[0][j]
    bahan.write(line)
    for i in range (1,4):
        bahan.write('\n')
        if data_bahan_bangunan[i]!="%":
            line=data_bahan_bangunan[i][0]
            for j in range (1,3):
                line+=";"+data_bahan_bangunan[i][j]
            bahan.write(line)
    bahan.close()
    print(f"\nBerhasil menyimpan data di folder save/{folder}!")