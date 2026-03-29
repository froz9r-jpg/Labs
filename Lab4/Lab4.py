import enum

class Kolir(enum.Enum):
    CHERVONYI = 0
    CHORNYI = 1

class Vuzol:
    def __init__(self, znachennia, priorytet):
        self.znachennia = znachennia
        self.priorytet = priorytet
        self.kolir = Kolir.CHERVONYI
        self.liva_dytyna = None
        self.prava_dytyna = None
        self.batko = None

class ChervonoChorneDerevoCherha:
    def __init__(self):
        self.NUL_VUZOL = Vuzol(None, None)
        self.NUL_VUZOL.kolir = Kolir.CHORNYI
        self.korin = self.NUL_VUZOL

    def _liva_rotatsiia(self, x):
        y = x.prava_dytyna
        x.prava_dytyna = y.liva_dytyna
        if y.liva_dytyna != self.NUL_VUZOL:
            y.liva_dytyna.batko = x
        y.batko = x.batko
        if x.batko is None:
            self.korin = y
        elif x == x.batko.liva_dytyna:
            x.batko.liva_dytyna = y
        else:
            x.batko.prava_dytyna = y
        y.liva_dytyna = x
        x.batko = y

    def _prava_rotatsiia(self, x):
        y = x.liva_dytyna
        x.liva_dytyna = y.prava_dytyna
        if y.prava_dytyna != self.NUL_VUZOL:
            y.prava_dytyna.batko = x
        y.batko = x.batko
        if x.batko is None:
            self.korin = y
        elif x == x.batko.prava_dytyna:
            x.batko.prava_dytyna = y
        else:
            x.batko.liva_dytyna = y
        y.prava_dytyna = x
        x.batko = y

    def _balansuvaty_vstavku(self, k):
        while k.batko.kolir == Kolir.CHERVONYI:
            if k.batko == k.batko.batko.prava_dytyna:
                u = k.batko.batko.liva_dytyna
                if u.kolir == Kolir.CHERVONYI:
                    u.kolir = Kolir.CHORNYI
                    k.batko.kolir = Kolir.CHORNYI
                    k.batko.batko.kolir = Kolir.CHERVONYI
                    k = k.batko.batko
                else:
                    if k == k.batko.liva_dytyna:
                        k = k.batko
                        self._prava_rotatsiia(k)
                    k.batko.kolir = Kolir.CHORNYI
                    k.batko.batko.kolir = Kolir.CHERVONYI
                    self._liva_rotatsiia(k.batko.batko)
            else:
                u = k.batko.batko.prava_dytyna
                if u.kolir == Kolir.CHERVONYI:
                    u.kolir = Kolir.CHORNYI
                    k.batko.kolir = Kolir.CHORNYI
                    k.batko.batko.kolir = Kolir.CHERVONYI
                    k = k.batko.batko
                else:
                    if k == k.batko.prava_dytyna:
                        k = k.batko
                        self._liva_rotatsiia(k)
                    k.batko.kolir = Kolir.CHORNYI
                    k.batko.batko.kolir = Kolir.CHERVONYI
                    self._prava_rotatsiia(k.batko.batko)
            if k == self.korin: break
        self.korin.kolir = Kolir.CHORNYI

    def vstavyty(self, znachennia, priorytet):
        vuzol = Vuzol(znachennia, priorytet)
        vuzol.liva_dytyna = self.NUL_VUZOL
        vuzol.prava_dytyna = self.NUL_VUZOL
        y = None
        x = self.korin
        while x != self.NUL_VUZOL:
            y = x
            if vuzol.priorytet < x.priorytet: x = x.liva_dytyna
            else: x = x.prava_dytyna
        vuzol.batko = y
        if y is None: self.korin = vuzol
        elif vuzol.priorytet < y.priorytet: y.liva_dytyna = vuzol
        else: y.prava_dytyna = vuzol
        if vuzol.batko is None:
            vuzol.kolir = Kolir.CHORNYI
            return
        if vuzol.batko.batko is None: return
        self._balansuvaty_vstavku(vuzol)

    def perehliad(self):
        if self.korin == self.NUL_VUZOL: return None
        vuzol = self.korin
        while vuzol.prava_dytyna != self.NUL_VUZOL: vuzol = vuzol.prava_dytyna
        return (vuzol.znachennia, vuzol.priorytet)

    def vydalyty_ta_povernuty(self):
        if self.korin == self.NUL_VUZOL: return None
        vuzol = self.korin
        while vuzol.prava_dytyna != self.NUL_VUZOL: vuzol = vuzol.prava_dytyna
        rez = (vuzol.znachennia, vuzol.priorytet)
        self._vydalyty_vuzol(vuzol)
        return rez

    def _zaminyty_vuzol(self, u, v):
        if u.batko is None: self.korin = v
        elif u == u.batko.liva_dytyna: u.batko.liva_dytyna = v
        else: u.batko.prava_dytyna = v
        v.batko = u.batko

    def _vydalyty_vuzol(self, z):
        y = z
        y_oryh_kolir = y.kolir
        if z.liva_dytyna == self.NUL_VUZOL:
            x = z.prava_dytyna
            self._zaminyty_vuzol(z, z.prava_dytyna)
        elif z.prava_dytyna == self.NUL_VUZOL:
            x = z.liva_dytyna
            self._zaminyty_vuzol(z, z.liva_dytyna)
        else:
            y = self._shukaty_min(z.prava_dytyna)
            y_oryh_kolir = y.kolir
            x = y.prava_dytyna
            if y.batko == z: x.batko = y
            else:
                self._zaminyty_vuzol(y, y.prava_dytyna)
                y.prava_dytyna = z.prava_dytyna
                y.prava_dytyna.batko = y
            self._zaminyty_vuzol(z, y)
            y.liva_dytyna = z.liva_dytyna
            y.liva_dytyna.batko = y
            y.kolir = z.kolir
        if y_oryh_kolir == Kolir.CHORNYI: self._balansuvaty_vydalennia(x)

    def _shukaty_min(self, vuzol):
        while vuzol.liva_dytyna != self.NUL_VUZOL: vuzol = vuzol.liva_dytyna
        return vuzol

    def _balansuvaty_vydalennia(self, x):
        while x != self.korin and x.kolir == Kolir.CHORNYI:
            if x == x.batko.liva_dytyna:
                s = x.batko.prava_dytyna
                if s.kolir == Kolir.CHERVONYI:
                    s.kolir = Kolir.CHORNYI
                    x.batko.kolir = Kolir.CHERVONYI
                    self._liva_rotatsiia(x.batko)
                    s = x.batko.prava_dytyna
                if s.liva_dytyna.kolir == Kolir.CHORNYI and s.prava_dytyna.kolir == Kolir.CHORNYI:
                    s.kolir = Kolir.CHERVONYI
                    x = x.batko
                else:
                    if s.prava_dytyna.kolir == Kolir.CHORNYI:
                        s.liva_dytyna.kolir = Kolir.CHORNYI
                        s.kolir = Kolir.CHERVONYI
                        self._prava_rotatsiia(s)
                        s = x.batko.prava_dytyna
                    s.kolir = x.batko.kolir
                    x.batko.kolir = Kolir.CHORNYI
                    s.prava_dytyna.kolir = Kolir.CHORNYI
                    self._liva_rotatsiia(x.batko)
                    x = self.korin
            else:
                s = x.batko.liva_dytyna
                if s.kolir == Kolir.CHERVONYI:
                    s.kolir = Kolir.CHORNYI
                    x.batko.kolir = Kolir.CHERVONYI
                    self._prava_rotatsiia(x.batko)
                    s = x.batko.liva_dytyna
                if s.prava_dytyna.kolir == Kolir.CHORNYI and s.liva_dytyna.kolir == Kolir.CHORNYI:
                    s.kolir = Kolir.CHERVONYI
                    x = x.batko
                else:
                    if s.liva_dytyna.kolir == Kolir.CHORNYI:
                        s.prava_dytyna.kolir = Kolir.CHORNYI
                        s.kolir = Kolir.CHERVONYI
                        self._liva_rotatsiia(s)
                        s = x.batko.liva_dytyna
                    s.kolir = x.batko.kolir
                    x.batko.kolir = Kolir.CHORNYI
                    s.liva_dytyna.kolir = Kolir.CHORNYI
                    self._prava_rotatsiia(x.batko)
                    x = self.korin
        x.kolir = Kolir.CHORNYI