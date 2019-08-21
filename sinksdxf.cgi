#!/bin/sh

echo "Content-type: text/html"
echo ""

echo "<html>"
echo "<head>"
echo "<TITLE>sinksdxf"
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

echo "<h1>DEAD!</h1>"
echo "<p><a href="index.html"><img class="wesnoth" src="mainimages/shadow-s-2.png" alt="" /></a>"
echo "This page is dead.<br/><br/>"
echo "sinksdxf.cgi has been merged with the main page:<br/>"
echo "sinks.cgi<br/><br/>"
echo "So click the link below and never come back:"
echo "</p>"
echo "<p class="big"><a href="sinks.cgi">sinks.cgi</a></p>"

echo "<p class="copyright">&copy; Copyright 2015 by laconiclizard"
echo "</p>"

echo "</div>"

echo "</body>"
echo "</html>"
