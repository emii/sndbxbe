Title: Parallax scrolling + fixed header
Date: 2013-06-26
Category: sandbox
Tags: javascript, html/css, web dev
Summary: a snnipet for creating my website's header

The first time I saw this effect was searching for templates for tumblr, well I am not sure anymore, the thing is that it looked pretty cool, you can see it yourself [here](http://anchorage-theme.pixelunion.net/), and it uses varios effects which are kind of trendy nowadays, we can see it on the google+ profiles too. The first of them is the [parallax scrolling](http://en.wikipedia.org/wiki/Parallax_scrolling) which basically means scrolling at different speeds for different elements (i.e. the header scrolls slower than the rest of the content), the second is a css3 feature to modify the opacity of the elements, in the case of _anchorage_ the image disappears while the subsequent fixed element appears. The secret is to connect the scrolling function (_jQuery_) to the opacity. The last effect is going from a floating header to a fixed one, this is also pretty straightforward using _jQuery_ and comparing the current position of the element to the position of the scroller. For emulating the _Anchorage theme_ I combined 3 approaches [headers for tables](http://jsfiddle.net/jbY6X/1/), [simple parallax scrolling](http://abduzeedo.com/super-easy-parallax-effect-jquery), and [opacity scrolling](http://stackoverflow.com/questions/17263216/fading-in-out-on-mouse-scroll-with-jquery) and [its demo](http://www.milknhny.co.uk/) and a bit of [css3 transitions and transformations](http://net.tutsplus.com/tutorials/html-css-techniques/css-fundametals-css-3-transitions/)

* You can see my implementation [here](http://jsfiddle.net/rKksD/12/)
* Other cool examples can be found over [here](http://blog.teamtreehouse.com/fixed-headers-and-navigation-bars-used-in-web-design)
* I also like this [design](http://jonrohan.me/guide/git/dead-simple-git-workflow-for-agile-teams/)
* Here is a pretty interesting [pure css implementation](http://jsfiddle.net/WDnyb/2/)