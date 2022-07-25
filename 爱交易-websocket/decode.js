95658:function (ie, ae, ce) {
    "use strict";
    var de = this && this.__createBinding || (Object.create ? function (ie, ae, ce, de) {
                void 0 === de && (de = ce),
                    Object.defineProperty(ie, de, {
                        enumerable: !0,
                        get: function () {
                            return ae[ce]
                        }
                    })
            }
            : function (ie, ae, ce, de) {
                void 0 === de && (de = ce),
                    ie[de] = ae[ce]
            }
        )
        , be = this && this.__setModuleDefault || (Object.create ? function (ie, ae) {
                Object.defineProperty(ie, "default", {
                    enumerable: !0,
                    value: ae
                })
            }
            : function (ie, ae) {
                ie.default = ae
            }
        )
        , _e = this && this.__importStar || function (ie) {
            if (ie && ie.__esModule)
                return ie;
            var ae = {};
            if (null != ie)
                for (var ce in ie)
                    "default" !== ce && Object.prototype.hasOwnProperty.call(ie, ce) && de(ae, ie, ce);
            return be(ae, ie),
                ae
        }
    ;
    Object.defineProperty(ae, "__esModule", {
        value: !0
    }),
        ae.decode_msg = ae.encode_msg = ae.msg_types = void 0;
    const ye = _e(ce(62100))
        , we = _e(ce(83111));

    function encode_msg(ie) {
        const ce = new ye.Writer;
        switch (ie.constructor) {
            case ae.msg_types.add_route_msg_t:
                return ce.uint32(71),
                    ae.msg_types.add_route_msg_t.encode(ie, ce).finish();
            case ae.msg_types.add_route_rep_t:
                return ce.uint32(68),
                    ae.msg_types.add_route_rep_t.encode(ie, ce).finish();
            case ae.msg_types.add_route_req_t:
                return ce.uint32(67),
                    ae.msg_types.add_route_req_t.encode(ie, ce).finish();
            case ae.msg_types.auth_rep_t:
                return ce.uint32(28),
                    ae.msg_types.auth_rep_t.encode(ie, ce).finish();
            case ae.msg_types.auth_req_t:
                return ce.uint32(27),
                    ae.msg_types.auth_req_t.encode(ie, ce).finish();
            case ae.msg_types.delete_route_msg_t:
                return ce.uint32(72),
                    ae.msg_types.delete_route_msg_t.encode(ie, ce).finish();
            case ae.msg_types.delete_route_rep_t:
                return ce.uint32(70),
                    ae.msg_types.delete_route_rep_t.encode(ie, ce).finish();
            case ae.msg_types.delete_route_req_t:
                return ce.uint32(69),
                    ae.msg_types.delete_route_req_t.encode(ie, ce).finish();
            case ae.msg_types.delete_topics_rep_t:
                return ce.uint32(84),
                    ae.msg_types.delete_topics_rep_t.encode(ie, ce).finish();
            case ae.msg_types.delete_topics_req_t:
                return ce.uint32(83),
                    ae.msg_types.delete_topics_req_t.encode(ie, ce).finish();
            case ae.msg_types.do2_rep_t:
                return ce.uint32(10),
                    ae.msg_types.do2_rep_t.encode(ie, ce).finish();
            case ae.msg_types.do2_req_t:
                return ce.uint32(9),
                    ae.msg_types.do2_req_t.encode(ie, ce).finish();
            case ae.msg_types.do_rep_t:
                return ce.uint32(8),
                    ae.msg_types.do_rep_t.encode(ie, ce).finish();
            case ae.msg_types.do_req_t:
                return ce.uint32(7),
                    ae.msg_types.do_req_t.encode(ie, ce).finish();
            case ae.msg_types.error2_rep_t:
                return ce.uint32(32),
                    ae.msg_types.error2_rep_t.encode(ie, ce).finish();
            case ae.msg_types.error_rep_t:
                return ce.uint32(30),
                    ae.msg_types.error_rep_t.encode(ie, ce).finish();
            case ae.msg_types.ok2_rep_t:
                return ce.uint32(31),
                    ae.msg_types.ok2_rep_t.encode(ie, ce).finish();
            case ae.msg_types.ok_rep_t:
                return ce.uint32(29),
                    ae.msg_types.ok_rep_t.encode(ie, ce).finish();
            case ae.msg_types.ping_rep_t:
                return ce.uint32(2),
                    ae.msg_types.ping_rep_t.encode(ie, ce).finish();
            case ae.msg_types.ping_req_t:
                return ce.uint32(1),
                    ae.msg_types.ping_req_t.encode(ie, ce).finish();
            case ae.msg_types.pull_rep_t:
                return ce.uint32(4),
                    ae.msg_types.pull_rep_t.encode(ie, ce).finish();
            case ae.msg_types.pull_req_t:
                return ce.uint32(3),
                    ae.msg_types.pull_req_t.encode(ie, ce).finish();
            case ae.msg_types.pull_routes_rep_t:
                return ce.uint32(76),
                    ae.msg_types.pull_routes_rep_t.encode(ie, ce).finish();
            case ae.msg_types.pull_routes_req_t:
                return ce.uint32(75),
                    ae.msg_types.pull_routes_req_t.encode(ie, ce).finish();
            case ae.msg_types.push_rep_t:
                return ce.uint32(6),
                    ae.msg_types.push_rep_t.encode(ie, ce).finish();
            case ae.msg_types.push_req_t:
                return ce.uint32(5),
                    ae.msg_types.push_req_t.encode(ie, ce).finish();
            case ae.msg_types.push_routes_rep_t:
                return ce.uint32(74),
                    ae.msg_types.push_routes_rep_t.encode(ie, ce).finish();
            case ae.msg_types.push_routes_req_t:
                return ce.uint32(73),
                    ae.msg_types.push_routes_req_t.encode(ie, ce).finish();
            case ae.msg_types.register_backend_rep_t:
                return ce.uint32(82),
                    ae.msg_types.register_backend_rep_t.encode(ie, ce).finish();
            case ae.msg_types.register_backend_req_t:
                return ce.uint32(81),
                    ae.msg_types.register_backend_req_t.encode(ie, ce).finish();
            case ae.msg_types.register_frontend_rep_t:
                return ce.uint32(66),
                    ae.msg_types.register_frontend_rep_t.encode(ie, ce).finish();
            case ae.msg_types.register_frontend_req_t:
                return ce.uint32(65),
                    ae.msg_types.register_frontend_req_t.encode(ie, ce).finish();
            case ae.msg_types.resolve_backend_rep_t:
                return ce.uint32(100),
                    ae.msg_types.resolve_backend_rep_t.encode(ie, ce).finish();
            case ae.msg_types.resolve_backend_req_t:
                return ce.uint32(99),
                    ae.msg_types.resolve_backend_req_t.encode(ie, ce).finish();
            case ae.msg_types.resolve_frontend_rep_t:
                return ce.uint32(98),
                    ae.msg_types.resolve_frontend_rep_t.encode(ie, ce).finish();
            case ae.msg_types.resolve_frontend_req_t:
                return ce.uint32(97),
                    ae.msg_types.resolve_frontend_req_t.encode(ie, ce).finish();
            case ae.msg_types.resolve_ip_rep_t:
                return ce.uint32(122),
                    ae.msg_types.resolve_ip_rep_t.encode(ie, ce).finish();
            case ae.msg_types.resolve_ip_req_t:
                return ce.uint32(121),
                    ae.msg_types.resolve_ip_req_t.encode(ie, ce).finish();
            case ae.msg_types.unwatch_rep_t:
                return ce.uint32(108),
                    ae.msg_types.unwatch_rep_t.encode(ie, ce).finish();
            case ae.msg_types.unwatch_req_t:
                return ce.uint32(107),
                    ae.msg_types.unwatch_req_t.encode(ie, ce).finish();
            case ae.msg_types.watch_rep_t:
                return ce.uint32(106),
                    ae.msg_types.watch_rep_t.encode(ie, ce).finish();
            case ae.msg_types.watch_req_t:
                return ce.uint32(105),
                    ae.msg_types.watch_req_t.encode(ie, ce).finish();
            default:
                throw `Unknown msg type: ${ie.constructor}`
        }
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

    ae.msg_types = we.maxwell.protocol,
        ae.encode_msg = encode_msg,
        ae.decode_msg = decode_msg,
        ae.default = {
            msg_types: ae.msg_types,
            encode_msg: encode_msg,
            decode_msg: decode_msg
        }
}


83111:(ie, ae, ce) => {
    "use strict";
    var de = ce(62100)
        , be = de.Reader
        , _e = de.Writer
        , ye = de.util
        , we = de.roots.default || (de.roots.default = {});
    we.maxwell = function () {
        var ie = {};
        return ie.protocol = function () {
            var ie = {};
            return ie.msg_type_t = function () {
                var ie = {}
                    , ae = Object.create(ie);
                return ae[ie[0] = "UNKNOWN"] = 0,
                    ae[ie[1] = "PING_REQ"] = 1,
                    ae[ie[2] = "PING_REP"] = 2,
                    ae[ie[3] = "PULL_REQ"] = 3,
                    ae[ie[4] = "PULL_REP"] = 4,
                    ae[ie[5] = "PUSH_REQ"] = 5,
                    ae[ie[6] = "PUSH_REP"] = 6,
                    ae[ie[7] = "DO_REQ"] = 7,
                    ae[ie[8] = "DO_REP"] = 8,
                    ae[ie[9] = "DO2_REQ"] = 9,
                    ae[ie[10] = "DO2_REP"] = 10,
                    ae[ie[27] = "AUTH_REQ"] = 27,
                    ae[ie[28] = "AUTH_REP"] = 28,
                    ae[ie[29] = "OK_REP"] = 29,
                    ae[ie[30] = "ERROR_REP"] = 30,
                    ae[ie[31] = "OK2_REP"] = 31,
                    ae[ie[32] = "ERROR2_REP"] = 32,
                    ae[ie[65] = "REGISTER_FRONTEND_REQ"] = 65,
                    ae[ie[66] = "REGISTER_FRONTEND_REP"] = 66,
                    ae[ie[67] = "ADD_ROUTE_REQ"] = 67,
                    ae[ie[68] = "ADD_ROUTE_REP"] = 68,
                    ae[ie[69] = "DELETE_ROUTE_REQ"] = 69,
                    ae[ie[70] = "DELETE_ROUTE_REP"] = 70,
                    ae[ie[71] = "ADD_ROUTE_MSG"] = 71,
                    ae[ie[72] = "DELETE_ROUTE_MSG"] = 72,
                    ae[ie[73] = "PUSH_ROUTES_REQ"] = 73,
                    ae[ie[74] = "PUSH_ROUTES_REP"] = 74,
                    ae[ie[75] = "PULL_ROUTES_REQ"] = 75,
                    ae[ie[76] = "PULL_ROUTES_REP"] = 76,
                    ae[ie[81] = "REGISTER_BACKEND_REQ"] = 81,
                    ae[ie[82] = "REGISTER_BACKEND_REP"] = 82,
                    ae[ie[83] = "DELETE_TOPICS_REQ"] = 83,
                    ae[ie[84] = "DELETE_TOPICS_REP"] = 84,
                    ae[ie[97] = "RESOLVE_FRONTEND_REQ"] = 97,
                    ae[ie[98] = "RESOLVE_FRONTEND_REP"] = 98,
                    ae[ie[99] = "RESOLVE_BACKEND_REQ"] = 99,
                    ae[ie[100] = "RESOLVE_BACKEND_REP"] = 100,
                    ae[ie[105] = "WATCH_REQ"] = 105,
                    ae[ie[106] = "WATCH_REP"] = 106,
                    ae[ie[107] = "UNWATCH_REQ"] = 107,
                    ae[ie[108] = "UNWATCH_REP"] = 108,
                    ae[ie[121] = "RESOLVE_IP_REQ"] = 121,
                    ae[ie[122] = "RESOLVE_IP_REP"] = 122,
                    ae
            }(),
                ie.ping_req_t = function () {
                    function ping_req_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return ping_req_t.prototype.ref = 0,
                        ping_req_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        ping_req_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.ping_req_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                if (_e >>> 3 === 15)
                                    de.ref = ie.uint32();
                                else
                                    ie.skipType(7 & _e)
                            }
                            return de
                        }
                        ,
                        ping_req_t
                }(),
                ie.ping_rep_t = function () {
                    function ping_rep_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return ping_rep_t.prototype.ref = 0,
                        ping_rep_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        ping_rep_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.ping_rep_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                if (_e >>> 3 === 15)
                                    de.ref = ie.uint32();
                                else
                                    ie.skipType(7 & _e)
                            }
                            return de
                        }
                        ,
                        ping_rep_t
                }(),
                ie.pull_req_t = function () {
                    function pull_req_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return pull_req_t.prototype.topic = "",
                        pull_req_t.prototype.offset = ye.Long ? ye.Long.fromBits(0, 0, !1) : 0,
                        pull_req_t.prototype.limit = 0,
                        pull_req_t.prototype.puller = 0,
                        pull_req_t.prototype.ref = 0,
                        pull_req_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.topic && Object.hasOwnProperty.call(ie, "topic") && ae.uint32(10).string(ie.topic),
                            null != ie.offset && Object.hasOwnProperty.call(ie, "offset") && ae.uint32(16).int64(ie.offset),
                            null != ie.limit && Object.hasOwnProperty.call(ie, "limit") && ae.uint32(24).uint32(ie.limit),
                            null != ie.puller && Object.hasOwnProperty.call(ie, "puller") && ae.uint32(32).uint32(ie.puller),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        pull_req_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.pull_req_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                switch (_e >>> 3) {
                                    case 1:
                                        de.topic = ie.string();
                                        break;
                                    case 2:
                                        de.offset = ie.int64();
                                        break;
                                    case 3:
                                        de.limit = ie.uint32();
                                        break;
                                    case 4:
                                        de.puller = ie.uint32();
                                        break;
                                    case 15:
                                        de.ref = ie.uint32();
                                        break;
                                    default:
                                        ie.skipType(7 & _e)
                                }
                            }
                            return de
                        }
                        ,
                        pull_req_t
                }(),
                ie.pull_rep_t = function () {
                    function pull_rep_t(ie) {
                        if (this.msgs = [],
                            ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return pull_rep_t.prototype.msgs = ye.emptyArray,
                        pull_rep_t.prototype.ref = 0,
                        pull_rep_t.encode = function encode(ie, ae) {
                            if (ae || (ae = _e.create()),
                            null != ie.msgs && ie.msgs.length)
                                for (var ce = 0; ce < ie.msgs.length; ++ce)
                                    we.maxwell.protocol.msg_t.encode(ie.msgs[ce], ae.uint32(10).fork()).ldelim();
                            return null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        pull_rep_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.pull_rep_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                switch (_e >>> 3) {
                                    case 1:
                                        de.msgs && de.msgs.length || (de.msgs = []),
                                            de.msgs.push(we.maxwell.protocol.msg_t.decode(ie, ie.uint32()));
                                        break;
                                    case 15:
                                        de.ref = ie.uint32();
                                        break;
                                    default:
                                        ie.skipType(7 & _e)
                                }
                            }
                            return de
                        }
                        ,
                        pull_rep_t
                }(),
                ie.push_req_t = function () {
                    function push_req_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return push_req_t.prototype.topic = "",
                        push_req_t.prototype.value = ye.newBuffer([]),
                        push_req_t.prototype.ref = 0,
                        push_req_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.topic && Object.hasOwnProperty.call(ie, "topic") && ae.uint32(10).string(ie.topic),
                            null != ie.value && Object.hasOwnProperty.call(ie, "value") && ae.uint32(18).bytes(ie.value),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        push_req_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.push_req_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                switch (_e >>> 3) {
                                    case 1:
                                        de.topic = ie.string();
                                        break;
                                    case 2:
                                        de.value = ie.bytes();
                                        break;
                                    case 15:
                                        de.ref = ie.uint32();
                                        break;
                                    default:
                                        ie.skipType(7 & _e)
                                }
                            }
                            return de
                        }
                        ,
                        push_req_t
                }(),
                ie.push_rep_t = function () {
                    function push_rep_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return push_rep_t.prototype.ref = 0,
                        push_rep_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        push_rep_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.push_rep_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                if (_e >>> 3 === 15)
                                    de.ref = ie.uint32();
                                else
                                    ie.skipType(7 & _e)
                            }
                            return de
                        }
                        ,
                        push_rep_t
                }(),
                ie.do_req_t = function () {
                    function do_req_t(ie) {
                        if (this.traces = [],
                            ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return do_req_t.prototype.type = "",
                        do_req_t.prototype.value = "",
                        do_req_t.prototype.sourceEnabled = !1,
                        do_req_t.prototype.source = null,
                        do_req_t.prototype.traces = ye.emptyArray,
                        do_req_t.encode = function encode(ie, ae) {
                            if (ae || (ae = _e.create()),
                            null != ie.type && Object.hasOwnProperty.call(ie, "type") && ae.uint32(10).string(ie.type),
                            null != ie.value && Object.hasOwnProperty.call(ie, "value") && ae.uint32(18).string(ie.value),
                            null != ie.sourceEnabled && Object.hasOwnProperty.call(ie, "sourceEnabled") && ae.uint32(104).bool(ie.sourceEnabled),
                            null != ie.source && Object.hasOwnProperty.call(ie, "source") && we.maxwell.protocol.source_t.encode(ie.source, ae.uint32(114).fork()).ldelim(),
                            null != ie.traces && ie.traces.length)
                                for (var ce = 0; ce < ie.traces.length; ++ce)
                                    we.maxwell.protocol.trace_t.encode(ie.traces[ce], ae.uint32(122).fork()).ldelim();
                            return ae
                        }
                        ,
                        do_req_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.do_req_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                switch (_e >>> 3) {
                                    case 1:
                                        de.type = ie.string();
                                        break;
                                    case 2:
                                        de.value = ie.string();
                                        break;
                                    case 13:
                                        de.sourceEnabled = ie.bool();
                                        break;
                                    case 14:
                                        de.source = we.maxwell.protocol.source_t.decode(ie, ie.uint32());
                                        break;
                                    case 15:
                                        de.traces && de.traces.length || (de.traces = []),
                                            de.traces.push(we.maxwell.protocol.trace_t.decode(ie, ie.uint32()));
                                        break;
                                    default:
                                        ie.skipType(7 & _e)
                                }
                            }
                            return de
                        }
                        ,
                        do_req_t
                }(),
                ie.do_rep_t = function () {
                    function do_rep_t(ie) {
                        if (this.traces = [],
                            ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return do_rep_t.prototype.value = "",
                        do_rep_t.prototype.traces = ye.emptyArray,
                        do_rep_t.encode = function encode(ie, ae) {
                            if (ae || (ae = _e.create()),
                            null != ie.value && Object.hasOwnProperty.call(ie, "value") && ae.uint32(10).string(ie.value),
                            null != ie.traces && ie.traces.length)
                                for (var ce = 0; ce < ie.traces.length; ++ce)
                                    we.maxwell.protocol.trace_t.encode(ie.traces[ce], ae.uint32(122).fork()).ldelim();
                            return ae
                        }
                        ,
                        do_rep_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.do_rep_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                switch (_e >>> 3) {
                                    case 1:
                                        de.value = ie.string();
                                        break;
                                    case 15:
                                        de.traces && de.traces.length || (de.traces = []),
                                            de.traces.push(we.maxwell.protocol.trace_t.decode(ie, ie.uint32()));
                                        break;
                                    default:
                                        ie.skipType(7 & _e)
                                }
                            }
                            return de
                        }
                        ,
                        do_rep_t
                }(),
                ie.do2_req_t = function () {
                    function do2_req_t(ie) {
                        if (this.traces = [],
                            ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return do2_req_t.prototype.type = "",
                        do2_req_t.prototype.sourceEnabled = !1,
                        do2_req_t.prototype.source = null,
                        do2_req_t.prototype.traces = ye.emptyArray,
                        do2_req_t.encode = function encode(ie, ae) {
                            if (ae || (ae = _e.create()),
                            null != ie.type && Object.hasOwnProperty.call(ie, "type") && ae.uint32(10).string(ie.type),
                            null != ie.sourceEnabled && Object.hasOwnProperty.call(ie, "sourceEnabled") && ae.uint32(104).bool(ie.sourceEnabled),
                            null != ie.source && Object.hasOwnProperty.call(ie, "source") && we.maxwell.protocol.source_t.encode(ie.source, ae.uint32(114).fork()).ldelim(),
                            null != ie.traces && ie.traces.length)
                                for (var ce = 0; ce < ie.traces.length; ++ce)
                                    we.maxwell.protocol.trace_t.encode(ie.traces[ce], ae.uint32(122).fork()).ldelim();
                            return ae
                        }
                        ,
                        do2_req_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.do2_req_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                switch (_e >>> 3) {
                                    case 1:
                                        de.type = ie.string();
                                        break;
                                    case 13:
                                        de.sourceEnabled = ie.bool();
                                        break;
                                    case 14:
                                        de.source = we.maxwell.protocol.source_t.decode(ie, ie.uint32());
                                        break;
                                    case 15:
                                        de.traces && de.traces.length || (de.traces = []),
                                            de.traces.push(we.maxwell.protocol.trace_t.decode(ie, ie.uint32()));
                                        break;
                                    default:
                                        ie.skipType(7 & _e)
                                }
                            }
                            return de
                        }
                        ,
                        do2_req_t
                }(),
                ie.do2_rep_t = function () {
                    function do2_rep_t(ie) {
                        if (this.traces = [],
                            ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return do2_rep_t.prototype.value = ye.newBuffer([]),
                        do2_rep_t.prototype.traces = ye.emptyArray,
                        do2_rep_t.encode = function encode(ie, ae) {
                            if (ae || (ae = _e.create()),
                            null != ie.value && Object.hasOwnProperty.call(ie, "value") && ae.uint32(10).bytes(ie.value),
                            null != ie.traces && ie.traces.length)
                                for (var ce = 0; ce < ie.traces.length; ++ce)
                                    we.maxwell.protocol.trace_t.encode(ie.traces[ce], ae.uint32(122).fork()).ldelim();
                            return ae
                        }
                        ,
                        do2_rep_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.do2_rep_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                switch (_e >>> 3) {
                                    case 1:
                                        de.value = ie.bytes();
                                        break;
                                    case 15:
                                        de.traces && de.traces.length || (de.traces = []),
                                            de.traces.push(we.maxwell.protocol.trace_t.decode(ie, ie.uint32()));
                                        break;
                                    default:
                                        ie.skipType(7 & _e)
                                }
                            }
                            return de
                        }
                        ,
                        do2_rep_t
                }(),
                ie.auth_req_t = function () {
                    function auth_req_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return auth_req_t.prototype.token = "",
                        auth_req_t.prototype.ref = 0,
                        auth_req_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.token && Object.hasOwnProperty.call(ie, "token") && ae.uint32(10).string(ie.token),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        auth_req_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.auth_req_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                switch (_e >>> 3) {
                                    case 1:
                                        de.token = ie.string();
                                        break;
                                    case 15:
                                        de.ref = ie.uint32();
                                        break;
                                    default:
                                        ie.skipType(7 & _e)
                                }
                            }
                            return de
                        }
                        ,
                        auth_req_t
                }(),
                ie.auth_rep_t = function () {
                    function auth_rep_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return auth_rep_t.prototype.ref = 0,
                        auth_rep_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        auth_rep_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.auth_rep_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                if (_e >>> 3 === 15)
                                    de.ref = ie.uint32();
                                else
                                    ie.skipType(7 & _e)
                            }
                            return de
                        }
                        ,
                        auth_rep_t
                }(),
                ie.ok_rep_t = function () {
                    function ok_rep_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return ok_rep_t.prototype.ref = 0,
                        ok_rep_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        ok_rep_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.ok_rep_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                if (_e >>> 3 === 15)
                                    de.ref = ie.uint32();
                                else
                                    ie.skipType(7 & _e)
                            }
                            return de
                        }
                        ,
                        ok_rep_t
                }(),
                ie.error_rep_t = function () {
                    function error_rep_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return error_rep_t.prototype.code = 0,
                        error_rep_t.prototype.desc = "",
                        error_rep_t.prototype.ref = 0,
                        error_rep_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.code && Object.hasOwnProperty.call(ie, "code") && ae.uint32(8).int32(ie.code),
                            null != ie.desc && Object.hasOwnProperty.call(ie, "desc") && ae.uint32(18).string(ie.desc),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        error_rep_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.error_rep_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                switch (_e >>> 3) {
                                    case 1:
                                        de.code = ie.int32();
                                        break;
                                    case 2:
                                        de.desc = ie.string();
                                        break;
                                    case 15:
                                        de.ref = ie.uint32();
                                        break;
                                    default:
                                        ie.skipType(7 & _e)
                                }
                            }
                            return de
                        }
                        ,
                        error_rep_t
                }(),
                ie.ok2_rep_t = function () {
                    function ok2_rep_t(ie) {
                        if (this.traces = [],
                            ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return ok2_rep_t.prototype.traces = ye.emptyArray,
                        ok2_rep_t.encode = function encode(ie, ae) {
                            if (ae || (ae = _e.create()),
                            null != ie.traces && ie.traces.length)
                                for (var ce = 0; ce < ie.traces.length; ++ce)
                                    we.maxwell.protocol.trace_t.encode(ie.traces[ce], ae.uint32(122).fork()).ldelim();
                            return ae
                        }
                        ,
                        ok2_rep_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.ok2_rep_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                if (_e >>> 3 === 15)
                                    de.traces && de.traces.length || (de.traces = []),
                                        de.traces.push(we.maxwell.protocol.trace_t.decode(ie, ie.uint32()));
                                else
                                    ie.skipType(7 & _e)
                            }
                            return de
                        }
                        ,
                        ok2_rep_t
                }(),
                ie.error2_rep_t = function () {
                    function error2_rep_t(ie) {
                        if (this.traces = [],
                            ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return error2_rep_t.prototype.code = 0,
                        error2_rep_t.prototype.desc = "",
                        error2_rep_t.prototype.traces = ye.emptyArray,
                        error2_rep_t.encode = function encode(ie, ae) {
                            if (ae || (ae = _e.create()),
                            null != ie.code && Object.hasOwnProperty.call(ie, "code") && ae.uint32(8).int32(ie.code),
                            null != ie.desc && Object.hasOwnProperty.call(ie, "desc") && ae.uint32(18).string(ie.desc),
                            null != ie.traces && ie.traces.length)
                                for (var ce = 0; ce < ie.traces.length; ++ce)
                                    we.maxwell.protocol.trace_t.encode(ie.traces[ce], ae.uint32(122).fork()).ldelim();
                            return ae
                        }
                        ,
                        error2_rep_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.error2_rep_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                switch (_e >>> 3) {
                                    case 1:
                                        de.code = ie.int32();
                                        break;
                                    case 2:
                                        de.desc = ie.string();
                                        break;
                                    case 15:
                                        de.traces && de.traces.length || (de.traces = []),
                                            de.traces.push(we.maxwell.protocol.trace_t.decode(ie, ie.uint32()));
                                        break;
                                    default:
                                        ie.skipType(7 & _e)
                                }
                            }
                            return de
                        }
                        ,
                        error2_rep_t
                }(),
                ie.watch_req_t = function () {
                    function watch_req_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return watch_req_t.prototype.type = "",
                        watch_req_t.prototype.ref = 0,
                        watch_req_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.type && Object.hasOwnProperty.call(ie, "type") && ae.uint32(10).string(ie.type),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        watch_req_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.watch_req_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                switch (_e >>> 3) {
                                    case 1:
                                        de.type = ie.string();
                                        break;
                                    case 15:
                                        de.ref = ie.uint32();
                                        break;
                                    default:
                                        ie.skipType(7 & _e)
                                }
                            }
                            return de
                        }
                        ,
                        watch_req_t
                }(),
                ie.watch_rep_t = function () {
                    function watch_rep_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return watch_rep_t.prototype.ref = 0,
                        watch_rep_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        watch_rep_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.watch_rep_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                if (_e >>> 3 === 15)
                                    de.ref = ie.uint32();
                                else
                                    ie.skipType(7 & _e)
                            }
                            return de
                        }
                        ,
                        watch_rep_t
                }(),
                ie.unwatch_req_t = function () {
                    function unwatch_req_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return unwatch_req_t.prototype.type = "",
                        unwatch_req_t.prototype.ref = 0,
                        unwatch_req_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.type && Object.hasOwnProperty.call(ie, "type") && ae.uint32(10).string(ie.type),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        unwatch_req_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.unwatch_req_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                switch (_e >>> 3) {
                                    case 1:
                                        de.type = ie.string();
                                        break;
                                    case 15:
                                        de.ref = ie.uint32();
                                        break;
                                    default:
                                        ie.skipType(7 & _e)
                                }
                            }
                            return de
                        }
                        ,
                        unwatch_req_t
                }(),
                ie.unwatch_rep_t = function () {
                    function unwatch_rep_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return unwatch_rep_t.prototype.ref = 0,
                        unwatch_rep_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        unwatch_rep_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.unwatch_rep_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                if (_e >>> 3 === 15)
                                    de.ref = ie.uint32();
                                else
                                    ie.skipType(7 & _e)
                            }
                            return de
                        }
                        ,
                        unwatch_rep_t
                }(),
                ie.register_frontend_req_t = function () {
                    function register_frontend_req_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return register_frontend_req_t.prototype.endpoint = "",
                        register_frontend_req_t.prototype.ref = 0,
                        register_frontend_req_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.endpoint && Object.hasOwnProperty.call(ie, "endpoint") && ae.uint32(10).string(ie.endpoint),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        register_frontend_req_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.register_frontend_req_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                switch (_e >>> 3) {
                                    case 1:
                                        de.endpoint = ie.string();
                                        break;
                                    case 15:
                                        de.ref = ie.uint32();
                                        break;
                                    default:
                                        ie.skipType(7 & _e)
                                }
                            }
                            return de
                        }
                        ,
                        register_frontend_req_t
                }(),
                ie.register_frontend_rep_t = function () {
                    function register_frontend_rep_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return register_frontend_rep_t.prototype.ref = 0,
                        register_frontend_rep_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        register_frontend_rep_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.register_frontend_rep_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                if (_e >>> 3 === 15)
                                    de.ref = ie.uint32();
                                else
                                    ie.skipType(7 & _e)
                            }
                            return de
                        }
                        ,
                        register_frontend_rep_t
                }(),
                ie.add_route_req_t = function () {
                    function add_route_req_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return add_route_req_t.prototype.type = "",
                        add_route_req_t.prototype.ref = 0,
                        add_route_req_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.type && Object.hasOwnProperty.call(ie, "type") && ae.uint32(10).string(ie.type),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        add_route_req_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.add_route_req_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                switch (_e >>> 3) {
                                    case 1:
                                        de.type = ie.string();
                                        break;
                                    case 15:
                                        de.ref = ie.uint32();
                                        break;
                                    default:
                                        ie.skipType(7 & _e)
                                }
                            }
                            return de
                        }
                        ,
                        add_route_req_t
                }(),
                ie.add_route_rep_t = function () {
                    function add_route_rep_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return add_route_rep_t.prototype.ref = 0,
                        add_route_rep_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        add_route_rep_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.add_route_rep_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                if (_e >>> 3 === 15)
                                    de.ref = ie.uint32();
                                else
                                    ie.skipType(7 & _e)
                            }
                            return de
                        }
                        ,
                        add_route_rep_t
                }(),
                ie.delete_route_req_t = function () {
                    function delete_route_req_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return delete_route_req_t.prototype.type = "",
                        delete_route_req_t.prototype.ref = 0,
                        delete_route_req_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.type && Object.hasOwnProperty.call(ie, "type") && ae.uint32(10).string(ie.type),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        delete_route_req_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.delete_route_req_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                switch (_e >>> 3) {
                                    case 1:
                                        de.type = ie.string();
                                        break;
                                    case 15:
                                        de.ref = ie.uint32();
                                        break;
                                    default:
                                        ie.skipType(7 & _e)
                                }
                            }
                            return de
                        }
                        ,
                        delete_route_req_t
                }(),
                ie.delete_route_rep_t = function () {
                    function delete_route_rep_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return delete_route_rep_t.prototype.ref = 0,
                        delete_route_rep_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        delete_route_rep_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.delete_route_rep_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                if (_e >>> 3 === 15)
                                    de.ref = ie.uint32();
                                else
                                    ie.skipType(7 & _e)
                            }
                            return de
                        }
                        ,
                        delete_route_rep_t
                }(),
                ie.add_route_msg_t = function () {
                    function add_route_msg_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return add_route_msg_t.prototype.endpoint = "",
                        add_route_msg_t.prototype.ref = 0,
                        add_route_msg_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.endpoint && Object.hasOwnProperty.call(ie, "endpoint") && ae.uint32(10).string(ie.endpoint),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        add_route_msg_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.add_route_msg_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                switch (_e >>> 3) {
                                    case 1:
                                        de.endpoint = ie.string();
                                        break;
                                    case 15:
                                        de.ref = ie.uint32();
                                        break;
                                    default:
                                        ie.skipType(7 & _e)
                                }
                            }
                            return de
                        }
                        ,
                        add_route_msg_t
                }(),
                ie.delete_route_msg_t = function () {
                    function delete_route_msg_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return delete_route_msg_t.prototype.type = "",
                        delete_route_msg_t.prototype.endpoint = "",
                        delete_route_msg_t.prototype.ref = 0,
                        delete_route_msg_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.type && Object.hasOwnProperty.call(ie, "type") && ae.uint32(10).string(ie.type),
                            null != ie.endpoint && Object.hasOwnProperty.call(ie, "endpoint") && ae.uint32(18).string(ie.endpoint),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        delete_route_msg_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.delete_route_msg_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                switch (_e >>> 3) {
                                    case 1:
                                        de.type = ie.string();
                                        break;
                                    case 2:
                                        de.endpoint = ie.string();
                                        break;
                                    case 15:
                                        de.ref = ie.uint32();
                                        break;
                                    default:
                                        ie.skipType(7 & _e)
                                }
                            }
                            return de
                        }
                        ,
                        delete_route_msg_t
                }(),
                ie.push_routes_req_t = function () {
                    function push_routes_req_t(ie) {
                        if (this.types = [],
                            ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return push_routes_req_t.prototype.types = ye.emptyArray,
                        push_routes_req_t.prototype.ref = 0,
                        push_routes_req_t.encode = function encode(ie, ae) {
                            if (ae || (ae = _e.create()),
                            null != ie.types && ie.types.length)
                                for (var ce = 0; ce < ie.types.length; ++ce)
                                    ae.uint32(10).string(ie.types[ce]);
                            return null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        push_routes_req_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.push_routes_req_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                switch (_e >>> 3) {
                                    case 1:
                                        de.types && de.types.length || (de.types = []),
                                            de.types.push(ie.string());
                                        break;
                                    case 15:
                                        de.ref = ie.uint32();
                                        break;
                                    default:
                                        ie.skipType(7 & _e)
                                }
                            }
                            return de
                        }
                        ,
                        push_routes_req_t
                }(),
                ie.push_routes_rep_t = function () {
                    function push_routes_rep_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return push_routes_rep_t.prototype.ref = 0,
                        push_routes_rep_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        push_routes_rep_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.push_routes_rep_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                if (_e >>> 3 === 15)
                                    de.ref = ie.uint32();
                                else
                                    ie.skipType(7 & _e)
                            }
                            return de
                        }
                        ,
                        push_routes_rep_t
                }(),
                ie.pull_routes_req_t = function () {
                    function pull_routes_req_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return pull_routes_req_t.prototype.ref = 0,
                        pull_routes_req_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        pull_routes_req_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.pull_routes_req_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                if (_e >>> 3 === 15)
                                    de.ref = ie.uint32();
                                else
                                    ie.skipType(7 & _e)
                            }
                            return de
                        }
                        ,
                        pull_routes_req_t
                }(),
                ie.pull_routes_rep_t = function () {
                    function pull_routes_rep_t(ie) {
                        if (this.routeGroups = [],
                            ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return pull_routes_rep_t.prototype.routeGroups = ye.emptyArray,
                        pull_routes_rep_t.prototype.ref = 0,
                        pull_routes_rep_t.encode = function encode(ie, ae) {
                            if (ae || (ae = _e.create()),
                            null != ie.routeGroups && ie.routeGroups.length)
                                for (var ce = 0; ce < ie.routeGroups.length; ++ce)
                                    we.maxwell.protocol.route_group_t.encode(ie.routeGroups[ce], ae.uint32(10).fork()).ldelim();
                            return null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        pull_routes_rep_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.pull_routes_rep_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                switch (_e >>> 3) {
                                    case 1:
                                        de.routeGroups && de.routeGroups.length || (de.routeGroups = []),
                                            de.routeGroups.push(we.maxwell.protocol.route_group_t.decode(ie, ie.uint32()));
                                        break;
                                    case 15:
                                        de.ref = ie.uint32();
                                        break;
                                    default:
                                        ie.skipType(7 & _e)
                                }
                            }
                            return de
                        }
                        ,
                        pull_routes_rep_t
                }(),
                ie.delete_topics_req_t = function () {
                    function delete_topics_req_t(ie) {
                        if (this.topics = [],
                            ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return delete_topics_req_t.prototype.topics = ye.emptyArray,
                        delete_topics_req_t.prototype.ref = 0,
                        delete_topics_req_t.encode = function encode(ie, ae) {
                            if (ae || (ae = _e.create()),
                            null != ie.topics && ie.topics.length)
                                for (var ce = 0; ce < ie.topics.length; ++ce)
                                    ae.uint32(10).string(ie.topics[ce]);
                            return null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        delete_topics_req_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.delete_topics_req_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                switch (_e >>> 3) {
                                    case 1:
                                        de.topics && de.topics.length || (de.topics = []),
                                            de.topics.push(ie.string());
                                        break;
                                    case 15:
                                        de.ref = ie.uint32();
                                        break;
                                    default:
                                        ie.skipType(7 & _e)
                                }
                            }
                            return de
                        }
                        ,
                        delete_topics_req_t
                }(),
                ie.delete_topics_rep_t = function () {
                    function delete_topics_rep_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return delete_topics_rep_t.prototype.ref = 0,
                        delete_topics_rep_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        delete_topics_rep_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.delete_topics_rep_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                if (_e >>> 3 === 15)
                                    de.ref = ie.uint32();
                                else
                                    ie.skipType(7 & _e)
                            }
                            return de
                        }
                        ,
                        delete_topics_rep_t
                }(),
                ie.register_backend_req_t = function () {
                    function register_backend_req_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return register_backend_req_t.prototype.endpoint = "",
                        register_backend_req_t.prototype.ref = 0,
                        register_backend_req_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.endpoint && Object.hasOwnProperty.call(ie, "endpoint") && ae.uint32(10).string(ie.endpoint),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        register_backend_req_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.register_backend_req_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                switch (_e >>> 3) {
                                    case 1:
                                        de.endpoint = ie.string();
                                        break;
                                    case 15:
                                        de.ref = ie.uint32();
                                        break;
                                    default:
                                        ie.skipType(7 & _e)
                                }
                            }
                            return de
                        }
                        ,
                        register_backend_req_t
                }(),
                ie.register_backend_rep_t = function () {
                    function register_backend_rep_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return register_backend_rep_t.prototype.ref = 0,
                        register_backend_rep_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        register_backend_rep_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.register_backend_rep_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                if (_e >>> 3 === 15)
                                    de.ref = ie.uint32();
                                else
                                    ie.skipType(7 & _e)
                            }
                            return de
                        }
                        ,
                        register_backend_rep_t
                }(),
                ie.resolve_frontend_req_t = function () {
                    function resolve_frontend_req_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return resolve_frontend_req_t.prototype.ref = 0,
                        resolve_frontend_req_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        resolve_frontend_req_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.resolve_frontend_req_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                if (_e >>> 3 === 15)
                                    de.ref = ie.uint32();
                                else
                                    ie.skipType(7 & _e)
                            }
                            return de
                        }
                        ,
                        resolve_frontend_req_t
                }(),
                ie.resolve_frontend_rep_t = function () {
                    function resolve_frontend_rep_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return resolve_frontend_rep_t.prototype.endpoint = "",
                        resolve_frontend_rep_t.prototype.ref = 0,
                        resolve_frontend_rep_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.endpoint && Object.hasOwnProperty.call(ie, "endpoint") && ae.uint32(10).string(ie.endpoint),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        resolve_frontend_rep_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.resolve_frontend_rep_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                switch (_e >>> 3) {
                                    case 1:
                                        de.endpoint = ie.string();
                                        break;
                                    case 15:
                                        de.ref = ie.uint32();
                                        break;
                                    default:
                                        ie.skipType(7 & _e)
                                }
                            }
                            return de
                        }
                        ,
                        resolve_frontend_rep_t
                }(),
                ie.resolve_backend_req_t = function () {
                    function resolve_backend_req_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return resolve_backend_req_t.prototype.topic = "",
                        resolve_backend_req_t.prototype.ref = 0,
                        resolve_backend_req_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.topic && Object.hasOwnProperty.call(ie, "topic") && ae.uint32(10).string(ie.topic),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        resolve_backend_req_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.resolve_backend_req_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                switch (_e >>> 3) {
                                    case 1:
                                        de.topic = ie.string();
                                        break;
                                    case 15:
                                        de.ref = ie.uint32();
                                        break;
                                    default:
                                        ie.skipType(7 & _e)
                                }
                            }
                            return de
                        }
                        ,
                        resolve_backend_req_t
                }(),
                ie.resolve_backend_rep_t = function () {
                    function resolve_backend_rep_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return resolve_backend_rep_t.prototype.endpoint = "",
                        resolve_backend_rep_t.prototype.ref = 0,
                        resolve_backend_rep_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.endpoint && Object.hasOwnProperty.call(ie, "endpoint") && ae.uint32(10).string(ie.endpoint),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        resolve_backend_rep_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.resolve_backend_rep_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                switch (_e >>> 3) {
                                    case 1:
                                        de.endpoint = ie.string();
                                        break;
                                    case 15:
                                        de.ref = ie.uint32();
                                        break;
                                    default:
                                        ie.skipType(7 & _e)
                                }
                            }
                            return de
                        }
                        ,
                        resolve_backend_rep_t
                }(),
                ie.resolve_ip_req_t = function () {
                    function resolve_ip_req_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return resolve_ip_req_t.prototype.ref = 0,
                        resolve_ip_req_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        resolve_ip_req_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.resolve_ip_req_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                if (_e >>> 3 === 15)
                                    de.ref = ie.uint32();
                                else
                                    ie.skipType(7 & _e)
                            }
                            return de
                        }
                        ,
                        resolve_ip_req_t
                }(),
                ie.resolve_ip_rep_t = function () {
                    function resolve_ip_rep_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return resolve_ip_rep_t.prototype.ip = "",
                        resolve_ip_rep_t.prototype.ref = 0,
                        resolve_ip_rep_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.ip && Object.hasOwnProperty.call(ie, "ip") && ae.uint32(10).string(ie.ip),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(120).uint32(ie.ref),
                                ae
                        }
                        ,
                        resolve_ip_rep_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.resolve_ip_rep_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                switch (_e >>> 3) {
                                    case 1:
                                        de.ip = ie.string();
                                        break;
                                    case 15:
                                        de.ref = ie.uint32();
                                        break;
                                    default:
                                        ie.skipType(7 & _e)
                                }
                            }
                            return de
                        }
                        ,
                        resolve_ip_rep_t
                }(),
                ie.msg_t = function () {
                    function msg_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return msg_t.prototype.offset = ye.Long ? ye.Long.fromBits(0, 0, !0) : 0,
                        msg_t.prototype.value = ye.newBuffer([]),
                        msg_t.prototype.timestamp = ye.Long ? ye.Long.fromBits(0, 0, !0) : 0,
                        msg_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.offset && Object.hasOwnProperty.call(ie, "offset") && ae.uint32(8).uint64(ie.offset),
                            null != ie.value && Object.hasOwnProperty.call(ie, "value") && ae.uint32(18).bytes(ie.value),
                            null != ie.timestamp && Object.hasOwnProperty.call(ie, "timestamp") && ae.uint32(24).uint64(ie.timestamp),
                                ae
                        }
                        ,
                        msg_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.msg_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                switch (_e >>> 3) {
                                    case 1:
                                        de.offset = ie.uint64();
                                        break;
                                    case 2:
                                        de.value = ie.bytes();
                                        break;
                                    case 3:
                                        de.timestamp = ie.uint64();
                                        break;
                                    default:
                                        ie.skipType(7 & _e)
                                }
                            }
                            return de
                        }
                        ,
                        msg_t
                }(),
                ie.source_t = function () {
                    function source_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return source_t.prototype.agent = "",
                        source_t.prototype.endpoint = "",
                        source_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.agent && Object.hasOwnProperty.call(ie, "agent") && ae.uint32(10).string(ie.agent),
                            null != ie.endpoint && Object.hasOwnProperty.call(ie, "endpoint") && ae.uint32(18).string(ie.endpoint),
                                ae
                        }
                        ,
                        source_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.source_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                switch (_e >>> 3) {
                                    case 1:
                                        de.agent = ie.string();
                                        break;
                                    case 2:
                                        de.endpoint = ie.string();
                                        break;
                                    default:
                                        ie.skipType(7 & _e)
                                }
                            }
                            return de
                        }
                        ,
                        source_t
                }(),
                ie.trace_t = function () {
                    function trace_t(ie) {
                        if (ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return trace_t.prototype.ref = 0,
                        trace_t.prototype.handlerId = 0,
                        trace_t.prototype.nodeId = ye.newBuffer([]),
                        trace_t.encode = function encode(ie, ae) {
                            return ae || (ae = _e.create()),
                            null != ie.ref && Object.hasOwnProperty.call(ie, "ref") && ae.uint32(8).uint32(ie.ref),
                            null != ie.handlerId && Object.hasOwnProperty.call(ie, "handlerId") && ae.uint32(16).uint32(ie.handlerId),
                            null != ie.nodeId && Object.hasOwnProperty.call(ie, "nodeId") && ae.uint32(26).bytes(ie.nodeId),
                                ae
                        }
                        ,
                        trace_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.trace_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                switch (_e >>> 3) {
                                    case 1:
                                        de.ref = ie.uint32();
                                        break;
                                    case 2:
                                        de.handlerId = ie.uint32();
                                        break;
                                    case 3:
                                        de.nodeId = ie.bytes();
                                        break;
                                    default:
                                        ie.skipType(7 & _e)
                                }
                            }
                            return de
                        }
                        ,
                        trace_t
                }(),
                ie.route_group_t = function () {
                    function route_group_t(ie) {
                        if (this.endpoints = [],
                            ie)
                            for (var ae = Object.keys(ie), ce = 0; ce < ae.length; ++ce)
                                null != ie[ae[ce]] && (this[ae[ce]] = ie[ae[ce]])
                    }

                    return route_group_t.prototype.type = "",
                        route_group_t.prototype.endpoints = ye.emptyArray,
                        route_group_t.encode = function encode(ie, ae) {
                            if (ae || (ae = _e.create()),
                            null != ie.type && Object.hasOwnProperty.call(ie, "type") && ae.uint32(10).string(ie.type),
                            null != ie.endpoints && ie.endpoints.length)
                                for (var ce = 0; ce < ie.endpoints.length; ++ce)
                                    ae.uint32(18).string(ie.endpoints[ce]);
                            return ae
                        }
                        ,
                        route_group_t.decode = function decode(ie, ae) {
                            ie instanceof be || (ie = be.create(ie));
                            for (var ce = void 0 === ae ? ie.len : ie.pos + ae, de = new we.maxwell.protocol.route_group_t; ie.pos < ce;) {
                                var _e = ie.uint32();
                                switch (_e >>> 3) {
                                    case 1:
                                        de.type = ie.string();
                                        break;
                                    case 2:
                                        de.endpoints && de.endpoints.length || (de.endpoints = []),
                                            de.endpoints.push(ie.string());
                                        break;
                                    default:
                                        ie.skipType(7 & _e)
                                }
                            }
                            return de
                        }
                        ,
                        route_group_t
                }(),
                ie
        }(),
            ie
    }(),
        ie.exports = we
}


var Writer = function (){
        // ie.exports = Writer;
        // var de, be = ce(99693), _e = be.LongBits, ye = be.base64, we = be.utf8;
        function Op(ie, ae, ce) {
            this.fn = ie,
            this.len = ae,
            this.next = void 0,
            this.val = ce
        }
        function noop() {}
        function State(ie) {
            this.head = ie.head,
            this.tail = ie.tail,
            this.len = ie.len,
            this.next = ie.states
        }
        function Writer() {
            this.len = 0,
            this.head = new Op(noop,0,0),
            this.tail = this.head,
            this.states = null
        }
        var Se = function create() {
            return be.Buffer ? function create_buffer_setup() {
                return (Writer.create = function create_buffer() {
                    return new de
                }
                )()
            }
            : function create_array() {
                return new Writer
            }
        };
        function writeByte(ie, ae, ce) {
            ae[ce] = 255 & ie
        }
        function VarintOp(ie, ae) {
            this.len = ie,
            this.next = void 0,
            this.val = ae
        }
        function writeVarint64(ie, ae, ce) {
            for (; ie.hi; )
                ae[ce++] = 127 & ie.lo | 128,
                ie.lo = (ie.lo >>> 7 | ie.hi << 25) >>> 0,
                ie.hi >>>= 7;
            for (; ie.lo > 127; )
                ae[ce++] = 127 & ie.lo | 128,
                ie.lo = ie.lo >>> 7;
            ae[ce++] = ie.lo
        }
        function writeFixed32(ie, ae, ce) {
            ae[ce] = 255 & ie,
            ae[ce + 1] = ie >>> 8 & 255,
            ae[ce + 2] = ie >>> 16 & 255,
            ae[ce + 3] = ie >>> 24
        }
        Writer.create = Se(),
        Writer.alloc = function alloc(ie) {
            return new be.Array(ie)
        }
        ,
        be.Array !== Array && (Writer.alloc = be.pool(Writer.alloc, be.Array.prototype.subarray)),
        Writer.prototype._push = function push(ie, ae, ce) {
            return this.tail = this.tail.next = new Op(ie,ae,ce),
            this.len += ae,
            this
        }
        ,
        VarintOp.prototype = Object.create(Op.prototype),
        VarintOp.prototype.fn = function writeVarint32(ie, ae, ce) {
            for (; ie > 127; )
                ae[ce++] = 127 & ie | 128,
                ie >>>= 7;
            ae[ce] = ie
        }
        ,
        Writer.prototype.uint32 = function write_uint32(ie) {
            return this.len += (this.tail = this.tail.next = new VarintOp((ie >>>= 0) < 128 ? 1 : ie < 16384 ? 2 : ie < 2097152 ? 3 : ie < 268435456 ? 4 : 5,ie)).len,
            this
        }
        ,
        Writer.prototype.int32 = function write_int32(ie) {
            return ie < 0 ? this._push(writeVarint64, 10, _e.fromNumber(ie)) : this.uint32(ie)
        }
        ,
        Writer.prototype.sint32 = function write_sint32(ie) {
            return this.uint32((ie << 1 ^ ie >> 31) >>> 0)
        }
        ,
        Writer.prototype.uint64 = function write_uint64(ie) {
            var ae = _e.from(ie);
            return this._push(writeVarint64, ae.length(), ae)
        }
        ,
        Writer.prototype.int64 = Writer.prototype.uint64,
        Writer.prototype.sint64 = function write_sint64(ie) {
            var ae = _e.from(ie).zzEncode();
            return this._push(writeVarint64, ae.length(), ae)
        }
        ,
        Writer.prototype.bool = function write_bool(ie) {
            return this._push(writeByte, 1, ie ? 1 : 0)
        }
        ,
        Writer.prototype.fixed32 = function write_fixed32(ie) {
            return this._push(writeFixed32, 4, ie >>> 0)
        }
        ,
        Writer.prototype.sfixed32 = Writer.prototype.fixed32,
        Writer.prototype.fixed64 = function write_fixed64(ie) {
            var ae = _e.from(ie);
            return this._push(writeFixed32, 4, ae.lo)._push(writeFixed32, 4, ae.hi)
        }
        ,
        Writer.prototype.sfixed64 = Writer.prototype.fixed64,
        Writer.prototype.float = function write_float(ie) {
            return this._push(be.float.writeFloatLE, 4, ie)
        }
        ,
        Writer.prototype.double = function write_double(ie) {
            return this._push(be.float.writeDoubleLE, 8, ie)
        }
        ;
        var xe = be.Array.prototype.set ? function writeBytes_set(ie, ae, ce) {
            ae.set(ie, ce)
        }
        : function writeBytes_for(ie, ae, ce) {
            for (var de = 0; de < ie.length; ++de)
                ae[ce + de] = ie[de]
        }
        ;
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
        ,
        Writer.prototype.string = function write_string(ie) {
            var ae = we.length(ie);
            return ae ? this.uint32(ae)._push(we.write, ae, ie) : this._push(writeByte, 1, 0)
        }
        ,
        Writer.prototype.fork = function fork() {
            return this.states = new State(this),
            this.head = this.tail = new Op(noop,0,0),
            this.len = 0,
            this
        }
        ,
        Writer.prototype.reset = function reset() {
            return this.states ? (this.head = this.states.head,
            this.tail = this.states.tail,
            this.len = this.states.len,
            this.states = this.states.next) : (this.head = this.tail = new Op(noop,0,0),
            this.len = 0),
            this
        }
        ,
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
        ,
        Writer.prototype.finish = function finish() {
            for (var ie = this.head.next, ae = this.constructor.alloc(this.len), ce = 0; ie; )
                ie.fn(ie.val, ae, ce),
                ce += ie.len,
                ie = ie.next;
            return ae
        }
        ,
        Writer._configure = function(ie) {
            de = ie,
            Writer.create = Se(),
            de._configure()
        }
    }
