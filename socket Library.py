#Python DNS Lookup Tool (Forward & Reverse Resolution)
import socket
hostname = 'www.google.com'
hn = socket.getfqdn(hostname)
print(socket.getfqdn("8.8.8.8"))
#getfqdn = get the quailified domain name  

#DNS Lookup Tool in Python (Domain To Ip)
Domain = input('Enter the Domain URL : ')
ip = socket.gethostbyname(Domain)  
print(ip)

#Get Local Hostname using Python scocket
import socket 
Hname = socket.gethostname()
print(Hname)

#pip install socket لو حصل مشكله نكتب كذا في التيرمنال