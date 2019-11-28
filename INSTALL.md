# INSTALL
FreeBSD 12-RELEASE

Python + telegraf

<pre><code># pkg install python
# pkg install py36-influxdb
# pkg install py36-protobuf
# pkg install telegraf</code></pre>

Telegraf configration for LSP stats:

<pre><code>urls = ["http://localhost:8086"]
database = "telemetry"

[[processors.regex]]  
  [[processors.regex.tags]]    
    key = "cntrname"     
    pattern = ".*"                 
    replacement = "a"         

  [[processors.regex.tags]]
    key = "cid"
    pattern = ".*"
    replacement = "a"
    
    
[[aggregators.basicstats]]    
period = "10s"  
drop_original = true    
stats = ["count", "min", "max", "mean", "stdev", "s2", "sum"]</code></pre>

