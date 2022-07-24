function Op(ie, ae, ce) {
    this.fn = ie,
        this.len = ae,
        this.next = void 0,
        this.val = ce
}

function noop() {
}

function State(ie) {
    this.head = ie.head,
        this.tail = ie.tail,
        this.len = ie.len,
        this.next = ie.states
}

function Writer() {
    this.len = 0,
        this.head = new Op(noop, 0, 0),
        this.tail = this.head,
        this.states = null
}

Writer.prototype.uint32 = function write_uint32(ie) {
    return this.len += (this.tail = this.tail.next = new VarintOp((ie >>>= 0) < 128 ? 1 : ie < 16384 ? 2 : ie < 2097152 ? 3 : ie < 268435456 ? 4 : 5, ie)).len,
        this
}
Writer.prototype.bytes = function write_bytes(ie) {
    var ae = ie.length >>> 0;
    if (!ae)
        return this._push(writeByte, 1, 0);
    if (be.isString(ie)) {
        var ce = Writer.alloc(ae = ye.length(ie));
        ye.decode(ie, ce, 0),
            ie = ce
    }
    return this.uint32(ae)._push(xe, ae, ie)
}
var we;

function utf8_length(ie) {
    for (var ae = 0, ce = 0, de = 0; de < ie.length; ++de)
        (ce = ie.charCodeAt(de)) < 128 ? ae += 1 : ce < 2048 ? ae += 2 : 55296 === (64512 & ce) && 56320 === (64512 & ie.charCodeAt(de + 1)) ? (++de,
            ae += 4) : ae += 3;
    return ae
}

function utf8_read(ie, ae, ce) {
    if (ce - ae < 1)
        return "";
    for (var de, be = null, _e = [], ye = 0; ae < ce;)
        (de = ie[ae++]) < 128 ? _e[ye++] = de : de > 191 && de < 224 ? _e[ye++] = (31 & de) << 6 | 63 & ie[ae++] : de > 239 && de < 365 ? (de = ((7 & de) << 18 | (63 & ie[ae++]) << 12 | (63 & ie[ae++]) << 6 | 63 & ie[ae++]) - 65536,
            _e[ye++] = 55296 + (de >> 10),
            _e[ye++] = 56320 + (1023 & de)) : _e[ye++] = (15 & de) << 12 | (63 & ie[ae++]) << 6 | 63 & ie[ae++],
        ye > 8191 && ((be || (be = [])).push(String.fromCharCode.apply(String, _e)),
            ye = 0);
    return be ? (ye && be.push(String.fromCharCode.apply(String, _e.slice(0, ye))),
        be.join("")) : String.fromCharCode.apply(String, _e.slice(0, ye))
}

function utf8_write(ie, ae, ce) {
    for (var de, be, _e = ce, ye = 0; ye < ie.length; ++ye)
        (de = ie.charCodeAt(ye)) < 128 ? ae[ce++] = de : de < 2048 ? (ae[ce++] = de >> 6 | 192,
            ae[ce++] = 63 & de | 128) : 55296 === (64512 & de) && 56320 === (64512 & (be = ie.charCodeAt(ye + 1))) ? (de = 65536 + ((1023 & de) << 10) + (1023 & be),
            ++ye,
            ae[ce++] = de >> 18 | 240,
            ae[ce++] = de >> 12 & 63 | 128,
            ae[ce++] = de >> 6 & 63 | 128,
            ae[ce++] = 63 & de | 128) : (ae[ce++] = de >> 12 | 224,
            ae[ce++] = de >> 6 & 63 | 128,
            ae[ce++] = 63 & de | 128);
    return ce - _e
}

Writer.prototype.string = function write_string(ie) {
    var ae = utf8_length(ie);
    return ae ? this.uint32(ae)._push(utf8_write, ae, ie) : this._push(writeByte, 1, 0)
}

Writer.prototype._push = function push(ie, ae, ce) {
    return this.tail = this.tail.next = new Op(ie, ae, ce),
        this.len += ae,
        this
}
Writer.prototype.fork = function fork() {
    return this.states = new State(this),
        this.head = this.tail = new Op(noop, 0, 0),
        this.len = 0,
        this
}

Writer.prototype.reset = function reset() {
    return this.states ? (this.head = this.states.head,
        this.tail = this.states.tail,
        this.len = this.states.len,
        this.states = this.states.next) : (this.head = this.tail = new Op(noop, 0, 0),
        this.len = 0),
        this
}

Writer.prototype.ldelim = function ldelim() {
    var ie = this.head
        , ae = this.tail
        , ce = this.len;
    return this.reset().uint32(ce),
    ce && (this.tail.next = ie.next,
        this.tail = ae,
        this.len += ce),
        this
}

function pool(ie, ae, ce) {
    var de = ce || 8192
        , be = de >>> 1
        , _e = null
        , ye = de;
    return function pool_alloc(ce) {
        if (ce < 1 || ce > be)
            return ie(ce);
        ye + ce > de && (_e = ie(de),
            ye = 0);
        var we = ae.call(_e, ye, ye += ce);
        return 7 & ye && (ye = 1 + (7 | ye)),
            we
    }
}

VarintOp.prototype = Object.create(Op.prototype)
VarintOp.prototype.fn = function writeVarint32(ie, ae, ce) {
    for (; ie > 127;)
        ae[ce++] = 127 & ie | 128,
            ie >>>= 7;
    ae[ce] = ie
}
Writer.prototype.finish = function finish() {
    console.log(pool(this.len))
    for (var ie = this.head.next, ae = new Uint8Array(this.len), ce = 0; ie;)
        ie.fn(ie.val, ae, ce),
            ce += ie.len,
            ie = ie.next;
    return ae
}

function writeByte(ie, ae, ce) {
    ae[ce] = 255 & ie
}

function VarintOp(ie, ae) {
    this.len = ie,
        this.next = void 0,
        this.val = ae
}

function encode2(ie, ae) {
    return ae || (ae = _e.create()),
    null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(8).uint32(ie.ref),
    null != ie.handlerId && Object.hasOwnProperty.call(ie, "handlerId") && ae.uint32(16).uint32(ie.handlerId),
    null != ie.nodeId && Object.hasOwnProperty.call(ie, "nodeId") && ae.uint32(26).bytes(ie.nodeId),
        ae
}

function encode(ie, ae) {
    if (ae || (ae = _e.create()),
    null != ie.type && Object.hasOwnProperty.call(ie, "type") && ae.uint32(10).string(ie.type),
    null != ie.value && Object.hasOwnProperty.call(ie, "value") && ae.uint32(18).string(ie.value),
    null != ie.sourceEnabled && Object.hasOwnProperty.call(ie, "sourceEnabled") && ae.uint32(104).bool(ie.sourceEnabled),
    null != ie.source && Object.hasOwnProperty.call(ie, "source") && we.maxwell.protocol.source_t.encode(ie.source, ae.uint32(114).fork()).ldelim(),
    null != ie.traces && ie.traces.length)
        for (var ce = 0; ce < ie.traces.length; ++ce)
            encode2(ie.traces[ce], ae.uint32(122).fork()).ldelim();
    return ae
}

function encode_msg(ie) {
    const ce = new Writer;
    console.log(ie.constructor)
    // switch (ie.constructor) {
    //     case ae.msg_types.add_route_msg_t:
    //         return ce.uint32(71),
    //             ae.msg_types.add_route_msg_t.encode(ie, ce).finish();
    //     case ae.msg_types.add_route_rep_t:
    //         return ce.uint32(68),
    //             ae.msg_types.add_route_rep_t.encode(ie, ce).finish();
    //     case ae.msg_types.add_route_req_t:
    //         return ce.uint32(67),
    //             ae.msg_types.add_route_req_t.encode(ie, ce).finish();
    //     case ae.msg_types.auth_rep_t:
    //         return ce.uint32(28),
    //             ae.msg_types.auth_rep_t.encode(ie, ce).finish();
    //     case ae.msg_types.auth_req_t:
    //         return ce.uint32(27),
    //             ae.msg_types.auth_req_t.encode(ie, ce).finish();
    //     case ae.msg_types.delete_route_msg_t:
    //         return ce.uint32(72),
    //             ae.msg_types.delete_route_msg_t.encode(ie, ce).finish();
    //     case ae.msg_types.delete_route_rep_t:
    //         return ce.uint32(70),
    //             ae.msg_types.delete_route_rep_t.encode(ie, ce).finish();
    //     case ae.msg_types.delete_route_req_t:
    //         return ce.uint32(69),
    //             ae.msg_types.delete_route_req_t.encode(ie, ce).finish();
    //     case ae.msg_types.delete_topics_rep_t:
    //         return ce.uint32(84),
    //             ae.msg_types.delete_topics_rep_t.encode(ie, ce).finish();
    //     case ae.msg_types.delete_topics_req_t:
    //         return ce.uint32(83),
    //             ae.msg_types.delete_topics_req_t.encode(ie, ce).finish();
    //     case ae.msg_types.do2_rep_t:
    //         return ce.uint32(10),
    //             ae.msg_types.do2_rep_t.encode(ie, ce).finish();
    //     case ae.msg_types.do2_req_t:
    //         return ce.uint32(9),
    //             ae.msg_types.do2_req_t.encode(ie, ce).finish();
    //     case ae.msg_types.do_rep_t:
    //         return ce.uint32(8),
    //             ae.msg_types.do_rep_t.encode(ie, ce).finish();
    //     case ae.msg_types.do_req_t:
    //         return ce.uint32(7),
    //             ae.msg_types.do_req_t.encode(ie, ce).finish();
    //     case ae.msg_types.error2_rep_t:
    //         return ce.uint32(32),
    //             ae.msg_types.error2_rep_t.encode(ie, ce).finish();
    //     case ae.msg_types.error_rep_t:
    //         return ce.uint32(30),
    //             ae.msg_types.error_rep_t.encode(ie, ce).finish();
    //     case ae.msg_types.ok2_rep_t:
    //         return ce.uint32(31),
    //             ae.msg_types.ok2_rep_t.encode(ie, ce).finish();
    //     case ae.msg_types.ok_rep_t:
    //         return ce.uint32(29),
    //             ae.msg_types.ok_rep_t.encode(ie, ce).finish();
    //     case ae.msg_types.ping_rep_t:
    //         return ce.uint32(2),
    //             ae.msg_types.ping_rep_t.encode(ie, ce).finish();
    //     case ae.msg_types.ping_req_t:
    //         return ce.uint32(1),
    //             ae.msg_types.ping_req_t.encode(ie, ce).finish();
    //     case ae.msg_types.pull_rep_t:
    //         return ce.uint32(4),
    //             ae.msg_types.pull_rep_t.encode(ie, ce).finish();
    //     case ae.msg_types.pull_req_t:
    //         return ce.uint32(3),
    //             ae.msg_types.pull_req_t.encode(ie, ce).finish();
    //     case ae.msg_types.pull_routes_rep_t:
    //         return ce.uint32(76),
    //             ae.msg_types.pull_routes_rep_t.encode(ie, ce).finish();
    //     case ae.msg_types.pull_routes_req_t:
    //         return ce.uint32(75),
    //             ae.msg_types.pull_routes_req_t.encode(ie, ce).finish();
    //     case ae.msg_types.push_rep_t:
    //         return ce.uint32(6),
    //             ae.msg_types.push_rep_t.encode(ie, ce).finish();
    //     case ae.msg_types.push_req_t:
    //         return ce.uint32(5),
    //             ae.msg_types.push_req_t.encode(ie, ce).finish();
    //     case ae.msg_types.push_routes_rep_t:
    //         return ce.uint32(74),
    //             ae.msg_types.push_routes_rep_t.encode(ie, ce).finish();
    //     case ae.msg_types.push_routes_req_t:
    //         return ce.uint32(73),
    //             ae.msg_types.push_routes_req_t.encode(ie, ce).finish();
    //     case ae.msg_types.register_backend_rep_t:
    //         return ce.uint32(82),
    //             ae.msg_types.register_backend_rep_t.encode(ie, ce).finish();
    //     case ae.msg_types.register_backend_req_t:
    //         return ce.uint32(81),
    //             ae.msg_types.register_backend_req_t.encode(ie, ce).finish();
    //     case ae.msg_types.register_frontend_rep_t:
    //         return ce.uint32(66),
    //             ae.msg_types.register_frontend_rep_t.encode(ie, ce).finish();
    //     case ae.msg_types.register_frontend_req_t:
    //         return ce.uint32(65),
    //             ae.msg_types.register_frontend_req_t.encode(ie, ce).finish();
    //     case ae.msg_types.resolve_backend_rep_t:
    //         return ce.uint32(100),
    //             ae.msg_types.resolve_backend_rep_t.encode(ie, ce).finish();
    //     case ae.msg_types.resolve_backend_req_t:
    //         return ce.uint32(99),
    //             ae.msg_types.resolve_backend_req_t.encode(ie, ce).finish();
    //     case ae.msg_types.resolve_frontend_rep_t:
    //         return ce.uint32(98),
    //             ae.msg_types.resolve_frontend_rep_t.encode(ie, ce).finish();
    //     case ae.msg_types.resolve_frontend_req_t:
    //         return ce.uint32(97),
    //             ae.msg_types.resolve_frontend_req_t.encode(ie, ce).finish();
    //     case ae.msg_types.resolve_ip_rep_t:
    //         return ce.uint32(122),
    //             ae.msg_types.resolve_ip_rep_t.encode(ie, ce).finish();
    //     case ae.msg_types.resolve_ip_req_t:
    //         return ce.uint32(121),
    //             ae.msg_types.resolve_ip_req_t.encode(ie, ce).finish();
    //     case ae.msg_types.unwatch_rep_t:
    //         return ce.uint32(108),
    //             ae.msg_types.unwatch_rep_t.encode(ie, ce).finish();
    //     case ae.msg_types.unwatch_req_t:
    //         return ce.uint32(107),
    //             ae.msg_types.unwatch_req_t.encode(ie, ce).finish();
    //     case ae.msg_types.watch_rep_t:
    //         return ce.uint32(106),
    //             ae.msg_types.watch_rep_t.encode(ie, ce).finish();
    //     case ae.msg_types.watch_req_t:
    //         return ce.uint32(105),
    //             ae.msg_types.watch_req_t.encode(ie, ce).finish();
    //     default:
    //         throw `Unknown msg type: ${ie.constructor}`
    // }
    ce.uint32(7);
    var unintArrayInfo = encode(ie, ce).finish();
    return Array.from(unintArrayInfo)
}

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

var ie = {
    "traces": [
        {
            "ref": 996
        }
    ],
    "type": "/v6/market/summary/get_summaries_by_symbols",
    "value": "{\"token\":\"29b7dde2a34ccb530af5a987f375f6fe\",\"symbols\":[\"OKEX:ETHUSDTPERP\",\"OKEX:BTCUSDTPERP\",\"BINANCE:ETHUSDPERP\",\"HUOBI:ETHUSDPERP\"]}"
}

// ret = encode_msg(ie)
//
// console.log(ret)
// console.log(Array.from(ret))
