(function(d, w, nav, sc) {
  function serialize(obj) {
    return Object.keys(obj)
      .map(function(key) {
        return [key, obj[key]].join('=');
      })
      .join('&');
  }

  function getCookie(name) {
    var matches = d.cookie.match(new RegExp('(?:^|; )' + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + '=([^;]*)'));
    return matches ? decodeURIComponent(matches[1]) : '';
  }

  function hit(referrer) {
    var s = w && w.sessionStorage ? w.sessionStorage : {};
    var query = {
      rnd: Math.random().toString(),
      u: encodeURIComponent(d.URL),
      r: encodeURIComponent(referrer || d.referrer)
    };

    try {
      var e = d.documentElement;
      query.v = 4;
      query.w = w.top === w ? 1 : 0;
      query.h = d.hidden ? 1 : 0;
      query.gW = Math.max(e.clientWidth, w.innerWidth || 0);
      query.gH = Math.max(e.clientHeight, w.innerHeight || 0);
      query.gDH = Math.max(d.body.scrollHeight, e.scrollHeight, d.body.offsetHeight, e.offsetHeight, d.body.clientHeight, e.clientHeight);
      query.gDW = Math.max(d.body.scrollWidth, e.scrollWidth, d.body.offsetWidth, e.offsetWidth, d.body.clientWidth, e.clientWidth);
      query.sW = sc.width || 0;
      query.sH = sc.height || 0;
      query.ga = getCookie('_ga');
      query.dpr = w.devicePixelRatio || '';
      query.c = (function() {
        var conn = '';
        if (nav && nav.connection) {
          if (nav.connection.type) conn = nav.connection.type;
          else if (nav.connection.effectiveType) conn = 'eff:' + nav.connection.effectiveType;
        }
        return conn;
      })();
      query.t = s && s._tid ? s._tid : (s._tid = Date.now());

      if (w.performance) {
        if (w.performance.navigation) {
          query.rc = w.performance.navigation.redirectCount;
          query.tn = w.performance.navigation.type;
        }

        if (w.performance.timing) query.dc = (w.performance.timing.secureConnectionStart || w.performance.timing.fetchStart) - w.performance.timing.fetchStart;
      }
    } catch (e) {}

    var path = '//statad.ru/pixel.gif';
    var qs = serialize(query);
    new Image().src = [path, '?', qs].join('');
  }

  hit();

  var url = w.location.href;
  var count = 0;
  var checkInterval = setInterval(function() {
    if (count >= 50) clearInterval(checkInterval);
    else if (url !== w.location.href) {
      hit(url);
      url = w.location.href;
      count++;
    }
  }, 1000);
})(document, window, navigator, screen);

/*
-----BEGIN PGP SIGNATURE-----
Version: OpenPGP.js v4.5.5
Comment: https://openpgpjs.org

wsDcBAEBCgAGBQJdgJHjAAoJEOOmc3IHnZzJXVEL/ixajYK8NvZoxwd50Moj
pK3ZuWizg5J28SZo+KASnwuF3tB3CPefpxymV9qDSg+XR1unRb/+mVqv8uZU
xsKK5eS6GZXQqcxXi53wW+pNfmdcaXz+nKvgpiUYO104B3c/SPMi/CeUEOtA
bcW00tSFj8BbsmzVgDM90VWSI6bSBixlpYjDJ95E1g0rqQQ575YrfcMPaUnU
wWzxlTqsRECSu859cugFjI8JQyShiKv1pgSJbUUg5IrCfd7ZXFqVbv0IchbT
VbtDwOzofKQusvD97bk+c9cuhS+E3x56W6LuXdC9z2rcOJfUz/3kiEPpR8u+
TS4HRFA8pEn+cp7Dz100TzSFwvfGQn4ZdRVx7AIa6K90XIibN4FA8FENdRJA
XakO5ePjShBE9sBISLHSoR2YEYktPW+ci8j1iU4nLg4yd4f79mQ1Ebd0Qoz5
5pxhjaZ7ioHsupL6orquUC8vm8zIMXm5EQtjvbQrrs/3K8XXAC2Vvkj05YhU
SAeo9bhNeToZtg==
=L+tP
-----END PGP SIGNATURE-----

*/