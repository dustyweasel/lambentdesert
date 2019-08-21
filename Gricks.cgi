#!/bin/sh

echo "Content-type: text/html"
echo ""

echo "<html>"
echo "<head>"
echo "<LINK REL="apple-touch-icon" HREF="mainimages/appleskirmisher.png" />"
echo "<TITLE>Gricks' Sinks"
echo "</TITLE>"
echo "<link rel="stylesheet" type="text/css" href="tips.css" />"

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
echo "<div class="main">"

echo "<h1><a href="moresinks.cgi"><img class="wesnoth" src="mainimages/fairy.jpg" alt="" /></a>Gricks' Sinks</h1>"
#<h1><a href="sinks.cgi"><img class="wesnoth" src="mainimages/fighter-melee-2.png" alt="" /></a>PRINT LIST!</h1>
#echo "<h1><a href="more.html"><img class="wesnoth" src="mainimages/flanker.jpg" alt="" />EXTRA!_&#11013;CLICK</a></h1>"

#echo "<p class="big">"
#echo "<img class="lightning" src="mainimages/bluebolt.jpg" alt="" > = old text list<br/>"
#echo "name = dxf list<br/>"

#echo "<mark class="red">"
#echo "updated: "
#harvester='update.txt'
#harvester2=`cat $harvester`
#echo "$harvester2"
#echo "</mark>"
#echo "</p>"

echo "<p class="copyright">"
echo "These sinks were donated by Gricks.  If you find them useful why not email me your sinks too?  Let's all be part of the problem"
echo "together!: <a href="expand.html">MASTER PLAN</a>"
#echo "<br/><br/>Per the donator:<br/>"
#echo "<br/><br/>&quotmost if not all of these sinks have a negative reveal because thats how we roll.&quot -SMG"
#echo "ATTENTION EURO MARBLES SUPPLY, US GRANITE, AND PARK INDUSTRIES, CLICK THIS LINK AND SCROLL TO THE BOTTOM: <a href="expand.html">PAY UP</a><br/><br/>"
#echo "Click here to go to the main page: <a href="index.html">MAIN PAGE</a><br/>"
#echo "As always, email me here: <a href="mailto:laconiclizard@lambentdesert.com">laconiclizard@lambentdesert.com</a>"
echo "</p>"

echo "<p class="big">"

for D in `find ./sinks/donations/Gricks/* -maxdepth 0 -type d`; do
#for D in ./sinks/donations/AI/*; do

    len=`echo $D|wc -c`
    #len=$((len-5))
	j=$(echo $D | cut -c26-$len)
	printf "<img class="lightning" src="mainimages/fairy2.jpg" alt="" > </img>"
    
	h="Gricksdxflist.cgi?"$j
    
	printf "<a href="%s">%s</a><br/>" "$h" "$j"
    

#len=`echo $i|wc -c`
    #len=$((len-5))
    #j=$(echo $i | cut -c9-$len)
    
    #h="dxflist.cgi?"$j
    
    #printf "<a href="%s"><img class="lightning" src="mainimages/bluebolt.jpg" alt="" > </img></a>" "$i"
    
    #printf "<a href="%s">%s</a><br/>" "$h" "$j"    
    
    
done

echo "<br/></p>"

echo "<p class="big"><a href="moresinks.cgi">HOME</a></p>"

echo "<p class="copyright">&copy; Copyright 2018 by laconiclizard</p>"

echo "</div>"

echo "</body>"
echo "</html>"
