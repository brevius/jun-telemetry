# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: optics.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import telemetry_top_pb2 as telemetry__top__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='optics.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0coptics.proto\x1a\x13telemetry_top.proto\"+\n\x06Optics\x12!\n\x0bOptics_diag\x18\x01 \x03(\x0b\x32\x0c.OpticsInfos\"i\n\x0bOpticsInfos\x12\x16\n\x07if_name\x18\x01 \x02(\tB\x05\x82@\x02\x08\x01\x12\x15\n\rsnmp_if_index\x18\x02 \x01(\r\x12+\n\x11optics_diag_stats\x18\x03 \x01(\x0b\x32\x10.OpticsDiagStats\"\xf6\x08\n\x0fOpticsDiagStats\x12\x13\n\x0boptics_type\x18\x01 \x01(\r\x12\x1a\n\x0bmodule_temp\x18\x02 \x01(\x01\x42\x05\x82@\x02 \x01\x12/\n module_temp_high_alarm_threshold\x18\x03 \x01(\x01\x42\x05\x82@\x02 \x01\x12.\n\x1fmodule_temp_low_alarm_threshold\x18\x04 \x01(\x01\x42\x05\x82@\x02 \x01\x12\x31\n\"module_temp_high_warning_threshold\x18\x05 \x01(\x01\x42\x05\x82@\x02 \x01\x12\x30\n!module_temp_low_warning_threshold\x18\x06 \x01(\x01\x42\x05\x82@\x02 \x01\x12:\n+laser_output_power_high_alarm_threshold_dbm\x18\x07 \x01(\x01\x42\x05\x82@\x02 \x01\x12\x39\n*laser_output_power_low_alarm_threshold_dbm\x18\x08 \x01(\x01\x42\x05\x82@\x02 \x01\x12<\n-laser_output_power_high_warning_threshold_dbm\x18\t \x01(\x01\x42\x05\x82@\x02 \x01\x12;\n,laser_output_power_low_warning_threshold_dbm\x18\n \x01(\x01\x42\x05\x82@\x02 \x01\x12\x36\n\'laser_rx_power_high_alarm_threshold_dbm\x18\x0b \x01(\x01\x42\x05\x82@\x02 \x01\x12\x35\n&laser_rx_power_low_alarm_threshold_dbm\x18\x0c \x01(\x01\x42\x05\x82@\x02 \x01\x12\x38\n)laser_rx_power_high_warning_threshold_dbm\x18\r \x01(\x01\x42\x05\x82@\x02 \x01\x12\x37\n(laser_rx_power_low_warning_threshold_dbm\x18\x0e \x01(\x01\x42\x05\x82@\x02 \x01\x12\x36\n\'laser_bias_current_high_alarm_threshold\x18\x0f \x01(\x01\x42\x05\x82@\x02 \x01\x12\x35\n&laser_bias_current_low_alarm_threshold\x18\x10 \x01(\x01\x42\x05\x82@\x02 \x01\x12\x38\n)laser_bias_current_high_warning_threshold\x18\x11 \x01(\x01\x42\x05\x82@\x02 \x01\x12\x37\n(laser_bias_current_low_warning_threshold\x18\x12 \x01(\x01\x42\x05\x82@\x02 \x01\x12\x1e\n\x16module_temp_high_alarm\x18\x13 \x01(\x08\x12\x1d\n\x15module_temp_low_alarm\x18\x14 \x01(\x08\x12 \n\x18module_temp_high_warning\x18\x15 \x01(\x08\x12\x1f\n\x17module_temp_low_warning\x18\x16 \x01(\x08\x12\x34\n\x16optics_lane_diag_stats\x18\x17 \x03(\x0b\x32\x14.OpticsDiagLaneStats\"\xe3\x06\n\x13OpticsDiagLaneStats\x12\x1a\n\x0blane_number\x18\x01 \x01(\rB\x05\x82@\x02\x08\x01\x12%\n\x16lane_laser_temperature\x18\x02 \x01(\x01\x42\x05\x82@\x02 \x01\x12*\n\x1blane_laser_output_power_dbm\x18\x03 \x01(\x02\x42\x05\x82@\x02 \x01\x12,\n\x1dlane_laser_receiver_power_dbm\x18\x04 \x01(\x02\x42\x05\x82@\x02 \x01\x12\x1f\n\x17lane_laser_bias_current\x18\x05 \x01(\x01\x12*\n\"lane_laser_output_power_high_alarm\x18\x06 \x01(\x08\x12)\n!lane_laser_output_power_low_alarm\x18\x07 \x01(\x08\x12,\n$lane_laser_output_power_high_warning\x18\x08 \x01(\x08\x12+\n#lane_laser_output_power_low_warning\x18\t \x01(\x08\x12,\n$lane_laser_receiver_power_high_alarm\x18\n \x01(\x08\x12+\n#lane_laser_receiver_power_low_alarm\x18\x0b \x01(\x08\x12.\n&lane_laser_receiver_power_high_warning\x18\x0c \x01(\x08\x12-\n%lane_laser_receiver_power_low_warning\x18\r \x01(\x08\x12*\n\"lane_laser_bias_current_high_alarm\x18\x0e \x01(\x08\x12)\n!lane_laser_bias_current_low_alarm\x18\x0f \x01(\x08\x12,\n$lane_laser_bias_current_high_warning\x18\x10 \x01(\x08\x12+\n#lane_laser_bias_current_low_warning\x18\x11 \x01(\x08\x12$\n\x1clane_tx_loss_of_signal_alarm\x18\x12 \x01(\x08\x12$\n\x1clane_rx_loss_of_signal_alarm\x18\x13 \x01(\x08\x12$\n\x1clane_tx_laser_disabled_alarm\x18\x14 \x01(\x08:9\n\x0fjnpr_optics_ext\x12\x17.JuniperNetworksSensors\x18\n \x01(\x0b\x32\x07.Optics'
  ,
  dependencies=[telemetry__top__pb2.DESCRIPTOR,])


JNPR_OPTICS_EXT_FIELD_NUMBER = 10
jnpr_optics_ext = _descriptor.FieldDescriptor(
  name='jnpr_optics_ext', full_name='jnpr_optics_ext', index=0,
  number=10, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)


_OPTICS = _descriptor.Descriptor(
  name='Optics',
  full_name='Optics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Optics_diag', full_name='Optics.Optics_diag', index=0,
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
  serialized_start=37,
  serialized_end=80,
)


_OPTICSINFOS = _descriptor.Descriptor(
  name='OpticsInfos',
  full_name='OpticsInfos',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='if_name', full_name='OpticsInfos.if_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\010\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='snmp_if_index', full_name='OpticsInfos.snmp_if_index', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='optics_diag_stats', full_name='OpticsInfos.optics_diag_stats', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=82,
  serialized_end=187,
)


_OPTICSDIAGSTATS = _descriptor.Descriptor(
  name='OpticsDiagStats',
  full_name='OpticsDiagStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='optics_type', full_name='OpticsDiagStats.optics_type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='module_temp', full_name='OpticsDiagStats.module_temp', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002 \001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='module_temp_high_alarm_threshold', full_name='OpticsDiagStats.module_temp_high_alarm_threshold', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002 \001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='module_temp_low_alarm_threshold', full_name='OpticsDiagStats.module_temp_low_alarm_threshold', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002 \001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='module_temp_high_warning_threshold', full_name='OpticsDiagStats.module_temp_high_warning_threshold', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002 \001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='module_temp_low_warning_threshold', full_name='OpticsDiagStats.module_temp_low_warning_threshold', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002 \001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='laser_output_power_high_alarm_threshold_dbm', full_name='OpticsDiagStats.laser_output_power_high_alarm_threshold_dbm', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002 \001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='laser_output_power_low_alarm_threshold_dbm', full_name='OpticsDiagStats.laser_output_power_low_alarm_threshold_dbm', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002 \001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='laser_output_power_high_warning_threshold_dbm', full_name='OpticsDiagStats.laser_output_power_high_warning_threshold_dbm', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002 \001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='laser_output_power_low_warning_threshold_dbm', full_name='OpticsDiagStats.laser_output_power_low_warning_threshold_dbm', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002 \001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='laser_rx_power_high_alarm_threshold_dbm', full_name='OpticsDiagStats.laser_rx_power_high_alarm_threshold_dbm', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002 \001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='laser_rx_power_low_alarm_threshold_dbm', full_name='OpticsDiagStats.laser_rx_power_low_alarm_threshold_dbm', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002 \001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='laser_rx_power_high_warning_threshold_dbm', full_name='OpticsDiagStats.laser_rx_power_high_warning_threshold_dbm', index=12,
      number=13, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002 \001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='laser_rx_power_low_warning_threshold_dbm', full_name='OpticsDiagStats.laser_rx_power_low_warning_threshold_dbm', index=13,
      number=14, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002 \001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='laser_bias_current_high_alarm_threshold', full_name='OpticsDiagStats.laser_bias_current_high_alarm_threshold', index=14,
      number=15, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002 \001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='laser_bias_current_low_alarm_threshold', full_name='OpticsDiagStats.laser_bias_current_low_alarm_threshold', index=15,
      number=16, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002 \001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='laser_bias_current_high_warning_threshold', full_name='OpticsDiagStats.laser_bias_current_high_warning_threshold', index=16,
      number=17, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002 \001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='laser_bias_current_low_warning_threshold', full_name='OpticsDiagStats.laser_bias_current_low_warning_threshold', index=17,
      number=18, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002 \001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='module_temp_high_alarm', full_name='OpticsDiagStats.module_temp_high_alarm', index=18,
      number=19, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='module_temp_low_alarm', full_name='OpticsDiagStats.module_temp_low_alarm', index=19,
      number=20, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='module_temp_high_warning', full_name='OpticsDiagStats.module_temp_high_warning', index=20,
      number=21, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='module_temp_low_warning', full_name='OpticsDiagStats.module_temp_low_warning', index=21,
      number=22, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='optics_lane_diag_stats', full_name='OpticsDiagStats.optics_lane_diag_stats', index=22,
      number=23, type=11, cpp_type=10, label=3,
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
  serialized_start=190,
  serialized_end=1332,
)


_OPTICSDIAGLANESTATS = _descriptor.Descriptor(
  name='OpticsDiagLaneStats',
  full_name='OpticsDiagLaneStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='lane_number', full_name='OpticsDiagLaneStats.lane_number', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002\010\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lane_laser_temperature', full_name='OpticsDiagLaneStats.lane_laser_temperature', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002 \001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lane_laser_output_power_dbm', full_name='OpticsDiagLaneStats.lane_laser_output_power_dbm', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002 \001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lane_laser_receiver_power_dbm', full_name='OpticsDiagLaneStats.lane_laser_receiver_power_dbm', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202@\002 \001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lane_laser_bias_current', full_name='OpticsDiagLaneStats.lane_laser_bias_current', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lane_laser_output_power_high_alarm', full_name='OpticsDiagLaneStats.lane_laser_output_power_high_alarm', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lane_laser_output_power_low_alarm', full_name='OpticsDiagLaneStats.lane_laser_output_power_low_alarm', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lane_laser_output_power_high_warning', full_name='OpticsDiagLaneStats.lane_laser_output_power_high_warning', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lane_laser_output_power_low_warning', full_name='OpticsDiagLaneStats.lane_laser_output_power_low_warning', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lane_laser_receiver_power_high_alarm', full_name='OpticsDiagLaneStats.lane_laser_receiver_power_high_alarm', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lane_laser_receiver_power_low_alarm', full_name='OpticsDiagLaneStats.lane_laser_receiver_power_low_alarm', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lane_laser_receiver_power_high_warning', full_name='OpticsDiagLaneStats.lane_laser_receiver_power_high_warning', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lane_laser_receiver_power_low_warning', full_name='OpticsDiagLaneStats.lane_laser_receiver_power_low_warning', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lane_laser_bias_current_high_alarm', full_name='OpticsDiagLaneStats.lane_laser_bias_current_high_alarm', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lane_laser_bias_current_low_alarm', full_name='OpticsDiagLaneStats.lane_laser_bias_current_low_alarm', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lane_laser_bias_current_high_warning', full_name='OpticsDiagLaneStats.lane_laser_bias_current_high_warning', index=15,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lane_laser_bias_current_low_warning', full_name='OpticsDiagLaneStats.lane_laser_bias_current_low_warning', index=16,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lane_tx_loss_of_signal_alarm', full_name='OpticsDiagLaneStats.lane_tx_loss_of_signal_alarm', index=17,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lane_rx_loss_of_signal_alarm', full_name='OpticsDiagLaneStats.lane_rx_loss_of_signal_alarm', index=18,
      number=19, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lane_tx_laser_disabled_alarm', full_name='OpticsDiagLaneStats.lane_tx_laser_disabled_alarm', index=19,
      number=20, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1335,
  serialized_end=2202,
)

_OPTICS.fields_by_name['Optics_diag'].message_type = _OPTICSINFOS
_OPTICSINFOS.fields_by_name['optics_diag_stats'].message_type = _OPTICSDIAGSTATS
_OPTICSDIAGSTATS.fields_by_name['optics_lane_diag_stats'].message_type = _OPTICSDIAGLANESTATS
DESCRIPTOR.message_types_by_name['Optics'] = _OPTICS
DESCRIPTOR.message_types_by_name['OpticsInfos'] = _OPTICSINFOS
DESCRIPTOR.message_types_by_name['OpticsDiagStats'] = _OPTICSDIAGSTATS
DESCRIPTOR.message_types_by_name['OpticsDiagLaneStats'] = _OPTICSDIAGLANESTATS
DESCRIPTOR.extensions_by_name['jnpr_optics_ext'] = jnpr_optics_ext
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Optics = _reflection.GeneratedProtocolMessageType('Optics', (_message.Message,), {
  'DESCRIPTOR' : _OPTICS,
  '__module__' : 'optics_pb2'
  # @@protoc_insertion_point(class_scope:Optics)
  })
_sym_db.RegisterMessage(Optics)

OpticsInfos = _reflection.GeneratedProtocolMessageType('OpticsInfos', (_message.Message,), {
  'DESCRIPTOR' : _OPTICSINFOS,
  '__module__' : 'optics_pb2'
  # @@protoc_insertion_point(class_scope:OpticsInfos)
  })
_sym_db.RegisterMessage(OpticsInfos)

OpticsDiagStats = _reflection.GeneratedProtocolMessageType('OpticsDiagStats', (_message.Message,), {
  'DESCRIPTOR' : _OPTICSDIAGSTATS,
  '__module__' : 'optics_pb2'
  # @@protoc_insertion_point(class_scope:OpticsDiagStats)
  })
_sym_db.RegisterMessage(OpticsDiagStats)

OpticsDiagLaneStats = _reflection.GeneratedProtocolMessageType('OpticsDiagLaneStats', (_message.Message,), {
  'DESCRIPTOR' : _OPTICSDIAGLANESTATS,
  '__module__' : 'optics_pb2'
  # @@protoc_insertion_point(class_scope:OpticsDiagLaneStats)
  })
_sym_db.RegisterMessage(OpticsDiagLaneStats)

jnpr_optics_ext.message_type = _OPTICS
telemetry__top__pb2.JuniperNetworksSensors.RegisterExtension(jnpr_optics_ext)

_OPTICSINFOS.fields_by_name['if_name']._options = None
_OPTICSDIAGSTATS.fields_by_name['module_temp']._options = None
_OPTICSDIAGSTATS.fields_by_name['module_temp_high_alarm_threshold']._options = None
_OPTICSDIAGSTATS.fields_by_name['module_temp_low_alarm_threshold']._options = None
_OPTICSDIAGSTATS.fields_by_name['module_temp_high_warning_threshold']._options = None
_OPTICSDIAGSTATS.fields_by_name['module_temp_low_warning_threshold']._options = None
_OPTICSDIAGSTATS.fields_by_name['laser_output_power_high_alarm_threshold_dbm']._options = None
_OPTICSDIAGSTATS.fields_by_name['laser_output_power_low_alarm_threshold_dbm']._options = None
_OPTICSDIAGSTATS.fields_by_name['laser_output_power_high_warning_threshold_dbm']._options = None
_OPTICSDIAGSTATS.fields_by_name['laser_output_power_low_warning_threshold_dbm']._options = None
_OPTICSDIAGSTATS.fields_by_name['laser_rx_power_high_alarm_threshold_dbm']._options = None
_OPTICSDIAGSTATS.fields_by_name['laser_rx_power_low_alarm_threshold_dbm']._options = None
_OPTICSDIAGSTATS.fields_by_name['laser_rx_power_high_warning_threshold_dbm']._options = None
_OPTICSDIAGSTATS.fields_by_name['laser_rx_power_low_warning_threshold_dbm']._options = None
_OPTICSDIAGSTATS.fields_by_name['laser_bias_current_high_alarm_threshold']._options = None
_OPTICSDIAGSTATS.fields_by_name['laser_bias_current_low_alarm_threshold']._options = None
_OPTICSDIAGSTATS.fields_by_name['laser_bias_current_high_warning_threshold']._options = None
_OPTICSDIAGSTATS.fields_by_name['laser_bias_current_low_warning_threshold']._options = None
_OPTICSDIAGLANESTATS.fields_by_name['lane_number']._options = None
_OPTICSDIAGLANESTATS.fields_by_name['lane_laser_temperature']._options = None
_OPTICSDIAGLANESTATS.fields_by_name['lane_laser_output_power_dbm']._options = None
_OPTICSDIAGLANESTATS.fields_by_name['lane_laser_receiver_power_dbm']._options = None
# @@protoc_insertion_point(module_scope)
