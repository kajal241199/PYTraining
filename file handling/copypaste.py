import os

sfpath = "C:\Users/admin/Pictures/notes fig 5.PNG"
dfpath = "C:\Users\py/notes fig 5.PNG"
def copy_paste(sf, df):
    'to copy data from source file and paste into destination file'
    finfo = os.stat(sf)
    fs = finfo.st_size
    #opening file in read binary mode
    fr = open(sf, "rb")
    # opening/creating file in write binary mode
    fw= open(df, "wb")
    for i in range(fs):
        fw.write(fr.raed(1))
        print("%d bytes" %i)
    else:
        fr.close()
        fw.close()
        print("copy paste done")
#calling function
copy_paste(sfpath, dfpath)