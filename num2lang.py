#!/bin/env python

# MIT License
#
# Copyright (c) 2024
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


LOC_PELETIER = ("n","no","nb","nor","norsk","norwegian",)
LOC_SHORT = ("e","en","eng","english","engelsk","us","usa","na","north_athlantic","north athlantic","american","america",)
class Num2Text:
    def __init__(self,root=None
                 ,lang='norsk'
                 ,num=0
                 ,numbers=[]
                 ,localeScaleFlag=False
                 ,easyreadFlag=True
                 ,newline=True
                 ,peletier = False
                 ,shortscale = False
                 ,*args,**kwargs
    ):
        super().__init__()

        self.lang               = 1 # norsk, ofc
        self._num               = num
        self.numbers            = numbers
        self.root               = root # does noting, just for convention and possible extension
        self.easyreadFlag    = easyreadFlag
        self.newline            = newline
        localescale             = localeScaleFlag



        if isinstance(lang, str):
            if lang.lower() in LOC_PELETIER:
                self.lang = 1
            elif lang.lower() in LOC_SHORT:
                self.lang = 2
        else:
            self.lang = 2

        if peletier:
            localescale = get_locale_scale(self.lang ,'peletier')
        elif shortscale:
            localescale = get_locale_scale(self.lang ,'shortscale')
        else:
            localescale = get_locale_scale(self.lang ,'')

        self.localeScaleFlag    = localescale

# ### ------------------------------------------------------------------------------------------------------------------------------------------ ###

    def n2w(self,num):
        d = { 0 : "zero", 1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five",
            6 : "six", 7 : "seven", 8 : "eight", 9 : "nine", 10 : "ten",
            11 : "eleven", 12 : "twelve", 13 : "thirteen", 14 : "fourteen",
            15 : "fifteen", 16 : "sixteen", 17 : "seventeen", 18 : "eighteen",
            19 : "nineteen", 20 : "twenty",
            30 : "thirty", 40 : "forty", 50 : "fifty", 60 : "sixty",
            70 : "seventy", 80 : "eighty", 90 : "ninety" }

        k = 1000
        m = k * 1000
        b = m * 1000
        t = b * 1000
        tr = t * 1000
        qu = tr * 1000
        sx = qu * 1000
        se = sx * 1000
        oc = se * 1000
        non = oc * 1000
        dec = non * 1000
        und = dec * 1000
        duo = und * 1000
        tre = duo * 1000
        qua = tre * 1000
        qui = qua * 1000
        sed = qui * 1000
        sep = sed * 1000
        ocd = sep * 1000
        nov = ocd * 1000
        vin = nov * 1000
        unv = vin * 1000
        duv = unv * 1000
        trv = duv * 1000
        qtv = trv * 1000
        qiv = qtv * 1000
        ssv = qiv * 1000
        spv = ssv * 1000
        spvg = spv * 1000
        kvde = spvg * 1000
        kvdil = kvde * 1000
        sedec = kvdil * 1000
        sedil = sedec * 1000
        sepec = sedil * 1000
        sepil = sepec * 1000
        octec = sepil * 1000


        if (num > octec * 1000):
            # print("num is too large: %s" % str(num))
            return f"{num} (a really big number)..."
            # sys.exit(1)

        if (num < 0):
            num = -num
            # sys.exit()

        if (num < 20):
            # print(num)
            return d[num]

        if (num < 100):
            if num % 10 == 0: return d[num]
            else: return d[num // 10 * 10] + "-" + d[num % 10]

        if (num < k):
            if num % 100 == 0:

                return d[num // 100] + " hundred"
            else:

                return d[num // 100] + " hundred " + self.n2w(num % 100)

        if (num < m):
            if num % k == 0:
                return self.n2w(num // k) + " thousand"
            else:
                return self.n2w(num // k) + " thousand, " + self.n2w(num % k)

        if (num < b):
            if (num % m) == 0:
                return self.n2w(num // m) + " million"
            else:
                return self.n2w(num // m) + " million, " + self.n2w(num % m)

        if (num < t):
            if (self.localeScaleFlag == False):
                if (num % b) == 0:
                    return self.n2w(num // b) + " billion"
                else:
                    return self.n2w(num // b) + " billion, " + self.n2w(num % b)
            else:
                if (num % b) == 0:
                    return self.n2w(num // b) + " milliard"
                else:
                    return self.n2w(num // b) + " milliard, " + self.n2w(num % b)


        if (num < tr):
            if (self.localeScaleFlag == False):
                if (num % t == 0):
                    return self.n2w(num // t) + " trillion"
                else:
                    return self.n2w(num // t) + " trillion, " + self.n2w(num % t)
            else:
                if (num % t == 0):
                    return self.n2w(num // t) + " billion"
                else:
                    return self.n2w(num // t) + " billion, " + self.n2w(num % t)

        if (num < qu):
            if (self.localeScaleFlag == False):
                if (num % tr == 0):
                    return self.n2w(num // tr) + " quadrillion"
                else:
                    return self.n2w(num // tr) + " quadrillion, " + self.n2w(num % tr)
            else:
                if (num % tr == 0):
                    return self.n2w(num // tr) + " billiard"
                else:
                    return self.n2w(num // tr) + " billiard, " + self.n2w(num % tr)

        if (num < sx):
            if (self.localeScaleFlag == False):
                if (num % qu == 0):
                    return self.n2w(num // qu) + " quintillion"
                else:
                    return self.n2w(num // qu) + " quintillion, " + self.n2w(num % qu)
            else:
                if (num % qu == 0):
                    return self.n2w(num // qu) + " trillion"
                else:
                    return self.n2w(num // qu) + " trillion, " + self.n2w(num % qu)

        if (num < se):
            if (self.localeScaleFlag == False):
                if (num % sx == 0):
                    return self.n2w(num // sx) + " sextillion"
                else:
                    return self.n2w(num // sx) + " sextillion, " + self.n2w(num % sx)
            else:
                if (num % sx == 0):
                    return self.n2w(num // sx) + " trilliard"
                else:
                    return self.n2w(num // sx) + " trilliard, " + self.n2w(num % sx)

        if (num < oc):
            if (self.localeScaleFlag == False):
                if (num % se == 0):
                    return self.n2w(num // se) + " septillion"
                else:
                    return self.n2w(num // se) + " septillion, " + self.n2w(num % se)
            else:
                if (num % se == 0):
                    return self.n2w(num // se) + " quadrillion"
                else:
                    return self.n2w(num // se) + " quadrillion, " + self.n2w(num % se)

        if (num < non):
            if (self.localeScaleFlag == False):
                if (num % oc == 0):
                    return self.n2w(num // oc) + " octillion"
                else:
                    return self.n2w(num // oc) + " octillion, " + self.n2w(num % oc)
            else:
                if (num % oc == 0):
                    return self.n2w(num // oc) + " quadrilliard"
                else:
                    return self.n2w(num // oc) + " quadrilliard, " + self.n2w(num % oc)

        if (num < dec):
            if (self.localeScaleFlag == False):
                if (num % non == 0):
                    return self.n2w(num // non) + " nonillion"
                else:
                    return self.n2w(num // non) + " nonillion, " + self.n2w(num % non)
            else:
                if (num % non == 0):
                    return self.n2w(num // non) + " quintillion"
                else:
                    return self.n2w(num // non) + " quintillion, " + self.n2w(num % non)

        if (num < und):
            if (self.localeScaleFlag == False):
                if (num % dec == 0):
                    return self.n2w(num // dec) + " decillion"
                else:
                    return self.n2w(num // dec) + " decillion, " + self.n2w(num % dec)
            else:
                if (num % dec == 0):
                    return self.n2w(num // dec) + " quintilliard"
                else:
                    return self.n2w(num // dec) + " quintilliard, " + self.n2w(num % dec)

        if (num < duo):
            if (self.localeScaleFlag == False):
                if (num % und == 0):
                    return self.n2w(num // und) + " undecillion"
                else:
                    return self.n2w(num // und) + " undecillion, " + self.n2w(num % und)
            else:
                if (num % und == 0):
                    return self.n2w(num // und) + " sextillion"
                else:
                    return self.n2w(num // und) + " sextillion, " + self.n2w(num % und)

        if (num < tre):
            if (self.localeScaleFlag == False):
                if (num % duo == 0):
                    return self.n2w(num // duo) + " duodecillion"
                else:
                    return self.n2w(num // duo) + " duodecillion, " + self.n2w(num % duo)
            else:
                if (num % duo == 0):
                    return self.n2w(num // duo) + " sextilliard"
                else:
                    return self.n2w(num // duo) + " sextilliard, " + self.n2w(num % duo)

        if (num < qua):
            if (self.localeScaleFlag == False):
                if (num % tre == 0):
                    return self.n2w(num // tre) + " tredecillion"
                else:
                    return self.n2w(num // tre) + " tredecillion, " + self.n2w(num % tre)
            else:
                if (num % tre == 0):
                    return self.n2w(num // tre) + " septillion"
                else:
                    return self.n2w(num // tre) + " septillion, " + self.n2w(num % tre)

        if (num < qui):
            if (self.localeScaleFlag == False):
                if (num % qua == 0):
                    return self.n2w(num // qua) + " quattuordecillion"
                else:
                    return self.n2w(num // qua) + " quattuordecillion, " + self.n2w(num % qua)
            else:
                if (num % qua == 0):
                    return self.n2w(num // qua) + " septilliard"
                else:
                    return self.n2w(num // qua) + " septilliard, " + self.n2w(num % qua)

        if (num < sed):
            if (self.localeScaleFlag == False):
                if (num % qui == 0):
                    return self.n2w(num // qui) + " quindecillion"
                else:
                    return self.n2w(num // qui) + " quindecillion, " + self.n2w(num % qui)
            else:
                if (num % qui == 0):
                    return self.n2w(num // qui) + " octillion"
                else:
                    return self.n2w(num // qui) + " octillion, " + self.n2w(num % qui)

        if (num < sep):
            if (self.localeScaleFlag == False):
                if (num % sed == 0):
                    return self.n2w(num // sed) + " sexdecillion"
                else:
                    return self.n2w(num // sed) + " sexdecillion, " + self.n2w(num % sed)
            else:
                if (num % sed == 0):
                    return self.n2w(num // sed) + " octilliard"
                else:
                    return self.n2w(num // sed) + " octilliard, " + self.n2w(num % sed)

        if (num < ocd):
            if (self.localeScaleFlag == False):
                if (num % sep == 0):
                    return self.n2w(num // sep) + " septendecillion"
                else:
                    return self.n2w(num // sep) + " septendecillion, " + self.n2w(num % sep)
            else:
                if (num % sep == 0):
                    return self.n2w(num // sep) + " nonillion"
                else:
                    return self.n2w(num // sep) + " nonillion, " + self.n2w(num % sep)

        if (num < nov):
            if (self.localeScaleFlag == False):
                if (num % ocd == 0):
                    return self.n2w(num // ocd) + " octodecillion"
                else:
                    return self.n2w(num // ocd) + " octodecillion, " + self.n2w(num % ocd)
            else:
                if (num % ocd == 0):
                    return self.n2w(num // ocd) + " nonilliard"
                else:
                    return self.n2w(num // ocd) + " nonilliard, " + self.n2w(num % ocd)

        if (num < vin):
            if (self.localeScaleFlag == False):
                if (num % nov == 0):
                    return self.n2w(num // nov) + " novendecillion"
                else:
                    return self.n2w(num // nov) + " novendecillion, " + self.n2w(num % nov)
            else:
                if (num % nov == 0):
                    return self.n2w(num // nov) + " decillion"
                else:
                    return self.n2w(num // nov) + " decillion, " + self.n2w(num % nov)
        if (num < unv):
            if (self.localeScaleFlag == False):
                if (num % vin == 0):
                    return self.n2w(num // vin) + " vigintillion"
                else:
                    return self.n2w(num // vin) + " vigintillion, " + self.n2w(num % vin)
            else:
                if (num % vin == 0):
                    return self.n2w(num // vin) + " decilliard"
                else:
                    return self.n2w(num // vin) + " decilliard, " + self.n2w(num % vin)

        if (num < duv):
            if (self.localeScaleFlag == False):
                if (num % unv == 0):
                    return self.n2w(num // unv) + " unvigintillion"
                else:
                    return self.n2w(num // unv) + " unvigintillion, " + self.n2w(num % unv)
            else:
                if (num % unv == 0):
                    return self.n2w(num // unv) + " undecillion"
                else:
                    return self.n2w(num // unv) + " undecillion, " + self.n2w(num % unv)

        if (num < trv):
            if (self.localeScaleFlag == False):
                if (num % duv == 0):
                    return self.n2w(num // duv) + " duovigintillion"
                else:
                    return self.n2w(num // duv) + " duovigintillion, " + self.n2w(num % duv)
            else:
                if (num % duv == 0):
                    return self.n2w(num // duv) + " undecilliard"
                else:
                    return self.n2w(num // duv) + " undecilliard, " + self.n2w(num % duv)

        if (num < qtv):
            if (self.localeScaleFlag == False):
                if (num % trv == 0):
                    return self.n2w(num // trv) + " tresvigintillion"
                else:
                    return self.n2w(num // trv) + " tresvigintillion, " + self.n2w(num % trv)
            else:
                if (num % trv == 0):
                    return self.n2w(num // trv) + " duodecillion"
                else:
                    return self.n2w(num // trv) + " duodecillion, " + self.n2w(num % trv)

        if (num < qiv):
            if (self.localeScaleFlag == False):
                if (num % qtv == 0):
                    return self.n2w(num // qtv) + " quattorvigintillion"
                else:
                    return self.n2w(num // qtv) + " quattorvigintillion, " + self.n2w(num % qtv)
            else:
                if (num % qtv == 0):
                    return self.n2w(num // qtv) + " duodecilliard"
                else:
                    return self.n2w(num // qtv) + " duodecilliard, " + self.n2w(num % qtv)

        if (num < ssv):
            if (self.localeScaleFlag == False):
                if (num % qiv == 0):
                    return self.n2w(num // qiv) + " quinvigintillion"
                else:
                    return self.n2w(num // qiv) + " quinvigintillion, " + self.n2w(num % qiv)
            else:
                if (num % qtv == 0):
                    return self.n2w(num // qiv) + " tredecillion"
                else:
                    return self.n2w(num // qiv) + " tredecillion, " + self.n2w(num % qiv)

        if (num < spv):
            if (self.localeScaleFlag == False):
                if (num % ssv == 0):
                    return self.n2w(num // ssv) + " sexvigintillion"
                else:
                    return self.n2w(num // ssv) + " sexvigintillion, " + self.n2w(num % ssv)
            else:
                if (num % ssv == 0):
                    return self.n2w(num // ssv) + " tredecilliard"
                else:
                    return self.n2w(num // ssv) + " tredecilliard, " + self.n2w(num % ssv)

        if (num < spvg):
            if (self.localeScaleFlag == False):
                if (num % spv == 0):
                    return self.n2w(num // spv) + " septenvigintillion"
                else:
                    return self.n2w(num // spv) + " septenvigintillion, " + self.n2w(num % spv)
            else:
                if (num % spv == 0):
                    return self.n2w(num // spv) + " quattordecillion"
                else:
                    return self.n2w(num // spv) + " quattordecillion, " + self.n2w(num % spv)

        if (num < kvde):
            if (self.localeScaleFlag == False):
                if (num % spvg == 0):
                    return self.n2w(num // spvg) + " octovigintillion"
                else:
                    return self.n2w(num // spvg) + " octovigintillion, " + self.n2w(num % spvg)
            else:
                if (num % spvg == 0):
                    return self.n2w(num // spvg) + " quindecilliard"
                else:
                    return self.n2w(num // spvg) + " quindecilliard, " + self.n2w(num % spvg)

        if (num < kvdil):
            if (self.localeScaleFlag == False):
                if (num % kvde == 0):
                    return self.n2w(num // kvde) + " novemvigintillion"
                else:
                    return self.n2w(num // kvde) + " novemvigintillion, " + self.n2w(num % kvde)
            else:
                if (num % kvde == 0):
                    return self.n2w(num // kvde) + " quindecillion"
                else:
                    return self.n2w(num // kvde) + " quindecillion, " + self.n2w(num % kvde)

        if (num < sedec):
            if (self.localeScaleFlag == False):
                if (num % kvdil == 0):
                    return self.n2w(num // kvdil) + " trigintillion"
                else:
                    return self.n2w(num // kvdil) + " trigintillion, " + self.n2w(num % kvdil)
            else:
                if (num % kvdil == 0):
                    return self.n2w(num // kvdil) + " quindecilliard"
                else:
                    return self.n2w(num // kvdil) + " quindecilliard, " + self.n2w(num % kvdil)

        if (num < sedil):
            if (self.localeScaleFlag == False):
                if (num % sedec == 0):
                    return self.n2w(num // sedec) + " untrigintillion"
                else:
                    return self.n2w(num // sedec) + " untrigintillion, " + self.n2w(num % sedec)
            else:
                if (num % sedec == 0):
                    return self.n2w(num // sedec) + " sedecillion"
                else:
                    return self.n2w(num // sedec) + " sedecillion, " + self.n2w(num % sedec)

        if (num < sepec):
            if (self.localeScaleFlag == False):
                if (num % sedil == 0):
                    return self.n2w(num // sedil) + " duotrigintillion"
                else:
                    return self.n2w(num // sedil) + " duotrigintillion, " + self.n2w(num % sedil)
            else:
                if (num % sedil == 0):
                    return self.n2w(num // sedil) + " sedecilliard"
                else:
                    return self.n2w(num // sedil) + " sedecilliard, " + self.n2w(num % sedil)

        if (num < sepil):
            if (self.localeScaleFlag == False):
                if (num % sepec == 0):
                    return self.n2w(num // sepec) + " trestrigintillion"
                else:
                    return self.n2w(num // sepec) + " trestrigintillion, " + self.n2w(num % sepec)
            else:
                if (num % sepec == 0):
                    return self.n2w(num // sepec) + " septendecillion"
                else:
                    return self.n2w(num // sepec) + " septendecillion, " + self.n2w(num % sepec)

        if (num < octec):
            if (self.localeScaleFlag == False):
                if (num % sepil == 0):
                    return self.n2w(num // sepil) + " quattuortrigintillion"
                else:
                    return self.n2w(num // sepil) + " quattuortrigintillion, " + self.n2w(num % sepil)
            else:
                if (num % sepil == 0):
                    return self.n2w(num // sepil) + " septendecilliard"
                else:
                    return self.n2w(num // sepil) + " septendecilliard, " + self.n2w(num % sepil)



    def n2wNo(self,numNo):
        no = { 0 : "null", 1 : "en", 2 : "to", 3 : "tre", 4 : "fire", 5 : "fem",
            6 : "seks", 7 : "syv", 8 : "åtte", 9 : "ni", 10 : "ti",
            11 : "elleve", 12 : "tolv", 13 : "tretten", 14 : "fjorten",
            15 : "femten", 16 : "seksten", 17 : "søtten", 18 : "atten",
            19 : "nitten", 20 : "tjue",
            30 : "tretti", 40 : "førti", 50 : "femti", 60 : "seksti",
            70 : "søtti", 80 : "åtti", 90 : "nitti" }

        k = 1000
        m = k * 1000
        b = m * 1000
        t = b * 1000
        tr = t * 1000
        qu = tr * 1000
        sx = qu * 1000
        se = sx * 1000
        oc = se * 1000
        non = oc * 1000
        dec = non * 1000
        und = dec * 1000
        duo = und * 1000
        tre = duo * 1000
        qua = tre * 1000
        qui = qua * 1000
        sed = qui * 1000
        sep = sed * 1000
        ocd = sep * 1000
        nov = ocd * 1000
        vin = nov * 1000
        unv = vin * 1000
        duv = unv * 1000
        trv = duv * 1000
        qtv = trv * 1000
        qiv = qtv * 1000
        ssv = qiv * 1000
        spv = ssv * 1000
        spvg = spv * 1000
        kvde = spvg * 1000
        kvdil = kvde * 1000
        sedec = kvdil * 1000
        sedil = sedec * 1000
        sepec = sedil * 1000
        sepil = sepec * 1000
        octec = sepil * 1000

        if (numNo > octec * 1000):
            # print("num is too large: %s" % str(num))
            return f"{numNo} (et veldig stort tall)..."
            # sys.exit(1)

        if (numNo < 0):
            numNo = -numNo

            # sys.exit()

        # assert(0 <= num and num < qu)
        # raise AssertionError("num is too large: %s" % str(num))

        if (numNo < 20):
            # print(num)
            return no[numNo]

        if (numNo < 100):
            if numNo % 10 == 0: return no[numNo]
            else:
                # return no[numNo // 10 * 10] + no[numNo % 10]
                if self.easyreadFlag == False:
                    return no[numNo // 10 * 10] + no[numNo % 10]
                else:
                    return no[numNo // 10 * 10] + "-" + no[numNo % 10]

        if (numNo < k):
            if numNo % 100 == 0:
                if numNo // 100 == 1:
                    # return "ett" + "hundre"
                    if self.easyreadFlag == False:
                        return "ett" + "hundre"
                    else:
                        return "ett" + "-hundre"
                else:
                    # return no[numNo // 100] + "hundre"
                    if self.easyreadFlag == False:
                        return no[numNo // 100] + "hundre"
                    else:
                        return no[numNo // 100] + "-hundre"
            else:
                if numNo // 100 == 1:
                    if self.easyreadFlag == False:
                        return "ett" + "hundreog" + self.n2wNo(numNo % 100)
                    else:
                        return "ett" + "-hundre og " + self.n2wNo(numNo % 100)
                else:
                    if self.easyreadFlag == False:
                        return no[numNo // 100] + "hundreog" + self.n2wNo(numNo % 100)
                    else:
                        return no[numNo // 100] + "-hundre og " + self.n2wNo(numNo % 100)

        if (numNo < m):
            if numNo % k == 0:
                if self.easyreadFlag == False:
                    if (numNo // k == 1):
                        return "ett-tusen"
                    else:
                        # print(numNo // k == 1)
                        return self.n2wNo(numNo // k) + "tusen"
                else:
                    if (numNo // k == 1):
                        return "ett-tusen"
                    else:
                        return self.n2wNo(numNo // k) + "-tusen"
            else:
                if self.easyreadFlag == False:
                    if (numNo // k == 1):
                        return "ett-tusen, " + self.n2wNo(numNo % k)
                    else:
                        return self.n2wNo(numNo // k) + "tusen, " + self.n2wNo(numNo % k)
                else:
                    if (numNo // k == 1):
                        return " ett-tusen, " + self.n2wNo(numNo % k)
                    else:
                        return self.n2wNo(numNo // k) + "-tusen, " + self.n2wNo(numNo % k)

        if (numNo < b):
            if (numNo % m) == 0:
                if(numNo // m == 1):
                    return self.n2wNo(numNo // m) + " million"
                else:
                    return self.n2wNo(numNo // m) + " millioner"
            else:
                if(numNo // m == 1):
                    return self.n2wNo(numNo // m) + " million, " + self.n2wNo(numNo % m)
                else:
                    return self.n2wNo(numNo // m) + " millioner, " + self.n2wNo(numNo % m)

        if (numNo < t):
            if (self.localeScaleFlag == True):
                if (numNo % b) == 0:
                    if(numNo // b == 1):
                        return self.n2wNo(numNo // b) + " billion"
                    else:
                        return self.n2wNo(numNo // b) + " billioner"
                else:
                    if(numNo // b == 1):
                        return self.n2wNo(numNo // b) + " billion, " + self.n2wNo(numNo % b)
                    else:
                        return self.n2wNo(numNo // b) + " billioner, " + self.n2wNo(numNo % b)
            else:
                if (numNo % b) == 0:
                    if(numNo // b == 1):
                        return self.n2wNo(numNo // b) + " milliard"
                    else:
                        return self.n2wNo(numNo // b) + " milliarder"
                else:
                    if(numNo // b == 1):
                        return self.n2wNo(numNo // b) + " milliard, " + self.n2wNo(numNo % b)
                    else:
                        return self.n2wNo(numNo // b) + " milliarder, " + self.n2wNo(numNo % b)


        if (numNo < tr):
            if (self.localeScaleFlag == True):
                if (numNo % t == 0):
                    if(numNo // t == 1):
                        return self.n2wNo(numNo // t) + " trillion"
                    else:
                        return self.n2wNo(numNo // t) + " trillioner"
                else:
                    if(numNo // t == 1):
                        return self.n2wNo(numNo // t) + " trillion, " + self.n2wNo(numNo % t)
                    else:
                        return self.n2wNo(numNo // t) + " trillioner, " + self.n2wNo(numNo % t)
            else:
                if (numNo % t == 0):
                    if(numNo // t == 1):
                        return self.n2wNo(numNo // t) + " billion"
                    else:
                        return self.n2wNo(numNo // t) + " billioner"
                else:
                    if(numNo // t == 1):
                        return self.n2wNo(numNo // t) + " billion, " + self.n2wNo(numNo % t)
                    else:
                        return self.n2wNo(numNo // t) + " billioner, " + self.n2wNo(numNo % t)

        if (numNo < qu):
            if (self.localeScaleFlag == True):
                if (numNo % tr == 0):
                    if(numNo // tr == 1):
                        return self.n2wNo(numNo // tr) + " kvadrillion"
                    else:
                        return self.n2wNo(numNo // tr) + " kvadrillioner"
                else:
                    if(numNo // tr == 1):
                        return self.n2wNo(numNo // tr) + " kvadrillion, " + self.n2wNo(numNo % tr)
                    else:
                        return self.n2wNo(numNo // tr) + " kvadrillioner, " + self.n2wNo(numNo % tr)
            else:
                if (numNo % tr == 0):
                    if(numNo // tr == 1):
                        return self.n2wNo(numNo // tr) + " billiard"
                    else:
                        return self.n2wNo(numNo // tr) + " billiarder"
                else:
                    if(numNo // tr == 1):
                        return self.n2wNo(numNo // tr) + " billiard, " + self.n2wNo(numNo % tr)
                    else:
                        return self.n2wNo(numNo // tr) + " billiarder, " + self.n2wNo(numNo % tr)

        if (numNo < sx):
            if (self.localeScaleFlag == True):
                if (numNo % qu == 0):
                    if(numNo // qu == 1):
                        return self.n2wNo(numNo // qu) + " kvintillion"
                    else:
                        return self.n2wNo(numNo // qu) + " kvintillioner"
                else:
                    if(numNo // qu == 1):
                        return self.n2wNo(numNo // qu) + " kvintillion, " + self.n2wNo(numNo % qu)
                    else:
                        return self.n2wNo(numNo // qu) + " kvintillioner, " + self.n2wNo(numNo % qu)
            else:
                if (numNo % qu == 0):
                    if(numNo // qu == 1):
                        return self.n2wNo(numNo // qu) + " trillion"
                    else:
                        return self.n2wNo(numNo // qu) + " trillioner"
                else:
                    if(numNo // qu == 1):
                        return self.n2wNo(numNo // qu) + " trillion, " + self.n2wNo(numNo % qu)
                    else:
                        return self.n2wNo(numNo // qu) + " trillioner, " + self.n2wNo(numNo % qu)

        if (numNo < se):
            if (self.localeScaleFlag == True):
                if (numNo % sx == 0):
                    if(numNo // sx == 1):
                        return self.n2wNo(numNo // sx) + " sekstillion"
                    else:
                        return self.n2wNo(numNo // sx) + " sekstillioner"
                else:
                    if(numNo // sx == 1):
                        return self.n2wNo(numNo // sx) + " sekstillion, " + self.n2wNo(numNo % sx)
                    else:
                        return self.n2wNo(numNo // sx) + " sekstillioner, " + self.n2wNo(numNo % sx)
            else:
                if (numNo % sx == 0):
                    if(numNo // sx == 1):
                        return self.n2wNo(numNo // sx) + " trilliard"
                    else:
                        return self.n2wNo(numNo // sx) + " trilliarder"
                else:
                    if(numNo // sx == 1):
                        return self.n2wNo(numNo // sx) + " trilliard, " + self.n2wNo(numNo % sx)
                    else:
                        return self.n2wNo(numNo // sx) + " trilliarder, " + self.n2wNo(numNo % sx)

        if (numNo < oc):
            if (self.localeScaleFlag == True):
                if (numNo % se == 0):
                    if(numNo // se == 1):
                        return self.n2wNo(numNo // se) + " septillion"
                    else:
                        return self.n2wNo(numNo // se) + " septillioner"
                else:
                    if(numNo // se == 1):
                        return self.n2wNo(numNo // se) + " septillion, " + self.n2wNo(numNo % se)
                    else:
                        return self.n2wNo(numNo // se) + " septillioner, " + self.n2wNo(numNo % se)
            else:
                if (numNo % se == 0):
                    if(numNo // se == 1):
                        return self.n2wNo(numNo // se) + " kvadrillion"
                    else:
                        return self.n2wNo(numNo // se) + " kvadrillioner"
                else:
                    if(numNo // se == 1):
                        return self.n2wNo(numNo // se) + " kvadrillion, " + self.n2wNo(numNo % se)
                    else:
                        return self.n2wNo(numNo // se) + " kvadrillioner, " + self.n2wNo(numNo % se)

        if (numNo < non):
            if (self.localeScaleFlag == True):
                if (numNo % oc == 0):
                    if(numNo // oc == 1):
                        return self.n2wNo(numNo // oc) + " oktillion"
                    else:
                        return self.n2wNo(numNo // oc) + " oktillioner"
                else:
                    if(numNo // oc == 1):
                        return self.n2wNo(numNo // oc) + " oktillion, " + self.n2wNo(numNo % oc)
                    else:
                        return self.n2wNo(numNo // oc) + " oktillioner, " + self.n2wNo(numNo % oc)
            else:
                if (numNo % oc == 0):
                    if(numNo // oc == 1):
                        return self.n2wNo(numNo // oc) + " kvadrilliard"
                    else:
                        return self.n2wNo(numNo // oc) + " kvadrilliarder"
                else:
                    if(numNo // oc == 1):
                        return self.n2wNo(numNo // oc) + " kvadrilliard, " + self.n2wNo(numNo % oc)
                    else:
                        return self.n2wNo(numNo // oc) + " kvadrilliarder, " + self.n2wNo(numNo % oc)

        if (numNo < dec):
            if (self.localeScaleFlag == True):
                if (numNo % non == 0):
                    if(numNo // non == 1):
                        return self.n2wNo(numNo // non) + " nonillion"
                    else:
                        return self.n2wNo(numNo // non) + " nonillioner"
                else:
                    if(numNo // non == 1):
                        return self.n2wNo(numNo // non) + " nonillion, " + self.n2wNo(numNo % non)
                    else:
                        return self.n2wNo(numNo // non) + " nonillioner, " + self.n2wNo(numNo % non)
            else:
                if (numNo % non == 0):
                    if(numNo // non == 1):
                        return self.n2wNo(numNo // non) + " kvintillion"
                    else:
                        return self.n2wNo(numNo // non) + " kvintillioner"
                else:
                    if(numNo // non == 1):
                        return self.n2wNo(numNo // non) + " kvintillion, " + self.n2wNo(numNo % non)
                    else:
                        return self.n2wNo(numNo // non) + " kvintillioner, " + self.n2wNo(numNo % non)

        if (numNo < und):
            if (self.localeScaleFlag == True):
                if (numNo % dec == 0):
                    if(numNo // dec == 1):
                        return self.n2wNo(numNo // dec) + " desillion"
                    else:
                        return self.n2wNo(numNo // dec) + " desillioner"
                else:
                    if(numNo // dec == 1):
                        return self.n2wNo(numNo // dec) + " desillion, " + self.n2wNo(numNo % dec)
                    else:
                        return self.n2wNo(numNo // dec) + " desillioner, " + self.n2wNo(numNo % dec)
            else:
                if (numNo % dec == 0):
                    if(numNo // dec == 1):
                        return self.n2wNo(numNo // dec) + " kvintilliard"
                    else:
                        return self.n2wNo(numNo // dec) + " kvintilliarder"
                else:
                    if(numNo // dec == 1):
                        return self.n2wNo(numNo // dec) + " kvintilliard, " + self.n2wNo(numNo % dec)
                    else:
                        return self.n2wNo(numNo // dec) + " kvintilliarder, " + self.n2wNo(numNo % dec)

        if (numNo < duo):
            if (self.localeScaleFlag == True):
                if (numNo % und == 0):
                    if(numNo // und == 1):
                        return self.n2wNo(numNo // und) + " undesillion"
                    else:
                        return self.n2wNo(numNo // und) + " undesillioner"
                else:
                    if(numNo // und == 1):
                        return self.n2wNo(numNo // und) + " undesillion, " + self.n2wNo(numNo % und)
                    else:
                        return self.n2wNo(numNo // und) + " undesillioner, " + self.n2wNo(numNo % und)
            else:
                if (numNo % und == 0):
                    if(numNo // und == 1):
                        return self.n2wNo(numNo // und) + " sekstillion"
                    else:
                        return self.n2wNo(numNo // und) + " sekstillioner"
                else:
                    if(numNo // und == 1):
                        return self.n2wNo(numNo // und) + " sekstillion, " + self.n2wNo(numNo % und)
                    else:
                        return self.n2wNo(numNo // und) + " sekstillioner, " + self.n2wNo(numNo % und)

        if (numNo < tre):
            if (self.localeScaleFlag == True):
                if (numNo % duo == 0):
                    if(numNo // duo == 1):
                        return self.n2wNo(numNo // duo) + " dodesillion"
                    else:
                        # return self.n2wNo(numNo // duo) + " dodesillion"
                        return self.n2wNo(numNo // duo) + " dodesillioner"
                else:
                    if(numNo // duo == 1):
                        return self.n2wNo(numNo // duo) + " dodesillion, " + self.n2wNo(numNo % duo)
                    else:
                        # return self.n2wNo(numNo // duo) + " dodesillion, " + self.n2wNo(numNo % duo)
                        return self.n2wNo(numNo // duo) + " dodesillioner, " + self.n2wNo(numNo % duo)
            else:
                if (numNo % duo == 0):
                    if(numNo // duo == 1):
                        return self.n2wNo(numNo // duo) + " sekstilliard"
                    else:
                        return self.n2wNo(numNo // duo) + " sekstilliarder"
                else:
                    if(numNo // und == 1):
                        return self.n2wNo(numNo // duo) + " sekstilliard, " + self.n2wNo(numNo % duo)
                    else:
                        return self.n2wNo(numNo // duo) + " sekstilliarder, " + self.n2wNo(numNo % duo)

        if (numNo < qua):
            if (self.localeScaleFlag == True):
                if (numNo % tre == 0):
                    if(numNo // tre == 1):
                        return self.n2wNo(numNo // tre) + " tredesillion"
                    else:
                        return self.n2wNo(numNo // tre) + " tredesillioner"
                else:
                    if(numNo // tre == 1):
                        return self.n2wNo(numNo // tre) + " tredesillion, " + self.n2wNo(numNo % tre)
                    else:
                        return self.n2wNo(numNo // tre) + " tredesillioner, " + self.n2wNo(numNo % tre)
            else:
                if (numNo % tre == 0):
                    if(numNo // tre == 1):
                        return self.n2wNo(numNo // tre) + " septillion"
                    else:
                        return self.n2wNo(numNo // tre) + " septillioner"
                else:
                    if(numNo // und == 1):
                        return self.n2wNo(numNo // tre) + " septillion, " + self.n2wNo(numNo % tre)
                    else:
                        return self.n2wNo(numNo // tre) + " septillioner, " + self.n2wNo(numNo % tre)

        if (numNo < qui):
            if (self.localeScaleFlag == True):
                if (numNo % qua == 0):
                    if(numNo // qua == 1):
                        return self.n2wNo(numNo // qua) + " quattordesillion"
                    else:
                        return self.n2wNo(numNo // qua) + " quattuordesillioner"
                else:
                    if(numNo // qua == 1):
                        return self.n2wNo(numNo // qua) + " quattuordesillion, " + self.n2wNo(numNo % qua)
                    else:
                        return self.n2wNo(numNo // qua) + " quattuordesillioner, " + self.n2wNo(numNo % qua)
            else:
                if (numNo % qua == 0):
                    if(numNo // qua == 1):
                        return self.n2wNo(numNo // qua) + " septilliard"
                    else:
                        return self.n2wNo(numNo // qua) + " septilliarder"
                else:
                    if(numNo // qua == 1):
                        return self.n2wNo(numNo // qua) + " septilliard, " + self.n2wNo(numNo % qua)
                    else:
                        return self.n2wNo(numNo // qua) + " septilliarder, " + self.n2wNo(numNo % qua)

        if (numNo < sed):
            if (self.localeScaleFlag == True):
                if (numNo % qui == 0):
                    if(numNo // qui == 1):
                        return self.n2wNo(numNo // qui) + " kvindesillion"
                    else:
                        return self.n2wNo(numNo // qui) + " kvindesillioner"
                else:
                    if(numNo // qui == 1):
                        return self.n2wNo(numNo // qui) + " kvindesillion, " + self.n2wNo(numNo % qui)
                    else:
                        return self.n2wNo(numNo // qui) + " kvindesillioner, " + self.n2wNo(numNo % qui)
            else:
                if (numNo % qui == 0):
                    if(numNo // qui == 1):
                        return self.n2wNo(numNo // qui) + " oktillion"
                    else:
                        return self.n2wNo(numNo // qui) + " oktillioner"
                else:
                    if(numNo // qui == 1):
                        return self.n2wNo(numNo // qui) + " oktillion, " + self.n2wNo(numNo % qui)
                    else:
                        return self.n2wNo(numNo // qui) + " oktillioner, " + self.n2wNo(numNo % qui)

        if (numNo < sep):
            if (self.localeScaleFlag == True):
                if (numNo % sed == 0):
                    if(numNo // sed == 1):
                        return self.n2wNo(numNo // sed) + " sexdesillion"
                    else:
                        return self.n2wNo(numNo // sed) + " sexdesillioner"
                else:
                    if(numNo // sed == 1):
                        return self.n2wNo(numNo // sed) + " sexdesillion, " + self.n2wNo(numNo % sed)
                    else:
                        return self.n2wNo(numNo // sed) + " sexdesillioner, " + self.n2wNo(numNo % sed)
            else:
                if (numNo % sed == 0):
                    if(numNo // sed == 1):
                        return self.n2wNo(numNo // sed) + " oktilliard"
                    else:
                        return self.n2wNo(numNo // sed) + " oktilliarder"
                else:
                    if(numNo // sed == 1):
                        return self.n2wNo(numNo // sed) + " oktilliard, " + self.n2wNo(numNo % sed)
                    else:
                        return self.n2wNo(numNo // sed) + " oktilliarder, " + self.n2wNo(numNo % sed)

        if (numNo < ocd):
            if (self.localeScaleFlag == True):
                if (numNo % sep == 0):
                    if(numNo // sep == 1):
                        return self.n2wNo(numNo // sep) + " septendesillion"
                    else:
                        return self.n2wNo(numNo // sep) + " septendesillioner"
                else:
                    if(numNo // sep == 1):
                        return self.n2wNo(numNo // sep) + " septendesillion, " + self.n2wNo(numNo % sep)
                    else:
                        return self.n2wNo(numNo // sep) + " septendesillioner, " + self.n2wNo(numNo % sep)
            else:
                if (numNo % sep == 0):
                    if(numNo // sep == 1):
                        return self.n2wNo(numNo // sep) + " nonillion"
                    else:
                        return self.n2wNo(numNo // sep) + " nonillioner"
                else:
                    if(numNo // sep == 1):
                        return self.n2wNo(numNo // sep) + " nonillion, " + self.n2wNo(numNo % sep)
                    else:
                        return self.n2wNo(numNo // sep) + " nonillioner, " + self.n2wNo(numNo % sep)

        if (numNo < nov):
            if (self.localeScaleFlag == True):
                if (numNo % ocd == 0):
                    if(numNo // ocd == 1):
                        return self.n2wNo(numNo // ocd) + " oktodesillion"
                    else:
                        return self.n2wNo(numNo // ocd) + " oktodesillioner"
                else:
                    if(numNo // ocd == 1):
                        return self.n2wNo(numNo // ocd) + " oktodesillion, " + self.n2wNo(numNo % ocd)
                    else:
                        return self.n2wNo(numNo // ocd) + " oktodesillioner, " + self.n2wNo(numNo % ocd)
            else:
                if (numNo % ocd == 0):
                    if(numNo // ocd == 1):
                        return self.n2wNo(numNo // ocd) + " nonilliard"
                    else:
                        return self.n2wNo(numNo // ocd) + " nonilliarder"
                else:
                    if(numNo // ocd == 1):
                        return self.n2wNo(numNo // ocd) + " nonilliard, " + self.n2wNo(numNo % ocd)
                    else:
                        return self.n2wNo(numNo // ocd) + " nonilliarder, " + self.n2wNo(numNo % ocd)

        if (numNo < vin):
            if (self.localeScaleFlag == True):
                if (numNo % nov == 0):
                    if(numNo // nov == 1):
                        return self.n2wNo(numNo // nov) + " novemdesillion"
                    else:
                        return self.n2wNo(numNo // nov) + " novemdesillioner"
                else:
                    if(numNo // nov == 1):
                        return self.n2wNo(numNo // nov) + " novemdesillion, " + self.n2wNo(numNo % nov)
                    else:
                        return self.n2wNo(numNo // nov) + " novemdesillioner, " + self.n2wNo(numNo % nov)
            else:
                if (numNo % nov == 0):
                    if(numNo // nov == 1):
                        return self.n2wNo(numNo // nov) + " desillion"
                    else:
                        return self.n2wNo(numNo // nov) + " desillioner"
                else:
                    if(numNo // nov == 1):
                        return self.n2wNo(numNo // nov) + " desillion, " + self.n2wNo(numNo % nov)
                    else:
                        return self.n2wNo(numNo // nov) + " desillioner, " + self.n2wNo(numNo % nov)

        if (numNo < unv):
            if (self.localeScaleFlag == True):
                if (numNo % vin == 0):
                    if(numNo // vin == 1):
                        return self.n2wNo(numNo // vin) + " vigintillion"
                    else:
                        return self.n2wNo(numNo // vin) + " vigintillioner"
                else:
                    if(numNo // vin == 1):
                        return self.n2wNo(numNo // vin) + " vigintillion, " + self.n2wNo(numNo % vin)
                    else:
                        return self.n2wNo(numNo // vin) + " vigintillioner, " + self.n2wNo(numNo % vin)
            else:
                if (numNo % vin == 0):
                    if(numNo // vin == 1):
                        return self.n2wNo(numNo // vin) + " desilliard"
                    else:
                        return self.n2wNo(numNo // vin) + " desilliarder"
                else:
                    if(numNo // vin == 1):
                        return self.n2wNo(numNo // vin) + " desilliard, " + self.n2wNo(numNo % vin)
                    else:
                        return self.n2wNo(numNo // vin) + " desilliarder, " + self.n2wNo(numNo % vin)

        if (numNo < duv):
            if (self.localeScaleFlag == True):
                if (numNo % unv == 0):
                    if(numNo // unv == 1):
                        return self.n2wNo(numNo // unv) + " unvigintillion"
                    else:
                        return self.n2wNo(numNo // unv) + " unvigintillioner"
                else:
                    if(numNo // unv == 1):
                        return self.n2wNo(numNo // unv) + " unvigintillion, " + self.n2wNo(numNo % unv)
                    else:
                        return self.n2wNo(numNo // unv) + " unvigintillioner, " + self.n2wNo(numNo % unv)
            else:
                if (numNo % unv == 0):
                    if(numNo // unv == 1):
                        return self.n2wNo(numNo // unv) + " undesillion"
                    else:
                        return self.n2wNo(numNo // unv) + " undesillioner"
                else:
                    if(numNo // unv == 1):
                        return self.n2wNo(numNo // unv) + " undesillion, " + self.n2wNo(numNo % unv)
                    else:
                        return self.n2wNo(numNo // unv) + " undesillioner, " + self.n2wNo(numNo % unv)

        if (numNo < trv):
            if (self.localeScaleFlag == True):
                if (numNo % duv == 0):
                    if(numNo // duv == 1):
                        return self.n2wNo(numNo // duv) + " dovigintillion"
                    else:
                        return self.n2wNo(numNo // duv) + " dovigintillioner"
                else:
                    if(numNo // duv == 1):
                        return self.n2wNo(numNo // duv) + " dovigintillion, " + self.n2wNo(numNo % duv)
                    else:
                        return self.n2wNo(numNo // duv) + " dovigintillioner, " + self.n2wNo(numNo % duv)
            else:
                if (numNo % duv == 0):
                    if(numNo // duv == 1):
                        return self.n2wNo(numNo // duv) + " undesilliard"
                    else:
                        return self.n2wNo(numNo // duv) + " undesilliarder"
                else:
                    if(numNo // duv == 1):
                        return self.n2wNo(numNo // duv) + " undesilliard, " + self.n2wNo(numNo % duv)
                    else:
                        return self.n2wNo(numNo // duv) + " undesilliarder, " + self.n2wNo(numNo % duv)

        if (numNo < qtv):
            if (self.localeScaleFlag == True):
                # print(numNo)
                if (numNo % trv == 0):
                    if(numNo // trv == 1):
                        return self.n2wNo(numNo // trv) + " trevigintillion"
                    else:
                        return self.n2wNo(numNo // trv) + " trevigintillioner"
                else:
                    if(numNo // trv == 1):
                        return self.n2wNo(numNo // trv) + " trevigintillion, " + self.n2wNo(numNo % trv)
                    else:
                        return self.n2wNo(numNo // trv) + " trevigintillioner, " + self.n2wNo(numNo % trv)
            else:
                if (numNo % trv == 0):
                    if(numNo // trv == 1):
                        return self.n2wNo(numNo // trv) + " dodesillion"
                    else:
                        return self.n2wNo(numNo // trv) + " dodesillioner"
                else:
                    if(numNo // trv == 1):
                        return self.n2wNo(numNo // trv) + " dodesillion, " + self.n2wNo(numNo % trv)
                    else:
                        return self.n2wNo(numNo // trv) + " dodesillioner, " + self.n2wNo(numNo % trv)

        if (numNo < qiv):
            if (self.localeScaleFlag == True):
                # print(numNo)
                if (numNo % qtv == 0):
                    if(numNo // qtv == 1):
                        return self.n2wNo(numNo // qtv) + " quattorvigintillion"
                    else:
                        return self.n2wNo(numNo // qtv) + " quattorvigintillioner"
                else:
                    if(numNo // qtv == 1):
                        return self.n2wNo(numNo // qtv) + " quattorvigintillion, " + self.n2wNo(numNo % qtv)
                    else:
                        return self.n2wNo(numNo // qtv) + " quattorvigintillioner, " + self.n2wNo(numNo % qtv)
            else:
                if (numNo % qtv == 0):
                    if(numNo // qtv == 1):
                        return self.n2wNo(numNo // qtv) + " dodesilliard"
                    else:
                        return self.n2wNo(numNo // qtv) + " dodesilliarder"
                else:
                    if(numNo // qtv == 1):
                        return self.n2wNo(numNo // qtv) + " dodesilliard, " + self.n2wNo(numNo % qtv)
                    else:
                        return self.n2wNo(numNo // qtv) + " dodesilliarder, " + self.n2wNo(numNo % qtv)

        if (numNo < ssv):
            if (self.localeScaleFlag == True):
                # print(numNo)
                if (numNo % qiv == 0):
                    if(numNo // qiv == 1):
                        return self.n2wNo(numNo // qiv) + " kvintvigintillion"
                    else:
                        return self.n2wNo(numNo // qiv) + " kvintvigintillioner"
                else:
                    if(numNo // qiv == 1):
                        return self.n2wNo(numNo // qiv) + " kvintvigintillion, " + self.n2wNo(numNo % qiv)
                    else:
                        return self.n2wNo(numNo // qiv) + " kvintvigintillioner, " + self.n2wNo(numNo % qiv)
            else:
                if (numNo % qiv == 0):
                    if(numNo // qiv == 1):
                        return self.n2wNo(numNo // qiv) + " tredesillion"
                    else:
                        return self.n2wNo(numNo // qiv) + " tredesillioner"
                else:
                    if(numNo // qiv == 1):
                        return self.n2wNo(numNo // qiv) + " tredesillion, " + self.n2wNo(numNo % qiv)
                    else:
                        return self.n2wNo(numNo // qiv) + " tredesillioner, " + self.n2wNo(numNo % qiv)

        if (numNo < spv):
            if (self.localeScaleFlag == True):
                # print(numNo)
                if (numNo % ssv == 0):
                    if(numNo // ssv == 1):
                        return self.n2wNo(numNo // ssv) + " sexvigintillion"
                    else:
                        return self.n2wNo(numNo // ssv) + " sexvigintillioner"
                else:
                    if(numNo // ssv == 1):
                        return self.n2wNo(numNo // ssv) + " sexvigintillion, " + self.n2wNo(numNo % ssv)
                    else:
                        return self.n2wNo(numNo // ssv) + " sexvigintillioner, " + self.n2wNo(numNo % ssv)
            else:
                if (numNo % ssv == 0):
                    if(numNo // ssv == 1):
                        return self.n2wNo(numNo // ssv) + " tredesilliard"
                    else:
                        return self.n2wNo(numNo // ssv) + " tredesilliarder"
                else:
                    if(numNo // ssv == 1):
                        return self.n2wNo(numNo // ssv) + " tredesilliard, " + self.n2wNo(numNo % ssv)
                    else:
                        return self.n2wNo(numNo // ssv) + " tredesilliarder, " + self.n2wNo(numNo % ssv)

        if (numNo < spvg):
            if (self.localeScaleFlag == True):
                # print(numNo)
                if (numNo % spv == 0):
                    if(numNo // spv == 1):
                        return self.n2wNo(numNo // spv) + " septenvigintillion"
                    else:
                        return self.n2wNo(numNo // spv) + " septenvigintillioner"
                else:
                    if(numNo // spv == 1):
                        return self.n2wNo(numNo // spv) + " septenvigintillion, " + self.n2wNo(numNo % spv)
                    else:
                        return self.n2wNo(numNo // spv) + " septenvigintillioner, " + self.n2wNo(numNo % spv)
            else:
                if (numNo % spv == 0):
                    if(numNo // spv == 1):
                        return self.n2wNo(numNo // spv) + " quattordesillion"
                    else:
                        return self.n2wNo(numNo // spv) + " quattordesillioner"
                else:
                    if(numNo // spv == 1):
                        return self.n2wNo(numNo // spv) + " quattordesillion, " + self.n2wNo(numNo % spv)
                    else:
                        return self.n2wNo(numNo // spv) + " quattordesillioner, " + self.n2wNo(numNo % spv)

        if (numNo < kvde):
            if (self.localeScaleFlag == True):

                if (numNo % spvg == 0):
                    if(numNo // spvg == 1):
                        return self.n2wNo(numNo // spvg ) + " octovigintillion"
                    else:
                        return self.n2wNo(numNo // spvg ) + " octovigintillioner"
                else:
                    if(numNo // spvg == 1):
                        return self.n2wNo(numNo // spvg ) + " octovigintillion, " + self.n2wNo(numNo % spvg)
                    else:
                        return self.n2wNo(numNo // spvg ) + " octovigintillioner, " + self.n2wNo(numNo % spvg)
            else:
                if (numNo % spvg == 0):
                    if(numNo // spvg == 1):
                        return self.n2wNo(numNo // spvg ) + " quattuordesilliard"
                    else:
                        return self.n2wNo(numNo // spvg ) + " quattuordesilliarder"
                else:
                    if(numNo // spvg == 1):
                        return self.n2wNo(numNo // spvg ) + " quattuordesilliard, " + self.n2wNo(numNo % spvg)
                    else:
                        return self.n2wNo(numNo // spvg ) + " quattuordesilliarder, " + self.n2wNo(numNo % spvg)

        if (numNo < kvdil):
            if (self.localeScaleFlag == True):

                if (numNo % kvde == 0):
                    if(numNo // kvde == 1):
                        return self.n2wNo(numNo // kvde ) + " novemvigintillion"
                    else:
                        return self.n2wNo(numNo // kvde ) + " novemvigintillioner"
                else:
                    if(numNo // kvde == 1):
                        return self.n2wNo(numNo // kvde ) + " novemvigintillion, " + self.n2wNo(numNo % kvde)
                    else:
                        return self.n2wNo(numNo // kvde ) + " novemvigintillioner, " + self.n2wNo(numNo % kvde)
            else:
                if (numNo % kvde == 0):
                    if(numNo // kvde == 1):
                        return self.n2wNo(numNo // kvde ) + " kvindesillion"
                    else:
                        return self.n2wNo(numNo // kvde ) + " kvindesillioner"
                else:
                    if(numNo // kvde == 1):
                        return self.n2wNo(numNo // kvde ) + " kvindesillion, " + self.n2wNo(numNo % kvde)
                    else:
                        return self.n2wNo(numNo // kvde ) + " kvindesillioner, " + self.n2wNo(numNo % kvde)

        if (numNo < sedec):
            if (self.localeScaleFlag == True):

                if (numNo % kvdil == 0):
                    if(numNo // kvdil == 1):
                        return self.n2wNo(numNo // kvdil ) + " trigintillion"
                    else:
                        return self.n2wNo(numNo // kvdil ) + " trigintillioner"
                else:
                    if(numNo // kvdil == 1):
                        return self.n2wNo(numNo // kvdil ) + " trigintillion, " + self.n2wNo(numNo % kvdil)
                    else:
                        return self.n2wNo(numNo // kvdil ) + " trigintillioner, " + self.n2wNo(numNo % kvdil)
            else:
                if (numNo % kvdil == 0):
                    if(numNo // kvdil == 1):
                        return self.n2wNo(numNo // kvdil ) + " kvindesilliard"
                    else:
                        return self.n2wNo(numNo // kvdil ) + " kvindesilliarder"
                else:
                    if(numNo // kvdil == 1):
                        return self.n2wNo(numNo // kvdil ) + " kvindesilliard, " + self.n2wNo(numNo % kvdil)
                    else:
                        return self.n2wNo(numNo // kvdil ) + " kvindesilliarder, " + self.n2wNo(numNo % kvdil)

        if (numNo < sedil):
            if (self.localeScaleFlag == True):

                if (numNo % sedec == 0):
                    if(numNo // sedec == 1):
                        return self.n2wNo(numNo // sedec ) + " untrigintillion"
                    else:
                        return self.n2wNo(numNo // sedec ) + " untrigintillioner"
                else:
                    if(numNo // sedec == 1):
                        return self.n2wNo(numNo // sedec ) + " untrigintillion, " + self.n2wNo(numNo % sedec)
                    else:
                        return self.n2wNo(numNo // sedec ) + " untrigintillioner, " + self.n2wNo(numNo % sedec)
            else:
                if (numNo % sedec == 0):
                    if(numNo // sedec == 1):
                        return self.n2wNo(numNo // sedec ) + " seksdesillion"
                    else:
                        return self.n2wNo(numNo // sedec ) + " seksdesillioner"
                else:
                    if(numNo // sedec == 1):
                        return self.n2wNo(numNo // sedec ) + " seksdesillion, " + self.n2wNo(numNo % sedec)
                    else:
                        return self.n2wNo(numNo // sedec ) + " seksdesillioner, " + self.n2wNo(numNo % sedec)

        if (numNo < sepec):
            if (self.localeScaleFlag == True):
                if (numNo % sedil == 0):
                    if(numNo // sedil == 1):
                        return self.n2wNo(numNo // sedil ) + " duotrigintillion"
                    else:
                        return self.n2wNo(numNo // sedil ) + " duotrigintillioner"
                else:
                    if(numNo // sedil == 1):
                        return self.n2wNo(numNo // sedil ) + " duotrigintillion, " + self.n2wNo(numNo % sedil)
                    else:
                        return self.n2wNo(numNo // sedil ) + " duotrigintillioner, " + self.n2wNo(numNo % sedil)
            else:
                # print(":::1:::",(numNo % sedil))
                # print(":::1:::",(numNo // sedil))
                if (numNo % sedil == 0):
                    if(numNo // sedil == 100):
                        return self.n2wNo(numNo // sedil ) + " seksdesilliarder [ti googler/gogoler]"
                    if(numNo // sedil == 10):
                        return self.n2wNo(numNo // sedil ) + " seksdesilliarder [en google/gogol]"
                    if(numNo // sedil == 1):
                        return self.n2wNo(numNo // sedil ) + " seksdesilliard"
                    else:
                        return self.n2wNo(numNo // sedil ) + " seksdesilliarder"
                else:
                    if(numNo // sedil == 100):
                        return self.n2wNo(numNo // sedil ) + " seksdesilliarder [ti googler/gogoler], " + self.n2wNo(numNo % sedil)
                    if(numNo // sedil == 10):
                        return self.n2wNo(numNo // sedil ) + " seksdesilliarder [en google/gogol], " + self.n2wNo(numNo % sedil)
                    if(numNo // sedil == 1):
                        return self.n2wNo(numNo // sedil ) + " seksdesilliard, " + self.n2wNo(numNo % sedil)
                    else:
                        return self.n2wNo(numNo // sedil ) + " seksdesilliarder, " + self.n2wNo(numNo % sedil)

        if (numNo < sepil):
            if (self.localeScaleFlag == True):
                if (numNo % sepec == 0):
                    if(numNo // sepec == 1):
                        return self.n2wNo(numNo // sepec ) + " trestrigintillion"
                    else:
                        return self.n2wNo(numNo // sepec ) + " trestrigintillioner"
                else:
                    if(numNo // sepec == 1):
                        return self.n2wNo(numNo // sepec ) + " trestrigintillion, " + self.n2wNo(numNo % sepec)
                    else:
                        return self.n2wNo(numNo // sepec ) + " trestrigintillioner, " + self.n2wNo(numNo % sepec)
            else:
                # print(":::1:::",(numNo % sepec))
                # print(":::1:::",(numNo // sepec))
                if (numNo % sepec == 0):
                    if(numNo // sepec == 1):
                        return self.n2wNo(numNo // sepec ) + " septendesillion"
                    else:
                        return self.n2wNo(numNo // sepec ) + " septendesillioner"
                else:
                    if(numNo // sepec == 1):
                        return self.n2wNo(numNo // sepec ) + " septendesillion, " + self.n2wNo(numNo % sepec)
                    else:
                        return self.n2wNo(numNo // sepec ) + " septendesillioner, " + self.n2wNo(numNo % sepec)

        if (numNo < octec):
            if (self.localeScaleFlag == True):
                if (numNo % sepil == 0):
                    if(numNo // sepil == 1):
                        return self.n2wNo(numNo // sepil ) + " quattuortrigintillion"
                    else:
                        return self.n2wNo(numNo // sepil ) + " quattuortrigintillioner"
                else:
                    if(numNo // sepil == 1):
                        return self.n2wNo(numNo // sepil ) + " quattuortrigintillion, " + self.n2wNo(numNo % sepil)
                    else:
                        return self.n2wNo(numNo // sepil ) + " quattuortrigintillioner, " + self.n2wNo(numNo % sepil)
            else:
                # print(":::1:::",(numNo % sepil))
                # print(":::1:::",(numNo // sepil))
                if (numNo % sepil == 0):
                    if(numNo // sepil == 1):
                        return self.n2wNo(numNo // sepil ) + " septendesilliard"
                    else:
                        return self.n2wNo(numNo // sepil ) + " septendesilliarder"
                else:
                    if(numNo // sepil == 1):
                        return self.n2wNo(numNo // sepil ) + " septendesilliard, " + self.n2wNo(numNo % sepil)
                    else:
                        return self.n2wNo(numNo // sepil ) + " septendesilliarder, " + self.n2wNo(numNo % sepil)






# ### ------------------------------------------------------------------------------------------------------------------------------------------ ###
#
# ### ------------------------------------------------------------------------------------------------------------------------------------------ ###



    def fix_float_string(self,string):

        if ( "," in string and '.' not in string ) and string.count(',') == 1:
            string = string.replace(",",".")
            # print("SWITCHED NUM",string)

        elif ( "," in string and '.' not in string ) and string.count(',') >= 2:
            string = string.replace(",","")

        elif ( "," in string and '.' in string ):
            string = string.replace(",","")

        return string

    def count_leading_zeroes(self,string):
        # is_float        = False
        zeroes        = []
        for x in string:
            if x and x.isnumeric():
                ix = int(x)
                if ix == 0:
                    zeroes.append(ix)
                else:
                    break
            else:
                break
        return zeroes

    def _split_float_into_ints(self,string,divider):

        _test = string.split(divider)
        for t in _test:
            # is_int      = False
            try:        int(t)
            except:     pass
            else:       yield int(t)

    def _split_float_into_strings(self,string,divider):

        _test = string.split(divider)
        for t in _test:
            # is_int      = False
            try:        int(t)
            except:     pass
            else:       yield t

    def preprocessed(self):

        if type(self._num) is float or ( type(self._num) is str and "." in self._num ):

            _float = []
            _float_strings = ()
            str_num = ""
            zero_string = ""


            def apply_and_out_float(string):
                sp = string.split(',')
                bas_ =sp[0:-1]
                end_ = sp.pop()
                end_ = end_.strip()
                sep = ""
                # print(bas_)
                if self. lang == 2:
                    sep = "and"
                else:
                    sep = "og"

                # if self.get_numeric(f"{self._num}") > 10000:
                    # print(f"APPLYING FLOAT STRING # 1: {string}")
                if len(bas_) and f" {sep} " not in end_ and self.easyreadFlag:
                    return f"{','.join(bas_)} — {sep} {end_}"
                elif len(bas_) and f" {sep} " not in end_ and not self.easyreadFlag:
                    return f"{','.join(bas_)}, {end_}"
                elif len(bas_) and f" {sep} " in end_:
                    return f"{','.join(bas_)}, {end_}"
                else:
                    return f"{end_}"
                # elif len(bas_) and f" {sep} " in end_:
                #     # print(f"APPLYING FLOAT STRING # 2: {string}")
                #     return f"{','.join(bas_)}, {end_}"
                # else:
                #     # print(f"APPLYING FLOAT STRING # 3: {string}")
                #     return f",{end_}"

            # print(f"str_num {str_num}")
            str_num = f"{self._num}"
            str_num = self.fix_float_string(str_num,)
            # print(f"str_num {str_num}")
            # print(str_num)

            if '.' in str_num:
                _float = [x for x in self._split_float_into_ints(str_num,'.')]
                _float_strings = [x for x in self._split_float_into_strings(str_num,'.')]
                # print(_float)


            if len(_float_strings) and len(_float_strings) == 2:
                # print()

                _b, _f,     = _float
                _lz         = self.count_leading_zeroes(_float_strings[1])
                # print     (_lz)

                for x in _lz:
                    if self. lang == 2:
                        zero_string += f"{self.n2w(0).strip()}, "
                    else:
                        zero_string += f"{self.n2wNo(0).strip()}, "

                if zero_string:
                    zero_string = zero_string.strip()
                    if len(_lz) > 1:
                        zero_string = f"{zero_string[0:-1]} ({len(_lz)}), "
                    else:
                        zero_string = f"{zero_string[0:-1]}, "

                if self. lang == 2:
                    stem = f"{self.n2w(_f)}"
                    if stem.strip() != "null":
                        stem = f"{zero_string}{stem}"
                    out = f"{self.n2w(_b)} .POINT. {stem}"
                    out_base , out_frac = out.split('.POINT.')
                    out_base = apply_and_out_float(out_base)
                    out = f"{out_base.strip()} .POINT. {out_frac.strip()}"

                    return  out

                else:
                    stem = f"{self.n2wNo(_f)}"
                    if stem.strip() != "null":
                        stem = f"{zero_string}{stem}"
                    out = f"{self.n2wNo(_b)} .PUNKT. {stem}"
                    out_base , out_frac =out.split('.PUNKT.')
                    out_base = apply_and_out_float(out_base)
                    out = f"{out_base.strip()} .PUNKT. {out_frac.strip()}"

                    return  out


        elif type(self._num) is str and "." not in self._num:
            try:
                self._num = int(self._num)
            except:
                raise TypeError( f"::: Could'nt convert {self._num} to int :::" )
            else:

                if self. lang == 2:
                    return  f"{self.n2w(self._num)}"
                else:
                    return  f"{self.n2wNo(self._num)}"

        else:

            if self. lang == 2:
                return  f"{self.n2w(self._num)}"
            else:
                return  f"{self.n2wNo(self._num)}"

        return ""

    def get_lang(self):
        # print("\n::: INSIDE Num2Text.py : get_lang()::: \n")
        out = []

        if isinstance(self.numbers,list) or isinstance(self.numbers,tuple):
            for x in self.numbers:
                if isinstance(x,str):
                    num,test_num = make_test_num(x)
                    if test_num == None:
                        continue
                elif isinstance(x,int) or isinstance(x,float):
                    num = x
                else:
                    continue


                self._num = num
                finalOut = self.preprocessed()
                langnum = self.lang
                lpoint = "."

                if langnum == 1:
                    lsep = " og "
                    lpoint = " .PUNKT. "
                else:
                    lsep = " and "
                    lpoint = ".POINT."

                finalOut = self.postProcessText(finalOut,lsep,lpoint,self.newline,self.easyreadFlag)

                out.append( finalOut )

            return out

        elif isinstance(self.numbers,int) or isinstance(self.numbers,float):
            self._num = self.numbers
            finalOut = self.preprocessed()
            langnum = self.lang
            lpoint = "."

            if langnum == 1:
                lsep = " og "
                lpoint = " .PUNKT. "
            else:
                lsep = " and "
                lpoint = ".POINT."

            finalOut = self.postProcessText(finalOut,lsep,lpoint,self.newline,self.easyreadFlag)

            out.append( finalOut )

        elif isinstance(self.numbers,str):
            num,test_num = make_test_num(self.numbers)

            if test_num == None:
                print(f"Num2Text.number is not a valid number: {num}")
            else:
                self._num = num
                finalOut = self.preprocessed()
                langnum = self.lang
                lpoint = "."

                if langnum == 1:
                    lsep = " og "
                    lpoint = " .PUNKT. "
                else:
                    lsep = " and "
                    lpoint = ".POINT."

                finalOut = self.postProcessText(finalOut,lsep,lpoint,self.newline,self.easyreadFlag)

                out.append( finalOut )

        return out

    def get_numeric(self,strn):
        _int = None
        _float = None
        _float_strings = []
        str_num = self.fix_float_string(strn,)
        # print(f"str_num {str_num}")
        # print(str_num)

        if '.' in str_num:
            # _float = [x for x in self._split_float_into_ints(str_num,'.')]
            _float_strings = [x for x in self._split_float_into_strings(str_num,'.')]
            _float = ".".join(_float_strings).strip()
            try:
                _float = float(_float)
            except:
                pass
        else:
            try:
                _int = int(strn)
            except:
                pass

            # print(_float)

        if isinstance(_float,float):
            return _float
        elif isinstance(_int,int):
            return _int

    def postProcessText(self,text,lsep,lpoint,newline,easyread):
        # ----------------------------------------
        def append_language_separator(text,lsep):
            out = text
            split = text.split(",")
            lsep = lsep.strip()

            if len(split) > 1 and split[-1] != "":
                pre = split[:-1]
                tail = split[-1].strip()
                prestr = ",".join(pre)

                if  " " in tail and f" {lsep} " not in tail:
                    # print(f"APPENDING {lsep} # 1")
                    tsplit = tail.split(" ")
                    tend = tsplit.pop(-1)
                    tpre = " ".join(tsplit)
                    fixedtail = f"{tpre.strip()} {lsep} {tend}"

                elif f" {lsep} " not in prestr:
                    # print(f"APPENDING {lsep} # 2")
                    fixedtail = f"{lsep} {tail}"

                else:
                    # print(f"APPENDING {lsep} # 3")
                    # fixedtail = f"{lsep} {tail}"
                    fixedtail = f"{tail}"

                out = f"{prestr}, {fixedtail}"

            return out.strip()
        # ----------------------------------------


        # ----------------------------------------
        def use_newline(text,lpoint):
            # ----------------------------------------
            def joinstring(string):

                if ',' in string:
                    stringsplit = [x.strip() for x in string.split(',')]

                    if stringsplit:
                        string = '\n'.join(stringsplit)

                return string
            # ----------------------------------------

            psplit = text.split(lpoint)
            if len(psplit) == 2 and psplit[-1] != "":

                pre = psplit[0]
                tail = psplit[-1]

                if pre:
                    pre = joinstring(pre)

                if tail:
                    tail = joinstring(tail)

                if pre and tail:
                    text = f"{pre}\n\n{lpoint.strip()}\n\n{tail}"

            else:
                text = joinstring(text)


            return text
        # ----------------------------------------
        # if self.get_numeric(f"{self._num}") > 10000:
        if ("." not in text
            and lsep not in text
            and "," in text
        ):
            text = append_language_separator(text,lsep)
        if lpoint in text:
            text = append_language_separator(text,lsep)


        if "," in text and newline:
            text = use_newline(text,lpoint)


        return text.strip()

def get_locale_scale(loc,scale):

    # ### --- DETERMINE IF WE OVERRIDE LOCALE SCALE

    if loc in LOC_PELETIER:
        if scale == "shortscale":
            return True
        else:
            return False

    if loc == 1: # ### NORWEGIAN LANGUAGE NUMBER
        if scale == "shortscale":
            return True
        else:
            return False

    if loc in LOC_SHORT:
        if scale == "peletier":
            return True
        else:
            return False

    if loc == 2: # ### ENGLISH SHORT SCALE LANGUAGE NUMBER
        if scale == "peletier":
            return True
        else:
            return False





def make_test_num(num):
    test_num = None
    if ( "," in num and '.' not in num ) and num.count(',') == 1:
        num = num.replace(",",".")
        # print("SWITCHED NUM",num)

    elif ( "," in num and '.' in num ) and num.count(',') > 0:
        num = num.replace(",","")
        # print("SWITCHED NUM",num)

    try:
        test_num  = int(num.replace(' ',''))

    except: pass
    else:
        num = num.replace(' ','')

    if test_num == None:
        try:
            test_num    = float(num.replace(' ',''))
        except: pass
        else:
            num = num.replace(' ','')
    # print("MAKE NUM",num)
    return [num,test_num]



if __name__ == '__main__':
    import argparse

    separator = "–––——————————————————————————————————–––"

    # Create the parser
    parser = argparse.ArgumentParser(description="Num2Text : Turns numbers into text!")

    parser.add_argument('-n','-num','-nums','-numbers','--numbers','--number'
                        , nargs='+'
                        , help='Number(s) to spell out'
                        )
    parser.add_argument('-nl','-newline','--newline'
                        , action="store_true" , default=False
                        , help='Replace "," with [NEWLINE]'
                        )
    parser.add_argument('-l','-lan','-lang','-language','--language'
                        , default="en"
                        , help='Select language: English,norwegian'
                        )
    parser.add_argument('-p','-pel','-peletier','--peletier'
                        , action="store_true" , default=False
                        , help='Use peletier (long scale)'
                        )
    parser.add_argument('-ss','-short','-shortscale','--shortscale','--short_scale'
                        , action="store_true" , default=False
                        , help='Use U.S.A / Canada / etc. -system (short scale)'
                        )
    parser.add_argument('-e','-er','--easyread','--easy_reading'
                        ,'-o','--oversiktlig'
                        ,'-r','-ir','--improved_readability'
                        , action="store_true" , default=False
                        , help='Make output (slightly) more readable'
                        )

    # Add an argument that collects a list
    args, unknown = parser.parse_known_args()
    argsnumbers = []
    argslanguage = args.language.lower()

    peletier = args.peletier
    shortscale = args.shortscale
    argseasyread = args.easyread
    newline = args.newline

    localescale = False

    if args.numbers:
        argsnumbers = args.numbers
    nums = [*argsnumbers,*unknown]

    if nums:
        textlist  = Num2Text(   lang=argslanguage
                                ,numbers=nums
                                ,localeScaleFlag=localescale
                                ,newline=newline
                                ,peletier=peletier
                                ,shortscale=shortscale
                                ,easyreadFlag=argseasyread

                            ).get_lang()
        if textlist:
            for text in textlist:
                print(separator) # SEP

                print(text)

                print(separator) # SEP

# Zombies
#
# def make_test_num(num):
#     test_num = None
#     if ( "," in num and '.' not in num ) and num.count(',') == 1:
#         num = num.replace(",",".")
#         # print("SWITCHED NUM",num)
#
#     elif ( "," in num and '.' in num ) and num.count(',') > 0:
#         num = num.replace(",","")
#         # print("SWITCHED NUM",num)
#
#     try:
#         test_num  = int(num.replace(' ',''))
#
#     except: pass
#     else:
#         num = num.replace(' ','')
#
#     if test_num == None:
#         try:
#             test_num    = float(num.replace(' ',''))
#         except: pass
#         else:
#             num = num.replace(' ','')
#     # print("MAKE NUM",num)
#     return [num,test_num]
#
#
# def fix_my_fucking_args(*args):
#
#     import decimal
#     from decimal import Decimal
#     clean_args = []
#     if args:
#         for arg in args:
#             if type(arg) is str:
#
#                 new = arg.replace(" ","")
#
#                 if ( "," in new and '.' not in new ) and new.count(',') == 1:
#                     new = new.replace(",",".")
#
#                 elif ( "," in new and '.' in new ):
#                     new = new.replace(",","")
#
#                 # if '.' not in new and new.isnumeric():
#                 #     new = int(new)
#
#                 clean_args.append(new)
#
#             elif type(arg) is int:
#                 test_int_string = f"{arg}"
#                 if "e" in test_int_string:
#                     print(":: Num2Text.fix_my_fucking_args :: ARG IS INT",arg)
#                 clean_args.append(arg)
#
#             if type(arg) is float:
#                 # default_prec = 1
#                 test_res = f"{Decimal(arg)}"
#                 if "E" in test_res.lower():
#
#                     with decimal.localcontext(prec=4299) as ctx:
#                         test_res = f"{Decimal(arg) * 1}"
#
#                         # print("default_prec",default_prec)
#
#                 clean_args.append(test_res)
#
#
#     if len(clean_args):
#         return clean_args
#     else:
#         return args
#                    # print("SWITCHED NUM",new)

