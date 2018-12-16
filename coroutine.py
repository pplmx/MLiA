#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author  : mystic
# @date    : 12/14/2018 21:18
import asyncio


@asyncio.coroutine
def hello():
    print('Hello World!')
    yield from asyncio.sleep(1)
    print('Hello again!')


async def hello_new_grammar():
    print('Hello World!')
    await asyncio.sleep(1)
    print('Hello again!')


loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()
