import json
import requests
import time
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from sys import stderr

# Colors
Bl = '\033[30m'
Re = '\033[1;31m'
Gr = '\033[1;32m'
Ye = '\033[1;33m'
Blu = '\033[1;34m'
Mage = '\033[1;35m'
Cy = '\033[1;36m'
Wh = '\033[1;37m'


# -------------------------------
# Utility Functions
# -------------------------------

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def run_banner():
    clear()
    time.sleep(0.5)
    stderr.write(f"""{Wh}
         .-.
       .'   `.          --------------------------------
       :g g   :         | {Gr}GHOST - TRACKER - IP ADDRESS{Wh} |
       : o    `.        |       {Gr}@CODE BY HUNXBYTS      {Wh} |
      :         ``.     --------------------------------
     :             `.
    :  :         .   `.
    :   :          ` . `.
     `.. :            `. ``;
        `:;             `:'
           :              `.
            `.              `.     .
              `'`'`'`---..,___`;.-'
    """)


def is_option(func):
    def wrapper(*args, **kwargs):
        run_banner()
        func(*args, **kwargs)
    return wrapper


# -------------------------------
# IP Tracker
# -------------------------------

@is_option
def IP_Track():
    ip = input(f"{Wh}\n Enter IP target : {Gr}")
    print(f"\n {Wh}============= {Gr}SHOW INFORMATION IP ADDRESS {Wh}=============")

    try:
        req_api = requests.get(f"http://ipwho.is/{ip}")
        ip_data = req_api.json()
    except:
        print(f"{Re}Error fetching IP data")
        return

    time.sleep(1)

    # Safe getters
    tz = ip_data.get("timezone", {})
    conn = ip_data.get("connection", {})
    flag = ip_data.get("flag", {})

    lat = ip_data.get("latitude", 0)
    lon = ip_data.get("longitude", 0)

    print(f"{Wh}\n IP target       :{Gr}", ip)
    print(f"{Wh} Type IP         :{Gr}", ip_data.get("type", "N/A"))
    print(f"{Wh} Country         :{Gr}", ip_data.get("country", "N/A"))
    print(f"{Wh} Country Code    :{Gr}", ip_data.get("country_code", "N/A"))
    print(f"{Wh} City            :{Gr}", ip_data.get("city", "N/A"))
    print(f"{Wh} Continent       :{Gr}", ip_data.get("continent", "N/A"))
    print(f"{Wh} Continent Code  :{Gr}", ip_data.get("continent_code", "N/A"))
    print(f"{Wh} Region          :{Gr}", ip_data.get("region", "N/A"))
    print(f"{Wh} Region Code     :{Gr}", ip_data.get("region_code", "N/A"))
    print(f"{Wh} Latitude        :{Gr}", lat)
    print(f"{Wh} Longitude       :{Gr}", lon)
    print(f"{Wh} Maps            :{Gr}", f"https://www.google.com/maps/@{lat},{lon},8z")
    print(f"{Wh} EU              :{Gr}", ip_data.get("is_eu", "N/A"))
    print(f"{Wh} Postal          :{Gr}", ip_data.get("postal", "N/A"))
    print(f"{Wh} Calling Code    :{Gr}", ip_data.get("calling_code", "N/A"))
    print(f"{Wh} Capital         :{Gr}", ip_data.get("capital", "N/A"))
    print(f"{Wh} Borders         :{Gr}", ip_data.get("borders", "N/A"))
    print(f"{Wh} Country Flag    :{Gr}", flag.get("emoji", "N/A"))
    print(f"{Wh} ASN             :{Gr}", conn.get("asn", "N/A"))
    print(f"{Wh} ORG             :{Gr}", conn.get("org", "N/A"))
    print(f"{Wh} ISP             :{Gr}", conn.get("isp", "N/A"))
    print(f"{Wh} Domain          :{Gr}", conn.get("domain", "N/A"))
    print(f"{Wh} ID              :{Gr}", tz.get("id", "N/A"))
    print(f"{Wh} ABBR            :{Gr}", tz.get("abbr", "N/A"))
    print(f"{Wh} DST             :{Gr}", tz.get("is_dst", "N/A"))
    print(f"{Wh} Offset          :{Gr}", tz.get("offset", "N/A"))
    print(f"{Wh} UTC             :{Gr}", tz.get("utc", "N/A"))
    print(f"{Wh} Current Time    :{Gr}", tz.get("current_time", "N/A"))


# -------------------------------
# Phone Number Tracker
# -------------------------------

@is_option
def phoneGW():
    User_phone = input(f"\n {Wh}Enter phone number target {Gr}Ex [+6281xxxxxxxxx] {Wh}: {Gr}")
    default_region = "ID"

    try:
        parsed_number = phonenumbers.parse(User_phone, default_region)
    except:
        print(f"{Re}Invalid phone number format")
        return

    region_code = phonenumbers.region_code_for_number(parsed_number)
    jenis_provider = carrier.name_for_number(parsed_number, "en")
    location = geocoder.description_for_number(parsed_number, "id")
    is_valid_number = phonenumbers.is_valid_number(parsed_number)
    is_possible_number = phonenumbers.is_possible_number(parsed_number)
    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    formatted_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region, True)
    number_type = phonenumbers.number_type(parsed_number)
    timezoneF = ", ".join(timezone.time_zones_for_number(parsed_number))

    print(f"\n {Wh}========== {Gr}SHOW INFORMATION PHONE NUMBERS {Wh}==========")
    print(f"\n {Wh}Location             :{Gr} {location}")
    print(f" {Wh}Region Code          :{Gr} {region_code}")
    print(f" {Wh}Timezone             :{Gr} {timezoneF}")
    print(f" {Wh}Operator             :{Gr} {jenis_provider}")
    print(f" {Wh}Valid number         :{Gr} {is_valid_number}")
    print(f" {Wh}Possible number      :{Gr} {is_possible_number}")
    print(f" {Wh}International format :{Gr} {formatted_number}")
    print(f" {Wh}Mobile format        :{Gr} {formatted_mobile}")
    print(f" {Wh}Original number      :{Gr} {parsed_number.national_number}")
    print(f" {Wh}E.164 format         :{Gr} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
    print(f" {Wh}Country code         :{Gr} {parsed_number.country_code}")
    print(f" {Wh}Local number         :{Gr} {parsed_number.national_number}")

    if number_type == phonenumbers.PhoneNumberType.MOBILE:
        print(f" {Wh}Type                 :{Gr} Mobile number")
    elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
        print(f" {Wh}Type                 :{Gr} Fixed-line number")
    else:
        print(f" {Wh}Type                 :{Gr} Other")


# -------------------------------
# Username Tracker
# -------------------------------

@is_option
def TrackLu():
    username = input(f"\n {Wh}Enter Username : {Gr}")
    results = {}

    social_media = [
        ("Facebook", "https://www.facebook.com/{}"),
        ("Twitter", "https://www.twitter.com/{}"),
        ("Instagram", "https://www.instagram.com/{}"),
        ("LinkedIn", "https://www.linkedin.com/in/{}"),
        ("GitHub", "https://www.github.com/{}"),
        ("Pinterest", "https://www.pinterest.com/{}"),
        ("Tumblr", "https://www.tumblr.com/{}"),
        ("YouTube", "https://www.youtube.com/{}"),
        ("SoundCloud", "https://soundcloud.com/{}"),
        ("Snapchat", "https://www.snapchat.com/add/{}"),
        ("TikTok", "https://www.tiktok.com/@{}"),
        ("Behance", "https://www.behance.net/{}"),
        ("Medium", "https://www.medium.com/@{}"),
        ("Quora", "https://www.quora.com/profile/{}"),
        ("Flickr", "https://www.flickr.com/people/{}"),
        ("Twitch", "https://www.twitch.tv/{}"),
    ]

    for name, url in social_media:
        full_url = url.format(username)
        try:
            r = requests.get(full_url)
            results[name] = full_url if r.status_code == 200 else f"{Ye}Not Found"
        except:
            results[name] = f"{Re}Error"

    print(f"\n {Wh}========== {Gr}SHOW INFORMATION USERNAME {Wh}==========\n")
    for site, result in results.items():
        print(f" {Wh}[ {Gr}+ {Wh}] {site} : {Gr}{result}")


# -------------------------------
# Show Your IP
# -------------------------------

@is_option
def showIP():
    try:
        Show_IP = requests.get("https://api.ipify.org/").text
    except:
        Show_IP = "Error"

    print(f"\n {Wh}========== {Gr}SHOW INFORMATION YOUR IP {Wh}==========")
    print(f"\n {Wh}[ {Gr}+ {Wh}] Your IP Address : {Gr}{Show_IP}")
    print(f"\n {Wh}==============================================")


# -------------------------------
# Menu System
# -------------------------------

options = [
    (1, "IP Tracker", IP_Track),
    (2, "Show Your IP", showIP),
    (3, "Phone Number Tracker", phoneGW),
    (4, "Username Tracker", TrackLu),
    (0, "Exit", exit)
]


def option_menu():
    clear()
    stderr.write(f"""
       ________               __      ______                __  
      / ____/ /_  ____  _____/ /_    /_  __/________ ______/ /__
     / / __/ __ \/ __ \/ ___/ __/_____/ / / ___/ __ `/ ___/ //_/
    / /_/ / / / / /_/ (__  ) /_/_____/ / / /  / /_/ / /__/ ,<   
    \____/_/ /_/\____/____/\__/     /_/ /_/   \__,_/\___/_/|_| 

              {Wh}[ + ]  C O D E   B Y  H U N X  [ + ]
    """)

    print()
    for num, text, _ in options:
        print(f"{Wh}[ {num} ] {Gr}{text}")


def main():
    while True:
        option_menu()
        try:
            opt = int(input(f"{Wh}\n [ + ] {Gr}Select Option : {Wh}"))
        except:
            print(f"{Re}Invalid input")
            time.sleep(1)
            continue

        for num, _, func in options:
            if opt == num:
                func()
                input(f"\n{Wh}[ {Gr}+ {Wh}] Press Enter to continue...")
                break
        else:
            print(f"{Re}Option not found")
            time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Re}Exit")
        time.sleep(1)
