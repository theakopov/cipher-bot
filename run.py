import contextlib
import asyncio
from bot import start_bot

with contextlib.suppress(KeyboardInterrupt, SystemExit):
    asyncio.run(start_bot())
