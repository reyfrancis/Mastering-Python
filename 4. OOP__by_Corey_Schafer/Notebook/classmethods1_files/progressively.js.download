/*!
 *  * progressively 1.0.0
 *   * https://github.com/thinker3197/progressively
 *    * @license MIT licensed
 *     *
 *      * Copyright (C) 2016 Ashish
 *       */

;

(function(root, factory) {
    if (typeof define === 'function' && define.amd) {
        define(function() {
            return factory(root);
        });
    } else if (typeof exports === 'object') {
        module.exports = factory;
    } else {
        root.progressively = factory(root);
    }
})(this, function(root) {

    'use strict';

    var progressively = {};

    var defaults, poll, onLoad, inodes;

    onLoad = function() {};

    function extend(primaryObject, secondaryObject) {
        var o = {};
        for (var prop in primaryObject) {
            o[prop] = secondaryObject.hasOwnProperty(prop) ? secondaryObject[prop] : primaryObject[prop];
        }
        return o;
    };

    function isHidden(el) {
        return (el.offsetParent === null);
    };
    function inView(el, view) {
        if (isHidden(el)) {
            return true;
        }

        var box = el.getBoundingClientRect();
        return (
            box.top >= 0 &&
            box.left >= 0 &&
            box.bottom <= (window.innerHeight || document.el.clientHeight) &&
            box.right <= (window.innerWidth || document.el.clientWidth));

    };
    function loadImage(el) {        
        setTimeout(function() {
            var img = new Image();
            img.onload = function() {
                el.classList.remove('progressive-not-loaded');
                el.classList.add('progressive-is-loaded');
               // el.classList.add('zoomable');
                el.src = this.src;
                onLoad(el);
            };
          
            var img_ctype = el.dataset.ctype;
            var img_type = el.dataset.type;
            var img_base = el.dataset.progressive;
            if(img_type == 'gif' || img_ctype == 'C'){
               img.src = img_base + '.'+img_type;
            } else {
               if(webp){ 
                  img.src = img_base + '.'+ 'webp';
               } else {
                  img.src = img_base + '.'+img_type;
               }
            }            
        }, defaults.delay);
    };
    function listen() {
        if (!!poll)
            return;
        clearTimeout(poll);
        poll = setTimeout(function() {
            progressively.check();
            progressively.render();
            poll = null;
        }, defaults.throttle);
    }
    defaults = {
        throttle: 300, //appropriate value, don't change unless intended
        delay: 200,
        onLoadComplete: function() {},
        onLoad: function() {}
    };

    progressively.init = function(options) {
        options = options || {};

        defaults = extend(defaults, options);

        onLoad = defaults.onLoad || onLoad;

        inodes = [].slice.call(document.querySelectorAll('.progressive-img'));

        progressively.render();

        if (document.addEventListener) {
            root.addEventListener('scroll', listen, false);
            root.addEventListener('load', listen, false);
        } else {
            root.attachEvent('onscroll', listen);
            root.attachEvent('onload', listen);
        }
    };
    progressively.render = function() {
        var elem;

        for (var i = inodes.length - 1; i >= 0; --i) {
            elem = inodes[i];

           // if (inView(elem) && elem.classList.contains('progressive-not-loaded')) {
            if ( elem.classList.contains('progressive-not-loaded') || elem.classList.contains('progressive-is-loaded')) {
               
                loadImage(elem);
                inodes.splice(i, 1);
            }
        }
        this.check();
    };
    progressively.check = function() {
        if (!inodes.length) {
            defaults.onLoadComplete();
            this.drop();
        }
    }
    progressively.drop = function() {
        if (document.removeEventListener) {
            root.removeEventListener('scroll', listen);
        } else {
            root.detachEvent('onscroll', listen);
        }
        clearTimeout(poll);
    };

    return progressively;
});

