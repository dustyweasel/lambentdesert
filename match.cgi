#!/bin/sh

echo "Content-type: text/html"
echo ""

echo "<html>"
echo "<head>"
echo "<TITLE>match"
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

echo "<h1><a href="more.html"><img class="wesnoth" src="mainimages/blademaster-melee-4.png" alt="" /></a>BLANCO MATCH!</h1>"
echo "<p>Enter a 6 digit Blanco model number to find  it and/or all models that get the same cutout.  Example: 440067<br/>"

echo "<form>"
echo "<input type="text" class="textboxclass" maxlength="6" name="search">"
echo "</form></p>"

len=`echo $QUERY_STRING|wc -c`

#########
#TempFile="/tmp/cgitmp.$$"

#find whatnot >"$TempFile"

#...

#process $TempFile

#rm -- "$TempFile"
###########

TempFile="/tmp/cgitmp.$$"
TempFile2="/tmp/cgitmp2.$$"
TempKeep="/tmp/cgitmp3.$$"
TempBlah="/tmp/cgitmp4.$$"
TempSMGalpha="/tmp/cgitmp5.$$"
TempBlah2="/tmp/cgitmp6.$$"
#TempTerrel="/tmp/cgitmp7.$$"
TempEstradaalpha="/tmp/cgitmp8.$$"
TempJOE="/tmp/cgitmp9.$$"
TempJOE2="/tmp/cgitmp11.$$"
TempJOE3="/tmp/cgitmp12.$$"
TempRJ="/tmp/cgitmp10.$$"
TempOLDE="/tmp/cgitmp13.$$"
TempOLDE2="/tmp/cgitmp14.$$"

#cat /dev/null > temp.txt
#cat /dev/null > temp2.txt
#cat /dev/null > keeper.txt
#cat /dev/null > blah.txt

if [ $len -gt 14 ] || [ $len -lt 14 ]
then
  QUERY_STRING="error"
  echo "<p>"
  echo "For older Blanco sinks with weird model #'s you want to go back to the regular search page:"
  echo "</p>"
  echo "<p class="big">"
  echo "<a href="search.cgi"><img class="wesnoth" src="mainimages/glider-fly.jpg" alt="" />Search!</a>"
  echo "</p>"  
else
  QUERY_STRING=$(echo $QUERY_STRING | cut -c8-$len)
  
  echo "<p>"
  echo "You entered: $QUERY_STRING"
  echo "</p>"
  echo "<h1>IDENTICAL CUTOUTS:</h1>"
  harvester='blanco.txt'
  harvester2=`cat $harvester`

  checker=false

  for line in $harvester2 ; do
    echo "$line" >> $TempFile
    if [ $line = $QUERY_STRING ]
    then
      checker=true
      switcher=$TempFile
      switcher2=`cat $switcher`
      for grab in $switcher2 ; do
        echo "$grab" >> $TempKeep
      done
    elif [ "$line" = "break" ]
    then
      cat /dev/null > $TempFile
      checker=false
    elif [ "$checker" = true ]
      then
      echo "$line" >> $TempKeep
    fi
  done

  cat /dev/null > $TempFile

  echo "<p>"  
  matcher=$TempKeep
  matcher2=`cat $matcher`
  echo "$matcher2"
  if [ "$matcher2" = "" ]
  then
    echo "NO IDENTICAL CUTOUTS!  Searching only for $QUERY_STRING"
    matcher2=$QUERY_STRING
  fi
  echo "</p>"
  for matchline in $matcher2; do
    #matchline=$(echo $matchline | cut -c 4-)
    ####################
    #printf "%si'm working on this page i'll fix it tomorrow good night<br/>" "$matchline"
    #find ./sinks/donations/AI/BLANCO -type f -iname \*$matchline\* | xargs -n 1 echo >> temp2.txt
    ###################
    
    matchline2=$(echo $matchline | sed 's/^\(.\{3\}\)/\1-/')  #i have no memeory of writing this line.  it sticks a hyphen in the middle?
    #printf "%sasdfdasfdasf<br/>" "$matchline2"
    find ./sinks/dxfs/Blanco -type f -iname \*$matchline2\* | xargs -n 1 echo >> $TempFile
    #################
    find ./sinks/donations/AI/BLANCO/ -type f -iname \*$matchline\* -name "*.dxf" | xargs -n 1 echo >> $TempFile2
    #find ./sinks/donations/AI/BLANCO/ -type f -iname \*$matchline\* -name *.dxf | xargs -n 1 echo >> $TempSMG
    find ./sinks/donations/SMG/Blanco/ -type f -iname \*$matchline\* -name "*.asd" | xargs -n 1 echo >> $TempSMGalpha
    find ./sinks/donations/Estrada/BLANCO/ -type f -iname \*$matchline2\* -name "*.ard" | xargs -n 1 echo >> $TempEstradaalpha
    #find ./sinks/donations/Terrel/Blanco/ -type f -iname \*$matchline\* -name "*.dxf" | xargs -n 1 echo >> $TempTerrel
    find ./sinks/donations/JOES_SINKS/BLANCO_440/ -type f -iname \*$matchline2\* -name "*.dxf" | xargs -n 1 echo >> $TempJOE
    find ./sinks/donations/JOES_SINKS/0-MISC/BLANCO_441-500/ -type f -iname \*$matchline2\* -name "*.dxf" | xargs -n 1 echo >> $TempJOE3
    find ./sinks/donations/JOES_SINKS/0-MISC/BLANCO_441-500/ -type f -iname \*$matchline2\* -name "*.dwg" | xargs -n 1 echo >> $TempJOE2
    find ./sinks/donations/RJ/Blanco/ -type f -iname \*$matchline2\* -name "*.asd" | xargs -n 1 echo >> $TempRJ
    find ./sinks/ruff/BLANCO/ -type f -iname \*$matchline2\* -name "*.dxf" | xargs -n 1 echo >> $TempOLDE
    find ./sinks/ruff/BLANCO_GERMANY/ -type f -iname \*$matchline2\* -name "*.dxf" | xargs -n 1 echo >> $TempOLDE2
    #for D in `find ./sinks/donations/AI/* -maxdepth 0 -type d`; do
    ################
    #more darksaurian2.txt | grep -i $matchline >> blah.txt
    #more laconiclizard2.txt | grep -i $matchline >> $TempBlah
    find ./sinks/FML/ -type f -iname \*$matchline\* -name "*.ard" | xargs -n 1 echo >> $TempBlah
    find ./sinks/FML/ -type f -iname \*$matchline\* -name "*.asd" | xargs -n 1 echo >> $TempBlah2
  done

  #echo "<p>If you find the following drawings useful please consider donating your sink drawings too!: <a href="expand.html">Donate</a></p>"
  echo "<p class="big">"
  echo "<mark class="red">"
  echo "<a href="sinks.cgi"><img class="lightning" src="mainimages/flanker.jpg" alt="" /></a> 1) lambentdesert DXF matches:<br/>"
  echo "</mark>"
 # echo "<p class="big">"
  harvester=$TempFile
  harvester2=`cat $harvester`
  for line in $harvester2 ; do
    line=$(echo $line | cut -c 3-)
    chop=$(echo $line | cut -c 19-) 
    printf "<a href="drawdxf.cgi?%s">%s</a><br/>" "$line" "$chop"
  done
  if ! [ -n "$harvester2" ];
  then
	echo "no lambentdesert.com dxf matches found<br/>"
  fi
  #echo "</p>"

  echo "<mark class="red">"
  echo "<a href="ai.cgi"><img class="lightning" src="mainimages/jawal.jpg" alt="" /></a> 2) A.I. DXF matches:<br/>"
  echo "</mark>"
  #echo "NEW! These were donated to the site.  Did you find them useful?<br/>(  <a href="expand.html">Then send in your sink files too! </a>):</h1>"
 # echo "<p class="big">"
  harvester=$TempFile2
  harvester2=`cat $harvester`
  for line in $harvester2 ; do
    line=$(echo $line | cut -c 3-)
    chop=$(echo $line | cut -c 27-) 
    printf "<a href="drawdxf.cgi?%s">%s</a><br/>" "$line" "$chop"
  done
  if ! [ -n "$harvester2" ];
  then
	echo "no A.I. dxf matches found<br/>"
  fi
 # echo "</p>"
  
  echo "<mark class="red">"
  echo "<a href="SMG.cgi"><img class="lightning" src="mainimages/draug-bob8.jpg" alt="" /></a> 3) SMG AlphaCAM matches:<br/>"
  echo "</mark>"
 # echo "NEW! These were donated to the site.  Did you find them useful?<br/>(  <a href="expand.html">Then send in your sink files too! </a>):</h1>"
#  echo "<p class="big">"
  harvester=$TempSMGalpha
  harvester2=`cat $harvester`
  for line in $harvester2 ; do
    line=$(echo $line | cut -c 3-)
    chop=$(echo $line | cut -c 28-) 
    printf "<a href="drawAlphaCAM.cgi?%s">%s</a><br/>" "$line" "$chop"
  done
  if ! [ -n "$harvester2" ];
  then
	echo "no SMG AlphaCAM matches found<br/>"
  fi
  
  echo "<mark class="red">"
  echo "<a href="Estrada.cgi"><img class="lightning" src="mainimages/troll.jpg" alt="" /></a> 4) Estrada AlphaCAM matches:<br/>"
  echo "</mark>"
 # echo "NEW! These were donated to the site.  Did you find them useful?<br/>(  <a href="expand.html">Then send in your sink files too! </a>):</h1>"
#  echo "<p class="big">"
  harvester=$TempEstradaalpha
  harvester2=`cat $harvester`
  for line in $harvester2 ; do
    line=$(echo $line | cut -c 3-)
    chop=$(echo $line | cut -c 32-) 
    printf "<a href="drawAlphaCAM.cgi?%s">%s</a><br/>" "$line" "$chop"
  done
  if ! [ -n "$harvester2" ];
  then
	echo "no Estrada AlphaCAM matches found<br/>"
  fi
  
##################
  echo "<mark class="red">"
  echo "<a href="Joes_Sinks.cgi"><img class="lightning" src="mainimages/silver-mage.jpg" alt="" /></a> 5) Joe's Sinks DXF matches:<br/>"
  echo "</mark>"
  #echo "NEW! These were donated to the site.  Did you find them useful?<br/>(  <a href="expand.html">Then send in your sink files too! </a>):</h1>"
 # echo "<p class="big">"
  crud=0
  harvester=$TempJOE
  harvester2=`cat $harvester`
  echo "BLANCO_440/<br/>"
  for line in $harvester2 ; do
    line=$(echo $line | cut -c 3-)
    chop=$(echo $line | cut -c 39-) 
    printf "<a href="drawdxf.cgi?%s">%s</a><br/>" "$line" "$chop"
  done
  
  if ! [ -n "$harvester2" ];
  then
	crud=1
  fi
  
  harvester=$TempJOE3
  harvester2=`cat $harvester`
  echo "0-MISC/BLANCO_441-550/<br/>"
  for line in $harvester2 ; do
    line=$(echo $line | cut -c 3-)
    chop=$(echo $line | cut -c 50-) 
    printf "<a href="drawdxf.cgi?%s">%s</a><br/>" "$line" "$chop"
  done
  
  if ! [ -n "$harvester2" ] && [ $crud == 1 ];
  then
	crud=2
  fi 
  
  harvester=$TempJOE2
  harvester2=`cat $harvester`
  for line in $harvester2 ; do
    line=$(echo $line | cut -c 3-)
    chop=$(echo $line | cut -c 50-) 
    printf "<a href="drawdwg.cgi?%s">%s</a><br/>" "$line" "$chop"
  done
 #############

 ##############
  if ! [ -n "$harvester2" ] && [ $crud == 2 ];
  then
	echo "no Joe's Sinks dxf or dwg matches found<br/>"
  fi
###################

##################
  echo "<mark class="red">"
  echo "<a href="RJ.cgi"><img class="lightning" src="mainimages/impaler.jpg" alt="" /></a> 6) RJ AlphaCAM matches:<br/>"
  echo "</mark>"
  #echo "NEW! These were donated to the site.  Did you find them useful?<br/>(  <a href="expand.html">Then send in your sink files too! </a>):</h1>"
 # echo "<p class="big">"
  harvester=$TempRJ
  harvester2=`cat $harvester`
  for line in $harvester2 ; do
    line=$(echo $line | cut -c 3-)
    chop=$(echo $line | cut -c 27-) 
    printf "<a href="drawdxf.cgi?%s">%s</a><br/>" "$line" "$chop"
  done
  if ! [ -n "$harvester2" ];
  then
	echo "no RJ AlphaCAM matches found<br/>"
  fi
###################


##################
  echo "<mark class="red">"
  echo "<a href="ye_olde_stash.cgi"><img class="lightning" src="mainimages/dark-sorcerer-magic-2.png" alt="" /></a> 7) Ye Olde Stash DXF matches:<br/>"
  echo "</mark>"
  echo "<mark class="blue">"
  echo "one more donation and i'll make these downloadable<br/>"
  echo "</mark>"
  
  #echo "NEW! These were donated to the site.  Did you find them useful?<br/>(  <a href="expand.html">Then send in your sink files too! </a>):</h1>"
 # echo "<p class="big">"
  crud=0
  harvester=$TempOLDE
  harvester2=`cat $harvester`
  echo "BLANCO/<br/>"
  for line in $harvester2 ; do
    line=$(echo $line | cut -c 3-)
    #chop=$(echo $line | cut -c 39-) 
    chop=$(echo $line | cut -c 19-) 
    #printf "<a href="drawdxf.cgi?%s">%s</a><br/>" "$line" "$chop"
    echo "$chop</br>"
  done
  
  if ! [ -n "$harvester2" ];
  then
	crud=1
  fi
  
  #harvester=$TempJOE3
  #harvester2=`cat $harvester`
  #echo "0-MISC/BLANCO_441-550/<br/>"
  #for line in $harvester2 ; do
  #  line=$(echo $line | cut -c 3-)
  #  chop=$(echo $line | cut -c 50-) 
  #  printf "<a href="drawdxf.cgi?%s">%s</a><br/>" "$line" "$chop"
  #done
  
  #if ! [ -n "$harvester2" ] && [ $crud == 1 ];
  #then
#	crud=2
 # fi 
  
  harvester=$TempOLDE2
  harvester2=`cat $harvester`
  echo "BLANCO/GERMANY/<br/>"
  for line in $harvester2 ; do
    line=$(echo $line | cut -c 3-)
    #chop=$(echo $line | cut -c 50-) 
    chop=$(echo $line | cut -c 27-)
    #printf "<a href="drawdxf.cgi?%s">%s</a><br/>" "$line" "$chop"
    echo "$chop</br>"
  done
 #############

 ##############
  if ! [ -n "$harvester2" ] && [ $crud == 1 ];
  then
	echo "no Ye Olde dxf matches found<br/>"
  fi
###################


 # echo "</p>"
  
  echo "<mark class="red">"
  echo "<a href="laconicdxflist.cgi"><img class="lightning" src="mainimages/skirmisher.png" alt="" /></a> 8) laconiclizard's AlphaCAM matches:<br/>"
  echo "</mark>"
 # echo "I drew all of these.  Are you using them?<br/>(  <a href="expand.html">Then send in your sinks too! </a> ):</h1>"
 # echo "<p>"
  #harvester=$TempBlah
  #harvester2=`cat $harvester`
  #for line in $harvester2 ; do
  #  echo "$line <br/>"
  #done
  
  
 # echo "<p class="big">"
  crud=0
  harvester=$TempBlah
  harvester2=`cat $harvester`
  #printf "%s" "$harvester2"
  for line in $harvester2 ; do
    line=$(echo $line | cut -c 3-)
    chop=$(echo $line | cut -c 11-) 
    printf "<a href="drawAlphaCAM.cgi?%s">%s</a><br/>" "$line" "$chop"
  done

  if ! [ -n "$harvester2" ];
  then
	crud=1
  fi 
  
  harvester=$TempBlah2
  harvester2=`cat $harvester`
  for line in $harvester2 ; do
    line=$(echo $line | cut -c 3-)
    chop=$(echo $line | cut -c 11-) 
    printf "<a href="drawAlphaCAM.cgi?%s">%s</a><br/>" "$line" "$chop"
  done
  
  if ! [ -n "$harvester2" ] && [ $crud == 1 ];
  then
	echo "no laconiclizard AlphaCAM matches found<br/>"
  fi
  echo "</p>"
  
  echo "<h1>Search:</h1>"
  echo "<p>"
  echo "Click the link below to go back to the regular search page:"
  echo "</p>"
  echo "<p class="big">"
  #<a href="print.html"><img src="mainimages/flanker.jpg" alt="" width="180" height="180" />PRINT LIST!</a>
  echo "<a href="search.cgi"><img class="wesnoth" src="mainimages/glider-fly.jpg" alt="" />Search!</a>"
  echo "</p>"  
  
fi

rm -- $TempFile
rm -- $TempFile2
rm -- $TempKeep
rm -- $TempBlah
rm -- $TempBlah2
rm -- $TempSMGalpha
rm -- $TempEstradaalpha
rm -- $TempJOE
rm -- $TempJOE2
rm -- $TempJOE3
rm -- $TempRJ
rm -- $TempOLDE
rm -- $TempOLDE2

echo "<p class="big"><a href="more.html">EXTRA</a></p>"

echo "<p class="copyright">&copy; Copyright 2018 by laconiclizard"
echo "</p>"

echo "</div>"

echo "</body>"
echo "</html>"
