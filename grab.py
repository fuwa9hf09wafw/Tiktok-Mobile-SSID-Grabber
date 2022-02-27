from os import system
import requests

from colorama import Fore
from time import sleep

class grab_ssid(object):
    def __init__(self, email: str, str = None) -> None:

        self._request_session = requests.Session()
        self._request_session.headers = {'Accept-Encoding': 'gzip','passport-sdk-version': '19','sdk-version': '2','User-Agent': 'com.zhiliaoapp.musically/2022209010 (Linux; U; Android 7.1.2; en_US; MGHN3VC/A; Build/N2G48H;tt-ok/3.10.0.2)',}
        self._session_id = ""
        self._ticket = ""
        self._email_code = ""
        self._email = email
        self._password = ""
        self._encrypt_algorythm = {"0": "35", "1": "34", "2": "37","3": "36","4": "31","5": "30","6": "33","7": "32","8": "3d", "9": "3c",}
        self.send_code(email)


    def encrypt(self,text: str):
        encryption = ''
        for _ in text:
            for key,value in self._encrypt_algorythm.items():
                if key == _:
                    encryption += value
        return encryption
    
    def new_password_set(self,ticket,password):
        cookies = {'passport_csrf_token': '7cf44766fba6039fb5d9a11d391ccd0a','passport_csrf_token_default': '7cf44766fba6039fb5d9a11d391ccd0a','store-idc': 'maliva','store-country-code': 'ca','odin_tt': '979436195002bfcc4c6e529c39e1472a449ed8601e3a7d626263375f64a2e23fe0d7c8170101a4bf1b44814c817d49458efe9e2175f17054763a4657ad6672e45311c041bba53b8fef59e60630397612','d_ticket': '2b21c627134e865c8b978a21d65f26bb8d96c',}
        headers = { 'X-SS-STUB': '9C17E0D1DEED41B0F1BD99705D5E2B97','Accept-Encoding': 'gzip','x-tt-passport-csrf-token': '7cf44766fba6039fb5d9a11d391ccd0a','passport-sdk-version': '19','sdk-version': '2','User-Agent': 'com.zhiliaoapp.musically/2022209010 (Linux; U; Android 7.1.2; en_US; MGHN3VC/A; Build/N2G48H;tt-ok/3.10.0.2)'}
        data = {'password': password,'ticket': ticket,'account_sdk_source': 'app','rules_version': 'v2','mix_mode': '1','multi_login': '1'}
        status = self._request_session.post('https://api16-normal-c-useast1a.tiktokv.com/passport/password/reset_by_email_ticket/?passport-sdk-version=19&iid=7052926935345284870&device_id=7044441236568081925&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=220901&version_name=22.9.1&device_platform=android&ab_version=22.9.1&ssmix=a&device_type=MGHN3VC%25%2FA&device_brand=iPhone+12&language=en&os_api=25&os_version=7.1.2&openudid=993a612a96d993af&manifest_version_code=2022209010&resolution=720%2A1280&dpi=240&update_version_code=2022209010&_rticket=1642138368216&current_region=HK&app_type=normal&sys_region=US&mcc_mnc=42501&timezone_name=Asia%25%2FShanghai&residence=HK&ts=1642138367&timezone_offset=28800&build_number=22.9.1&region=US&uoo=0&app_language=en&carrier_region=IL&locale=en&op_region=HK&ac2=wifi&host_abi=x86&cdid=82f9ac8f-2b2a-4f08-98da-872978252032&support_webview=1&okhttp_version=4.1.73.9-tiktok',headers=headers, cookies=cookies, data=data) 
        
        if 'session_key' not in status.text:
            if 'Too many attempts' in status.text:
                 print(f'[{Fore.RED}!{Fore.RESET}] Try again later.')
                 system("pause")

            elif '"message":"error"' in status.text:
                print(f'[{Fore.RED}!{Fore.RESET}] The Password you set was invalid. Make sure it contains: \n8-20 characters\nMust include letters numbers and a special character.')
                self._password = input(f'[{Fore.RED}>{Fore.RESET}] New Password: ')
            
            return self.new_password_set(ticket=self._ticket, password=self._password)
        
        elif 'session_key' in status.text:
            self._session_id = status.text.split('session_key')[1].split(':')[1].split('"')[1]
            print(f'[{Fore.RED}+{Fore.RESET}] Successfully Grabbed SSID!.')
            print(f'[{Fore.RED}+{Fore.RESET}] Your SSID is > {self._session_id}!')
            print(f'[{Fore.RED}+{Fore.RESET}] Your New Password is {self._password}!.')
      

    def auth_change(self, email, code):
        cookies = {'passport_csrf_token': '7cf44766fba6039fb5d9a11d391ccd0a','passport_csrf_token_default': '7cf44766fba6039fb5d9a11d391ccd0a','store-idc': 'maliva','store-country-code': 'ca','odin_tt': '979436195002bfcc4c6e529c39e1472a449ed8601e3a7d626263375f64a2e23fe0d7c8170101a4bf1b44814c817d49458efe9e2175f17054763a4657ad6672e45311c041bba53b8fef59e60630397612',}
        headers = {'X-SS-STUB': 'C5773D6281A62169718A45F703CF2C60','Accept-Encoding': 'gzip','x-tt-passport-csrf-token': '7cf44766fba6039fb5d9a11d391ccd0a','passport-sdk-version': '19','sdk-version': '2','User-Agent': 'com.zhiliaoapp.musically/2022209010 (Linux; U; Android 7.1.2; en_US; MGHN3VC/A; Build/N2G48H;tt-ok/3.10.0.2)'}
        data = {'fixed_mix_mode': '1','rules_version': 'v2','mix_mode': '1','multi_login': '1','email': email,'account_sdk_source': 'app','type': '31','code': self.encrypt(code)}

        status = self._request_session.post('https://api16-normal-c-useast1a.tiktokv.com/passport/email/check_code/?passport-sdk-version=19&iid=7052926935345284870&device_id=7044441236568081925&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=220901&version_name=22.9.1&device_platform=android&ab_version=22.9.1&ssmix=a&device_type=MGHN3VC%25%2FA&device_brand=iPhone+12&language=en&os_api=25&os_version=7.1.2&openudid=993a612a96d993af&manifest_version_code=2022209010&resolution=720%2A1280&dpi=240&update_version_code=2022209010&_rticket=1642138345234&current_region=HK&app_type=normal&sys_region=US&mcc_mnc=42501&timezone_name=Asia%25%2FShanghai&residence=HK&ts=1642138344&timezone_offset=28800&build_number=22.9.1&region=US&uoo=0&app_language=en&carrier_region=IL&locale=en&op_region=HK&ac2=wifi&host_abi=x86&cdid=82f9ac8f-2b2a-4f08-98da-872978252032&support_webview=1&okhttp_version=4.1.73.9-tiktok', headers=headers,cookies=cookies,data=data)

        if 'ticket' not in status.text:
            
            if 'code error' in status.text:
                print(f'\n[{Fore.RED}!{Fore.RESET}] Invalid Code.')
                self._email_code = input(f'[{Fore.RED}>{Fore.RESET}] Code From inbox: ')
            
            elif 'code expired' in status.text:
                print(f'\n[{Fore.RED}!{Fore.RESET}] Code has Expired.')
                self._email_code = input(f'[{Fore.RED}>{Fore.RESET}] Code From inbox: ')


            elif 'Too many attempts' in status.text:
                print(f'\n[{Fore.RED}!{Fore.RESET}] You are sending too many requests too fast, Please wait up to an hour.')
                system('pause')
            
            else:
                print(f'\n[{Fore.RED}!{Fore.RESET}] Unknown Error.')
                system('pause')


            return self.auth_change(email=self._email, code=self._email_code)
        
        elif 'ticket' in status.text:
            self._ticket = status.text.split('ticket')[1].split(':')[1].split('"')[1]
            self._password = input(f'[{Fore.RED}>{Fore.RESET}] New Password: ')
            self.new_password_set(ticket=self._ticket, password=self._password)



    def send_code(self, email):
        cookies = {'passport_csrf_token': '7cf44766fba6039fb5d9a11d391ccd0a','passport_csrf_token_default': '7cf44766fba6039fb5d9a11d391ccd0a','store-idc': 'maliva',}
        data = {'email': email,'account_sdk_source': 'app','rules_version': 'v2','mix_mode': '1','multi_login': '1','type': '31'}
        status = self._request_session.post('https://api16-normal-c-useast1a.tiktokv.com/passport/email/send_code/?passport-sdk-version=19&iid=7052926935345284870&device_id=7044441236568081925&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=220901&version_name=22.9.1&device_platform=android&ab_version=22.9.1&ssmix=a&device_type=MGHN3VC%25%2FA&device_brand=iPhone+12&language=en&os_api=25&os_version=7.1.2&openudid=993a612a96d993af&manifest_version_code=2022209010&resolution=720%2A1280&dpi=240&update_version_code=2022209010&_rticket=1642138306798&current_region=HK&app_type=normal&sys_region=US&mcc_mnc=42501&timezone_name=Asia%25%2FShanghai&residence=HK&ts=1642138305&timezone_offset=28800&build_number=22.9.1&region=US&uoo=0&app_language=en&carrier_region=IL&locale=en&op_region=HK&ac2=wifi&host_abi=x86&cdid=82f9ac8f-2b2a-4f08-98da-872978252032&support_webview=1&okhttp_version=4.1.73.9-tiktok',cookies=cookies,data=data)
        
        if not 'success' in status.text:
            if 'The account you entered does not exist' in status.text:
                print(f'\n[{Fore.RED}!{Fore.RESET}] Could not find an account associasted with that account.')
                self._email = input(f'[{Fore.RED}>{Fore.RESET}] Email: ')

            elif "You're sending too many" in status.text:
                print(f'\n[{Fore.RED}!{Fore.RESET}] You are sending too many requests too fast, waiting 60 seconds.')
                sleep(60)
                self._email = input(f'[{Fore.RED}>{Fore.RESET}] Email: ')
            
            elif 'Too many attempts.' in status.text:
                print(f'\n[{Fore.RED}!{Fore.RESET}] You are sending too many requests too fast, Please wait up to an hour.')
                system('pause')
                
            else:
                pass

            return self.send_code(email=self._email)

        elif 'success' in status.text:
            self._email_code = input(f'[{Fore.RED}>{Fore.RESET}] Code From inbox: ')
            self.auth_change(email=self._email,code=self._email_code)

email = input(f'[{Fore.RED}>{Fore.RESET}] Email: ')
ssid = grab_ssid(email=email)
