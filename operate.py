from bs4 import BeautifulSoup
import ht1
import re
import xlwt

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
    count = 0
    count2 = 0
    count3 = 0
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('result', cell_overwrite_ok=True)
    sheet.write(0, 0, '编号')
    sheet.write(0, 1, '手机名称')
    sheet.write(0, 2, '参考价')
    sheet.write(0, 3, '评分')
    sheet.write(0, 4, '特点')
    sheet.write(0, 5, '详情页')
    f = open('addresses.txt', 'a', encoding='gbk', errors='ignore')
    for i in range(104):
        print('第' + str(i) + '页\n')
        url = 'http://detail.zol.com.cn/cell_phone_index/subcate57_0_list_1_0_1_2_0_' + str(i + 1) + '.html'
        text = ht1.get1(url)
        soup = BeautifulSoup(text, 'html.parser')
        #address, id
        content = soup.find_all('h3')
        content = content[1: -6]
        #content = content[6:]
        content2 = soup.find_all('b', class_ = 'price-type')
        content3 = soup.find_all('span', class_ = 'score')
        #print(content)
        #print(content2)
        for i in content:
            # if i in content2:
            #     #print(i.get_text())
            #     pass
            a = re.findall(r'(/cell_phone/index\d+.shtml)', str(i))
            #print(str(count) + ' ')
            count += 1
            #f.write(a[0] + '\n')
            sheet.write(count, 5, 'detail.zol.com.cn' + a[0])
            sheet.write(count, 0, str(count))
            soup2 = BeautifulSoup(str(i), 'html.parser')
            cha = soup2.h3.a.span.get_text()
            sheet.write(count, 4, cha)
            n = re.findall(r'">.*?<', str(i))
            sheet.write(count, 1, n[0][2:-1])
            #print(n)
        for i in content2:
            #print(i)
            count2 += 1
            soup3 = BeautifulSoup(str(i), 'html.parser')
            p = soup3.b.get_text()
            sheet.write(count2, 2, p)
        for i in content3:
            count3 += 1
            soup4 = BeautifulSoup(str(i), 'html.parser')
            s = soup4.span.get_text()
            sheet.write(count3, 3, s)

        #name
        for i in content:
            pass


        book.save(r'f:/phone.xls')

def operate2():
    tmp = 'http://detail.zol.com.cn'
    count = 0
    count2 = 0
    count3 = 0
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('result', cell_overwrite_ok=True)
    sheet.write(0, 0, '编号')
    sheet.write(0, 1, '相机名称')
    sheet.write(0, 2, '参考价')
    sheet.write(0, 3, '评分')
    sheet.write(0, 4, '特点')
    sheet.write(0, 5, '详情页')
    f = open('addresses.txt', 'a', encoding='gbk', errors='ignore')
    for i in range(104):
        print('第' + str(i) + '页\n')
        url = 'http://detail.zol.com.cn/digital_camera_index/subcate15_0_list_1_0_1_2_0_' + str(i + 1) + '.html'
        text = ht1.get1(url)
        soup = BeautifulSoup(text, 'html.parser')
        #address, id
        content = soup.find_all('h3')
        content = content[1: -6]
        #content = content[6:]
        content2 = soup.find_all('b', class_ = 'price-type')
        content3 = soup.find_all('span', class_ = 'score')
        #print(content)
        #print(content2)
        for i in content:
            # if i in content2:
            #     #print(i.get_text())
            #     pass
            a = re.findall(r'(/digital_camera/index\d+.shtml)', str(i))
            #print(str(count) + ' ')
            count += 1
            #f.write(a[0] + '\n')
            sheet.write(count, 5, 'detail.zol.com.cn' + a[0])
            sheet.write(count, 0, str(count))
            soup2 = BeautifulSoup(str(i), 'html.parser')
            cha = soup2.h3.a.span.get_text()
            sheet.write(count, 4, cha)
            n = re.findall(r'">.*?<', str(i))
            sheet.write(count, 1, n[0][2:-1])
            #print(n)
        for i in content2:
            #print(i)
            count2 += 1
            soup3 = BeautifulSoup(str(i), 'html.parser')
            p = soup3.b.get_text()
            sheet.write(count2, 2, p)
        for i in content3:
            count3 += 1
            soup4 = BeautifulSoup(str(i), 'html.parser')
            s = soup4.span.get_text()
            sheet.write(count3, 3, s)

        #name
        for i in content:
            pass


        book.save(r'f:/camera.xls')

if __name__ == '__main__':
    operate1()
    operate2()