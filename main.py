from telethon import TelegramClient
import yaml
from source.card import getcards

class tg:
    '''
    :D @joavo1337
    '''
    def __init__(self):
        with open("config.yaml", "r") as config_file:
            config = yaml.safe_load(config_file)
        self.apiId = config['apiId']
        self.apiHash = config['apiHash']
        self.channelUsername = str(input("[+] Channel: "))
        self.amount = int(input("[+] Amount: "))
        self.client = TelegramClient('watchdog', self.apiId, self.apiHash)

    async def start(self):
        count = 0
        with open('ccs.txt', 'w', encoding='utf-8') as file:
            async for m in self.client.iter_messages(self.channelUsername):
                if m.text:
                    cardInfo = getcards(m.text)
                    if cardInfo:
                        cc = f"{cardInfo[0]}|{cardInfo[1]}|{cardInfo[2]}|{cardInfo[3]}"
                        print("[+] Card:",cc)
                        file.write(cc + "\n")
                        count += 1
                        if count >= self.amount:
                            return


if __name__ == "__main__":
    print("""
                                    
           .--.              .--.
          : (\ ". _......_ ." /) :
           '.    `        `    .'
            |'   _        _   `|
           |     0}      {0     |
          |       /      \       |
          |     /'        `\     |
           \   | .  .==.  . |   /
            '._ \.' \__/ './ _.'
       cool |  ``'._-''-_.'``  |
                    `--`
     _________________________________________________________________
   
                           Made by @joavo1337
                        https://my.telegram.org/apps
                  ^^ use this link to get ur api_id and hash 
     _________________________________________________________________
""")
    checkout = tg()
    with checkout.client:
        checkout.client.loop.run_until_complete(checkout.start())
    print(f"[+] Scrapped")
