import whois
import socket
import geocoder

from geocoder import ipinfo

def banner():
	print("""\033[32m
██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗    ██╗    ██╗██╗  ██╗ ██████╗ ██╗███████╗
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║    ██║    ██║██║  ██║██╔═══██╗██║██╔════╝
██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║    ██║ █╗ ██║███████║██║   ██║██║███████╗
██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║    ██║███╗██║██╔══██║██║   ██║██║╚════██║
██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║    ╚███╔███╔╝██║  ██║╚██████╔╝██║███████║
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝     ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝
\033[30;42m Simple Domain Information Gathering using WHOIS in Python \033[0m """)
banner()

example = input("\n\033[32mEnter Domain name : \033[0m")

y = whois.get(example)
x = socket.gethostbyname(example)
a = ipinfo(x)

print("\033[32mName :\033[0m",y.get("name"))
print("\033[32mIP :\033[0m",x)
print("\033[32mTLD :\033[0m",y.get("tld"))
print("\033[32mCountry :\033[0m",a.country)
print("\033[32mCity :\033[0m",a.city)
print("\033[32mRegion :\033[0m",a.state)
print("\033[32mLatitude :\033[0m",a.lat)
print("\033[32mLongitude :\033[0m",a.lng)
print("\033[32mRegistrar :\033[0m",y.get("registrar"))
print("\033[32mRegistrant country :\033[0m",y.get("registrant_country"))
print("\033[32mCreation date :\033[0m",y.get("creation_date"))
print("\033[32mExpiration date :\033[0m",y.get("expiration_date"))
print("\033[32mLast updated :\033[0m",y.get("last_updated"))
print("\033[32mStatus :\033[0m",y.get("status"))
print("\033[32mStatuses :\033[0m",y.get("statuses"))
print("\033[32mDNSSEC :\033[0m",y.get("dnssec"))
print("\033[32mName servers :\033[0m",y.get("name_servers"))
print("\033[32mASN :\033[0m",a.org)
print("\033[32mZIP/Postal code :\033[0m",a.postal)
print("\033[32mRegistrant :\033[0m",y.get("registrant"))
print("\033[32mEmails :\033[0m",y.get("emails"))
