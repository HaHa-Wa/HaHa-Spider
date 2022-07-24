function decode_msg(ie) {
    const ce = new ye.Reader(new Uint8Array(ie))
      , de = ce.uint32();
    switch (de) {
    case 71:
        return ae.msg_types.add_route_msg_t.decode(ce);
    case 68:
        return ae.msg_types.add_route_rep_t.decode(ce);
    case 67:
        return ae.msg_types.add_route_req_t.decode(ce);
    case 28:
        return ae.msg_types.auth_rep_t.decode(ce);
    case 27:
        return ae.msg_types.auth_req_t.decode(ce);
    case 72:
        return ae.msg_types.delete_route_msg_t.decode(ce);
    case 70:
        return ae.msg_types.delete_route_rep_t.decode(ce);
    case 69:
        return ae.msg_types.delete_route_req_t.decode(ce);
    case 84:
        return ae.msg_types.delete_topics_rep_t.decode(ce);
    case 83:
        return ae.msg_types.delete_topics_req_t.decode(ce);
    case 10:
        return ae.msg_types.do2_rep_t.decode(ce);
    case 9:
        return ae.msg_types.do2_req_t.decode(ce);
    case 8:
        return ae.msg_types.do_rep_t.decode(ce);
    case 7:
        return ae.msg_types.do_req_t.decode(ce);
    case 32:
        return ae.msg_types.error2_rep_t.decode(ce);
    case 30:
        return ae.msg_types.error_rep_t.decode(ce);
    case 31:
        return ae.msg_types.ok2_rep_t.decode(ce);
    case 29:
        return ae.msg_types.ok_rep_t.decode(ce);
    case 2:
        return ae.msg_types.ping_rep_t.decode(ce);
    case 1:
        return ae.msg_types.ping_req_t.decode(ce);
    case 4:
        return ae.msg_types.pull_rep_t.decode(ce);
    case 3:
        return ae.msg_types.pull_req_t.decode(ce);
    case 76:
        return ae.msg_types.pull_routes_rep_t.decode(ce);
    case 75:
        return ae.msg_types.pull_routes_req_t.decode(ce);
    case 6:
        return ae.msg_types.push_rep_t.decode(ce);
    case 5:
        return ae.msg_types.push_req_t.decode(ce);
    case 74:
        return ae.msg_types.push_routes_rep_t.decode(ce);
    case 73:
        return ae.msg_types.push_routes_req_t.decode(ce);
    case 82:
        return ae.msg_types.register_backend_rep_t.decode(ce);
    case 81:
        return ae.msg_types.register_backend_req_t.decode(ce);
    case 66:
        return ae.msg_types.register_frontend_rep_t.decode(ce);
    case 65:
        return ae.msg_types.register_frontend_req_t.decode(ce);
    case 100:
        return ae.msg_types.resolve_backend_rep_t.decode(ce);
    case 99:
        return ae.msg_types.resolve_backend_req_t.decode(ce);
    case 98:
        return ae.msg_types.resolve_frontend_rep_t.decode(ce);
    case 97:
        return ae.msg_types.resolve_frontend_req_t.decode(ce);
    case 122:
        return ae.msg_types.resolve_ip_rep_t.decode(ce);
    case 121:
        return ae.msg_types.resolve_ip_req_t.decode(ce);
    case 108:
        return ae.msg_types.unwatch_rep_t.decode(ce);
    case 107:
        return ae.msg_types.unwatch_req_t.decode(ce);
    case 106:
        return ae.msg_types.watch_rep_t.decode(ce);
    case 105:
        return ae.msg_types.watch_req_t.decode(ce);
    default:
        throw `Unknown msg type: ${de}`
    }
}
function Uint8ArrayToString(fileData) {
    let dataString = "";
    for (let i = 0; i < fileData.length; i++) {
        dataString += String.fromCharCode(fileData[i]);
    }
    console.log(dataString)
    return dataString
}

haha = [8, 2, 2, 8, 2]
Uint8ArrayToString(haha)


function stringToUint8Array(str){
  var arr = [];
  for (var i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }

  var tmpUint8Array = new Uint8Array(arr);
  return tmpUint8Array
}

haha = '{"traces":[{"ref":1}],"type":"/v2/user/product/get_product_types","value":"{"token":null}"}'
ret = stringToUint8Array(haha)
console.log(ret)
// {
//     "traces": [
//         {
//             "ref": 2
//         }
//     ],
//     "type": "/v4/rankings/price/get_quote_curreny_prices",
//     "value": "{}"
// }
