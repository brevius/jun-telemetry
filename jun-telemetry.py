#!/usr/bin/env python
############################################################
# Copyright (C) 2017, TomekS                               #
# All rights reserved.                                     #
#                                                          #
# Author:                                                  #
#        Tomasz Szewczyk                                   #
#                                                          #
# Purpose:                                                 #
#        Script for decoding JUNOS JVision messages.       #
#        Results are going to be sent to InfluxDB          #
#                                                          #
# Version: 0.1                                             #
#                                                          #
############################################################


import sys
sys.path.insert(0, 'proto')
import ntidecoder as nti                   #sensors decoders

# other modules
import os
import re
import logging
import socket
import json
import configparser
import argparse
import datetime
from multiprocessing import Process, Queue, cpu_count, Pool
from influxdb import InfluxDBClient
from copy import deepcopy

def getOptions(args=sys.argv[1:]):

    cmdline = argparse.ArgumentParser(description="NTI decoder")
    cmdline.add_argument("-c", metavar="file", help="Read configuration template from file", default=str(exec_path + '/jun-telemetry.conf'))
    cmdline.add_argument("-d", help="Dump decoded data", action='store_true')
    cmdline.add_argument("-t", help="Do NOT use Telegraf for LSP data", action='store_true')
    options = cmdline.parse_args(args)
    return options

def get_config_options(config_file):
    cfg = configparser.ConfigParser()
    cfg.optionxform=str
    cfg.read(config_file)
    return cfg._sections

def influxWrite(result):  # write to InfluxDB
    if type(result) is list:
        try:
            if any('lsp_usage' in item['measurement'] for item in result) and not options.t:
                influxWriteTelegraf(result)
            else:
                influxdb_client.write_points(result)
        except BaseException:
            LOG.exception('')

def influxWriteTelegraf(result):  # write to InfluxDB
    try:
        telegraf_client.write_points(result)
    except BaseException:
        LOG.exception('')

def telemetry_worker(pqueue):
    while True:
        if options.d:
            print (nti.telemetry_decoder(pqueue.get()))
        else:
            influxWrite(nti.telemetry_decoder(pqueue.get()))


#   f = tel_info.DESCRIPTOR.fields_by_name.keys()

exec_path = os.path.dirname(sys.argv[0])
options = getOptions()

try:
    conf = get_config_options(options.c)
except BaseException as err:
    print ("Config file error: ", options.c)
    print (err)
    quit()

try:
    for sensor in conf['RouterSensors'].keys():
        nti.sensor_conf[sensor] = conf['RouterSensors'][sensor]
    for msmt in conf['DBMeasurements'].keys():
        nti.measurement_conf[msmt] = conf['DBMeasurements'][msmt]
except BaseException as err:
    print ("Some RouterSensors/DBMeasurements problem - using defaults")
    print (err)

influxdb_client = InfluxDBClient(conf['InfluxDB']['Influx_server'], int(conf['InfluxDB']['Influx_port']), conf['InfluxDB']['Influx_user'],  conf['InfluxDB']['Influx_pass'], conf['InfluxDB']['Influx_database'])  # InfluxDB definition
telegraf_client = InfluxDBClient(conf['Telegraf']['Telegraf_server'], int(conf['Telegraf']['Telegraf_port']), conf['Telegraf']['Telegraf_user'],  conf['Telegraf']['Telegraf_pass'], "test")

logging.basicConfig(stream=open(conf['TelemetryServer']['LOG_FILE'], "a+"), format="%(asctime)-15s")
LOG = logging.getLogger(__name__)

# main function
def main():
    pqueue = Queue()
    decoder_proc = [Process(target=telemetry_worker, args=(pqueue,)) for i in range(cpu_count())]
    for i in range (cpu_count()):
        decoder_proc[i].start()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((conf['TelemetryServer']['UDP_IP'], int(conf['TelemetryServer']['UDP_PORT'])))
    while True:
        data, addr = sock.recvfrom(16000)
        pqueue.put(data)

if __name__ == "__main__":
    main()
