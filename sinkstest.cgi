#!/bin/sh

echo "Content-type: text/html"
echo ""

echo "<html>"
echo "<head>"
echo "<TITLE>sinks"
echo "</TITLE>"
echo "<link rel="stylesheet" type="text/css" href="tipstest.css" />"

#<style type="text/css">
#    /* default styles here for older browsers. 
#       I tend to go for a 600px - 960px width max but using percentages
#    */
#    @media only screen and (min-width:960px){
#        /* styles for browsers larger than 960px; */
#    }
#    @media only screen and (min-width:1440px){
#        /* styles for browsers larger than 1440px; */
#    }
#    @media only screen and (min-width:2000px){
#        /* for sumo sized (mac) screens */
#    }
#    @media only screen and (max-device-width:480px){
#       /* styles for mobile browsers smaller than 480px; (iPhone) */
#    }
#    @media only screen and (device-width:768px){
#       /* default iPad screens */
#    }
#    /* different techniques for iPad screening */
#    @media only screen and (min-device-width: 481px) and (max-device-width: 1024px) and (orientation:portrait) {
#      /* For portrait layouts only */
#    }

#    @media only screen and (min-device-width: 481px) and (max-device-width: 1024px) and (orientation:landscape) {
#      /* For landscape layouts only */
#    }
#</style>

#echo "<!--google analytics-->"
echo "<script>"
echo "  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){"
echo "  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),"
echo "  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)"
echo "  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');"

echo "  ga('create', 'UA-102515378-1', 'auto');"
echo "  ga('send', 'pageview');"

echo "</script>"

echo "</head>"
echo "<body>"
#&#11013
echo "<div class="main">"

echo "<p class="small">"
echo "Disclaimer: Every sink drawing on this website is wrong.  If you use any drawings from"
echo "this website for fabrication purposes then your countertops will be wrong, you will lose thousands"
echo "of dollars, you will go out of business, and your family will starve."
#echo "The sink webpage has moved to www.lambentdesert.com but I guess you already know that.  Tell all"
#echo "your friends!  Is the website faster now?  Tell me what you think.  At lambentdesert.com your"
#echo "feedback is important to us! (not really)"
echo "</p>"

echo "<h1><a href="search.cgi"><img src="mainimages/glider-fly.jpg" alt="" width="180" height="180" />SEARCH!_&#11013;CLICK</a></h1>"
echo "<h1><a href="more.html"><img src="mainimages/flanker.jpg" alt="" width="180" height="180" />EXTRA!_&#11013;CLICK</a></h1>"

echo "<p class="big">"
#echo "&#9735 = old text list <br/>"
echo "<img src="mainimages/bluebolt.jpg" alt="" width="85" height="85"> = old text list<br/>"
echo "name = dxf list<br/>"
#echo "</p>"


echo "<mark class="red">"
#echo "<p class="note">
echo "updated: "
harvester='update.txt'
harvester2=`cat $harvester`
echo "$harvester2"
echo "</mark>"
echo "</p>"

echo "<p class="big">"

for i in sinks/*.txt; do
    len=`echo $i|wc -c`
    len=$((len-5))
    j=$(echo $i | cut -c7-$len)
    
    h="dxflist.cgi?"$j
    
    printf "<a href="%s"><img src="mainimages/bluebolt.jpg" alt="" width="170" height="85"> </img></a>" "$i"
    
    printf "<a href="%s">%s</a><br/>" "$h" "$j"
done

printf "<a href="laconiclizard.txt"><img src="mainimages/bluebolt.jpg" alt="" width="85" height="85"> </a>"
printf "AlphaCAM sinks<br/>"

echo "<br/></p>"

echo "<p class="copyright">&copy; Copyright 2015 by laconiclizard</p>"

echo "</div>"

echo "</body>"
echo "</html>"
