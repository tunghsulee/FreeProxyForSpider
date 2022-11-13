from multiprocessing.dummy import Pool

f =  open('/var/pyproject/https-anonymous.csv','r')
ips = []
for line in f:
    listip = list(line.split(","))
    ip = str(listip[0]) +':'+str(listip[1])  
    ips.append(ip)

def testip(ip):
    headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    }
    try:
        
        r = requests.get(url = 'The siteUrl you want to test' , proxies = { 'https' : 'https://' + ip } ,headers=headers,timeout=5,verify =False) #若失败，请将proxies = { 'https' : 'https://' + ip }改为proxies = { 'https' : 'http://' + ip }
        result = ip + '\n'
        print(r.status_code)
        print('第',ips.index(ip),'个：yes:\t'+result + '------------------------------------------------------------')
        with open('canuse.csv','a') as fp:
            fp.write(result)
        
    except Exception as e:
        result = ip + '\n'
        print('第',ips.index(ip),'个：no:\t'+result + '-------------------------------------------------------------')
        with open ('reason.csv','a') as fp:
            fp.write(str(e)+'\n')

p = Pool(1024)  #自行选择
p.map(testip,ips)
