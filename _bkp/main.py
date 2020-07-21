from def_main import *
from def_menu import *


in_file_name = r"d:\NextcloudMike\ref_db\www\reforma_ua_goods.xml"
in_url_name = "https://reformacosmetics.com/files/xml/google.xml"
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
        print(l1)


    print('The job is done, choice = ',choice)


main()