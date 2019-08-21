#!/bin/sh

####
#TempFile="/tmp/cgitmp.$$"

#find whatnot >"$TempFile"

#...

#process $TempFile

#rm -- "$TempFile"
#####



echo "Content-type: text/html"
echo ""

echo "<html>"
echo "<head>"
echo "<TITLE>search"
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

echo "<h1><a href="sinks.cgi"><img class="wesnoth" src="mainimages/glider-fly.jpg" alt="" /></a>SEARCH!</h1>"
echo "<p>Enter any 3 to 10 digit string. For best results try fragments like ELUH or 3118"

echo "<form>"
#echo "<input type="text" class="textboxclass" maxlength="10" name="search" style="font-size:110px">"
echo "<input type="text" class="textboxclass" maxlength="10" name="search">"
echo "</form></p>"

#echo "$QUERY_STRING<br/>"

#############
#if [ "${var1,,}" = "${var2,,}" ]; then
#  echo ":)"
#fi

#var=True
#typeset -l var
#if [[ $var == "true" ]]; then
#    print "match"
#fi

#[[ $(fgrep -ix $str1 <<< $str2) ]]
#if grep -q foo <<<"$string"; then
#    echo "It's there"
#fi
#############


len=`echo $QUERY_STRING|wc -c`
#typset -l $QUERY_STRING
if [ $len -gt 18 ] || [ $len -lt 11 ] || [ $(fgrep -ix $QUERY_STRING <<< "search=dxf") ] || [ $(fgrep -ix $QUERY_STRING <<< "search=dwg") ] || 
                                         [ $(fgrep -ix $QUERY_STRING <<< "search=asd") ] || [ $(fgrep -ix $QUERY_STRING <<< "search=ard") ] ||
                                         [[ $QUERY_STRING = *"."* ]];
then
  QUERY_STRING="error"
  #echo "<h2>Example:</h2>"
  echo "<p>"
  echo "Can't find anything?  <a href="special.html">Click here for instructions.</a>"
#  echo "If searching for Bredskar 502.254.98 then just search for 254 or 502.  If we named it 502.254.98 then a search"
#  echo "for 502.254.98 or 254.98 will find it but if we named it 502-254-98 or 50225498 then you will not find it.  254 or 502 is guaranteed"
#  echo "to find it no matter what it's named.  Hey you people are typing in multiple fragments with spaces between them, that doesn't work, I'm not google.  Just 254 and"
#  echo " nothing else or just 502 and nothing else.  Get it?  Or instead of pl035 try 035.  See?"
  echo "</p>"
  echo "<h2>Blanco:</h2>"
  echo "<p>"
  echo "If searching for a Blanco sink then skip this page entirely and click the link below to go to the blanco match page:"
  echo "</p>"
  echo "<p class="big">"
  echo "<a href="match.cgi"><img class="wesnoth" src="mainimages/blademaster-melee-4.png" alt="" />Blanco Match!</a>"
  echo "</p>"
else
  QUERY_STRING=$(echo $QUERY_STRING | cut -c8-$len)
  echo "<p>"
  echo "You entered: $QUERY_STRING"
  echo "<mark class="blue">"
  echo "<br/>Can't find it below?  Read this: <a href="alert.html">CLICK CLICK CLICK</a>"
  echo "</mark>"
  echo "</p>"
  echo "<p class="big">"
  echo "<mark class="red">"
  echo "<a href="sinks.cgi"><img class="lightning" src="mainimages/flanker.jpg" alt="" /></a> 1) lambentdesert DXF results:<br/>"
  echo "</mark>"
  #echo "<p class="big">"
  ###
  TempFile="/tmp/cgitmp.$$"
  ###
  #find ./sinks/dxfs -type f -iname \*$QUERY_STRING\* -name *.dxf | xargs -n 1 echo > temp.txt
  find ./sinks/dxfs -type f -iname \*$QUERY_STRING\* -name "*.dxf" | xargs -n 1 echo > $TempFile
  harvester=$TempFile
  harvester2=`cat $harvester`
  for line in $harvester2 ; do
    line=$(echo $line | cut -c 3-)
    chop=$(echo $line | cut -c 12-) 
    printf "<a href="drawdxf.cgi?%s">%s</a><br/>" "$line" "$chop"
    
  done
  if ! [ -n "$harvester2" ];
  then
	echo "no lambentdesert.com dxf files found<br/>"
  #else
  #  echo "whatever<br/>"
  fi
  #echo "</p>"
#######i think i can get rid of the file i/o here and above, see ai.cgi#######
  echo "<mark class="red">"
  echo "<a href="ai.cgi"><img class="lightning" src="mainimages/jawal.jpg" alt="" /></a> 2) A.I. dxf results:</br>"
  echo "</mark>"
  #echo "<p class="big">"
  #echo "NEW! These were donated to the site.  Did you find them useful?<br/>  <a href="expand.html">Then send in your sink files too!</a><br/><br/>"
  find ./sinks/donations/AI/ -type f -iname \*$QUERY_STRING\* -name "*.dxf" | xargs -n 1 echo > $TempFile
  harvester=$TempFile
  harvester2=`cat $harvester`
  for line in $harvester2 ; do
    line=$(echo $line | cut -c 3-)
    chop=$(echo $line | cut -c 20-)
    printf "<a href="drawdxf.cgi?%s">%s</a><br/>" "$line" "$chop"
    
  done
  
  if ! [ -n "$harvester2" ];
  then
	echo "no A.I. dxf files found<br/>"
  fi
#################
  
#  echo "</p>"
  
#######################################
  echo "<mark class="red">"
  echo "<a href="SMG.cgi"><img class="lightning" src="mainimages/draug-bob8.jpg" alt="" /></a> 3) SMG dxf and AlphaCAM results:<br/>"
  echo "</mark>"
 # echo "NEW! These were donated to the site.  Did you find them useful?<br/>(  <a href="expand.html">Then send in your sink files too! </a> ):</h1>"
  #echo "<p class="big">"
  #echo "NEW! These were donated to the site.  Did you find them useful?<br/>  <a href="expand.html">Then send in your sink files too!</a><br/><br/>"
  find ./sinks/donations/SMG/ -type f -iname \*$QUERY_STRING\* -name "*.dxf" | xargs -n 1 echo > $TempFile
  harvester=$TempFile
  harvester2=`cat $harvester`
  for line in $harvester2 ; do
    line=$(echo $line | cut -c 3-)
    chop=$(echo $line | cut -c 21-) 
    printf "<a href="drawdxf.cgi?%s">%s</a><br/>" "$line" "$chop"
    
  done
  
  if ! [ -n "$harvester2" ];
  then
	echo "no SMG dxf files found<br/>"
  fi
  
  find ./sinks/donations/SMG/ -type f -iname \*$QUERY_STRING\* -name "*.asd" | xargs -n 1 echo > $TempFile
  harvester=$TempFile
  harvester2=`cat $harvester`
  for line in $harvester2 ; do
    line=$(echo $line | cut -c 3-)
    chop=$(echo $line | cut -c 21-) 
    printf "<a href="drawAlphaCAM.cgi?%s">%s</a><br/>" "$line" "$chop"
    
  done
  
  if ! [ -n "$harvester2" ];
  then
	echo "no SMG AlphaCAM files found<br/>"
  fi
  
  ##################################
  echo "<mark class="red">"
  echo "<a href="Terrel.cgi"><img class="lightning" src="mainimages/peasant.jpg" alt="" /></a> 4) Terrel dxf results:</br>"
  echo "</mark>"
 # echo "<p class="big">"
  #echo "NEW! These were donated to the site.  Did you find them useful?<br/>  <a href="expand.html">Then send in your sink files too!</a><br/><br/>"
  find ./sinks/donations/Terrel/ -type f -iname \*$QUERY_STRING\* -name "*.dxf" | xargs -n 1 echo > $TempFile
  harvester=$TempFile
  harvester2=`cat $harvester`
  for line in $harvester2 ; do
    line=$(echo $line | cut -c 3-)
    chop=$(echo $line | cut -c 24-) 
    printf "<a href="drawdxf.cgi?%s">%s</a><br/>" "$line" "$chop"
    
  done
  
  if ! [ -n "$harvester2" ];
  then
	echo "no Terrel dxf files found<br/>"
  fi
  
########################################
  echo "<mark class="red">"
  echo "<a href="Estrada.cgi"><img class="lightning" src="mainimages/troll.jpg" alt="" /></a> 5) Estrada AlphaCAM results:</br>"
  echo "</mark>"
 # echo "NEW! These were donated to the site.  Did you find them useful?<br/>(  <a href="expand.html">Then send in your sink files too! </a> ):</h1>"
  #echo "<p class="big">"
  #echo "NEW! These were donated to the site.  Did you find them useful?<br/>  <a href="expand.html">Then send in your sink files too!</a><br/><br/>"
  find ./sinks/donations/Estrada/ -type f -iname \*$QUERY_STRING\* -name "*.ard" | xargs -n 1 echo > $TempFile
  harvester=$TempFile
  harvester2=`cat $harvester`
  for line in $harvester2 ; do
    line=$(echo $line | cut -c 3-)
    chop=$(echo $line | cut -c 25-) 
    printf "<a href="drawAlphaCAM.cgi?%s">%s</a><br/>" "$line" "$chop"
    
  done
  
  if ! [ -n "$harvester2" ];
  then
	echo "no Estrada AlphaCAM files found<br/>"
  fi
#######################################




###############MARCELO########################
  echo "<mark class="red">"
  echo "<a href="Marcelo.cgi"><img class="lightning" src="mainimages/hoplite.jpg" alt="" /></a> 6) Marcelo dxf and dwg results:<br/>"
  echo "</mark>"
 # echo "NEW! These were donated to the site.  Did you find them useful?<br/>(  <a href="expand.html">Then send in your sink files too! </a> ):</h1>"
  #echo "<p class="big">"
  #echo "NEW! These were donated to the site.  Did you find them useful?<br/>  <a href="expand.html">Then send in your sink files too!</a><br/><br/>"
  find ./sinks/donations/Marcelo/ -type f -iname \*$QUERY_STRING\* -name "*.dxf" | xargs -n 1 echo > $TempFile
  harvester=$TempFile
  harvester2=`cat $harvester`
  for line in $harvester2 ; do
    line=$(echo $line | cut -c 3-)
    chop=$(echo $line | cut -c 25-) 
    printf "<a href="drawdxf.cgi?%s">%s</a><br/>" "$line" "$chop"
    
  done
  
  if ! [ -n "$harvester2" ];
  then
	echo "no Marcelo dxf files found<br/>"
  fi
  
  find ./sinks/donations/Marcelo/ -type f -iname \*$QUERY_STRING\* -name "*.dwg" | xargs -n 1 echo > $TempFile
  harvester=$TempFile
  harvester2=`cat $harvester`
  for line in $harvester2 ; do
    line=$(echo $line | cut -c 3-)
    chop=$(echo $line | cut -c 25-) 
    printf "<a href="drawdwg.cgi?%s">%s</a><br/>" "$line" "$chop"
    
  done
  
  if ! [ -n "$harvester2" ];
  then
	echo "no Marcelo dwg files found<br/>"
  fi
  
  ##################################
  
  ###############Gricks########################
  echo "<mark class="red">"
  echo "<a href="Gricks.cgi"><img class="lightning" src="mainimages/fairy.jpg" alt="" /></a> 7) Gricks' AlphaCAM results:<br/>"
  echo "</mark>"
 # echo "NEW! These were donated to the site.  Did you find them useful?<br/>(  <a href="expand.html">Then send in your sink files too! </a> ):</h1>"
  #echo "<p class="big">"
  #echo "NEW! These were donated to the site.  Did you find them useful?<br/>  <a href="expand.html">Then send in your sink files too!</a><br/><br/>"
  find ./sinks/donations/Gricks/ -type f -iname \*$QUERY_STRING\* -name "*.ard" | xargs -n 1 echo > $TempFile
  harvester=$TempFile
  harvester2=`cat $harvester`
  for line in $harvester2 ; do
    line=$(echo $line | cut -c 3-)
    chop=$(echo $line | cut -c 24-) 
    printf "<a href="drawAlphaCAM.cgi?%s">%s</a><br/>" "$line" "$chop"
    
  done
  
#  if ! [ -n "$harvester2" ];
#  then
#	echo "no Marcelo dxf files found<br/>"
#  fi
  
#  find ./sinks/donations/Marcelo/ -type f -iname \*$QUERY_STRING\* -name *.dwg | xargs -n 1 echo > $TempFile
#  harvester=$TempFile
#  harvester2=`cat $harvester`
#  for line in $harvester2 ; do
#    line=$(echo $line | cut -c 3-)
#    chop=$(echo $line | cut -c 17-) 
#    printf "<a href="drawdwg.cgi?%s">%s</a><br/>" "$line" "$chop"
    
#  done
  
  if ! [ -n "$harvester2" ];
  then
	echo "no Gricks' AlphaCAM files found<br/>"
  fi
  
  ##################################

#######################################
  echo "<mark class="red">"
  echo "<a href="Joes_Sinks.cgi"><img class="lightning" src="mainimages/silver-mage.jpg" alt="" /></a> 8) Joe's dxf and dwg results:<br/>"
  echo "</mark>"
 # echo "NEW! These were donated to the site.  Did you find them useful?<br/>(  <a href="expand.html">Then send in your sink files too! </a> ):</h1>"
  #echo "<p class="big">"
  #echo "NEW! These were donated to the site.  Did you find them useful?<br/>  <a href="expand.html">Then send in your sink files too!</a><br/><br/>"
  find ./sinks/donations/JOES_SINKS/ -type f -iname \*$QUERY_STRING\* -name "*.dxf" | xargs -n 1 echo > $TempFile
  harvester=$TempFile
  harvester2=`cat $harvester`
  for line in $harvester2 ; do
    line=$(echo $line | cut -c 3-)
    chop=$(echo $line | cut -c 28-) 
    printf "<a href="drawdxf.cgi?%s">%s</a><br/>" "$line" "$chop"
    
  done
  
  if ! [ -n "$harvester2" ];
  then
	echo "no Joe's Sinks dxf files found<br/>"
  fi
  
  find ./sinks/donations/JOES_SINKS/ -type f -iname \*$QUERY_STRING\* -name "*.dwg" | xargs -n 1 echo > $TempFile
  harvester=$TempFile
  harvester2=`cat $harvester`
  for line in $harvester2 ; do
    line=$(echo $line | cut -c 3-)
    chop=$(echo $line | cut -c 28-) 
    printf "<a href="drawdwg.cgi?%s">%s</a><br/>" "$line" "$chop"
    
  done
  
  if ! [ -n "$harvester2" ];
  then
	echo "no Joe's Sinks dwg files found<br/>"
  fi
  
  ##################################
  
  ########################################
  echo "<mark class="red">"
  echo "<a href="RJ.cgi"><img class="lightning" src="mainimages/impaler.jpg" alt="" /></a> 9) RJ AlphaCAM results:</br>"
  echo "</mark>"
 # echo "NEW! These were donated to the site.  Did you find them useful?<br/>(  <a href="expand.html">Then send in your sink files too! </a> ):</h1>"
  #echo "<p class="big">"
  #echo "NEW! These were donated to the site.  Did you find them useful?<br/>  <a href="expand.html">Then send in your sink files too!</a><br/><br/>"
  find ./sinks/donations/RJ/ -type f -iname \*$QUERY_STRING\* -name "*.asd" | xargs -n 1 echo > $TempFile
  harvester=$TempFile
  harvester2=`cat $harvester`
  for line in $harvester2 ; do
    line=$(echo $line | cut -c 3-)
    chop=$(echo $line | cut -c 20-) 
    printf "<a href="drawAlphaCAM.cgi?%s">%s</a><br/>" "$line" "$chop"
    
  done
  
  if ! [ -n "$harvester2" ];
  then
	echo "no RJ AlphaCAM files found<br/>"
  fi
#######################################

########################################
  echo "<mark class="red">"
  echo "<a href="cam_belph.cgi"><img class="lightning" src="mainimages/fighter.png" alt="" /></a> 10) cam_belph AlphaCAM results:</br>"
  echo "</mark>"
 # echo "NEW! These were donated to the site.  Did you find them useful?<br/>(  <a href="expand.html">Then send in your sink files too! </a> ):</h1>"
  #echo "<p class="big">"
  #echo "NEW! These were donated to the site.  Did you find them useful?<br/>  <a href="expand.html">Then send in your sink files too!</a><br/><br/>"
  find ./sinks/donations/cam_belph/ -type f -iname \*$QUERY_STRING\* -name "*.asd" | xargs -n 1 echo > $TempFile
  harvester=$TempFile
  harvester2=`cat $harvester`
  for line in $harvester2 ; do
    line=$(echo $line | cut -c 5-)
    chop=$(echo $line | cut -c 25-) 
    printf "<a href="drawAlphaCAM.cgi?%s">%s</a><br/>" "$line" "$chop"
    
  done
  
  if ! [ -n "$harvester2" ];
  then
	echo "no cam_belph AlphaCAM files found<br/>"
  fi
#######################################

#######################################
  echo "<mark class="red">"
  echo "<a href="ye_olde_stash.cgi"><img class="lightning" src="mainimages/dark-sorcerer-magic-2.png" alt="" /></a> 11) Ye Olde Stash DXF results:<br/>"
  echo "</mark>"
  echo "<mark class="blue">"
  echo "one more donation and i'll make these downloadable<br/>"
  echo "</mark>"
 # echo "NEW! These were donated to the site.  Did you find them useful?<br/>(  <a href="expand.html">Then send in your sink files too! </a> ):</h1>"
  #echo "<p class="big">"
  #echo "NEW! These were donated to the site.  Did you find them useful?<br/>  <a href="expand.html">Then send in your sink files too!</a><br/><br/>"
  find ./sinks/ruff/ -type f -iname \*$QUERY_STRING\* -name "*.dxf" | xargs -n 1 echo > $TempFile
  harvester=$TempFile
  harvester2=`cat $harvester`
  for line in $harvester2 ; do
    line=$(echo $line | cut -c 3-)
    #chop=$(echo $line | cut -c 28-)
    chop=$(echo $line | cut -c 12-) 
    #printf "<a href="drawdxf.cgi?%s">%s</a><br/>" "$line" "$chop"
    echo "$chop</br>"
    
  done
  
  if ! [ -n "$harvester2" ];
  then
	echo "no Ye Olde Stash DXF files found<br/>"
  fi
  
  find ./sinks/ruff/ -type f -iname \*$QUERY_STRING\* -name "*.dwg" | xargs -n 1 echo > $TempFile
  harvester=$TempFile
  harvester2=`cat $harvester`
  for line in $harvester2 ; do
    line=$(echo $line | cut -c 3-)
    #chop=$(echo $line | cut -c 28-)
    chop=$(echo $line | cut -c 12-) 
    #printf "<a href="drawdwg.cgi?%s">%s</a><br/>" "$line" "$chop"
    echo "$chop</br>"
    
  done
  
  if ! [ -n "$harvester2" ];
  then
	echo "no Ye Olde Stash DWG files found<br/>"
  fi
  
  ##################################



  echo "<mark class="red">"
  echo "<a href="laconicdxflist.cgi"><img class="lightning" src="mainimages/skirmisher.png" alt="" /></a> 12) laconiclizard's AlphaCAM results:<br/>"
  echo "</mark>"
#  echo "I drew all of these.  Are you using them?<br/>(  <a href="expand.html">Then send in your sinks too! </a> ):</h1>"
  #echo "<p class="big">"
  #echo "If I get 2 more donations I'll make all these downloadable:<br/><br/>"
  #more laconiclizard2.txt | grep -i $QUERY_STRING > $TempFile
  #harvester=$TempFile
  #harvester2=`cat $harvester`
  #for line in $harvester2 ; do
  #  echo "$line <br/>"
  #done
  count=0
  find ./sinks/FML/ -type f -iname \*$QUERY_STRING\* -name "*.ard" | xargs -n 1 echo > $TempFile
  harvester=$TempFile
  harvester2=`cat $harvester`
  for line in $harvester2 ; do
    line=$(echo $line | cut -c 3-)
    chop=$(echo $line | cut -c 11-) 
    printf "<a href="drawAlphaCAM.cgi?%s">%s</a><br/>" "$line" "$chop"
    
  done
  
  if ! [ -n "$harvester2" ];
  then
	count=1
  fi
  
  find ./sinks/FML/ -type f -iname \*$QUERY_STRING\* -name "*.asd" | xargs -n 1 echo > $TempFile
  harvester=$TempFile
  harvester2=`cat $harvester`
  for line in $harvester2 ; do
    line=$(echo $line | cut -c 3-)
    chop=$(echo $line | cut -c 11-) 
    printf "<a href="drawAlphaCAM.cgi?%s">%s</a><br/>" "$line" "$chop"
    
  done
  
  if ! [ -n "$harvester2" ] && [ $count == 1 ];
  then
	echo "no laconiclizard AlphaCAM files found<br/>"
  fi
  echo "</p>"

  echo "<h1>Blanco:</h1>"
  echo "<p>"
  echo "If searching for a Blanco sink then skip this page entirely and click the link below to go to the blanco match page:"
  echo "</p>"
  echo "<p class="big">"
  #<a href="print.html"><img src="mainimages/flanker.jpg" alt="" width="180" height="180" />PRINT LIST!</a>
  echo "<a href="match.cgi"><img class="wesnoth" src="mainimages/blademaster-melee-4.png" alt="" />Blanco Match!</a>"
  echo "</p>"  
fi

rm -- $TempFile

echo "<p class="big"><a href="sinks.cgi">HOME</a></p>"

echo "<p class="copyright">&copy; Copyright 2018 by laconiclizard"
echo "</p>"

echo "</div>"

echo "</body>"
echo "</html>"
