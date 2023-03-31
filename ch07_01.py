def main():
    with open('le_fichier.txt','r') as f:
        # all = f.read()
        # print(all)
        # one = f.readline()
        # print(one)
        # all_list = f.readlines()
        # print(all_list)
        for line in f:
            print(line.strip())



def main_write():
    with open('le_fichier.txt','a') as f:
        # f.write("Ligne 01")
        # f.write("Ligne 02")
        print("Ligne 01",file=f)
        print("Ligne 02",file=f)



if __name__=='__main__':
    main()
