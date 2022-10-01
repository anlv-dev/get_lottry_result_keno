from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen
from collections import Counter
import re
import csv



def check_No_Re_Str(no):
    if len(str(no)) == 1:
        return '000000' + str(no)
    elif  len(str(no)) == 2:
        return '00000' + str(no)
    elif  len(str(no)) == 3:
        return '0000' + str(no)
    elif  len(str(no)) == 4:
        return '000' + str(no)
    elif  len(str(no)) == 5:
        return '00' & str(no)
    elif  len(str(no)) == 6:
        return '0' + str(no)
    elif  len(str(no)) == 7:
        return str(str(no))
    else:
        print('Vietlotte da thay doi day so crow')

PAGE_NUMBER = 1
ARAWDATA = []
BRAWDATA = []
OFFICALDATA = {}

while PAGE_NUMBER<=1:
    COUNTER = 0
    CURRENT_PAGE = 104199
    PAGE = check_No_Re_Str(CURRENT_PAGE)
    #print(PAGE)
    url = urlopen('https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/view-detail-keno-result?id={}'.format(PAGE))
    #url = urlopen('https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/view-detail-keno-result?id=0104199')
    RAW = url.read()
    url.close()
    PARSED = Soup(RAW,'html.parser')
    
    new_content = PARSED.find_all('span', {'class' : 'bong_tron small'}) # using beautiful soup's find_all
    date_content = PARSED.find_all('td',style="vertical-align:top; padding:5px;color:maroon;font-size:16px")
    p='\d+'
    k = '\b(\d{2}/\d{2}/\d{4})'
    for content in new_content:
        temp1 = re.findall(r'\d+', str(content)) # find number of digits through regular expression
        res1 = list(map(int, temp1))
        #print(res1[0])
    for d in date_content:
        if d:
            print(d)
            temp2 = re.findall(r'\b(\d{2}/\d{2}/\d{4})', str(d)) # find date through regular expression
            #res2 = list(map(int, temp2))
            print(temp2[0])
            
            

    PAGE_NUMBER +=1




