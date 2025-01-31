/*
    Licensed to the Apache Software Foundation (ASF) under one
    or more contributor license agreements.  See the NOTICE file
    distributed with this work for additional information
    regarding copyright ownership.  The ASF licenses this file
    to you under the Apache License, Version 2.0 (the
    "License"); you may not use this file except in compliance
    with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing,
    software distributed under the License is distributed on an
    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
*/

/* BLS API Functions */

var BLS256 = function(ctx) {
  "use strict";

  var BLS256 = {
    BLS_OK: 0,
    BLS_FAIL: -1,

    BFS: ctx.BIG.MODBYTES,
    BGS: ctx.BIG.MODBYTES,

    bytestostring: function(b) {
      var s = "",
        len = b.length,
        ch,
        i;

      for (i = 0; i < len; i++) {
        ch = b[i];
        s += ((ch >>> 4) & 15).toString(16);
        s += (ch & 15).toString(16);
      }

      return s;
    },

    stringtobytes: function(s) {
        var b = [],
                i;

        for (i = 0; i < s.length; i+=2) {
            b.push(parseInt(s.substr(i,2),16));
        }

        return b;
    },

    /* hash a message to an ECP point, using SHA3 */

    bls_hashit: function(m) {
      var sh = new ctx.SHA3(ctx.SHA3.SHAKE256);
      var hm = [];
      var t = this.stringtobytes(m);
      for (var i = 0; i < t.length; i++) sh.process(t[i]);
      sh.shake(hm, this.BFS);
      var P = ctx.ECP.mapit(hm);
      return P;
    },

    /* generate key pair, private key S, public key W */

    KeyPairGenerate: function(rng, S, W) {
      var G = ctx.ECP8.generator();
      var q = new ctx.BIG(0);
      q.rcopy(ctx.ROM_CURVE.CURVE_Order);
      var s = ctx.BIG.randomnum(q, rng);
      s.toBytes(S);
      G = ctx.PAIR256.G2mul(G, s);
      G.toBytes(W); // To use point compression on public keys, change to true
      return this.BLS_OK;
    },

    /* Sign message m using private key S to produce signature SIG */

    sign: function(SIG, m, S) {
      var D = this.bls_hashit(m);
      var s = ctx.BIG.fromBytes(S);
      D = ctx.PAIR256.G1mul(D, s);
      D.toBytes(SIG, true);
      return this.BLS_OK;
    },

    /* Verify signature given message m, the signature SIG, and the public key W */

    verify: function(SIG, m, W) {
      var HM = this.bls_hashit(m);
      var D = ctx.ECP.fromBytes(SIG);
      var G = ctx.ECP8.generator();
      var PK = ctx.ECP8.fromBytes(W);
      D.neg();

      // Use new multi-pairing mechanism
      var r = ctx.PAIR256.initmp();
      ctx.PAIR256.another(r, G, D);
      ctx.PAIR256.another(r, PK, HM);
      var v = ctx.PAIR256.miller(r);

      //.. or alternatively
      //			var v=ctx.PAIR256.ate2(G,D,PK,HM);

      v = ctx.PAIR256.fexp(v);
      if (v.isunity()) return this.BLS_OK;
      return this.BLS_FAIL;
    },
  };

  return BLS256;
};

// CommonJS module exports
if (typeof module !== "undefined" && typeof module.exports !== "undefined") {
  module.exports.BLS256 = BLS256;
}
