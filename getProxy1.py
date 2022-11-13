import requests
from lxml import etree
def Spider(pagestart,pagenum):
    headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
    for pagenum in range(pagestart,pagenum+1):
        pagenum = str(pagenum)
        url = 'https://www.toolbaba.cn/ip?p=' + pagenum  #pagenum从0开始
        response = requests.get(url=url,headers=headers)
        status_code = str(response.status_code)
        tree = etree.HTML(response.text)
        trs = tree.xpath('/html/body/div/div[1]/div[4]/div/table//tr')
        for tr in trs:
            if status_code == '200' :
                try:
                    protocol = tr.xpath('./td[3]/text()')[0]  #protocol是协议的意思
                except:
                    protocol = 'na'
                if protocol == 'na':
                    continue
                ip = tr.xpath('./td[1]/text()')[0]
                port = tr.xpath('./td[2]/text()')[0]
                safe = tr.xpath('./td[5]/text()')[0]   #匿名程度
                result = ip + "," + port + "," + protocol + "," + safe + ","+ pagenum + "\n"
                print(result)
                if 'HTTPS' in protocol and '高' in safe: 
                    with open('https-anonymous.csv','a') as fp:
                        fp.write(result)
                elif 'HTTPS' in protocol and '高' not in safe:
                    with open('https-unanonymous.csv','a') as fp:
                        fp.write(result)
                else :
                    with open('other-proxies.csv','a') as fp:
                        fp.write(result)
            else :
                result = status_code , str(pagenum)
                print(result)
                break
            print('第'+pagenum+"页爬取完成！！")
            print('=====================================')
