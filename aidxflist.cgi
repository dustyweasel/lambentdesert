#!/bin/sh

echo "Content-type: text/html"
echo ""

echo "<html>"
echo "<head>"
echo "<TITLE>aidxflist"
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

echo "<h1><a href="ai.cgi"><img class="wesnoth" src="mainimages/batal.jpg" alt="" /></a>A.I. DXF'S!</h1>"

echo "<p class="big">"

####
#TempFile="/tmp/cgitmp.$$"

#find whatnot >"$TempFile"

#...

#process $TempFile

#rm -- "$TempFile"
#####

TempFile="/tmp/cgitmp.$$"

len=`echo $QUERY_STRING|wc -c`
if [ $len -gt 20 ] || [ $len -lt 3 ]
then
	QUERY_STRING="error"
	echo "$QUERY_STRING:<br/>"
else

	echo "$QUERY_STRING:<br/>"

	find ./sinks/donations/AI/$QUERY_STRING -type f -iname "*.dxf" | xargs -n 1 echo > $TempFile
	harvester=$TempFile
	harvester2=`cat $harvester`
	len=$(($len + 20))
    for line in $harvester2 ; do
		line=$(echo $line | cut -c 3-)
		chop=$(echo $line | cut -c $len-) 
	printf "<a href="drawdxf.cgi?%s">%s</a><br/>" "$line" "$chop"
	 
	done
fi



#for i in ./sinks/donations/AI/dxfs/$QUERY_STRING/*.dxf; do
#    len=`echo $i|wc -c`
#    len2=`echo $QUERY_STRING|wc -c`
#    len2=$((len2+14))
#    j=$(echo $i | cut -c$len2-$len)
#    h=drawdxf.cgi?"sinks/dxfs/"$QUERY_STRING"/"$j
#    printf "<a href="%s">%s</a><br/>" "$h" "$j"
#done

echo "</p>"
echo "</p><p class="big"><a href="ai.cgi">A.I. SINKS</a></p>"

echo "<p class="copyright">&copy; Copyright 2018 by laconiclizard"
echo "</p>"

rm -- $TempFile

echo "</div>"

echo "</body>"
echo "</html>"
