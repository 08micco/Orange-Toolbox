import requests
import logging
import time
import configparser
from discord_webhook import DiscordWebhook, DiscordEmbed


# Discord Webhook
config = configparser.ConfigParser()
config.read("settings.ini")
orig_mail = config.get("Settings", "mail")
webhook = config.get("Settings", "discord_webhook")

webhook = DiscordWebhook(
    url=webhook,
    username="Orange Toolbox",
)
embed = DiscordEmbed(
    title="Coupon code generated successfully",
    color="e59400",
)
embed.set_author(name="Orange Toolbox")
embed.set_footer(
    text="Orange Toolbox • 0.0.1",
    icon_url="https://media.istockphoto.com/videos/coral-colored-background-video-id1080215750?s=640x640",
)
embed.set_timestamp()

# Module
module = "Zalando Coupon Gen"

# User Agent
user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}


# Colors
class colors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
}

# Code Gen
class code_gen:
    webhook.add_embed(embed)
    # def gen(mail, amount, delay):
    def gen(x, delay):
        # Logging
        logging.basicConfig(
            format="%(asctime)s %(message)s",
            level=logging.INFO,
            datefmt="[%Y-%d-%m - %H:%M:%S] [" + module + "] Task [" + str(x) + "]-->",
        )
        logging.info(f"{colors.HEADER}Code generation started{colors.ENDC}")

        mail_num = None
        mail = None

        with open("mail_num.txt", "r") as file1:
            mail_num = int(file1.read())

        url = "https://www.zalando.dk/api/graphql/"

        mail = str(code_gen.format_mail((orig_mail), mail_num))
        
        data = (
            '[{"id":"f321f59294a4ffd369951dc5d8f92b801cb7c3c7302de9e5118b3569416c844f","variables":{"input":{"email":"%s","preference":{"category":"MEN","topics":[{"id":"fashion_fix","isEnabled":true},{"id":"follow_brand","isEnabled":true},{"id":"survey","isEnabled":true},{"id":"recommendations","isEnabled":true},{"id":"subscription_confirmations","isEnabled":true},{"id":"offers_sales","isEnabled":true},{"id":"item_alerts","isEnabled":true}]},"referrer":"nl_subscription_page","clientMutationId":"1632924298366"}}}]'
            % (mail)
        )

        time.sleep(delay)
        logging.info(f"{colors.OKCYAN}Generating code number: {x} {colors.ENDC}")
        response = requests.post(url, headers=headers, data=data)

        mail_num += 1

        if response.status_code == 201 or response.status_code == 200:
            logging.info(
                f"{colors.OKGREEN}Successfully generated code number: {x} with email: {mail}.{colors.ENDC}"
            )
            code_gen.send_webhook()
            logging.info(
                f"{colors.OKGREEN}Successfully sent discord webhook{colors.ENDC}"
            )

        with open("mail_num.txt", "w") as file1:
            file1.write(str(mail_num))

    def format_mail(mail, num):
        mails = mail.split("@")
        return "" + mails[0] + "+" + str(num) + "@" + mails[1]

    def send_webhook():
        webhook.execute()


if __name__ == "__main__":
    code_gen()
