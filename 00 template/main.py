import calendar
import time
start = time.time()

print(time.time() - start, "detik")

cal = calendar.month(2021, 4)
print(cal)

def bintang(baris):
    kolom = baris *2 -1
    spasi = 0
    hasil = ""
    for i in range(baris):
        for j in range(spasi):
            hasil += " "
        for j in range(kolom):
            if i == 0:
                simbol = "*"
            elif i == baris -1:
                simbol =  "."
            elif j == 0 or j == kolom -1 :
                simbol = "*"
            else :
                simbol = "."
            hasil += simbol
        kolom -= 2
        spasi += 1
        if baris ==1 :
            hasil += ""
        else:
            hasil += "\n"
    baris = baris -1
    kolom = 3
    spasi = baris -1
    for i in range(baris):
        for j in range(spasi):
            hasil += " "
        for j in range(kolom):
            if j == 0 or j == kolom -1:
                simbol = "*"
            elif i == baris -1:
                simbol = "*"
            else :
                simbol = "."
            hasil += simbol
        kolom += 2
        spasi -= 1
        if i != baris -1:
            hasil += "\n"
        else :
            hasil+=""
    return hasil
ok = int(input())
print (bintang(ok))