import asyncio
import time
import requests
import aiohttp

BASE_URL = "https://pokeapi.co/api/v2/"
EXCHANGES = ['pokemon']

# threads = [
#     Thread(target=check_price, args=(exchange, 'btc', '2020-04-01'))
#     for exchange in EXCHANGES
# ]


async def check_pokemon(base_url=BASE_URL):
    resp = requests.get(f"{base_url}/{EXCHANGES}")
    f = resp.json()


async def main():
    start = time.time()
    await asyncio.gather(check_pokemon())
    print(time.time() - start)


asyncio.run(main())
