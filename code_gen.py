import requests
import logging
import time
import configparser
from discord_webhook import DiscordWebhook, DiscordEmbed


# Discord Webhook
config = configparser.ConfigParser()
config.read("settings.ini")
mail = config.get("Settings", "mail")
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

        # Generate codes

        mail = str(code_gen.format_mail("bertram.lorenzen93@gmail.com", mail_num))

        headers = {
            "authority": "www.zalando.dk",
            "sec-ch-ua": '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
            "x-xsrf-token": "AAAAAIfBN0PyCF8aQf7Qp8yIzxk4VekCZNVPogl4bRJHi9WEym_SyW6y5D6uz-NyZ--qLquW-3GUrDel7grg8s7tuy98z0zl8UHO6rVMYbWv82_uCvgp7o6nebkoW1tE6jN2cZBZbajOv74sRNB79Xg=",
            "sec-ch-ua-mobile": "?0",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
            "x-zalando-intent-context": "navigationTargetGroup=WOMEN",
            "content-type": "application/json",
            "x-zalando-request-uri": "/nyhedsbrev/",
            "x-page-impression-id": "rendering-engine-d650a4f9-5954-40d0-8ec7-8901d755de28",
            "dpr": "1",
            "viewport-width": "915",
            "sec-ch-ua-platform": '"Windows"',
            "accept": "*/*",
            "origin": "https://www.zalando.dk",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://www.zalando.dk/nyhedsbrev/",
            "accept-language": "da-DK,da;q=0.9,en-DK;q=0.8,en-US;q=0.7,en-GB;q=0.6,en;q=0.5",
            "cookie": "Zalando-Client-Id=f18e0170-bba2-49f1-bfa6-64d6c3d3d0a7; _gcl_au=1.1.605967993.1628344852; _ga=GA1.2.303581862.1628344852; _fbp=fb.1.1628344862063.1119350973; _gac_UA-29919521-1=1.1628381753.CjwKCAjw3riIBhAwEiwAzD3TiYSPPi4NzWklomVuQqEq5wvdmHltnSywHzDtuVBJLcXo74-bxKb9ihoCmMgQAvD_BwE; _gcl_aw=GCL.1628381754.CjwKCAjw3riIBhAwEiwAzD3TiYSPPi4NzWklomVuQqEq5wvdmHltnSywHzDtuVBJLcXo74-bxKb9ihoCmMgQAvD_BwE; catalog.follow_brand_banner_re=%7B%22count%22%3A2%2C%22isClosed%22%3Afalse%7D; zac=AAAAANOWq7g8vNu_Xsje-HVeCVaHBqXRh6xldLdX7zEn9cYm3KH1tuzqz-T4v2uFRWyRYp6VlRHfkr6WMJI1khwXfwB0Twa1pGZOEUBZUDYR1f_r4AI9W8YjbkZEbEo-0bX_eMI2q_MR9MNiQPOvw4gFXzl3qkQlws4y6d8x7pWMcjjQxdteuYWI2TjefiXCNcnvlM0fN6O-5tchikNnsuVybgII_fNSvSCgLhWYpe6_2H4WdxXdIaKwGhKBbwEjt9Hh2s9sYrGEb5g7rvhj3nsGYDQAg8gAliA0s8-3u5PUbcDyTZwAgMuacKRqFLTZF_T0qAnfT209PzWuekHPaJg47H8HA9RZeYtrTN13ivwC-IfBo7KlariBip9YGClbhE7WHaGmRahpJY1UstU_02aGD-gMRDePe6zoNS6rdX5XgBEOuLGncqgeuSErG1SlRKX-dMooZ-LpZIB-2hVygIH2qcUP2sKr5BU7hLIsPgzGwhPKqWCR-msVi4tB5DfGurq9ofW5BOi_Ly55Py79JqkVsTdrC6a9dZ3_mreLlEFXxsEhaMaDGVRJb_nur3E6DGqDynPQRak0Ds2BXLIyZMw0V8bXTy2SrEcEPNZXWYdUyUgwyy_7cLfb-hNSX1afDc5f_Fd92qRnIRnUtHnDxWLOUX9yggJHUxias4NQT-fUFqsQN5T-VE6NwqTcGXu6OZJnXDW_8u8rD7eYLdFy4S3UkCuqYejopXBIFC12jB1Rmge2Tw2ozG2YWfVg9WaZkg2MHdXWgnjY9iCVBmWvQxUtA0QLPGXqXidogaXHI0Nm3mJO7itYOpCYHLhIljTLxGpJYzPqmP8WbFLTtUiGutpzCGa_hKMI00YlDkOIdR8lHsioZFEIAhQDDIi-Bh2avH6V_PoygHCXQbwj-mrI7tzFNiYLJVawvk1vgZBK2w6kBYZZs_a1n7q6Ami5mcBYkwn3sCNLlP58OjT75J3TfhcpoIQfQ1jzsfoXUmG2BYuptim9PoDZ8Q26Av2I9QVh-IVoip03ODiueLUCwR4mcV_vAsgWoZ_aA0iOj3uPI357FuUzPAN6Yh0Av3AeVE5OgqslKAl9W993cRGFPwameh_TvEpv3A4nzxT6lPFQ1e6cIUfka6OyktQqRJjeRFqctjx5per9s0ZX8z-WYHgv5pnPCZ8efVhOr410C4hfFX-HFtctN0uC5__P_0sOCXTGnXUnJCBluVrejqQyDlyfg1zh5C8WT1K64Tqo6h8s1t1-OjQI8QSIeH1f17t2u2kCTldKOOLMJg==; fvgs_ml=mosaic; sqt_cap=1632344167181; _gid=GA1.2.2125672964.1632659719; ncx=f; bm_sz=AF5DC72E6E8CE7D02D21551F76F188E7~YAAQl29faIRj+Cx8AQAAz6ncMQ09osCiVRJukn6aqNXZZ3r6mRMVJU3xxRWyKdaUzr28/J4jW9oF85Ng7zFrW8dx2NYSUoBoOgURqEN2sKT98cs83KHkupHO8jr+NUutx8pSDrtN4VHFU/hNdbZMx0HHR1D1dPK8aef1Gtr2hjFug4UI4tmaswP/MY8+i3Vk0SMIBCSv4Vu+hflNXpOEVUWWR+CuQqdmeQFXfKM8hnFhtlSqsQ8bP5SZgH0gEPwdG0w7aMtef7+j/BrNSVIxZ8nxe3UcOTRLneAWNT2n1Z6vEstD7n6oJEN8aesTSdJNOtQxSwk7T9eF1jZ+RdLOJTbVzAR9/fDoid7YS+GB2LlOPb1zeqVG+JuSggqc3h7d0I46pqbAT9SHilYXnsHNFQ==~3359798~3556163; frsx=AAAAAIfBN0PyCF8aQf7Qp8yIzxk4VekCZNVPogl4bRJHi9WEym_SyW6y5D6uz-NyZ--qLquW-3GUrDel7grg8s7tuy98z0zl8UHO6rVMYbWv82_uCvgp7o6nebkoW1tE6jN2cZBZbajOv74sRNB79Xg=; zsa=eyJraWQiOiJwbGF0Zm9ybS1pYW0tdmNlaHloajYiLCJhbGciOiJFUzI1NiJ9.eyJzdWIiOiIzMTUwMTM3NTA1OCIsImFjciI6Imh0dHBzOlwvXC9jdXN0b21lci1zc28uZG9jcy56YWxhbmRvLm5ldFwvcG9saWNpZXNcL3NpbmdsZS1mYWN0b3IiLCJodHRwczpcL1wvaWRlbnRpdHkuemFsYW5kby5jb21cL3JlYWxtIjoiY3VzdG9tZXJzIiwiaHR0cHM6XC9cL2lkZW50aXR5LnphbGFuZG8uY29tXC90b2tlbiI6IkJlYXJlciIsImF6cCI6ImZhc2hpb24tc3RvcmUtd2ViIiwiYXV0aF90aW1lIjoxNjMyOTI0MTE3LCJpc3MiOiJodHRwczpcL1wvYWNjb3VudHMuemFsYW5kby5jb20iLCJleHAiOjE2MzI5Mjc3MTcsImlhdCI6MTYzMjkyNDExNywic2lkIjoiYmJkMDdmMjUtMjdiZS00NzZkLWFkYWUtYzJlZmViOWRiMmZhIn0.AjulI-sj7YvGh1aXrPD8BAuDnxRaWElGjSdlZ6o_GijQzWU5uujCRnwja-dY99vcj8QO6-eRyDmEVJoCWO3Qww; zsr=eyJlcGsiOnsia3R5IjoiRUMiLCJjcnYiOiJQLTI1NiIsIngiOiJ0MmYtazNQeDRlenhLSXYweUR4S253VHBaTVMtTWgtWE5vWkRRM3B3V2dnIiwieSI6ImduekNWRUliYW9LUUZCUlRBb3JfMXhXemVpTzZIY3ZsaDJ4Y2U2NkhUbDAifSwia2lkIjoicGxhdGZvcm0taWFtLXZjZWh5aGo2IiwiY3R5IjoiSldUIiwiZW5jIjoiQTI1NkNCQy1IUzUxMiIsImFsZyI6IkVDREgtRVMrQTI1NktXIn0.3cvuNmMqqiZgpvLfFvlnzZSjbvkuRxT1R02uuJcB2hxOhNULlmAIHOBtHwW6uNbeGy9unq_iPVe0Nv1_4YrDzxpiMNM-m62B.8wol5YkrlJKP9N2T6oIDVQ.AbNfZY6DoDfnggRf7KNDiK7ggidQCTxC_Y0OD58LpOhIu3dVoQsneip7JQ9AHIuNYtRdUZU_6eG-m2MyutBrfN5rAhUzs45X0KjzQkmF6joKSSlVnK9CLQ7W9qxjO9ICENxcDztSWiyahEGZdIyR1uO_qzip2mIXx6dPbM7nVL7XOIi2R5deHH2ACEfz3t5orbq1tuKOHj5BJC6NFancQ2R4n7k4CqdOjyw4xc7ZzNPVjazofZbiQmbbkSOSAbHwlNNfPBtmVfDatl3H46gd1xBG0bz375ZLIaljWQeIa7V4yk76kKjbq7Da4y8tWiQK7xXEBGOx-lC7Np_j_VGERz9K-Ml5IOR72_A5gCqKNysIvDsDzOniGl9MiY8LbNw-fp1A17ckW4C-JN0qu741g01_289N0riKBHlSgfdMnq65icidFmBKkIWHRpxX2ZFGpXdOfCQ1A2sPa28QrN7_hJtu-ucojKgWpTUWCP3bPUCp6U0fuio_7ham3mWo-OcI.c3PFjF7_BfZYqMKvX06oZYHv273xQ3rfORErNhToAwE; zsi=eyJraWQiOiJwbGF0Zm9ybS1pYW0tdmNlaHloajYiLCJhbGciOiJFUzI1NiJ9.eyJhdF9oYXNoIjoiQ2YtQjRtZjhwUTRHWUVJc2VGYXMxQSIsInN1YiI6IjMxNTAxMzc1MDU4IiwiYXVkIjoiZmFzaGlvbi1zdG9yZS13ZWIiLCJhY3IiOiJodHRwczpcL1wvY3VzdG9tZXItc3NvLmRvY3MuemFsYW5kby5uZXRcL3BvbGljaWVzXC9zaW5nbGUtZmFjdG9yIiwiaXNzIjoiaHR0cHM6XC9cL2FjY291bnRzLnphbGFuZG8uY29tIiwiZXhwIjoxNjMyOTI3NzE3LCJnaXZlbl9uYW1lIjoiTWlra2VsIiwiaWF0IjoxNjMyOTI0MTE3LCJmYW1pbHlfbmFtZSI6Ildpc3NpbmciLCJlbWFpbCI6IjA4bWlra2Vsd2lzc2luZ0BnbWFpbC5jb20iLCJzaWQiOiJiYmQwN2YyNS0yN2JlLTQ3NmQtYWRhZS1jMmVmZWI5ZGIyZmEifQ.HAbzxJpgEQei2R8iLgwirojoqXJKjLezdqXSnAlq48IH4uvIfiMkg7Mj3h9WeT5wSQOcsz9LxADvIxt8UaO2zg; mpulseinject=false; ak_bmsc=2E05102315DCC826ABD52F7E97F59FEA~000000000000000000000000000000~YAAQl29faMJj+Cx8AQAAabHcMQ1Gfmy9IBaV9vpKqUZkTEpJRRZE7jpAfeqS5RvExVJkiBnODJgc1pNpgNp/Geh5nGilZtr/fHEIs1rj4LYH8aEcRhamW+0lKfCVDHAnw8lLNOWPTjp2C1u75sNk8dDR8ca5F0AHhwaC6eVR+mF4vqWVP6mDtwzGoBRg0vwsuaDDD9/cCu1TkVAJGm3IyAz8mcMQN40oquHFFhAvD+XwQoZ72m1VzopBXdyygfZ+8s44aPSwNu3EHAWRk5bPEI1n4ST3McEnra7lL3PhmhuKCjbkloqMZM9h9W58vA9LKGiRpOqhVXw2Rdz2FU6hF251mC/c3ciZshQgFwyE3DDIFfeeQfp/iP87WvmOK0XhXNKQvGh911SiZIYJjYpUlhrbBohB5EeGy/a7akcUN7SR11iNGrqBcm3FrvP6bgB+tD+xYvl3PVtzOMqqa9BVWbM6BCeoBwihm5vbe+bgtFvx13hdAsp1FEMC; _gat_zalga=1; bm_sv=7F854623888FE6C50583E7DD152BF004~47j/BL8n7WRpsC8vmrUl+vtjuU7zF6jnuP/Rqp4/j2eDfciThwx6EYKUbQmNTOKrYdlX1EyHaUy1+UjnHXbgAKXmcl9T+o7g0R5dm+WScWRhu28VHakyWOSOavoB2YQsM7AF/gxAMCkP6+MHcjqrt74YxnNyOGrH26XtozhQCS0=; _abck=7AA13C29B4BDE30BAD2889C2BFEF3876~-1~YAAQn29faFlalDB8AQAANXDfMQb1E9U1l2SJqsg+RorZrblGoTrp/Z6CwlSIsRTzubwjSzWbJvVuaP2KSoROdwDVAQdtG2Xg3DpBWgCRoPF8UpEmm5Cr3VMKxlvw+nc6SbNEde8qK15FOLFhEOtUBbH0BTckAxxwI5QCpvFW4M67cKtTHkOHJBsG9RCS1VoMJFf0k5ny8sy/vZkjx6QFLuVu6cbGeDt8p5bwyGnjKWU7IEk0t2Fd3RrOgQc+3Rc4+tKWCXFbhCd9WYITzOzSywIpDvGXwhT+MEJmE19AyBkFDYUhyOi61jVQJsWOZRQR354oGXpzLXmX4f7POtRGmjPOctoPbOA1Gy8BvgP5WvDelEXXwE/qA222aEDF5d/5pgV7MqNOZtPmeogBMh2ZFbwCQPyAiVkS0GufNNB6TfXgoUeflul0j1jm7uxrRojaIJ3rN5FDdE+6aQ/70Y/Z9Isnec4XVpJRTp3vJWLfH0b/NClNySqkV/dv2nYBLXyl3g==~-1~-1~-1",
        }
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
