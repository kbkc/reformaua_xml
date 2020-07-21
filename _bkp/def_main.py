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
"{http://base.google.com/ns/1.0}image_link"
]




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
    for node in tree.iter('item'):
        #print(node.tag, node.text)
        a=''
        l2=[]
        for node1 in node.getchildren():
            
            if(node1.tag in ltags):
                tx = html.unescape(node1.text).replace('"',"'").replace('&quot;',"'")
                if(flag == 'data'):
                    if(node1.tag == ltags[1]):
                        a+= '"'+ tx[-6:]+ '";' # get art No from name in new column
                        a+= '"'+ tx[:-7]+ '";' # cut art No from name
                    else:
                        a+= '"'+ tx+ '";'
                elif(flag=='img'):
                    if(node1.tag == ltags[1] ):
                        a+= '"'+ tx[-6:]+ '";' # get art No from name in new column
                    elif(node1.tag == ltags[8] ):
                        a+= '"'+ tx+ '";'
                elif(flag=='img_list'):
                    if(node1.tag == ltags[1] ):
                        l2.append(tx[-6:])
                    elif(node1.tag == ltags[8] ):
                        l2.append(tx)
            
        if(flag=='img_list' and l2!=[]):
                l1.append(l2)
                a=';'.join(l2)              
        out.write((a + '\n').encode('utf8'))
        
        #if(flag=='img_list'):
         #   writer = csv.writer(out)
          #  writer.writeline(l1)
    out.close()
    return(l1)


