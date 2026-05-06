class amarine:#class bernama amarin e untuk menyimpan objek dan jaraknya
    def __init__(self,nama, jarak):
        self.__nama = nama
        self.__jarak = jarak
    
    #getter
    def getNama(self):
        return self.__nama
    def getJarak(self):
        return self.__jarak
    
    #setter
    def setNama(self, nama):
        self.__nama = nama

    def setJarak(self, jarak):
        self.__jarak = jarak


class RobotAUV():#class robotAUV untuk menyimpan list objek amarine yang telah dibuat                              
    def __init__ (self):
        self.__listObjek = []
    
    #fungsi append
    def tambahObjek(self, objek):
        self.__listObjek.append(objek)
        print(f"==============objek '{objek.getNama()}' berhasil ditambahkan==================\n")
    
    #getter
    def getlistObjek(self):
        return self.__listObjek
    
    #jumlah total objek
    def totallistObjek(self):
        return len(self.__listObjek)
    

def menu():    
    
    robot = RobotAUV()
    
    while True:
        print("MENU\n1. menambah objek \n2. menampilkan list objek\n3. keluar ")
        #input pilihan di menu
        pilihan = input("pilihan anda: ")
        
        #jika pilioh 1 menambah dan memanggil fungsi append
        if pilihan == "1":
            nama = input("masukan nama: ")
            jarak = input("masukan jarak: ")
            objek = amarine(nama, jarak)
            robot.tambahObjek(objek)           
            
        #pilih 2 menampilkan semua objek yang telah ditambah 
        elif pilihan == "2":
            if not robot.getlistObjek():
                print("=========Daftar list masih kosong, silahkan tambahkan objek terlebih dahulu=========\n")
            else:
                print("\n=============menampilkan list objek==================")
                for i, objek in enumerate(robot.getlistObjek(),1):
                    print(f"{i}. Nama: {objek.getNama()}, dengan jarak: {objek.getJarak()}")
                print(f"\ntotal objek pada daftar = {robot.totallistObjek()}\n")
        
        #pilih 3 untuk keluar dari program
        elif pilihan == "3":
            print("=================Keluar dari program...====================")
            break
        
        #jika salah ketik dari pilihan yang tersedia
        else:
            print("Pilihan anda tidak valid silahkan masukkan pilihan yang benar\n1")
            
menu()


