import subprocess                     # install subprocess
from bs4 import BeautifulSoup         # install beautifulsoup4
import os


list_subdomains=['wiki.owasp.org','dsomm.owasp.org','ahihi.org']   # list subdomain input
dir_output="/home/kali/Downloads/ahihi"                            # path de file html dc tao ra
name_output="amass2"                                               # ten file html
root_domain="owasp.org"                                            # root domain


command = 'amass viz -d3 -o {0} -oA {1} -d {2} '.format(dir_output,name_output,root_domain)  # create file HTML for priority
print(command)
os.system(command)

# Opening the html file
HTMLFile = open("{0}/{1}.html".format(dir_output,name_output), "r")

# Reading the file
index = HTMLFile.read()

# Creating a BeautifulSoup object and specifying the parser
S = BeautifulSoup(index, 'html.parser' )

print(type(S.select('script:nth-of-type(1)')))

script = S.select('script:nth-of-type(1)').__str__()

start=script.find("nodes: [")+8
end=script.find("],")

script=script[start:end:1].replace(" ", "").replace("\n\n", " ")

# print(script)


# create bien dictionary ( KEY - VALUE)  (subdomain - num )
def createDict(list_subdomains,script):
    dict ={}
    a_list = list_subdomains.copy()
    total =0
    ave = 0
    for x in list_subdomains:
        index=script.find(x)
        if index != -1 :
            end= script.rfind(",label:",0,index)
            start= script.rfind(",num:",0,index)+5
            num = int(script[start:end:1])
            # print(num)
            dict[x]=num
            a_list.remove(x)
            total += num
            # print(dict)

    # print(len(dict))
    # print(total)
    if total !=0:
        ave = total//len(dict)
    # print(ave)
    for x in a_list:
        dict[x] = ave
    return dict

dic = createDict(list_subdomains,script)
def get_num(subdomain,dict):
    return dict[subdomain]

def checkWAF(subdomain):
    output = subprocess.check_output(["wafw00f",subdomain],universal_newlines=True)
    if output.find(" is behind ") != -1:
        return 1
    else:
        return 0


new_list = sorted(list_subdomains, key=lambda x: (get_num(x,dic), checkWAF(x)))
print(new_list)
