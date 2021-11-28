import asyncio
import aiofiles
import aiohttp

async def fetch(url):
    async with aiohttp.clientsession() as session:
        response = await session.get(urls)
        html = await response.text()
        return html

async def write_to_file(fie, text):
    async with aiofiles.open(file, 'w') as f:
        await f.write(text)

async def main(urls):
    taks = []
    for url in urls:
        file = f'{url.split("//")[-1]}.txt'
        html = await fetch(url)
        tasks.append(write_to_file(file, html))
    await asyncio.gather(*tasks)

urls = ['https://google.in', 'https://python.org', 'https://facebook.com']

asyncio.run(main(urls))
