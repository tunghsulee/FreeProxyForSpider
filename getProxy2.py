def Spider2():
    for i in range(1,101): #最大支持100页
        print('第%d页爬取完成' %i)
        headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        'cookie': 'page=%d;anonymity=anonymous'  %i   #这里可以改，具体请查看readme.md
        }
        url = 'https://proxyhub.me/zh/all-https-proxy-list.html'
        response = requests.get(url = url,headers=headers)
        print(response.status_code)
        tree = etree.HTML(response.text)
        servers = tree.xpath('/html/body/div/div/div[3]/table/tbody/tr')
        for server in servers:
            try:
                ip = server.xpath('./td[1]/text()')[0]
                port = server.xpath('./td[2]/text()')[0]
                type = server.xpath('./td[3]/text()')[0]
            except:
                continue
            anonymity = server.xpath('./td[4]/text()')[0]
            try:
                country = server.xpath('./td[5]/a/text()')[0]
            except:
                country = 'unknown'
            result = [ip , port , type , anonymity , country ]
            result = ",".join(result) + '\n'
            # print(result)
            with open ('/var/pyproject/https-anonymous.csv','a') as fp:
                fp.write(result)
        i = i+1
