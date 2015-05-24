function HeaderFader(tagName, colors)
{
        this.tagName = tagName; // Pass "h1" or similar.
        this.colors = colors; // An array of colours in order.
        this.left = true; // false for right-aligned.
        this.frames = 20;
        this.elements = [];

        var obj = this;
        if (window.addEventListener) {
                window.addEventListener('load', function() {
                        obj.setup();
                }, false);
        } else {
                var oldOnload = window.onload;
                window.onload = function() {
                        if (oldOnload) oldOnload();
                        obj.setup();
                }
        }
};

HeaderFader.prototype.setup = function() {
        this.elements = document.getElementsByTagName(this.tagName);
        for (var h = 0; h < this.elements.length; h++) {
                var h1 = this.elements[h],
                        text = h1.firstChild.nodeValue;
                h1.removeChild(h1.firstChild);
                h1.animNodes = [];
                for (var i = 0; i < text.length; i++) {
                        var span = document.createElement('span');
                        span.appendChild(document.createTextNode(text.substring(i, i+1)));
                        h1.appendChild(span);
                        h1.animNodes[h1.animNodes.length] = span;
                }
                h1.animCount = 0;
                var obj = this;
                h1.animTimer = setInterval((function(hh) {
                        return function() {
                                obj.animate(hh);
                        }
                }(h)), 50);
        }
};

HeaderFader.prototype.animate = function(h) {
        var h1 = this.elements[h], c = h1.animCount++, noAnim = 1;
        for (var i = 0; i < h1.animNodes.length; i++) {
                var s = h1.animNodes[i],
                        pc = (this.left ? (c-i) : (c-(h1.animNodes.length+this.frames-i))),
                        frac = Math.max(0, Math.min(1, pc/this.frames)),
                        marg = document.all && !window.opera ? 'marginRight' : 'marginLeft';
                if (s.animDone) continue;
                noAnim = 0;
                s.style.color = this.colors[Math.floor(frac * 0.99999 * this.colors.length)];
                if (frac == 1) {
                        s.style[marg] = '0';
                        s.animDone = 1;
                } else {
                        s.style[marg] = 0.6*(1-frac) + 'em';
                }
        }
        if (noAnim) {
                clearInterval(h1.animTimer);
        }
        h1.style.visibility = 'inherit';
};

// SCRIPT SETUP
if (document.documentElement)
{
        // Hide H1 elements for animation and trigger show on load.
        document.write('<style type="text/css"> h3 { visibility: hidden } <\/style>');
        // Off we go!
        var h1Anim = new HeaderFader(
                'h3',
                ['#FFFFFF','#F90A0A', '#DDDDDD','#FF0000' '#BBBBBB', '#999999', '#777777', '#555555']
        );
        //h1Anim.left = true; // Try setting to false if using text-align: right;
        //h1Anim.frames = 10;
};