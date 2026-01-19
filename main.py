import aiohttp
import asyncio
import os
import ctypes
from datetime import datetime, timezone
from colorama import Fore, init

init(autoreset=True)

class Stats:
    def __init__(self):
        self.checked = 0
        self.valid = 0
        self.bad = 0
        self.nitro = 0
        self.total = 0

stats = Stats()

def update_title():
    ctypes.windll.kernel32.SetConsoleTitleW(f"Total Checked: {stats.checked}/{stats.total} | Hits: {stats.valid} | Bads: {stats.bad} | Nitro: {stats.nitro}")

if not os.path.exists('Result'):
    os.makedirs('Result')

for file in ['Valid_Token.txt', 'Bad_Tokens.txt', 'Nitro_Tokens.txt', 'Capture.txt']:
    if not os.path.exists(f'Result/{file}'):
        open(f'Result/{file}', 'w').close()

def get_age(user_id):
    try:
        timestamp = ((int(user_id) >> 22) + 1420070400000) / 1000
        return datetime.fromtimestamp(timestamp).strftime('%b %d, %Y')
    except:
        return "Unknown"

async def check(session, token, sem):
    async with sem:
        headers = {
            'Authorization': token,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
        }
        try:
            async with session.get('https://discord.com/api/v9/users/@me', headers=headers) as r:
                if r.status in [401, 403]:
                    print(f"{Fore.RED}[-] Invalid: {token[:25]}...")
                    stats.bad += 1
                    stats.checked += 1
                    update_title()
                    with open('Result/Bad_Tokens.txt', 'a', encoding='utf-8') as f:
                        f.write(token + '\n')
                    return
                elif r.status != 200:
                    stats.checked += 1
                    update_title()
                    return
                
                user = await r.json()

            username = f"{user['username']}#{user['discriminator']}" if user.get('discriminator') != '0' else user['username']
            age = get_age(user['id'])
            
            nitro = "False"
            has_nitro = False
            async with session.get('https://discord.com/api/v9/users/@me/billing/subscriptions', headers=headers) as r:
                if r.status == 200:
                    subs = await r.json()
                    if any(s.get('status') == 1 for s in subs):
                        nitro = "True"
                        has_nitro = True

            boosts = "False"
            async with session.get('https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots', headers=headers) as r:
                if r.status == 200:
                    slots = await r.json()
                    if slots:
                        boosts = "True"

            print(f"{Fore.GREEN}[+] Valid: {token[:25]}... | Nitro: {nitro} | Boosts: {boosts} | Age: {age}")
            stats.valid += 1
            if has_nitro:
                stats.nitro += 1
            
            stats.checked += 1
            update_title()
            
            with open('Result/Valid_Token.txt', 'a', encoding='utf-8') as f:
                f.write(token + '\n')
            
            with open('Result/Capture.txt', 'a', encoding='utf-8') as f:
                f.write(f'username - "{username}" | Nitro - {nitro} | Available boost - {boosts} | Account Age - "{age}" | Token - "{token}"\n')
            
            if has_nitro:
                print(f"{Fore.MAGENTA}[*] Nitro Found: {username}")
                with open('Result/Nitro_Tokens.txt', 'a', encoding='utf-8') as f:
                    f.write(token + '\n')

        except Exception:
            stats.checked += 1
            update_title()

async def main():
    if not os.path.exists('tokens.txt'):
        print(f"{Fore.RED}tokens.txt not found!")
        return

    with open('tokens.txt', 'r', encoding='utf-8') as f:
        tokens = [x.strip().strip('"').strip("'") for x in f if x.strip()]

    if not tokens:
        print(f"{Fore.YELLOW}No tokens in tokens.txt")
        return

    stats.total = len(tokens)
    update_title()
    print(f"{Fore.CYAN}Loaded {len(tokens)} tokens...")
    
    sem = asyncio.Semaphore(100)
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[check(session, token, sem) for token in tokens])

    print(f"{Fore.CYAN}Done.")
    input("\nChecking Completed Press enter to Close")

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
