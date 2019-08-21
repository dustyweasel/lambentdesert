#!/bin/sh

echo "Content-type: text/html"
echo ""

echo "<html>"
echo "<head>"
echo "<TITLE>laconicdxflist"
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

####
#TempFile="/tmp/cgitmp.$$"

#find whatnot >"$TempFile"

#...

#process $TempFile

#rm -- "$TempFile"
#####

echo "<h1><a href="moresinks.cgi"><img class="wesnoth" src="mainimages/skirmisher.png" alt="" /></a>laconiclizard's AlphaCAM drawings!</h1>"

echo "<p class="copyright">"
echo "I think I drew all of these.  Almost everything from the past few years has a construction line for the rim and a geometry line for 5/16&quot overhang.  Also"
echo "I put vertical construction lines centered on dividers in case I want to know where they are later."
echo "<br/><br/>Oh yeah, and this page suffers from my &quoteverything in one folder&quot philosophy.  In fact, you're probably better off just using"
echo "the <a href="search.cgi">search</a> page.  (Or use ctrl-F.)  Maybe someday I'll alphabetize this page."
#echo "<h1><a href="sinks.cgi"><img class="wesnoth" src="mainimages/glider-fly.jpg" alt="" /></a>SEARCH!</h1>"

echo "<br/><br/>Every drawing here comes with my 100% guarantee that if it's wrong, it's not my problem."

#echo "These sinks were donated by SMG.  If you find them useful why not email me your sinks too?  Let's all be part of the problem"
#echo "together!: <a href="expand.html">MASTER PLAN</a>"
#echo "<br/><br/>Per the donator:<br/>"
#echo "most if not all of these sinks have a negative reveal because thats how we roll."
#echo "ATTENTION EURO MARBLES SUPPLY, US GRANITE, AND PARK INDUSTRIES, CLICK THIS LINK AND SCROLL TO THE BOTTOM: <a href="expand.html">PAY UP</a><br/><br/>"
#echo "Click here to go to the main page: <a href="index.html">MAIN PAGE</a><br/>"
#echo "As always, email me here: <a href="mailto:laconiclizard@lambentdesert.com">laconiclizard@lambentdesert.com</a>"
echo "</p>"

echo "<p class="big">"


####
#TempFile="/tmp/cgitmp.$$"

#find whatnot >"$TempFile"

#...

#process $TempFile

#rm -- "$TempFile"
#####

TempFile="/tmp/cgitmp.$$"
#TempFile2="/tmp/cgitmp2.$$"

#len=`echo $QUERY_STRING|wc -c`
#if [ $len -gt 20 ] || [ $len -lt 3 ]
#then
#	QUERY_STRING="error"
#	echo "$QUERY_STRING:<br/>"
#else

#	echo "$QUERY_STRING:<br/>"

#	find ./sinks/donations/SMG/$QUERY_STRING -type f -iname *.dxf | xargs -n 1 echo > $TempFile
	find ./sinks/FML -type f -iname "*.ard" | xargs -n 1 echo > $TempFile
	#find ./sinks/FML -type f -iname *.ard | xargs -n 1 echo > $TempFile
	harvester=$TempFile
	harvester2=`cat $harvester`
	#harvester3=$TempFile2
	#harvester4=`cat $harvester3`
    for line in $harvester2 ; do
		line=$(echo $line | cut -c 3-)
		chop=$(echo $line | cut -c 11-) 
	printf "<a href="drawAlphaCAM.cgi?%s">%s</a><br/>" "$line" "$chop"
	done
	
	#find ./sinks/FML -type f -iname *.asd | xargs -n 1 echo > $TempFile
	find ./sinks/FML -type f -iname "*.asd" | xargs -n 1 echo > $TempFile
	harvester=$TempFile
	harvester2=`cat $harvester`
	#harvester3=$TempFile2
	#harvester4=`cat $harvester3`
    for line in $harvester2 ; do
		line=$(echo $line | cut -c 3-)
		chop=$(echo $line | cut -c 11-) 
	printf "<a href="drawAlphaCAM.cgi?%s">%s</a><br/>" "$line" "$chop"
	done
	
	#for line in $harvester4 ; do
	#	line=$(echo $line | cut -c 3-)
	#	chop=$(echo $line | cut -c 17-) 
	#printf "<a href="drawAlphaCAM.cgi?%s">%s</a><br/>" "$line" "$chop"		 
	#done
#fi



#for i in ./sinks/donations/AI/dxfs/$QUERY_STRING/*.dxf; do
#    len=`echo $i|wc -c`
#    len2=`echo $QUERY_STRING|wc -c`
#    len2=$((len2+14))
#    j=$(echo $i | cut -c$len2-$len)
#    h=drawdxf.cgi?"sinks/dxfs/"$QUERY_STRING"/"$j
#    printf "<a href="%s">%s</a><br/>" "$h" "$j"
#done

echo "</p>"

rm -- $TempFile
#rm -- $TempFile2

echo "</p><p class="big"><a href="moresinks.cgi">HOME</a></p>"

echo "<p class="copyright">&copy; Copyright 2018 by laconiclizard"
echo "</p>"

echo "</div>"

echo "</body>"
echo "</html>"
