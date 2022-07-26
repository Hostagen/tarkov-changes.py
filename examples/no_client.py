import asyncio

from tvc import Ammunition, TVCClient
from typing import List

TOKEN: str = 'blahblah some token string'


async def main():

    async with TVCClient(TOKEN) as api:
        ammunition: List[Ammunition] = await api.fetch_ammunition('7.62x39mm BP gzh')

        if not ammunition:
            # fetch result can be return empty list.
            # If the list of ammunition what responded to is empty.
            print('Can not found ammunition!')
            return

        for ammo in ammunition:
            print(f"Name: {ammo}")

        # Returns all entries if you do not insert a query into the fetch function argument.
        ammunition: List[Ammunition] = await api.fetch_ammunition()

        for ammo in ammunition:
            print(f"Name: {ammo}")

    # When you exit the `async with` syntax, aiohttp.ClientSession is automatically and securely terminated.
    # When you use the `async with` with again, a new aiohttp.ClientSession is created again.

    async with TVCClient(TOKEN) as api:
        ...

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
