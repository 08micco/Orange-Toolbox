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
module = "Zalando Checkout"

# User Agent
user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}

# Logging
logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.INFO,
    datefmt="[%Y-%d-%m - %H:%M:%S] [" + module + "] Task -->",
)

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


Zalando_Client_Id = "45c395db-7521-45ba-871d-5553f7fa8d0d"


def login():
    logging.info(f"{colors.HEADER}Logging in{colors.ENDC}")


def get_cookie():
    response = requests.get("https://www.zalando.dk/myaccount/")
    return response.cookies


class zalando_preload:
    def preload(pid):
        login()
        logging.info(f"{colors.HEADER}Preloading item{colors.ENDC}")


class zalando_checkout:
    def atc(pid):
        login()
        logging.info(f"{colors.HEADER}Carting item{colors.ENDC}")

        headers = {
            "authority": "www.zalando.dk",
            "sec-ch-ua": '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
            "x-xsrf-token": "AAAAACfuu9VMr3anPtc2ocRhfGHovC69NGyrz1PFJrUTmoANFrrhBFkf5unxKq5ApXgik8w20IcXCoom5K6VI_brX9flV5B2s5rjd8tnNSDrEpVdpUEk4Ugq4I7OGvFCS8zQkzcX4r8nuNkvy06K5BU=",
            "x-zalando-feature": "pdp",
            "sec-ch-ua-mobile": "?0",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
            "x-zalando-intent-context": "navigationTargetGroup=MEN",
            "content-type": "application/json",
            "x-zalando-request-uri": "/loungeable-mens-chicken-hjemmesko-blackwhite-low12i00w-q11.html",
            "x-page-impression-id": "rendering-engine-62a9eb41-3827-4839-9d19-c32ba4e09809",
            "dpr": "1",
            "viewport-width": "1527",
            "sec-ch-ua-platform": '"Windows"',
            "accept": "*/*",
            "origin": "https://www.zalando.dk",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://www.zalando.dk/loungeable-mens-chicken-hjemmesko-blackwhite-low12i00w-q11.html",
            "accept-language": "da-DK,da;q=0.9,en-DK;q=0.8,en-US;q=0.7,en-GB;q=0.6,en;q=0.5",
            "cookie": "Zalando-Client-Id=f18e0170-bba2-49f1-bfa6-64d6c3d3d0a7; _ga=GA1.2.303581862.1628344852; _fbp=fb.1.1628344862063.1119350973; catalog.follow_brand_banner_re=%7B%22count%22%3A3%2C%22isClosed%22%3Atrue%7D; _gcl_au=1.1.1166779595.1636363803; sqt_cap=1636363817743; _gid=GA1.2.1073183315.1636626977; fvgs_ml=mosaic; bm_sz=EF9BA32F2262A0FCD4E490845C7996AC~YAAQj3ymX3rC/tl8AQAAGa+JFg1Jc+IZZJsdZU4v+YAq//ubbkOee0r6Iaf02YDF/QGxDb8UAuml/MtanGtibnfBAdSyC5zO/bj3KK7vWAXqzZaPHOE2IooCH+dcyuatI8uDuzXzZB3hmdXxg/yBwrynDU2ZG0T0n6bvJ6le6PhhUpeTJ2ZaROUo/+oRyx9xB5JXA7+fOqgJu2CCExxhPF0Vk1dUdSTg944MlX1MKjpoXrjx1C622C1G/AioAL215xg+vv9RQROw9Pt48dORvZmlG7mlR4IbsMAjMKfuc1krRN0EtI4KY3gy9+1H2xSdfb1jnHMD9GvrGGUqj4wCdgeIOwSAUvXMAtb6hYMX6pPlmgRXmKEaIdBMG+aF8vXZ1bkUCxmzSUy29iyYpn7gWVfaDFGYgp+mwgTkd4zG+Q4Ktij80IMJWw==~3752774~3687235; zsa=eyJraWQiOiJwbGF0Zm9ybS1pYW0tdmNlaHloajYiLCJhbGciOiJFUzI1NiJ9.eyJzdWIiOiIzMTUwMTM3NTA1OCIsImFjciI6Imh0dHBzOlwvXC9jdXN0b21lci1zc28uZG9jcy56YWxhbmRvLm5ldFwvcG9saWNpZXNcL3NpbmdsZS1mYWN0b3IiLCJodHRwczpcL1wvaWRlbnRpdHkuemFsYW5kby5jb21cL3JlYWxtIjoiY3VzdG9tZXJzIiwiaHR0cHM6XC9cL2lkZW50aXR5LnphbGFuZG8uY29tXC90b2tlbiI6IkJlYXJlciIsImF6cCI6ImZhc2hpb24tc3RvcmUtd2ViIiwiYXV0aF90aW1lIjoxNjM2NzYwNjYxLCJpc3MiOiJodHRwczpcL1wvYWNjb3VudHMuemFsYW5kby5jb20iLCJleHAiOjE2MzY3NjQyNjEsImlhdCI6MTYzNjc2MDY2MSwic2lkIjoiYmJkMDdmMjUtMjdiZS00NzZkLWFkYWUtYzJlZmViOWRiMmZhIn0.SyhOWBGQBrW9C0fbmfyCuFaKD9umN3vk7AQnG81tsWk2zAHeFPgG0O0C0zKbKlknHTTGhKYZIcDPRs6I0RsD0A; zsr=eyJlcGsiOnsia3R5IjoiRUMiLCJjcnYiOiJQLTI1NiIsIngiOiIzRGxFbnZYT2U3di0xcUxSdzBQU2FfWldfdHRRZkNuclNydjdwd196UDNRIiwieSI6Ikx3cVBCSUswa3hBeE0xM0gwYkVKRzJIb2pnVE9pbXpuNnh1N2VuVlRRbFkifSwia2lkIjoicGxhdGZvcm0taWFtLXZjZWh5aGo2IiwiY3R5IjoiSldUIiwiZW5jIjoiQTI1NkNCQy1IUzUxMiIsImFsZyI6IkVDREgtRVMrQTI1NktXIn0.2RE_zAmTtj3zeOHjvo_G5Eu-nqghIxJHdiefVi5-7CnV5EwZPIR5ZK_enSxE1VrChOsbtrKSt4-iEdQhenbpR84etw1rVjV0.JQh3eQ0qu-nmF2vLBLkqeQ.pXmmjB0w9IuW8dul_zzpSzPSNnR8wgs_FXy5WgpjPV8C16lAQeF0O-kcOZUBStr4ZD7_KOM0gs3hA0Id6sYMF4xUSMZtEUaT2TnVFdiNPjg79oaJAjq7954qPpj72peh-rISjLV1n7U6eP0rXyPFi48fQ85fN9nCozQqJs0PSiDpXDJPqhwfQH0h1luhREJal4jbLIliOcjL5il-hLJjgGJQ9f4M6faWxvl9CO6pYCj_QUWFbrWguOJtee6vUXwyvecAL6UeUSBkK0m69bpGUlWH-c3WaYbqV4Y7hNbqcLr-K2pdA8572iB_Qw_AzZmVmZkKqJG7wufeYmBamf-7oOmSwDy5XgAJKFb4ZSwoMiSXAZdBPsZZarGuNZVzZmm0KT_dlwielC3xyQ0B3D3PJn8PT9AhEXY28Wzc4FiXF1BFEA9z6Tg8p604Hblhv5hF6CuNXBtggV7jRXOZLfScmtEaAaY-F-oy67Pd8BMfht-u3Exksiv3Ok42TdaBnkQ4.yTnQ6uGk0LX3R_inf-pEYVL0M8yiRqspoT5Q2FEN07w; zsi=eyJraWQiOiJwbGF0Zm9ybS1pYW0tdmNlaHloajYiLCJhbGciOiJFUzI1NiJ9.eyJhdF9oYXNoIjoiRW1YS05TM1pIMVBLQ0dXQnlGLVgyZyIsInN1YiI6IjMxNTAxMzc1MDU4IiwiYXVkIjoiZmFzaGlvbi1zdG9yZS13ZWIiLCJhY3IiOiJodHRwczpcL1wvY3VzdG9tZXItc3NvLmRvY3MuemFsYW5kby5uZXRcL3BvbGljaWVzXC9zaW5nbGUtZmFjdG9yIiwiaXNzIjoiaHR0cHM6XC9cL2FjY291bnRzLnphbGFuZG8uY29tIiwiZXhwIjoxNjM2NzY0MjYxLCJnaXZlbl9uYW1lIjoiTWlra2VsIiwiaWF0IjoxNjM2NzYwNjYxLCJmYW1pbHlfbmFtZSI6Ildpc3NpbmciLCJlbWFpbCI6IjA4bWlra2Vsd2lzc2luZ0BnbWFpbC5jb20iLCJzaWQiOiJiYmQwN2YyNS0yN2JlLTQ3NmQtYWRhZS1jMmVmZWI5ZGIyZmEifQ.BqMJ_9vsnL8kegj-Xx0fAZ_TA2b0lZt1bzMnLT9kUEFvTkrEupbGhsKTBjVRp8OZUQXdrKDfVxOIe1uOwIaXjA; mpulseinject=false; ak_bmsc=4821A2DEA37E9C336037E2297D545A00~000000000000000000000000000000~YAAQj3ymX3/C/tl8AQAAdbSJFg22p+29UFy1wOJu0EcQ6OOc6JYeYwR1b7o2n9U9qRBcw3ZC2gUkraEoqV0KUmCmyzYtQnsb9SupvCm60i9zKapPjEb3wnPOAyZffaQkX5+fZoYzmvQp1mecQbvDHTpoovA275ZkFF0lnmcK7MJFXhFYnFclCgDVKU7oy15zV94urZliRAT4HXIqtoc52t037IUEtkjj4co2MquHXNUCKKFRYkEw/yigt2tGlwHncIZ3zd2pobInaWrMik8OaLYhqcesoUBBdRo9HwqEZR0Wdql3dW32F9wYZPdu5O/CVOEGtGehYR+StLxWr551SyjLOqqRlsFs7wIkPQ7QNT9ytkugnStpVkOBhQD8PUl+9ZZgj/euSYTNt8PJGKnPwJIhIu0c4nb34mFsQk1Dyq/ksViqMVc8iA3djZVsedkiriLNNLelZkSQdIGYkin32Rn/gqhd7XVchR2RytWs32RZqz/6sbzytpJv; catalog.size_onboarding__size_filter_applied_tooltip=true; ncx=m; frsx=AAAAACfuu9VMr3anPtc2ocRhfGHovC69NGyrz1PFJrUTmoANFrrhBFkf5unxKq5ApXgik8w20IcXCoom5K6VI_brX9flV5B2s5rjd8tnNSDrEpVdpUEk4Ugq4I7OGvFCS8zQkzcX4r8nuNkvy06K5BU=; _gat_zalga=1; bm_sv=D9CFC14EBF99540A3833D9FC836453C6~PKQjyb/xapD7ENCqxL0wsqhfHhns23dhpL6JcW8AxLi3xxBkXvubz/lZj+HjpPby/LzcIgEDKrTrS/BAJVnCdECvE3C23lrWQJbvbVnm8Xk8v1ASWEmDJKy7khAlZqYfGBEiDv358wc+go3zajrAdW8i6vpghbIK2JhaG9mHwBA=; _abck=7AA13C29B4BDE30BAD2889C2BFEF3876~-1~YAAQnXymX/2sreh8AQAAd/uTFgZebqb9okJLQECoq+rK2N1z7rOD/dbvRblNDnBDaU05JYqMX/nLykPIcQtrqWKkY597juk+Q3qGt3L0J0vMIMtPtpsw3kXu5RDAuvRUIdxR/g+xl5/Nnsq7E031lPFtztPujaalO/pSqUiNCZE5b8tNilFCfYeJmVG5RVyz1UTJhzNg+ZzuaiARZbhxrbqam+RuaGSc6pBGt8/C1qr+uV4w7b/yGtnl24x46UnLbEz7DPuojqNZZSN8/eyclmAphD8JMOtk5YMrzzs/RkwbhfS3JPrZPKEbWedmpCAvn4k+esjNPabjED+lzff2A/gq3L3rFQLsX4Y1icEheEo1jMuFtUxVHGZtfPvzA7qNOo04tAJ+cwgC37pUnPgox4n8AqdH1D3Izgg7vITvJnGPZLe96SCbMcNusof69XSHsI87qyBRK7C8Vi+CLh1f6zRmPA1lHnu/ai44oFQKDbLkmLw=~-1~-1~-1",
        }

        data = (
            '[{"id":"e7f9dfd05f6b992d05ec8d79803ce6a6bcfb0a10972d4d9731c6b94f6ec75033","variables":{"addToCartInput":{"productId":"%s","clientMutationId":"addToCartMutation"}}}]'
            % (pid)
        )

        response = requests.post(
            "https://www.zalando.dk/api/graphql/add-to-cart/",
            headers=headers,
            data=data,
        )

        print(response.status_code)

        if response.status_code == 200:
            logging.info(f"{colors.OKGREEN}Item Carted{colors.ENDC}")
            zalando_checkout.checkout()
        else:
            logging.info(
                f"{colors.OKGREEN}Item Carted Unsuccesfully. Status code: {response.status_code}{colors.ENDC}"
            )

    def checkout():
        logging.info(f"{colors.HEADER}Checking Out{colors.ENDC}")

        headers = {
            "authority": "www.zalando.dk",
            "sec-ch-ua": '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
            "x-xsrf-token": "AAAAADmsUqmcrPyEPutnIh99tAwgRHPcsx1KWopXSd7hSs85-oDjAhlH38sJ70MOXIwloFwsUypmhrmJCK4ywmOp6EJgfaFWVVHliEz5AGxi-f6NBFIbJkWP1R2EkzNNr6y5EjLsWZyy35HspYhgiJw=",
            "sec-ch-ua-mobile": "?0",
            "x-zalando-header-mode": "desktop",
            "x-zalando-checkout-app": "web",
            "content-type": "application/json",
            "x-zalando-footer-mode": "desktop",
            "accept": "application/json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
            "sec-ch-ua-platform": '"Windows"',
            "origin": "https://www.zalando.dk",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://www.zalando.dk/checkout/confirm",
            "accept-language": "en-US,en;q=0.9",
            "cookie": "Zalando-Client-Id=45c395db-7521-45ba-871d-5553f7fa8d0d; _ga=GA1.2.902405791.1629743603; _gcl_au=1.1.1153984449.1629743627; _fbp=fb.1.1629743627128.298103729; sqt_cap=1632944861747; mpulseinject=false; bm_sz=36D02C9BEC59C9099164497B0818F626~YAAQz29faBIi4Fd8AQAAd6+ZYQ08KHoCFio9vmulMlWiPQodqTCuCIRmEDYgEub7L8P7Jah72xjxrQf45TseIMaLq8ZWkCwhJayCONTdAfZvvWL2uJ8H44XJViNU10vHxUf9A32Q0rw4HYi1xdqvfCJOn5SPRSItpRSWv+kzsUd9iRF6mQLSdN6dbsWuaIwlvkicC+0Wl9P3kHBPcXw9fScklfmxE18Te9dxZWPKZQLQ5b3tgICszokDDXddwjOPVVXK6qU9/myJy5dNomGheDWwy1gbYAcyb5UM0GG6+eJgJXN6jukFojxEAdjPH4J19DqkLd02VpAzWc8EtJeUk37BWDhLNRfMs3TRTBrJTHJ5YxdxdpxYQKsozSxiIkod13/i9J9RiHD78ysD6dQJAQ==~4534833~3491384; ncx=m; bm_mi=60090E73C5EC2F2D964B05DD9F236EF8~pvgpRN5VmcXe/lpBV8olf50GKVIFPKJtMl8wPHIl2+xt8H5lZPXrqbehjaxlz5//Pndu0qvobzUtiIJzfGOWJOHylE3sXAHsuMSNyNxUvImngzC5mMHtgGslRvLW6JWUVrfk73CCK0teTEYhx+lplzy1GHPeEhviAeEZOz/tVHMIICEyvNJ4i66ikNQ98oErrD90MQQLRLKayvHxx2twXkr4faaIMwsbyrCv9b/ltjqSWLWPcajd4sFNzN4kAN4N81NZU3HR0FN7D+kEV6gR8Qn0NdCBrNT6sOhTNceVN4M=; _gid=GA1.2.1905854292.1633725036; ak_bmsc=805746800B7CFC1D8B57233456F428CD~000000000000000000000000000000~YAAQz29faD8i4Fd8AQAAbreZYQ30N5QYRbV7Drxhg3ReX6uTri216XGnIAVMXgKWkMgnlDXoKKk+N1hzwh7RLZZzeFHZbMTcFhdVDefe5ODS4viQq/lMM52wvfTi0JtAvqnVmt2l23u89WRJOi0Xb5r4g+vOBIGsh0kms1m0as29b0np7zsn3/5wdI+P0XNHder7HodOugEdtPho2EEJasJ2iOmxWSXeB6G4zyZlFpGWmah6jK/hcR+qRabDv3GmAEXsH1NaU9sba3ZOEGBmJUb4+OxscYtHEg07RLqGOal2ho7tpeQCGLClCW8HdwBdwznhQdnuzE/+TXqIksyR49FAbJq4+hxdAFIQkIWG37Re23hW7xBDPpn26iCy+9V6DQAPlilJACAYFwNmwu2CcVgoDkPj02VaqIM9Jw8oZCGJXpxzekgkIjLx2pdeLolIIs9b7cmGOsu3oMN/DSYUEXNVXIywxhz4OJbveiaWa0Xeas5faX6h4IyNHgADJ7O1TMTGqLm0EDyQHg==; frsx=AAAAADmsUqmcrPyEPutnIh99tAwgRHPcsx1KWopXSd7hSs85-oDjAhlH38sJ70MOXIwloFwsUypmhrmJCK4ywmOp6EJgfaFWVVHliEz5AGxi-f6NBFIbJkWP1R2EkzNNr6y5EjLsWZyy35HspYhgiJw=; zsa=eyJraWQiOiJwbGF0Zm9ybS1pYW0tdmNlaHloajYiLCJhbGciOiJFUzI1NiJ9.eyJzdWIiOiI0NDI4NjUxMzY2MzcxNyIsImFjciI6Imh0dHBzOlwvXC9jdXN0b21lci1zc28uZG9jcy56YWxhbmRvLm5ldFwvcG9saWNpZXNcL3NpbmdsZS1mYWN0b3IiLCJodHRwczpcL1wvaWRlbnRpdHkuemFsYW5kby5jb21cL3JlYWxtIjoiY3VzdG9tZXJzIiwiaHR0cHM6XC9cL2lkZW50aXR5LnphbGFuZG8uY29tXC90b2tlbiI6IkJlYXJlciIsImF6cCI6ImZhc2hpb24tc3RvcmUtd2ViIiwiYXV0aF90aW1lIjoxNjMzNzI2OTc5LCJpc3MiOiJodHRwczpcL1wvYWNjb3VudHMuemFsYW5kby5jb20iLCJleHAiOjE2MzM3MzA1NzksImlhdCI6MTYzMzcyNjk3OSwic2lkIjoiZWJiZTFhOGItZTNmZC00OTA4LTllZWYtNzk2ODc0Mzc0OWE5In0.neEBLrtSeHa3KrjbqX0p_nt2PvLki7Ab6q-mSAuORsRzh1-zZebdAsd1mUE7DFuMwBqYoAms0mXbbuGsaWIVxQ; zsr=eyJlcGsiOnsia3R5IjoiRUMiLCJjcnYiOiJQLTI1NiIsIngiOiJXQThiay04ZkhuLVhvNmpVS2VfT0pYX003QUJzR3J1U09ORk8yY21CMmNZIiwieSI6ImItc05SMnBoSzAxV1hoRTlTNk5Xdjd2cmZSbEVhang2aGxSaExndVR2R1EifSwia2lkIjoicGxhdGZvcm0taWFtLXZjZWh5aGo2IiwiY3R5IjoiSldUIiwiZW5jIjoiQTI1NkNCQy1IUzUxMiIsImFsZyI6IkVDREgtRVMrQTI1NktXIn0.5zOHfqqkRE0NDuX1Oii8r0YP8heHlirOHeWSXBfTiTcpQq37zCLyarkUeGflEfXWSf3pmkKzDHdwJgssA4f_Us5qujMXnVWD.UVkfgVpzXs1iNpIww7BcVQ.LFGpe2YlTWEdAW15vVGYiJb6hS4bXeynV91oI3bYn0DbW2lQpT7xl834eZ25XH1kZganRq6znH0RkFfOz6NzwsDFmK9K-Mv0wCZRaGjzDd3qiculv_mMU4q6o-P-jtsTKTbnSlniFtW28nBJ7jUpFSyywQDq4_UPTyWkNmBg2qp5ryamtJn2MEkoLeHIyCH0tR_cHCRtZ9LYk--SlsCAGbpoPuVMOvZ4YOs7TEn6FelAdfkWjKojWrPBJ94YrtCT2962v1xnQxsCSg2VDJk8WQ5xq9y05gWjYnaL1i3L7hL6xV_7R3qXg5Q5ZuWfu1UKTogJAmTfPdwenpuUP0UCxGABp5P2qIWQwpkgrtnxOmHC5lhjFHhTxP7lX9v7O8-x8s7OtrwaaL4lWrSiO3aPEWhcuEGR3IGQpXIPPT4rP1Jw1ogPafe8sghth-3NTMfQEAocjDoUVpb4rutcdD7CwrjnyGRVsNwGTdWk8fqaO8du_EIQU4MknlU8TgIjJXWv._m75641B1MiY1pAFwaXXQiBCV_rwQVqo50cyrFqbkx8; zsi=eyJraWQiOiJwbGF0Zm9ybS1pYW0tdmNlaHloajYiLCJhbGciOiJFUzI1NiJ9.eyJhdF9oYXNoIjoid0U2WW90enhPN1FzR0piQmh0enBWUSIsInN1YiI6IjQ0Mjg2NTEzNjYzNzE3IiwiaXNzIjoiaHR0cHM6XC9cL2FjY291bnRzLnphbGFuZG8uY29tIiwiZ2l2ZW5fbmFtZSI6Ik1pa2tlbCIsIm5vbmNlIjoiZDlhNGE5YzctM2JmYS00ZWFmLWFiZGMtMGI3MTFhMzVkZjg3Iiwic2lkIjoiZWJiZTFhOGItZTNmZC00OTA4LTllZWYtNzk2ODc0Mzc0OWE5IiwiYXVkIjoiZmFzaGlvbi1zdG9yZS13ZWIiLCJhY3IiOiJodHRwczpcL1wvY3VzdG9tZXItc3NvLmRvY3MuemFsYW5kby5uZXRcL3BvbGljaWVzXC9zaW5nbGUtZmFjdG9yIiwiZXhwIjoxNjMzNzMwNTc5LCJpYXQiOjE2MzM3MjY5NzksImZhbWlseV9uYW1lIjoiQWFnYWFyZCIsImVtYWlsIjoibWlra2VsYWFnYWFyZDUyQGdtYWlsLmNvbSJ9.UpcUekp4lbYhhPHjM0FFcWiCjPDgTzsQXKNE9yLwF825YlBeZXrfGpN6zKKt_mO3F6Tusbmsm0umOX9epcGzvQ; zac=AAAAACW07XrYwrW3JVWqYCX8vMstxPSKJQSCdUQkvgjLY83CvqsPZZ7TiFDi25PGmVVBIIFJouKAfQXhLejf4hjVLB0PsbNmpjbY07K1QbjIvHMupFkDMSR49PpoicTy9fLyf0b5W4rS58rHTFl7Nx7bVhVjol4sKLd-UgiQxg4V-HLpYb3JT9L2nYMfoIIAjsUmOBSvFHF4u03JbLu4r4Jev9ECeDkPH7QKUlIWBvE5SJVVVTiyE1kHd0LTWm9gkV_uxHSSyAVBy8Q6UCoujTXa7iPdkjlkx3qpMto08emw4Ai91qshYMY1iEYyEh-MMoB4xBHa69798N30t7EOAik-JC4oO32SHOOfw_a0vEsF8sGrLCQ8l_ENp5nEMFMmGMUEeZ8N_mx2DKe6-eN6ij4dsNHblO5Dp6KA2vqq8JqCW9Ym6W2JZN2Yfkt42pFuwaW73pWxUOx4d_TTFGSwoxdrp81JfIsuQ4O5PNLh_dQgTD2TnjgIjf7IdPXEI9XNL_Vcth-l_b8b6FVXv3IxioEFFOPXn6DwrClv0LIbb9BL1PV9YTcQf72EjaZEu0mIqQGH8lRrkYVAhsO-Sed-y3z7o3rha47Fjyqm21f_JMQSZ8wuOIU9j2iWrhu6YcgTVUgeYDEyeOM17rLe_UGOspF-h6DC2ucJU8D0kxoi-LK9APtBMt5lvh1XvSjhwbNJSE0aeDgUo5hFwycIBsODiRB7IuDV2bYtgzas4bUcTZZBZ1XluKxkRo_iPA9keVf_Lu3cP43cAv9vU6e3O5CiIJk6y5HcGk2IjCOxouEOGZAXW5wiy4eM2FRxPzKbZihRx7Om0XU4AdzIl-3tviZZ9jl6Z4Rj7TS7PfdbyAnCp-M8TldU-WAodGFAnPvpwOOmxR0qj-WvPcWMhzrFIrKwm6gCD6G6GcVvyoQWZ-_j2b_AmTrCmFPKrY0BjzqzQ8Oc74t8DXqFRUdrnW2bTH8PIjEV-Bftt5shpXXN0vg845DOqyNb9Dq7oXo2Xt9U7QcNsJeLT3R2aRBjHC7OZhN7o_H0cbE7fCTqLo8b7Y9SytdpM3dIe80XNsuryc0JPYkfrJvD02ypfhig0_c205ZeZYc4EVmPkvVNPTrY6NzbgeX_Fr1Ln9LuXkT7_jPxm4A29RW59PCimk-pSm1HRztG-UoLJZ2kUR2KBNGlWwJHbMd7iH5p1qrsjQr4ktHZTeAMtbg0dYfGtx5PFtcDcGYuLaCF7SRni1ewOQLEsr6n37wfIFiaZwMaKaUwKRo9c8Bu5nwF23ojafAnj4sgTwVvgA==; _gat_zalga=1; bm_sv=DEAC04753D896415042CF27EFE6BC9F1~ksLBha2hW/fj4MFKPDeRHXvkZ0jZZmGzjuIeh1abfoGEnatpxHRH8uMjXYMW7kPjNUJMkCiTctQR8IM3yZ98d8OphA+mmONdWy8UNfktsdq33BjQWetLscIYBJTH87kpgKI4zfMMA6mAG5sVvjYjELwVVirvZ3CA2Mawi2Dd+KI=; _abck=B1444B036936A98C16C07AF25EE7290B~-1~YAAQ129faCqINV58AQAAFIa3YQZA1O7GpJmsN0c4xzRY2fa1PzqXbSZhg6iOSXm9gUTXsddrf28I/tA7BAYTlrCzorgAMelcC4phg+txua/63u8QoNNSjhKlPNmesaw5MFC1hzhnxDqiV+ko6Tar7ctFiCMdMySgGQB+ayNQo8wmUvJScSpKBiKod/9i9VMHTN55DCpK0EqfFsXoFK6IYTG/ESMqlGNU6rdaf/dCkYr19WIKp47x/kpvAvu53+AJptF7Fzw0XS8TuTB9MDd2hnBcAqvW7OeVk/s6cpb77nfyzzpfIJ0FGxAaqm10Eu1o7U+hFUj1HwlEodR+PRko6a+alUU6Z2hoFiYK4tgsW1iaDnmIoaYNFJmozJCw9bm/lIC8b0InP7u9cuJOoscES98VFfxM9oMEeuiBQmtntstgW7bAvNDnjYrAaNOunyIQ+r6RgyIAd8TmMxtKJugOkJfqufJvVIQSnAthq6pGIJHDfRcjvVCz2pNyaP4AxoLy~-1~-1~-1",
        }

        data = '{"checkoutId":"e43bryKCz7-SoCM8GhgPVN7QjLL3OlVzMCGPx0vlJQY","eTag":"\\"6a44d975-c281-4c7c-88a3-ddd0817be0fd\\""}'

        response = requests.post(
            "https://www.zalando.dk/api/checkout/buy-now", headers=headers, data=data
        )

        print(response.status_code)


# NI112N02Y-A110070000


def main(mode):

    if mode == "1":
        print("\nZalando Preload Drop Chosen")
        pid = input("PID: ")
        zalando_preload.preload(pid)

    if mode == "2":
        print("\nZalando ACO Chosen")
        pid = input("PID: ")
        zalando_checkout.atc(pid)
