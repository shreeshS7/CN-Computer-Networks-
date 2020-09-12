import socket

url = input("Enter url : ")
ip = socket.gethostbyname(url)
print("IP address of",url, ": " ,ip)
ip2 = input("Enter IP : ")
url2 = socket.gethostbyaddr(ip2)
print("DNS Server for given IP",ip2,": ",url2[0])


'''
Output:

Enter url : www.facebook.com
IP address of www.facebook.com :  157.240.16.35
Enter IP : 157.240.16.35
DNS Server for given IP 157.240.16.35 :  edge-star-mini-shv-01-bom1.facebook.com
'''
