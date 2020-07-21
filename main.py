from def_main import *
from def_menu import *
import os


in_file_name = r"d:\NextcloudMike\ref_db\www\reforma_ua_goods.xml"
in_url_name = "https://reformacosmetics.com/files/xml/google.xml"
#             "https://reformacosmetics.com/files/xml/google.xml"
out_file_name = r'd:\out.csv'


def main():
    choice=run_menu()
    print('you pressed ',choice)

    if choice == "1":
        tree = read_data(in_url_name)
        write_csv(tree, out_file_name,'data')
    elif choice=="2":
        tree = read_data(in_url_name)
        write_csv(tree, out_file_name,'img')       
    elif choice=="3":
        tree = read_data(in_url_name)
        l1 = write_csv(tree, out_file_name,'img_list')
        #d = ['234','45','55','234','56','45','67','234']
        #print(dup_rename(d)#l1[0]))
        i=0
        for a,u in zip(l1[0],l1[1]):
            save_url('d:\\tmp\\pics\\',a,os.path.splitext(u)[1],u)
            print(a,os.path.splitext(u)[1],'   saved')
            i+=1
            #if(i >100):
            #    break
    elif choice=="4":
        l1 = read_custom_csv(r'D:\out_rc.csv')
        i=0
        #print(l1)
        for l2 in l1:
            if(len(l2)==2):
                if(l2[1]!=''):
                    save_url('d:\\tmp\\pics_sbor\\',l2[0],os.path.splitext(l2[1])[1],l2[1])
                    print(l2[0],os.path.splitext(l2[1])[1],'   saved')
            i+=1
            #if(i >100):
            #    break
    print('\nThe job is done, choice = ',choice)


main()