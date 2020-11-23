#! /home/akalend/anaconda3/bin/python
from aiohttp import web
import aiohttp
import aio_pika as rabbit

async def handle_start(request):
    params = request.rel_url.query
    # session = aiohttp.ClientSession()
    id = params['id']

    # create connections
    connection = await rabbit.connect("amqp://guest:guest@localhost/")

    # Creating a channel
    channel = await connection.channel()

    await channel.default_exchange.publish(
        rabbit.Message(id.encode()),
        routing_key="hello",
    )


    # redis = await aioredis.create_redis_pool('redis://127.0.0.1')
    # await redis.lpush("queue", id)
    # redis.close()
    # await redis.wait_closed()

    return web.Response(text='id =%s'  % id )



async def handle_status(request):
    id = request.match_info.get('id', "0")
    if id == '0' :
        return web.Response(text='error' )

    # print(id)    
    # redis = await aioredis.create_redis_pool('redis://127.0.0.1')
    # res = await redis.get("status_" + id)



    if res is None:
        res = '0'
    else:
        print('retult id=%s Ok' % id)
        res = '1'    
    redis.close()

    await redis.wait_closed()

    return web.Response(text=res )



app = web.Application()
app.add_routes([  web.get('/start', handle_start), web.get('/status/{id}', handle_status)])


if __name__ == '__main__':
    web.run_app(app, port=8000)