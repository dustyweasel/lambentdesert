#!/bin/sh

echo "Content-type: text/html"
echo ""

echo "<html>"
echo "<head>"
echo "<TITLE>dxflist"
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

echo "<h1><a href="sinks.cgi"><img class="wesnoth" src="mainimages/ambusher.jpg" alt="" /></a>DXF'S!</h1>"

echo "<p class="copyright">"
echo "These are the lambentdesert.com stock sink dxf files.  I only drew a few of these."
echo "(The good ones.)  Who knows who drew the rest.  Some of these drawings suck but I've only had them cause a remake once"
echo "or twice over the past four years.  (and last time was a couple years ago and that sink was deleted.)  They mostly have 1/4&quot overhang unless they say flush or something.  If you use a flush one"
echo "you might want to shrink it 1/16&quot for good luck.  In fact anything with square corners I'd change the radii to 1/2&quot for good luck.  At least if cutting on a waterjet."
echo "<br/><br/>Can't find what you're looking for?  Use the <a href="search.cgi">SEARCH PAGE</a>.  It will scan this folder as well as all the donated folders."
#echo "in the world: <a href="expand.html">MASTER PLAN</a>"
echo "</p>"

echo "<p class="big">"

len=`echo $QUERY_STRING|wc -c`
if [ $len -gt 19 ] || [ $len -lt 3 ]
then
  QUERY_STRING="error"
fi

#echo "$len"
echo "$QUERY_STRING:<br/>"

for i in ./sinks/dxfs/$QUERY_STRING/*.dxf; do
    len=`echo $i|wc -c`
    len2=`echo $QUERY_STRING|wc -c`
    len2=$((len2+14))
    j=$(echo $i | cut -c$len2-$len)
    h=drawdxf.cgi?"sinks/dxfs/"$QUERY_STRING"/"$j
    printf "<a href="%s">%s</a><br/>" "$h" "$j"
done

echo "</p>"
echo "</p><p class="big"><a href="sinks.cgi">HOME</a></p>"

echo "<p class="copyright">&copy; Copyright 2015 by laconiclizard"
echo "</p>"

echo "</div>"

echo "</body>"
echo "</html>"
