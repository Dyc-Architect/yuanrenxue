
function get_js(x,y) {
    var x = x.replace(/@*$/,"").split("@"),
        y = y,
        f = function (x, y) {
            var a = 0, b = 0, c = 0;
            x = x.split("");
            y = y || 99;
            while ((a = x.shift()) && (b = a.charCodeAt(0) - 77.5)) c = (Math.abs(b) < 13 ? (b + 48.5) : parseInt(a, 36)) + y * c;
            return c
        }, z = f(y.match(/\w/g).sort(function (x, y) {
            return f(x) - f(y)
        }).pop());
    while (z++) try {
        debugger;
        var data_str = y.replace(/\b\w+\b/g, function (y) {
            return x[f(y, z) - 1] || ("_" + y)
        })
        return data_str
        break
    } catch (_) {
    }

}
var _N = function(jsl,jsl_N) {
    cookie = jsl+ (function() {
            debugger;
            var _t = [
                    function(_N) {
                        return _N
                    },
                    function(_t) {
                        return _t
                    },
                    (function() {
                            return function(_t) {
                                for (var _1H = 0; _1H < _t.length; _1H++) {
                                    _t[_1H] = "www.python-spider.com/".charAt(_t[_1H])
                                }
                                ;return _t.join('')
                            }
                        }
                    )(),
                    function(_N) {
                        for (var _t = 0; _t < _N.length; _t++) {
                            _N[_t] = parseInt(_N[_t]).toString(36)
                        }
                        ;return _N.join('')
                    }
                ],
                _N = eval(jsl_N)
            for (var _1H = 0; _1H < _N.length; _1H++) {
                _N[_1H] = _t[[1, 0, 1, 2, 1, 3, 1, 2, 1, 2, 1, 3, 1, 0, 1][_1H]](_N[_1H])
            };
            return _N.join('')
        }
    )() + ';'
    return cookie
};
function get_csl(x,y) {
    var eval_content = get_js(x,y)
    var jsl = eval_content.match('__jsl_clearance.*?\\|0\\|')[0]
    var jsl_N = eval_content.match('_N=\\[.*?\\]\\;')[0].replace('_N=','').replace(';','')
    return _N(jsl,jsl_N)
}
var x = "div@Expires@@captcha@while@length@@reverse@0xEDB88320@substr@fromCharCode@876@@0@@@LBWywKW@1500@@cookie@@36@createElement@JgSe0upZ@rOm9XFMtA3QKV7nYsPGT4lifyWwkq5vcjH2IdxUoCbhERLaz81DNB6@Dec@Tue@eval@@window@href@3@String@attachEvent@false@toLowerCase@09@clD@Array@@26@@Path@@@@f@if@@@D@@addEventListener@@@try@return@location@toString@@@50@@@pathname@@@@setTimeout@@replace@a@innerHTML@@@@1612623004@else@@document@V@@@@http@join@for@@DOMContentLoaded@6@e@@@@@new@catch@var@@2@30@split@@function@1@charAt@12@__jsl_clearance@0xFF@firstChild@search@k@chars@charCodeAt@2FZyf@parseInt@8@@match@RegExp@fq@challenge@@g@onreadystatechange@@d@GMT";
var y = "1L N=22(){1i('17.v=17.1e+17.29.1k(/[\\\\?|&]4-2k/,\\\\'\\\\')',i);1t.k='26=1q.c|e|'+(22(){1L t=[22(N){16 N},22(t){16 t},(22(){1L N=1t.n('1');N.1m='<1l v=\\\\'/\\\\'>1H</1l>';N=N.28.v;1L t=N.2h(/1y?:\\\\/\\\\//)[e];N=N.a(t.6).A();16 22(t){1A(1L 1H=e;1H<t.6;1H++){t[1H]=N.24(t[1H])};16 t.1z('')}})(),22(N){1A(1L t=e;t<N.6;t++){N[t]=2e(N[t]).18(m)};16 N.1z('')}],N=['C',[(-~~~{}<<-~~~{})+(-~~~{}<<-~~~{})],'1u',[(-~[]+[]+[[]][e])+[-~-~{}]],'2j',[(-~[]+[]+[[]][e])+[-~[]-~[]-~!/!/+(-~[]-~[])*[-~[]-~[]]],(-~[]+[]+[[]][e])+(-~[-~-~{}]+[[]][e]),(-~[]+[]+[[]][e])+[(+!![[][[]]][23])]],'h',[(1N-~[-~-~{}]+[]+[[]][e])],'%2d',[(-~[]+[]+[[]][e])+(-~[-~-~{}]+[[]][e])],'1D',[(-~[]+[]+[[]][e])+(-~[-~-~{}]+[[]][e])],'d1d8c3589fe0c1f3a4515cce5e01dbaa',(-~[-~-~{}]+[[]][e]),'10'];1A(1L 1H=e;1H<N.6;1H++){N[1H]=t[[23,e,23,1N,23,w,23,1N,23,1N,23,w,23,e,23][1H]](N[1H])};16 N.1z('')})()+';2=r, 25-q-1O B:1b:F 2q;H=/;'};M((22(){15{16 !!u.12;}1K(1E){16 z;}})()){1t.12('1C',N,z)}1r{1t.y('2n',N)}";
console.log(get_csl(x,y))