#!/usr/bin/env python
import itertools
import os
import sys

# Color Setup
RED = '\033[91m'
GREEN = '\033[1;32m'
YELLOW = '\033[93m'
END = '\033[0m'

def message():
    os.system('clear')
    # ব্যানারটি ভেরিয়েবলে আলাদাভাবে রাখা হয়েছে যাতে এরর না হয়
    print(RED + "######################################")
    print("##            EVIL URL v3.0         ##")
    print("##      [ Modified for Termux ]      ##")
    print("######################################" + END)

def check_EVIL(url):
    bad_chars = ['\u0430', '\u03F2', '\u0435', '\u043E', '\u0440', '\u0455', '\u0501', '\u051B', '\u051D']
    result = [char for char in bad_chars if char in url]
    if result:
        return f"\n{GREEN}[*]{END} Evil URL detected: {RED}{url}{END}\n{GREEN}[*]{END} Unicode characters used: {result}"
    return f"\n{YELLOW}[!]{END} No Evil characters detected in: {url}"

def gen(url, tld):
    evils = [{'a':'\u0430'},{'c': '\u03F2'}, {'e': '\u0435'}, {'o': '\u043E'}, {'p': '\u0440'}, {'s': '\u0455'}, {'d': '\u0501'}, {'q': '\u051B'}, {'w': '\u051D'}]
    e_matchs = [list(em)[0] for em in evils if list(em)[0] in url.lower()]
    
    if not e_matchs:
        print(f"{RED}দুঃখিত! এই ডোমেইনে কোনো পরিবর্তনযোগ্য ক্যারেক্টার পাওয়া যায়নি।{END}")
        return

    words = []
    for i in range(1, len(e_matchs) + 1):
        for j in itertools.combinations(e_matchs, i):
            words.append(''.join(j))

    print(f"\n{GREEN}[+]{END} Generating Evil URLs for: {YELLOW}{url}{tld}{END}")
    print("-" * 40)
    for word in words:
        newurl = url.lower()
        for w in word:
            for em in evils:
                if list(em)[0] == w:
                    newurl = newurl.replace(w, em[w])
        print(f"{RED}-> {newurl}{tld}{END}")
    print("-" * 40)

def main_menu():
    while True:
        message()
        print(f"\n{GREEN}১.{END} নতুন Evil URL তৈরি করুন (Generate)")
        print(f"{GREEN}২.{END} একটি URL চেক করুন (Check Single)")
        print(f"{GREEN}৩.{END} ফাইল থেকে লিস্ট চেক করুন (Check File)")
        print(f"{RED}৪. এক্সিট (Exit){END}")
        
        choice = input(f"\n{YELLOW}অপশন সিলেক্ট করুন (১-৪): {END}")

        if choice == '1' or choice == '১':
            target = input("\nডোমেইন নাম দিন (যেমন- google.com): ")
            if '.' in target:
                name = target.split('.')[0]
                tld = '.' + '.'.join(target.split('.')[1:])
                gen(name, tld)
            else:
                print(f"{RED}ভুল ফরম্যাট! (example.com) এভাবে লিখুন।{END}")
            input("\nএন্টার চাপুন ফিরে যেতে...")

        elif choice == '2' or choice == '২':
            target = input("\nচেক করার জন্য URL দিন: ")
            print(check_EVIL(target))
            input("\nএন্টার চাপুন ফিরে যেতে...")

        elif choice == '3' or choice == '৩':
            path = input("\nফাইলের নাম/পাথ দিন: ")
            try:
                with open(path, 'r') as f:
                    for line in f:
                        if line.strip():
                            print(check_EVIL(line.strip()))
            except FileNotFoundError:
                print(f"{RED}ফাইল পাওয়া যায়নি!{END}")
            input("\nএন্টার চাপুন ফিরে যেতে...")

        elif choice == '4' or choice == '৪':
            print(f"{YELLOW}বিদায়!{END}")
            break
        else:
            print(f"{RED}ভুল অপশন!{END}")
            os.system('sleep 1')

if __name__ == '__main__':
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nবন্ধ করা হচ্ছে...")
        sys.exit()
