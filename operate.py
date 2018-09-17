from bs4 import BeautifulSoup
import ht1
import re

def getInfo(url):
    url = 'http://detail.zol.com.cn/cell_phone/index1185512.shtml'
    text = ht1.request(url)
    soup = BeautifulSoup(text, "html.parser")
    price = str(soup.find_all('b', 'price-type'))
    num = re.findall('\d+', price)
    price = str(soup)

def writeToFile(text):
    f = open('result.txt', 'a', encoding='gbk', errors='ignore')
    f.write(str(text))
    f.close()

def operate1():
    tmp = 'http://detail.zol.com.cn'
    count = 1
    f = open('addresses.txt', 'a', encoding='gbk', errors='ignore')
    for i in range(104):
        #print('第' + str(i) + '页\n')
        url = 'http://detail.zol.com.cn/cell_phone_index/subcate57_0_list_1_0_1_2_0_' + str(i + 1) + '.html'
        text = ht1.get1(url)
        soup = BeautifulSoup(text, 'html.parser')
        content = soup.find_all(href=re.compile('/cell_phone/index\d+\.shtml'))
        for i in content:
            a = re.findall(r'(/cell_phone/index\d+.shtml)', str(i))
            #print(str(count) + ' ')
            #count += 1
            f.write(a[0] + '\n')

if __name__ == '__main__':
    operate1()