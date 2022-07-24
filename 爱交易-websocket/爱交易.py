import asyncio
import json
import logging
from datetime import datetime

import websocket
from aiowebsocket.converses import AioWebSocket


async def startup(uri):
    async with AioWebSocket(uri) as aws:
        converse = aws.manipulator
        message = {
            "traces": [
                {
                    "ref": 1
                }
            ],
            "type": "/v2/user/product/get_product_types",
            "value": "{\"token\":null}"
        }
        # 客户端给服务端发送消息
        await converse.send(list(json.dumps(message)), opencode=websocket.ABNF.OPCODE_BINARY)
        print('发送成功')
        while True:
            mes = await converse.receive()
            print('{time}-Client receive: {rec}'
                  .format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), rec=mes))


if __name__ == '__main__':
    remote = 'ws://39.106.210.189:10000/'
    try:
        asyncio.get_event_loop().run_until_complete(startup(remote))
    except KeyboardInterrupt as exc:
        logging.info('Quit.')
