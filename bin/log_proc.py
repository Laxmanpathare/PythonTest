f1=open(r'C:\Users\Admin\Desktop\Laxman\log\server_log.txt')
f2=open('out3.txt','w')
f3=open('out4.csv','w')
f2.writelines(['IP\t','DATE\t','PICS\t','WEBSITE\n'])
print('IP','DATE','PICS','WEBSITE',sep=',',file=f3)
for line in f1:
    if line[:3].isdigit():
        #print(line)
        sp=line.split()
        #print(sp)
        ip=sp[0]
        #print(ip)
        dt1=sp[3]#'[20/jun/2018:00:00:'
        dt1=dt1.split(':')#['[20/jun/2018','00']
        dt1=dt1[0]#'[20/jun/2018'
        dt2=dt1.lstrip('[')
        dt3=dt1[1:]
        dt4=dt1.replace('[','')
        dt5=dt1.split('[')[-1]

        dt6=sp[3]
        dt6=dt6[dt6.index('[')+1:dt6.index(':')]
        #if sp[6].startswith('/pics'):
        #if 'pics'in sp[6]:
        if sp[6][:5]=='/pics':
            im=sp[6]#/pics/abc.jpg
            im1=im.split('/')#['','pics','abc.jpg]
            im1=im1[-1]
        else:
            im1='No image'

        wb=sp[10]
        wb1=wb.strip('"')
        wb2=wb[1:-1]
        print(ip, dt6, im1,wb2)

        r=ip+'\t'+dt6+'\t'+im1+'\t'+wb2+'\n'
        f2.write(r)
        print(ip,dt6,im1,wb2,sep=',',file=f3)