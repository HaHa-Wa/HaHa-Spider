import time
import execjs
from websocket import create_connection


def encode_params(rawdata):
    with open('decode2.js', 'r', encoding='UTF-8') as f:
        js_code = f.read()
    context = execjs.compile(js_code)
    result = context.call("encode_msg", rawdata)  # 参数一为函数名，参数二和三为函数的参数
    return result


def main():
    ws = create_connection("ws://39.106.210.189:10000/")
    haha = b'{"traces":[{}],"type":"/v4/rankings/price/get_quote_curreny_prices","value":"{}"}'
    # arrayInfo = [
    #     7, 10, 34, 47, 118, 50, 47, 117, 115, 101,
    #     114, 47, 112, 114, 111, 100, 117, 99, 116, 47,
    #     103, 101, 116, 95, 112, 114, 111, 100, 117, 99,
    #     116, 95, 116, 121, 112, 101, 115, 18, 14, 123,
    #     34, 116, 111, 107, 101, 110, 34, 58, 110, 117,
    #     108, 108, 125, 122, 2, 8, 1
    # ]
    data = {
        "traces": [
            {
                "ref": 996
            }
        ],
        "type": "/v6/market/summary/get_summaries_by_symbols",
        "value": "{\"token\":\"29b7dde2a34ccb530af5a987f375f6fe\",\"symbols\":[\"OKEX:ETHUSDTPERP\",\"OKEX:BTCUSDTPERP\",\"BINANCE:ETHUSDPERP\",\"HUOBI:ETHUSDPERP\"]}"
    }
    arrayInfo = encode_params(data)
    print(arrayInfo)
    ws.send_binary(arrayInfo)
    print("Sent")
    print("Receiving...")
    time.sleep(2)
    result = ws.recv()
    print(type(result))
    str2 = str(result, )
    print(str2)
    # print("Received '%s'" % str(result))
    time.sleep(4)
    ws.close()


if __name__ == '__main__':
    main()
