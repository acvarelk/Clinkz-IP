import requests
import json
from colorama import *
init()
banner = Fore.GREEN + """
_________ .__  .__        __             ._____________ 
\_   ___ \|  | |__| ____ |  | __________ |   \______   |
/    \  \/|  | |  |/    \|  |/ /\___   / |   ||     ___/
\     \___|  |_|  |   |  \    <  /    /  |   ||    |    
 \______  /____/__|___|  /__|_ \/_____ \ |___||____|    
        \/             \/     \/      \/                """
print(banner)
ip = input("ENTER IP ][ ")
try:
        infoList1 = requests.get(f"http://ipwho.is/{ip}")
        infoList = infoList1.json()      
        if infoList.get("success"):
            print(f'╔══════════════                     ══════════════╗')
            print(f'    [+] Айпи адрес: {infoList["ip"]}')
            print(f'    [+] Успех: {infoList["success"]}  ')
            print(f'    [+] Тип: {infoList["type"]}     ')
            print(f'    [+] Континент: {infoList["continent"]}')
            print(f'    [+] Страна: {infoList["country"]}')
            print(f'    [+] Регион: {infoList["region"]}')
            print(f'    [+] Город: {infoList["city"]}')
            print(f'    [+] Широта: {infoList["latitude"]}')
            print(f'    [+] Долгота: {infoList["longitude"]}')
            print(f'    [+] Член ЕС: {infoList["is_eu"]}')
            print(f'    [+] Почтовый код: {infoList["postal"]}')
            print(f'    [+] Столица: {infoList["capital"]}')
            connection_info = infoList.get("connection", {})
            print(f'    [+] АСН: {connection_info.get("asn", "N/A")}')
            print(f'    [+] Организация: {connection_info.get("org", "N/A")}')
            print(f'    [+] Интернет-провайдер: {connection_info.get("isp", "N/A")}')
            print(f'    [+] Домен: {connection_info.get("domain", "N/A")}')
            currency_info = infoList.get("currency", {})
            print(f'    [+] Название валюты: {currency_info.get("name", "N/A")}')
            print(f'    [+] Код валюты: {currency_info.get("code", "N/A")}')
            print(f'    [+] Символ валюты:{currency_info.get("symbol", "N/A")}')
            print(f'    [+] Валюта во множественном числе: {currency_info.get("plural", "N/A")}')
            print(f'    [+] Обменный курс:{currency_info.get("exchange_rate", "N/A")}')
            security_info = infoList.get("security", {})
            print(f'    [+] Anonymous Proxy: {security_info.get("anonymous", "N/A")}')
            print(f'    [+] Web Proxy: {security_info.get("proxy", "N/A")}')
            print(f'    [+] VPN: {security_info.get("vpn", "N/A")}')
            print(f'    [+] TOR Node: {security_info.get("tor", "N/A")}')
            print(f'    [+] Hosting Provider: {security_info.get("hosting", "N/A")}')
            print(f'╚══════════════                     ══════════════╝\n')
            input('')  
        else:
            print(f'╔══════════════                     ══════════════╗')
            print(f'    [+] IP: {infoList["ip"]}')
            print(f'    [+] Success: {infoList["success"]}')
            print(f'    [+] Message: {infoList["message"]}')
            print(f'╚══════════════                     ══════════════╝\n')
except Exception as e:
        print(f'An error occurred: {e}')