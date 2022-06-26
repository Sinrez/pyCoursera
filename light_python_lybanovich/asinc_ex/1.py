import asyncio

async def wicked():
    print("Surrender,")
    await asyncio.sleep(2)
    print("Dorothy!")

asyncio.run(wicked())