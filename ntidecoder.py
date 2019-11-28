############################################################
# Copyright (C) 2017, TomekS                               #
# All rights reserved.                                     #
#                                                          #
# Author:                                                  #
#        Tomasz Szewczyk   tomeks@man.poznan.pl            #
#                                                          #
# Version: 0.1                                             #
#                                                          #
############################################################

import os
import re
from copy import deepcopy

# Juniper .proto definitions
import cpu_memory_utilization_pb2
import fabric_pb2
import firewall_pb2
import inline_jflow_pb2
import logical_port_pb2
import lsp_stats_pb2
import npu_memory_utilization_pb2
import npu_utilization_pb2
import optics_pb2
import packet_stats_pb2
import port_pb2
import telemetry_top_pb2

sensor_conf = {
  'npu_util':    'npu-util',
  'optic':       'optic',
  'int_phy':     'int_phy',
  'int_logic':   'if-logic',
  'pfe':         'pfe',
  'fabric':      'fabric',
  'lsp_usage':   'lsp-usage',
  'npu_mem_ext': 'npu-mem-ext',
  'firewall':    'fw'
}

measurement_conf = {
  'npu_util':        'npu-util',
  'optic':           'optics',
  'int_phy':         'interface',
  'queue_info':      'int-queue',
  'int_logic':       'if_logic',
  'pfe_detail':      'pfe_detail',
  'pfe':             'pfe',
  'fabric.sw':       'fabric.sw',
  'fabric.lnsw':     'fabric.lnsw',
  'fabric.lncrd':    'fabric.lncrd',
  'lsp_usage':       'lsp.usage',
  'npu_mem_ext':     'npu_mem_ext',
  'npu_mem_ext_det': 'npu_mem_ext_det',
  'fw_counter':      'fw_counter'
}

pfe_packet_stats = {
# Junos 16.1
  'input'                       :'in',
  'output'                      :'out',
  'local_packets_input'         :'lpi',
  'local_packets_output'        :'lpo',
  'control_high_drops'          :'chd',
  'input_high_drops'            :'ihd',
  'input_medium_drops'          :'imd',
  'input_low_drops'             :'ild',
  'input_drops'                 :'id',
  'output_drops'                :'od',
  'hardware_input_drops'        :'hwid',
  'Notification/control_packet_drops_in_ISR':'ncpd',
  'fabric_drops'                :'fd',
  'regular_discards'            :'rd',
  'packet_get_failure'          :'pgf',
  'rate_limited'                :'rl',
  'dma_failure'                 :'dmaf',
  'total_dma_packets'           :'tdma',
# Junos 17.3
  'lts-input-packets'           :'ltsin',
  'lts-output-packets'          :'ltsout',
  'lts-sw-input-control-drops'  :'ltssw-icd',
  'lts-sw-input-high-drops'     :'ltssw-ihd',
  'lts-sw-input-medium-drops'   :'ltssw-imd',
  'lts-sw-input-low-drops'      :'ltssw-ild',
  'lts-sw-output-low-drops'     :'ltssw-old'
}

packet_stats_pfe = {
# Junos 16.1
  'firewall-drops'              :'fw_drps',
  'inet-drops'                  :'inet_drps',
  'inet6-drops'                 :'inet6_drps',
  'mpls-drops'                  :'mpls_drps',
  'ttl-expires'                 :'ttl_exp',
  'bad-interface-discards'      :'badif_disc',
  'bad-fabric-token-discards'   :'badfabtoken_disc',
# Junos 17.3
  'ts-input-packets'            :'ts-in',
  'ts-output-packets'           :'ts-out',
  'ts-fabric-input-packets'     :'ts-fab-in',
  'ts-fabric-output-packets'    :'ts-fab-out',
  'lpbk-packets'                :'lpbk',
  'lpbk-drop-packets'           :'lpbk-d',
  'lts-hw-input-drops'          :'lts-hw-id',
  'hwds-normal'                 :'hwds-norm',
  'hwds-fabric'                 :'hwds-fab',
  'hwds-info-cell'              :'hwds-info-cell',
  'hwds-timeout'                :'hwds-timeout',
  'hwds-truncated-key'          :'hwds-trunc-key',
  'hwds-bits-to-test'           :'hwds-btt',
  'hwds-stack-underflow'        :'hwds-stck-uf',
  'hwds-stack-overflow'         :'hwds-stck-of',
  'hwds-data-error'             :'hwds-de',
  'hwds-extended'               :'hwds-ext',
  'hwds-invalid-iif'            :'hwds-inv-iif',
  'hwds-input-checksum'         :'hwds-in-chck',
  'hwds-output-mtu'             :'hwds-out-mtu',
  'hwds-inet-bad-route'         :'hwds-inet-bad-rt',
  'hwds-inet6-bad-route'        :'hwds-inet6-bad-rt',
  'hwds-filter-discard'         :'hwds-filter-discard',
  'hwds-dlu-not-routable'       :'hwds-dlu-notrt'
}

firewall_stats = {
  'packets'    :'pkts',
  'bytes'      :'bytes'
}

def telemetry_decoder(sampledata):
    tel_info = telemetry_top_pb2.TelemetryStream()
    tel_info.ParseFromString(sampledata)
    print ('sensorname: ', tel_info.sensor_name, 'process id:', os.getpid())
    sensorname = tel_info.sensor_name.split(':')[0]  # split pfe:/junos/system/linecard/packet/usage/:/junos/system/linecard/packet/usage/:PFE
    systemid = re.sub('-re.$', '', tel_info.system_id.split(':')[0] )  # cut -reX:A.B.C.D from mx-aaa-re0
    componentid = tel_info.component_id

    def npu_util_decode(systemid):  # /junos/system/linecard/npu/utilization/
        final_result = []
        result = {}
        result['measurement'] = measurement_conf['npu_util']
        fields = {}
        tags = {}
        tags['system_id'] = systemid
        for i in tel_info.enterprise.Extensions[telemetry_top_pb2.juniperNetworks].Extensions[npu_utilization_pb2.jnpr_npu_utilization_ext].npu_util_stats:
            for b in i.packets:
                fields['npu_pckt_rate'] = b.rate
                fields['npu_pckt_aipp'] = b.average_instructions_per_packet
                fields['npu_pckt_awcpp'] = b.average_wait_cycles_per_packet
                fields['npu_pckt_acpp'] = b.average_cycles_per_packet

            for b in i.memory:
                fields["%s_au" % (b.name[:2],)] = b.average_util
                fields["%s_hu" % (b.name[:2],)] = b.highest_util
                fields["%s_lu" % (b.name[:2],)] = b.lowest_util
                fields["%s_achr" % (b.name[:2],)] = b.average_cache_hit_rate
                fields["%s_hchr" % (b.name[:2],)] = b.highest_cache_hit_rate
                fields["%s_lchr" % (b.name[:2],)] = b.lowest_cache_hit_rate
            tags['identifier'] = i.identifier
            result['fields'] = fields
            result['tags'] = tags
            final_result.append(deepcopy(result))

        return final_result

    def npu_mem_ext_decode(systemid):
        final_result = []
        result = {}
        fields = {}
        tags = {}
        try:
            for i in tel_info.enterprise.Extensions[telemetry_top_pb2.juniperNetworks].Extensions[npu_memory_utilization_pb2.npu_memory_ext].memory_stats:
                result = {}
                tags={}
                for sum in i.summary:
                    fields['size'] = sum.size
                    fields['alloc'] = sum.allocated
                    fields['util'] = sum.utilization
                    result['measurement'] = 'npm_mem_ext'
                    tags['system_id'] = systemid
                    tags['elem'] = i.identifier
                    tags['res'] = sum.resource_name
                    result['fields'] = fields
                    result['tags'] = tags
                    final_result.append(deepcopy(result))
                result={}
                tags={}
                for part in i.partition:
                    fields['free'] = part.free_count
                    fields['byte_alloc'] = part.bytes_allocated
                    fields['alloc_cnt'] = part.allocation_count
                    result['measurement'] = 'npm_mem_ext_det'
                    result['fields'] = fields
                    tags['system_id'] = systemid
                    tags['elem'] = i.identifier
                    tags['ident'] = part.name
                    tags['app'] = part.application_name
                    result['tags'] = tags
                    final_result.append(deepcopy(result))
        except BaseException as err:
            print (err)
            pass
        return final_result

    def optic_decode(systemid):
        final_result = []
        result = {}
        result['measurement'] = measurement_conf['optic']
        fields = {}
        tags = {}
        tags['system_id'] = systemid
        for i in tel_info.enterprise.Extensions[telemetry_top_pb2.juniperNetworks].Extensions[optics_pb2.jnpr_optics_ext].Optics_diag:
            tags['if'] = i.if_name
            fields['mtemp'] = i.optics_diag_stats.module_temp
            fields['mtha'] = i.optics_diag_stats.module_temp_high_alarm
            fields['mthw'] = i.optics_diag_stats.module_temp_high_warning
            for b in i.optics_diag_stats.optics_lane_diag_stats:
                tags['lane'] = b.lane_number
                fields['lrx'] = b.lane_laser_receiver_power_dbm
                fields['ltemp'] = b.lane_laser_temperature
                fields['ltx'] = b.lane_laser_output_power_dbm
                fields['lrxha'] = b.lane_laser_receiver_power_high_alarm
                fields['lrxla'] = b.lane_laser_receiver_power_low_alarm
                fields['lrxwa'] = b.lane_laser_receiver_power_high_warning
                fields['lrxlw'] = b.lane_laser_receiver_power_low_warning
                fields['llos'] = b.lane_rx_loss_of_signal_alarm

                result['fields'] = fields
                result['tags'] = tags
                final_result.append(deepcopy(result))

        return final_result


    def int_phy_decode(systemid):  # /junos/system/linecard/interface/

        def queue_info_process(systemid, if_name, b):  # queue info processing (separate measurement)
            qresult = {}
            qfields = {}
            qtags = {}
            qtags['system_id'] = systemid
            qtags['queue'] = b.queue_number
            qtags['if'] = i.if_name
            qresult['measurement'] = measurement_conf['queue_info']

            qfields['q_pkts'] = b.packets
            qfields['q_bytes'] = b.bytes
            qfields['q_tdrpkts'] = b.tail_drop_packets
            qfields['q_rldrpkts'] = b.rl_drop_packets
            qfields['q_rldrbytes'] = b.rl_drop_bytes
            qfields['q_reddrpkts'] = b.red_drop_packets
            qfields['q_reddrbytes'] = b.red_drop_bytes
            qfields['q_avbufoc'] = b.avg_buffer_occupancy
            qfields['q_curbufocc'] = b.cur_buffer_occupancy
            qfields['q_pkbufocc'] = b.peak_buffer_occupancy
            qfields['q_allocbufsize'] = b.allocated_buffer_size
    
            qresult['fields'] = qfields
            qresult['tags'] = qtags
            final_result.append(deepcopy(qresult))
    
        final_result = []
        result = {}
        fields = {}
        tags = {}
        tags['system_id'] = systemid
        result['measurement'] = measurement_conf['int_phy']
        for i in tel_info.enterprise.Extensions[telemetry_top_pb2.juniperNetworks].Extensions[port_pb2.jnpr_interface_ext].interface_stats:
            tags['if'] = i.if_name
            tags['if_idx'] = i.snmp_if_index
            if i.parent_ae_name:
                tags['lag'] = i.parent_ae_name
            for b in i.egress_queue_info:
                queue_info_process(systemid, i.if_name, b)
    
            fields['i_pkts'] = i.ingress_stats.if_pkts
            fields['i_octets'] = i.ingress_stats.if_octets
            fields['i_1sec_pkts'] = i.ingress_stats.if_1sec_pkts
            fields['i_1sec_octets'] = i.ingress_stats.if_1sec_octets
            fields['i_uc_pkts'] = i.ingress_stats.if_uc_pkts
            fields['i_mc_pkts'] = i.ingress_stats.if_mc_pkts
            fields['i_bc_pkts'] = i.ingress_stats.if_bc_pkts
            fields['i_bc_error'] = i.ingress_stats.if_error
            fields['i_pause'] = i.ingress_stats.if_pause_pkts
    
            fields['e_pkts'] = i.egress_stats.if_pkts
            fields['e_octets'] = i.egress_stats.if_octets
            fields['e_1sec_pkts'] = i.egress_stats.if_1sec_pkts
            fields['e_1sec_octets'] = i.egress_stats.if_1sec_octets
            fields['e_uc_pkts'] = i.egress_stats.if_uc_pkts
            fields['e_mc_pkts'] = i.egress_stats.if_mc_pkts
            fields['e_bc_pkts'] = i.egress_stats.if_bc_pkts
            fields['e_bc_error'] = i.egress_stats.if_error
            fields['e_pause'] = i.egress_stats.if_pause_pkts
    
            fields['ie_errors'] = i.ingress_errors.if_errors
            fields['ie_qdrops'] = i.ingress_errors.if_in_qdrops
            fields['ie_frerrors'] = i.ingress_errors.if_in_frame_errors
            fields['ie_disc'] = i.ingress_errors.if_discards
            fields['ie_runts'] = i.ingress_errors.if_in_runts
            fields['ie_l3incomp'] = i.ingress_errors.if_in_l3_incompletes
            fields['ie_l2chan'] = i.ingress_errors.if_in_l2chan_errors
            fields['ie_l2mis_t'] = i.ingress_errors.if_in_l2_mismatch_timeouts
            fields['ie_fifo'] = i.ingress_errors.if_in_fifo_errors
            fields['ie_res'] = i.ingress_errors.if_in_resource_errors
    
            result['fields'] = fields
            result['tags'] = tags
            final_result.append(deepcopy(result))
        return final_result
    
    
    def int_logic_decode(systemid):  # /junos/system/linecard/interface/logical/usage/
        final_result = []
        result = {}
        fields = {}
        tags = {}
        tags['system_id'] = systemid
        result['measurement'] = measurement_conf['int_logic']
        for i in tel_info.enterprise.Extensions[telemetry_top_pb2.juniperNetworks].Extensions[logical_port_pb2.jnprLogicalInterfaceExt].interface_info:
            tags['if'] = i.if_name
            fields['op_state'] = i.op_state.operational_status
            fields['i_packets'] = i.ingress_stats.if_packets
            fields['i_octets'] = i.ingress_stats.if_octets
            fields['i_ucast_packets'] = i.ingress_stats.if_ucast_packets
            fields['i_mcast_packets'] = i.ingress_stats.if_mcast_packets
    
            fields['e_packets'] = i.egress_stats.if_packets
            fields['e_octets'] = i.egress_stats.if_octets
            fields['e_ucast_packets'] = i.egress_stats.if_ucast_packets
            fields['e_mcast_packets'] = i.egress_stats.if_mcast_packets
    
            result['fields'] = fields
            result['tags'] = tags
            final_result.append(deepcopy(result))
    
        return final_result
    
    
    def pfe_decode(systemid, componentid):  # pfe
    
        def pfe_detail_decode(systemid, b, pfe_name):                 # pfe module details decode
            presult = {}
            pfields = {}
            ptags = {}
            ptags['system_id'] = systemid
            ptags['cid'] = componentid
            presult['measurement'] = measurement_conf['pfe_detail']
            ptags['pfe_id'] = pfe_name
            try:
                pfields[packet_stats_pfe[b.name]+'_pc'] = b.counter.packet_count
            except:
                print ('Unknown field type ', b.name)
                pass
            presult['fields'] = pfields
            presult['tags'] = ptags
            final_result.append(deepcopy(presult))
    
        final_result = []
        final_result[:] = []
        result = {}
        fields = {}
        tags = {}
        tags['system_id'] = systemid
        result['measurement'] = measurement_conf['pfe']
        tags['elem'] = 'global'
        tags['cid'] = componentid
        for i in tel_info.enterprise.Extensions[telemetry_top_pb2.juniperNetworks].Extensions[packet_stats_pb2.jnpr_packet_statistics_ext].packet_stats:
    
            try:
                if i.counter.packet_count < 30000000000000:        # Junos bug 16.1
                    fields[pfe_packet_stats[i.name]+'_pc'] = i.counter.packet_count
            except:
                print ('Unknown field type ', i.name)
                pass
    
        result['fields'] = fields
        result['tags'] = tags
        final_result.append(deepcopy(result))
    
        pfenumber = 0
        for i in tel_info.enterprise.Extensions[telemetry_top_pb2.juniperNetworks].Extensions[packet_stats_pb2.jnpr_packet_statistics_ext].packet_stats_pfe:
            if i.pfe_identifier == "pfe-":       # pfe- without identifier! incremental workaround!!!
                pfe_ident = 'pfe-' + str(componentid) + '/' + str(pfenumber)
            else:
                pfe_ident = deepcopy(i.pfe_identifier)
            for b in i.packet_stats:
                pfe_detail_decode(systemid, b, pfe_ident)
            pfenumber += 1
    
        return final_result
    
    
    def fabric_decode(systemid):  # /junos/system/linecard/fabric/
        final_result = []
        result = {}
        fields = {}
        tags = {}
        for i in tel_info.enterprise.Extensions[telemetry_top_pb2.juniperNetworks].Extensions[fabric_pb2.fabricMessageExt].edges:
            if i.source_type == 1:  # Switch_Fabric
                tags['system_id'] = systemid
                tags['dst_slot'] = i.destination_slot
                tags['dst_pfe'] = i.destination_pfe
                for b in i.class_stats:
                    fields["pkts"] = b.transmit_counts.packets
                    fields["bytes"] = b.transmit_counts.bytes
                    fields["pps"] = b.transmit_counts.packets_per_second
                    fields["bytsps"] = b.transmit_counts.bytes_per_second
                    fields["dpkts"] = b.transmit_counts.drop_packets
                    fields["dpps"] = b.transmit_counts.drop_packets_per_second
                    fields["epkts"] = b.transmit_counts.error_packets
                    fields["epps"] = b.transmit_counts.error_packets_per_second
    
                    result['measurement'] = measurement_conf['fabric.sw']
                    result['fields'] = fields
                    result['tags'] = tags
                    final_result.append(deepcopy(result))
                    result = {}
                    fields = {}
                    tags = {}
    
            if i.source_type == 2:  # Line_Card
                if i.destination_type == 1:  # Switch_Fabric
                    tags['system_id'] = systemid
                    tags['src_slot'] = i.source_slot
                    tags['src_pfe'] = i.source_pfe
                    for b in i.class_stats:
                        fields["pkts"] = b.transmit_counts.packets
                        fields["bytes"] = b.transmit_counts.bytes
                        fields["pps"] = b.transmit_counts.packets_per_second
                        fields["bytsps"] = b.transmit_counts.bytes_per_second
    
                        result['measurement'] = measurement_conf['fabric.lnsw']
                        result['fields'] = fields
                        result['tags'] = tags
                        final_result.append(deepcopy(result))
                        result = {}
                        fields = {}
                        tags = {}
    
                if i.destination_type == 2:  # Line_Card
                    tags['system_id'] = systemid
                    tags['src_slot'] = i.source_slot
                    tags['src_pfe'] = i.source_pfe
                    tags['dst_slot'] = i.destination_slot
                    tags['dst_pfe'] = i.destination_pfe
                    for b in i.class_stats:
                        tags['pri'] = b.priority
                        fields["pkts"] = b.transmit_counts.packets
                        fields["bytes"] = b.transmit_counts.bytes
                        fields["pps"] = b.transmit_counts.packets_per_second
                        fields["bytsps"] = b.transmit_counts.bytes_per_second
                        fields["dpkts"] = b.transmit_counts.drop_packets
                        fields["dbytes"] = b.transmit_counts.drop_bytes
                        fields["dpps"] = b.transmit_counts.drop_packets_per_second
                        fields["dbytsps"] = b.transmit_counts.drop_bytes_per_second
                        fields["qdav"] = b.transmit_counts.queue_depth_average
                        fields["qdc"] = b.transmit_counts.queue_depth_current
                        fields["qdp"] = b.transmit_counts.queue_depth_peak
                        fields["qdmax"] = b.transmit_counts.queue_depth_maximum
    
                        result['measurement'] = measurement_conf['fabric.lncrd']
                        result['fields'] = fields
                        result['tags'] = tags
                        final_result.append(deepcopy(result))
                        result = {}
                        fields = {}
                        tags = {}
        return final_result
    
    
    def lsp_usage_decode(systemid, componentid):
        final_result = []
        final_result[:] = []
        result = {}
        fields = {}
        tags = {}
        for i in tel_info.enterprise.Extensions[telemetry_top_pb2.juniperNetworks].Extensions[lsp_stats_pb2.jnpr_lsp_statistics_ext].lsp_stats_records:
            result['measurement'] = measurement_conf['lsp_usage']
            if "Bypass" not in i.name:
                if i.packets != 0 and i.bytes != 0 and i.packet_rate != 0 and i.byte_rate != 0:
                    result['measurement'] = measurement_conf['lsp_usage']
                    tags['system_id'] = systemid
                    tags['lspname'] = i.name
                    tags['instanceid'] = i.instance_identifier
                    tags['cntrname'] = i.counter_name
                    tags['cid'] = componentid
                    fields["pkts"] = i.packets
                    fields["bytes"] = i.bytes
                    fields["pps"] = i.packet_rate
                    fields["bytsps"] = i.byte_rate

                    result['fields'] = fields
                    result['tags'] = tags
                    final_result.append(deepcopy(result))
                    result = {}
                    fields = {}
                    tags = {}

        if final_result:
            return final_result

    def firewall_decode(systemid, componentid):
        final_result = []
        final_result[:] = []
        result = {}
        fields = {}
        tags = {}
        try:
            for i in tel_info.enterprise.Extensions[telemetry_top_pb2.juniperNetworks].Extensions[firewall_pb2.jnpr_firewall_ext].firewall_stats:
                tags['system_id'] = systemid
                tags['fw_name'] = i.filter_name
                tags['cid'] = componentid
                if i.counter_stats:
                    result['measurement'] = measurement_conf['fw_counter']
                    for b in i.counter_stats:
                        fields[firewall_stats['packets']] = b.packets
                        fields[firewall_stats['bytes']] = b.bytes
                        tags['ctrname'] = b.name
                        result['fields'] = fields
                        result['tags'] = tags
                        final_result.append(deepcopy(result))
        except BaseException as err:
            print (err)
            pass
        return final_result
            
    if sensorname == sensor_conf['npu_util']:
        return npu_util_decode(systemid)

    if sensorname == sensor_conf['npu_mem_ext']:
        return npu_mem_ext_decode(systemid)

    if sensorname == sensor_conf['optic']:
        return optic_decode(systemid)

    if sensorname == sensor_conf['int_phy']:
        return int_phy_decode(systemid)

    if sensorname == sensor_conf['int_logic']:
        return int_logic_decode(systemid)

    if sensorname == sensor_conf['pfe']:
        return pfe_decode(systemid, componentid)

    if sensorname == sensor_conf['fabric']:
        return fabric_decode(systemid)

    if sensorname == sensor_conf['lsp_usage']:
        return lsp_usage_decode(systemid, componentid)
        
    if sensorname == sensor_conf['firewall']:
        return firewall_decode(systemid, componentid)
