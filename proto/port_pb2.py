# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: port.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import telemetry_top_pb2 as telemetry__top__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='port.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nport.proto\x1a\x13telemetry_top.proto\"0\n\x04Port\x12(\n\x0finterface_stats\x18\x01 \x03(\x0b\x32\x0f.InterfaceInfos\"\x8d\x04\n\x0eInterfaceInfos\x12\x16\n\x07if_name\x18\x01 \x02(\tB\x05\x82@\x02\x08\x01\x12\x11\n\tinit_time\x18\x02 \x01(\x04\x12\x15\n\rsnmp_if_index\x18\x03 \x01(\r\x12\x16\n\x0eparent_ae_name\x18\x04 \x01(\t\x12&\n\x11\x65gress_queue_info\x18\x05 \x03(\x0b\x32\x0b.QueueStats\x12\'\n\x12ingress_queue_info\x18\x06 \x03(\x0b\x32\x0b.QueueStats\x12&\n\ringress_stats\x18\x07 \x01(\x0b\x32\x0f.InterfaceStats\x12%\n\x0c\x65gress_stats\x18\x08 \x01(\x0b\x32\x0f.InterfaceStats\x12/\n\x0eingress_errors\x18\t \x01(\x0b\x32\x17.IngressInterfaceErrors\x12 \n\x18if_administration_status\x18\n \x01(\t\x12\x1d\n\x15if_operational_status\x18\x0b \x01(\t\x12\x16\n\x0eif_description\x18\x0c \x01(\t\x12\x1d\n\x0eif_transitions\x18\r \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\x14\n\x0cifLastChange\x18\x0e \x01(\r\x12\x13\n\x0bifHighSpeed\x18\x0f \x01(\r\x12-\n\regress_errors\x18\x10 \x01(\x0b\x32\x16.EgressInterfaceErrors\"\x8d\x03\n\nQueueStats\x12\x1b\n\x0cqueue_number\x18\x01 \x01(\rB\x05\x82@\x02\x08\x01\x12\x16\n\x07packets\x18\x02 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\x14\n\x05\x62ytes\x18\x03 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12 \n\x11tail_drop_packets\x18\x04 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\x1e\n\x0frl_drop_packets\x18\x05 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\x1c\n\rrl_drop_bytes\x18\x06 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\x1f\n\x10red_drop_packets\x18\x07 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\x1d\n\x0ered_drop_bytes\x18\x08 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12#\n\x14\x61vg_buffer_occupancy\x18\t \x01(\x04\x42\x05\x82@\x02 \x01\x12#\n\x14\x63ur_buffer_occupancy\x18\n \x01(\x04\x42\x05\x82@\x02 \x01\x12$\n\x15peak_buffer_occupancy\x18\x0b \x01(\x04\x42\x05\x82@\x02 \x01\x12$\n\x15\x61llocated_buffer_size\x18\x0c \x01(\x04\x42\x05\x82@\x02 \x01\"\xac\x02\n\x0eInterfaceStats\x12\x16\n\x07if_pkts\x18\x01 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\x18\n\tif_octets\x18\x02 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\x1b\n\x0cif_1sec_pkts\x18\x03 \x01(\x04\x42\x05\x82@\x02 \x01\x12\x1d\n\x0eif_1sec_octets\x18\x04 \x01(\x04\x42\x05\x82@\x02 \x01\x12\x19\n\nif_uc_pkts\x18\x05 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\x19\n\nif_mc_pkts\x18\x06 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\x19\n\nif_bc_pkts\x18\x07 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\x17\n\x08if_error\x18\x08 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\x1c\n\rif_pause_pkts\x18\t \x01(\x04\x42\x05\x82@\x02\x18\x01\x12$\n\x15if_unknown_proto_pkts\x18\n \x01(\x04\x42\x05\x82@\x02\x18\x01\"\xe6\x02\n\x16IngressInterfaceErrors\x12\x18\n\tif_errors\x18\x01 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\x1b\n\x0cif_in_qdrops\x18\x02 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12!\n\x12if_in_frame_errors\x18\x03 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\x1a\n\x0bif_discards\x18\x04 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\x1a\n\x0bif_in_runts\x18\x05 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12#\n\x14if_in_l3_incompletes\x18\x06 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\"\n\x13if_in_l2chan_errors\x18\x07 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12)\n\x1aif_in_l2_mismatch_timeouts\x18\x08 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12 \n\x11if_in_fifo_errors\x18\t \x01(\x04\x42\x05\x82@\x02\x18\x01\x12$\n\x15if_in_resource_errors\x18\n \x01(\x04\x42\x05\x82@\x02\x18\x01\"M\n\x15\x45gressInterfaceErrors\x12\x18\n\tif_errors\x18\x01 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\x1a\n\x0bif_discards\x18\x02 \x01(\x04\x42\x05\x82@\x02\x18\x01::\n\x12jnpr_interface_ext\x12\x17.JuniperNetworksSensors\x18\x03 \x01(\x0b\x32\x05.Port'
  ,
  dependencies=[telemetry__top__pb2.DESCRIPTOR,])


JNPR_INTERFACE_EXT_FIELD_NUMBER = 3
jnpr_interface_ext = _descriptor.FieldDescriptor(
  name='jnpr_interface_ext', full_name='jnpr_interface_ext', index=0,
  number=3, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)


_PORT = _descriptor.Descriptor(
  name='Port',
  full_name='Port',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='interface_stats', full_name='Port.interface_stats', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=83,
)


_INTERFACEINFOS = _descriptor.Descriptor(
  name='InterfaceInfos',
  full_name='InterfaceInfos',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='if_name', full_name='InterfaceInfos.if_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\010\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='init_time', full_name='InterfaceInfos.init_time', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='snmp_if_index', full_name='InterfaceInfos.snmp_if_index', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parent_ae_name', full_name='InterfaceInfos.parent_ae_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='egress_queue_info', full_name='InterfaceInfos.egress_queue_info', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ingress_queue_info', full_name='InterfaceInfos.ingress_queue_info', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ingress_stats', full_name='InterfaceInfos.ingress_stats', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='egress_stats', full_name='InterfaceInfos.egress_stats', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ingress_errors', full_name='InterfaceInfos.ingress_errors', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='if_administration_status', full_name='InterfaceInfos.if_administration_status', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='if_operational_status', full_name='InterfaceInfos.if_operational_status', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='if_description', full_name='InterfaceInfos.if_description', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='if_transitions', full_name='InterfaceInfos.if_transitions', index=12,
      number=13, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ifLastChange', full_name='InterfaceInfos.ifLastChange', index=13,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ifHighSpeed', full_name='InterfaceInfos.ifHighSpeed', index=14,
      number=15, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='egress_errors', full_name='InterfaceInfos.egress_errors', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=611,
)


_QUEUESTATS = _descriptor.Descriptor(
  name='QueueStats',
  full_name='QueueStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='queue_number', full_name='QueueStats.queue_number', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\010\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='packets', full_name='QueueStats.packets', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bytes', full_name='QueueStats.bytes', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tail_drop_packets', full_name='QueueStats.tail_drop_packets', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rl_drop_packets', full_name='QueueStats.rl_drop_packets', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rl_drop_bytes', full_name='QueueStats.rl_drop_bytes', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='red_drop_packets', full_name='QueueStats.red_drop_packets', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='red_drop_bytes', full_name='QueueStats.red_drop_bytes', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='avg_buffer_occupancy', full_name='QueueStats.avg_buffer_occupancy', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002 \001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cur_buffer_occupancy', full_name='QueueStats.cur_buffer_occupancy', index=9,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002 \001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='peak_buffer_occupancy', full_name='QueueStats.peak_buffer_occupancy', index=10,
      number=11, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002 \001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='allocated_buffer_size', full_name='QueueStats.allocated_buffer_size', index=11,
      number=12, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002 \001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=614,
  serialized_end=1011,
)


_INTERFACESTATS = _descriptor.Descriptor(
  name='InterfaceStats',
  full_name='InterfaceStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='if_pkts', full_name='InterfaceStats.if_pkts', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='if_octets', full_name='InterfaceStats.if_octets', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='if_1sec_pkts', full_name='InterfaceStats.if_1sec_pkts', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002 \001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='if_1sec_octets', full_name='InterfaceStats.if_1sec_octets', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002 \001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='if_uc_pkts', full_name='InterfaceStats.if_uc_pkts', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='if_mc_pkts', full_name='InterfaceStats.if_mc_pkts', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='if_bc_pkts', full_name='InterfaceStats.if_bc_pkts', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='if_error', full_name='InterfaceStats.if_error', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='if_pause_pkts', full_name='InterfaceStats.if_pause_pkts', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='if_unknown_proto_pkts', full_name='InterfaceStats.if_unknown_proto_pkts', index=9,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1014,
  serialized_end=1314,
)


_INGRESSINTERFACEERRORS = _descriptor.Descriptor(
  name='IngressInterfaceErrors',
  full_name='IngressInterfaceErrors',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='if_errors', full_name='IngressInterfaceErrors.if_errors', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='if_in_qdrops', full_name='IngressInterfaceErrors.if_in_qdrops', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='if_in_frame_errors', full_name='IngressInterfaceErrors.if_in_frame_errors', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='if_discards', full_name='IngressInterfaceErrors.if_discards', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='if_in_runts', full_name='IngressInterfaceErrors.if_in_runts', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='if_in_l3_incompletes', full_name='IngressInterfaceErrors.if_in_l3_incompletes', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='if_in_l2chan_errors', full_name='IngressInterfaceErrors.if_in_l2chan_errors', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='if_in_l2_mismatch_timeouts', full_name='IngressInterfaceErrors.if_in_l2_mismatch_timeouts', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='if_in_fifo_errors', full_name='IngressInterfaceErrors.if_in_fifo_errors', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='if_in_resource_errors', full_name='IngressInterfaceErrors.if_in_resource_errors', index=9,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1317,
  serialized_end=1675,
)


_EGRESSINTERFACEERRORS = _descriptor.Descriptor(
  name='EgressInterfaceErrors',
  full_name='EgressInterfaceErrors',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='if_errors', full_name='EgressInterfaceErrors.if_errors', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='if_discards', full_name='EgressInterfaceErrors.if_discards', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1677,
  serialized_end=1754,
)

_PORT.fields_by_name['interface_stats'].message_type = _INTERFACEINFOS
_INTERFACEINFOS.fields_by_name['egress_queue_info'].message_type = _QUEUESTATS
_INTERFACEINFOS.fields_by_name['ingress_queue_info'].message_type = _QUEUESTATS
_INTERFACEINFOS.fields_by_name['ingress_stats'].message_type = _INTERFACESTATS
_INTERFACEINFOS.fields_by_name['egress_stats'].message_type = _INTERFACESTATS
_INTERFACEINFOS.fields_by_name['ingress_errors'].message_type = _INGRESSINTERFACEERRORS
_INTERFACEINFOS.fields_by_name['egress_errors'].message_type = _EGRESSINTERFACEERRORS
DESCRIPTOR.message_types_by_name['Port'] = _PORT
DESCRIPTOR.message_types_by_name['InterfaceInfos'] = _INTERFACEINFOS
DESCRIPTOR.message_types_by_name['QueueStats'] = _QUEUESTATS
DESCRIPTOR.message_types_by_name['InterfaceStats'] = _INTERFACESTATS
DESCRIPTOR.message_types_by_name['IngressInterfaceErrors'] = _INGRESSINTERFACEERRORS
DESCRIPTOR.message_types_by_name['EgressInterfaceErrors'] = _EGRESSINTERFACEERRORS
DESCRIPTOR.extensions_by_name['jnpr_interface_ext'] = jnpr_interface_ext
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Port = _reflection.GeneratedProtocolMessageType('Port', (_message.Message,), {
  'DESCRIPTOR' : _PORT,
  '__module__' : 'port_pb2'
  # @@protoc_insertion_point(class_scope:Port)
  })
_sym_db.RegisterMessage(Port)

InterfaceInfos = _reflection.GeneratedProtocolMessageType('InterfaceInfos', (_message.Message,), {
  'DESCRIPTOR' : _INTERFACEINFOS,
  '__module__' : 'port_pb2'
  # @@protoc_insertion_point(class_scope:InterfaceInfos)
  })
_sym_db.RegisterMessage(InterfaceInfos)

QueueStats = _reflection.GeneratedProtocolMessageType('QueueStats', (_message.Message,), {
  'DESCRIPTOR' : _QUEUESTATS,
  '__module__' : 'port_pb2'
  # @@protoc_insertion_point(class_scope:QueueStats)
  })
_sym_db.RegisterMessage(QueueStats)

InterfaceStats = _reflection.GeneratedProtocolMessageType('InterfaceStats', (_message.Message,), {
  'DESCRIPTOR' : _INTERFACESTATS,
  '__module__' : 'port_pb2'
  # @@protoc_insertion_point(class_scope:InterfaceStats)
  })
_sym_db.RegisterMessage(InterfaceStats)

IngressInterfaceErrors = _reflection.GeneratedProtocolMessageType('IngressInterfaceErrors', (_message.Message,), {
  'DESCRIPTOR' : _INGRESSINTERFACEERRORS,
  '__module__' : 'port_pb2'
  # @@protoc_insertion_point(class_scope:IngressInterfaceErrors)
  })
_sym_db.RegisterMessage(IngressInterfaceErrors)

EgressInterfaceErrors = _reflection.GeneratedProtocolMessageType('EgressInterfaceErrors', (_message.Message,), {
  'DESCRIPTOR' : _EGRESSINTERFACEERRORS,
  '__module__' : 'port_pb2'
  # @@protoc_insertion_point(class_scope:EgressInterfaceErrors)
  })
_sym_db.RegisterMessage(EgressInterfaceErrors)

jnpr_interface_ext.message_type = _PORT
telemetry__top__pb2.JuniperNetworksSensors.RegisterExtension(jnpr_interface_ext)

_INTERFACEINFOS.fields_by_name['if_name']._options = None
_INTERFACEINFOS.fields_by_name['if_transitions']._options = None
_QUEUESTATS.fields_by_name['queue_number']._options = None
_QUEUESTATS.fields_by_name['packets']._options = None
_QUEUESTATS.fields_by_name['bytes']._options = None
_QUEUESTATS.fields_by_name['tail_drop_packets']._options = None
_QUEUESTATS.fields_by_name['rl_drop_packets']._options = None
_QUEUESTATS.fields_by_name['rl_drop_bytes']._options = None
_QUEUESTATS.fields_by_name['red_drop_packets']._options = None
_QUEUESTATS.fields_by_name['red_drop_bytes']._options = None
_QUEUESTATS.fields_by_name['avg_buffer_occupancy']._options = None
_QUEUESTATS.fields_by_name['cur_buffer_occupancy']._options = None
_QUEUESTATS.fields_by_name['peak_buffer_occupancy']._options = None
_QUEUESTATS.fields_by_name['allocated_buffer_size']._options = None
_INTERFACESTATS.fields_by_name['if_pkts']._options = None
_INTERFACESTATS.fields_by_name['if_octets']._options = None
_INTERFACESTATS.fields_by_name['if_1sec_pkts']._options = None
_INTERFACESTATS.fields_by_name['if_1sec_octets']._options = None
_INTERFACESTATS.fields_by_name['if_uc_pkts']._options = None
_INTERFACESTATS.fields_by_name['if_mc_pkts']._options = None
_INTERFACESTATS.fields_by_name['if_bc_pkts']._options = None
_INTERFACESTATS.fields_by_name['if_error']._options = None
_INTERFACESTATS.fields_by_name['if_pause_pkts']._options = None
_INTERFACESTATS.fields_by_name['if_unknown_proto_pkts']._options = None
_INGRESSINTERFACEERRORS.fields_by_name['if_errors']._options = None
_INGRESSINTERFACEERRORS.fields_by_name['if_in_qdrops']._options = None
_INGRESSINTERFACEERRORS.fields_by_name['if_in_frame_errors']._options = None
_INGRESSINTERFACEERRORS.fields_by_name['if_discards']._options = None
_INGRESSINTERFACEERRORS.fields_by_name['if_in_runts']._options = None
_INGRESSINTERFACEERRORS.fields_by_name['if_in_l3_incompletes']._options = None
_INGRESSINTERFACEERRORS.fields_by_name['if_in_l2chan_errors']._options = None
_INGRESSINTERFACEERRORS.fields_by_name['if_in_l2_mismatch_timeouts']._options = None
_INGRESSINTERFACEERRORS.fields_by_name['if_in_fifo_errors']._options = None
_INGRESSINTERFACEERRORS.fields_by_name['if_in_resource_errors']._options = None
_EGRESSINTERFACEERRORS.fields_by_name['if_errors']._options = None
_EGRESSINTERFACEERRORS.fields_by_name['if_discards']._options = None
# @@protoc_insertion_point(module_scope)
