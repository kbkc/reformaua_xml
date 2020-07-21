# parse .xml into .csv
from xml.etree import ElementTree
import pprint
import html

import urllib
from urllib.request import urlopen

import csv
import io

ltags = [
"{http://base.google.com/ns/1.0}id",
"{http://base.google.com/ns/1.0}title",
"{http://base.google.com/ns/1.0}description",
"{http://base.google.com/ns/1.0}condition",
"{http://base.google.com/ns/1.0}product_type",
"{http://base.google.com/ns/1.0}google_product_category",
"{http://base.google.com/ns/1.0}price",
"{http://base.google.com/ns/1.0}brand",
"{http://base.google.com/ns/1.0}image_link",
"{http://base.google.com/ns/1.0}link",
"{http://base.google.com/ns/1.0}availability",
"{http://base.google.com/ns/1.0}sale_price",
"{http://base.google.com/ns/1.0}mpn"
]


def read_custom_csv(fn):
    with open(fn, 'r') as f:
        reader = csv.reader(f,delimiter=';')
        your_list = list(reader)
    return your_list

def save_url(dir,art,ext,url):
    file_name = dir+art+ext
    with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
        data = response.read() # a `bytes` object
        out_file.write(data)
        out_file.close()
    return

def dup_rename(l):
    dupes = [x for n, x in enumerate(l) if x in l[:n]]
    print(dupes)

    return l


def read_data(in_url_name):
    # # ########################## # #
    # #   begin xml read block

    ## read file from url:
    response = urllib.request.urlopen(in_url_name)
    tree = ElementTree.parse(response)
    ## read from file:
    #with open(in_file_name, 'rb') as f:
    #    tree = ElementTree.parse(f)

    # #    end xml read block
    # # ########################## # #
    return tree

def write_csv(tree, out_file_name,flag):
    out = open(out_file_name, 'wb')
    l1=[]
    l01=[]
    l02=[]
    for node in tree.iter('item'):       
        l2= []
        for node1 in node.getchildren():
            #print(node1)
            if(node1.tag in ltags):
                tx =html.unescape(node1.text).replace('"',"'").replace('&quot;',"'")
                if(flag!='img_list' and node1.tag in [ltags[1],ltags[2],ltags[3],ltags[8]]):
                    tx ='"'+ tx +'"'
                if(flag == 'data'):
                    if(node1.tag == ltags[1]):
                        l2.append(tx[-7:-1]) # get art No from name in new column
                        l2.append(tx[:-8]+'"') # cut art No from name
                    else:
                        l2.append(tx)
                elif(flag=='img'):
                    if(node1.tag == ltags[1] ):
                         l2.append(tx[-7:-1]) # get art No from name in new column
                    elif(node1.tag == ltags[8] ):
                         l2.append(tx)
                elif(flag=='img_list'):
                    if(node1.tag == ltags[1] ):
                        l2.append(tx[-6:])
                        l01.append(tx[-6:])
                    elif(node1.tag == ltags[8] ):
                        l2.append(tx)
                        l02.append(tx)
            
        #if(flag=='img_list' and l2!=[]):
         #       l1.append(l2)       
        out.write((';'.join(l2)+'\n').encode('utf8'))
        #if(flag=='img_list'):
         #   writer = csv.writer(out)
          #  writer.writeline(l1)
    l1.append(l01)
    l1.append(l02)
    out.close()
    return(l1)


