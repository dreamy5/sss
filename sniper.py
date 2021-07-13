from discord.ext import commands
import ctypes
from colorama import init, Fore, Style
import json
import requests
init()

with open('config.json') as f:
    config = json.load(f)
token = config.get('token')

ctypes.windll.kernel32.SetConsoleTitleW(f'Da$nip3r | By Dreamy#8888 | Loggin in..')

prefix = "$"
bot = commands.Bot(description='Da$nip3r', command_prefix=prefix, self_bot=True)


@bot.event
async def on_ready():
    ctypes.windll.kernel32.SetConsoleTitleW(f'Da$nip3r | By Dreamy#8888 | Logged in as {bot.user} | {len(bot.guilds)} Guilds')
    print(f'{Fore.GREEN}+ {Fore.RED}{Style.BRIGHT}User connected as' + Fore.GREEN + f' {Fore.RED}[{Fore.GREEN}{bot.user}{Fore.RED}]')
    print(f'{Fore.GREEN}+ {Fore.RED}Guilds: {Fore.RED}[{Fore.GREEN}{len(bot.guilds)}{Fore.RED}]')
    print(f'{Fore.BLUE}+ Coded by Dreamy#8888')
    print()
    print(Fore.RED + """
                ▓█████▄  ▄▄▄           ██████  ███▄    █  ██▓ ██▓███  ▓█████  ██▀███
                ▒██▀ ██▌▒████▄       ▒██    ▒  ██ ▀█   █ ▓██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
                ░██   █▌▒██  ▀█▄     ░ ▓██▄   ▓██  ▀█ ██▒▒██▒▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
                ░▓█▄   ▌░██▄▄▄▄██      ▒   ██▒▓██▒  ▐▌██▒░██░▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄
                ░▒████▓  ▓█   ▓██▒   ▒██████▒▒▒██░   ▓██░░██░▒██▒ ░  ░░▒████▒░██▓ ▒██▒
                 ▒▒▓  ▒  ▒▒   ▓▒█░   ▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒ ░▓  ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
                 ░ ▒  ▒   ▒   ▒▒ ░   ░ ░▒  ░ ░░ ░░   ░ ▒░ ▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░
                 ░ ░  ░   ░   ▒      ░  ░  ░     ░   ░ ░  ▒ ░░░          ░     ░░   ░
                   ░          ░  ░         ░           ░  ░              ░  ░   ░
                 ░                                                                    """)
print()

@bot.event
async def on_message(message):
    if 'https://discord.gift/' in message.content:
        print(f"{Fore.GREEN}+ {Fore.RED}Nitro Code Sniped..{Fore.GREEN} +")
        code = message.content.split('https://discord.gift')[1].split(' ')[0]
        headers = {'Authorization': token, 'Content-Type': 'application/json', 'Accept': 'application/json'}
        json = {
        'channel_id': None,
        'payment_source_id': None
        }
        r = requests.post('https://discordapp.com/api/v6/entitlements/gift-codes'+code+'/redeem',headers=headers, json=json)
        if r.status_code == 200:
            with open("valid_nitro_logs.txt", "a") as f:
                f.write(f'\nhttps://discord.gift{code}')
            print(Fore.GREEN + "Sucesfully claimed the code: https://discord.gift" + code)
            print(f"Channel: {message.channel}")
            print(f"Server: {message.guild}")
            print(f"Author: {message.author}")
            print("")
        else:
            with open("claimed_nitro_logs.txt", "a") as f:
                f.write(f'\nhttps://discord.gift{code}')
            print(f"{Fore.GREEN}+ {Fore.RED}Invalid Code: https://discord.gift{code}{Fore.GREEN} +")
            print(f"[Channel: {message.channel}]")
            print(f"[Server: {message.guild}]")
            print(f"[Author: {message.author}]")
            print("")

@bot.command(pass_context=True)
async def info(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=f"Developer Dreamy#8888", description="Best discord sniper.", color=0xff0000)
    await ctx.send(embed=embed)

bot.run(token, bot=False, reconnect=True)
