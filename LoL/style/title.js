function HeaderFader(tagName, colors)
{
        this.tagName = tagName; // Pass "h3" or similar.
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
                var h3 = this.elements[h],
                        text = h3.firstChild.nodeValue;
                h3.removeChild(h3.firstChild);
                h3.animNodes = [];
                for (var i = 0; i < text.length; i++) {
                        var span = document.createElement('span');
                        span.appendChild(document.createTextNode(text.substring(i, i+1)));
                        h3.appendChild(span);
                        h3.animNodes[h3.animNodes.length] = span;
                }
                h3.animCount = 0;
                var obj = this;
                h3.animTimer = setInterval((function(hh) {
                        return function() {
                                obj.animate(hh);
                        }
                }(h)), 50);
        }
};

HeaderFader.prototype.animate = function(h) {
        var h3 = this.elements[h], c = h3.animCount++, noAnim = 1;
        for (var i = 0; i < h3.animNodes.length; i++) {
                var s = h3.animNodes[i],
                        pc = (this.left ? (c-i) : (c-(h3.animNodes.length+this.frames-i))),
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
                clearInterval(h3.animTimer);
        }
        h3.style.visibility = 'inherit';
};

// SCRIPT SETUP
if (document.documentElement)
{
        // Hide h3 elements for animation and trigger show on load.
        document.write('<style type="text/css"> h3 { visibility: hidden } <\/style>');
        // Off we go!
        var h3Anim = new HeaderFader(
                'h3',
                ['#09C', '#ff2121', '#201e1e', '#4c4c4c', '#056c22', '#0721a5']
        );
        //h3Anim.left = true; // Try setting to false if using text-align: right;
        //h3Anim.frames = 10;
}