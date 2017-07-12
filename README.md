# python-tor-selenium

here you can find some code for using python and selenium with tor connection.
it can be used for changing ip while you are testing something using chromedriver for example.

if you are on mac :<br>
<code>brew install tor</code><br>
<code>vi /usr/local/etc/tor/torrc</code>  commentout #ControlPort 9051 <br>
<code>brew install polipo </code> it is used for routing tor socks proxy to http proxy so it can be used by chromedriver<br>  
<code>polipo socksParentProxy=localhost:9050</code> execute polipo so it listens to tor's 9050 port and establishes listening socket on port 8123.<br>
<code>tor</code> execute tor<br>
now you can add proxy to your chrome driver and enjoy !

if you are on ubuntu :
you can use privoxy instead of polopo 
the port is 8118
