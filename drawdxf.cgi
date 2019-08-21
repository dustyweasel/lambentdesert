#!/bin/sh

echo "Content-type: text/html"
echo ""

echo "<html>"
echo "<head>"
echo "<TITLE>drawdxf"
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

#printf "%s" "$QUERY_STRING"

len=`echo $QUERY_STRING|wc -c`
if [ $len -gt 150 ] || [ $len -lt 13 ]
then
  QUERY_STRING="sinks/dxfs/error"
fi

##############################
#printf "%s" "$QUERY_STRING"
####
#b=$(echo "RAMSITALS|HMAN|1223333" | grep -aob '|' | grep --color=never -oE '[0-9]+' )
b=$(echo $QUERY_STRING | grep -aob '/' | grep --color=never -oE '[0-9]+' | head -n2 | tail -n1)
let b=$(($b+2))
####let a=$(($a+0))
#printf "%i" "$b"
#############################

len=`echo $QUERY_STRING|wc -c`
#j=$(echo $QUERY_STRING | cut -c12-$len)
j=$(echo $QUERY_STRING | cut -c$b-$len)

echo "<h1><a href="sinks.cgi"><img class="wesnoth" src="mainimages/augur.jpg" alt="" /></a>View!</h1>"

echo "<p>"
echo "If you're dying to see a picture of this dxf that takes forever to load then click here:"

echo "<a href="http://www.sharecad.org/cadframe/load?url=http://www.lambentdesert.com/$QUERY_STRING" width="90%" height="40%" scrolling="no">ShareCAD</a>"

#echo "<br/><br/>WARNING: By clicking the link below you agree that every dxf downloaded from this site"
#echo "is completely wrong and if used for fabrication purposes will cause remakes, bankruptcy, suicide,"
#echo "and also your family will starve."
#echo "ATTENTION EURO MARBLES SUPPLY, US GRANITE, AND PARK INDUSTRIES, CLICK THE FOLLOWING LINK AND SCROLL TO THE BOTTOM: <a href="expand.html">PAY UP</a><br/><br/>"
echo "<br/><br/>Donate sink drawings instead of just downloading them for free like a parasite: <a href="expand.html">DONATE</a></p>"
#echo "<p>Donate sinks to lambentdesert.com!  Click here to learn more!: <a href="expand.html">Master Plan</a></p>"

#echo "<p class="big">By clicking the link below you agree that your soul belongs to #lambentdesert.com for all eternity:<br/><a href=$QUERY_STRING>$j<br/><br/></a>"
echo "<p class="big">Download this dxf at your own risk:<br/><a href=$QUERY_STRING>$j<br/><br/></a>"
#echo "<img src="https://media.giphy.com/media/77f2SrKYNOnYs/giphy.gif" /><br/>"
echo "Check dimensions on your phone with this:<br/>"
echo "<a href="http://www.cadpockets.com/en/">CAD Pockets</a>"
echo "</p>"

#echo "<p>"
#echo "Top Ten CeLebrity life hacks!!!  Number 8 blew my mind!!  Banana Bread!??  From old, frozen bananas??  WHat!!??  Click NOW!: <a href=https://currentopinionsofnews.files.wordpress.com/2015/01/middle-finger.png?w=640>TOP TEN</a>"
#echo "</p>"

echo "<p class="big"><a href="sinks.cgi">HOME</a></p>"
echo "<p class="copyright">&copy; Copyright 2015 by laconiclizard"
echo "</p>"

echo "</div>"



echo "</body>"

echo "</html>"
