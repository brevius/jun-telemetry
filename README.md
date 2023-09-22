# jun-telemetry
NTI message decoder for Juniper routers

Receives GPB data from Juniper routers and sends decoded counters to InfluxDB. Requires python3 and protobuf. Tested with Junos 16.1/17.3 and FreeBSD12.0-RELEASE

NOTE: Each Junos version require compiled `.proto` files (19.4 now included)

<pre><code>usage: jun-telemetry.py [-h] [-c file] [-d] [-t]

NTI decoder

optional arguments:
  -h, --help  show this help message and exit
  -c file     Read configuration template from file
  -d          Dump decoded data
  -t          Do NOT use Telegraf for LSP data</code></pre>

Configuration file is used to setup collector and InfluxDB database parameters. It is recommended to use Telegraf for LSP statistics (default).

`[TelemetryServer]` section defines IP address and UDP port to listen on for GPB data:

<pre><code>[TelemetryServer]
UDP_IP   = 0.0.0.0
UDP_PORT = 50000
LOG_FILE = jun-telemetry.log</code></pre>

`[InfluxDB]` section defines IP address and TCP port on which http interface of InfluxDB database is enabled:

<pre><code>[InfluxDB]
Influx_server   = 127.0.0.1
Influx_port     = 8086
Influx_user     = root
Influx_pass     = root
Influx_database = telemetry</code></pre>

Telegraf is used to summarize LSP usage data in order to avoid InfluxDB overload.

<pre><code>[Telegraf]
Telegraf_server  = localhost
Telegraf_port    = 8186
Telegraf_user    = root
Telegraf_pass    = root</code></pre>


`[RouterSensors]` section maps sensor decoders to names configured on routers (do not change the left side):

`npu_util     = npu-util-test` maps `npu-util-test` sensor configured on the router to NPU utilizastion decoder:

<pre><code>sensor npu-util-test {
    resource /junos/system/linecard/npu/utilization/;
}</code></pre>

Currently supported sensors:

<pre><code>pfe          /junos/system/linecard/packet/usage/
int_phy      /junos/system/linecard/interface/
optic        /junos/system/linecard/optics/
int_logic    /junos/system/linecard/interface/logical/usage/
npu_util     /junos/system/linecard/npu/utilization/
lsp_usage    /junos/services/label-switched-path/usage/
fabric       /junos/system/linecard/fabric/
npu_mem_ext  /junos/system/linecard/npu/memory/
firewall     /junos/system/linecard/firewall/
inline-jflow /junos/system/linecard/services/inline-jflow/</code></pre>

`[DBMeasurements]` section defines names for InfluxDB measurements saved in database.

`npu_util     = npu-util` defines InfluxDB `npu-util` measurement for `npu_util` sensor.

<pre><code>InfluxDB shell version: 1.7.6
Enter an InfluxQL query
> use telemetry
Using database telemetry
> show measurements
name: measurements
name
----
fw_counter
int-queue
interface
lsp.usage
npm_mem_ext
npm_mem_ext_det
optics
pfe
pfe_detail</code></pre>

## Docker
Docker image available 

https://hub.docker.com/r/brevius/juntelemetry

<code>docker pull brevius/juntelemetry</code>
  
Docker-compose contains jun-telemetry, telegraf and VictoriaMetrics applications 
