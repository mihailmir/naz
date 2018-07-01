import asyncio

import typing


class DefaultOutboundQueue(object):
    """
    this allows users to provide their own queue managers eg redis etc.
    """

    def __init__(self, maxsize: int, loop: asyncio.events.AbstractEventLoop) -> None:
        """
        maxsize is the max number of items(not size) that can be put in the queue.
        """
        self.queue: asyncio.queues.Queue = asyncio.Queue(maxsize=maxsize, loop=loop)

    async def enqueue(self, item: dict) -> None:
        self.queue.put_nowait(item)

    async def dequeue(self) -> typing.Any:
        return await self.queue.get()
