# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: accumulo/contrib/komorebidb/resources/komorebi.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='accumulo/contrib/komorebidb/resources/komorebi.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n4accumulo/contrib/komorebidb/resources/komorebi.proto\">\n\x03Key\x12\x0b\n\x03row\x18\x01 \x01(\x0c\x12\n\n\x02\x63\x66\x18\x02 \x01(\x0c\x12\n\n\x02\x63q\x18\x03 \x01(\x0c\x12\x12\n\nvisibility\x18\x04 \x01(\x0c\"\x1c\n\x06KeySet\x12\x12\n\x04keys\x18\x01 \x03(\x0b\x32\x04.Keyb\x06proto3'
)




_KEY = _descriptor.Descriptor(
  name='Key',
  full_name='Key',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row', full_name='Key.row', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cf', full_name='Key.cf', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cq', full_name='Key.cq', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='visibility', full_name='Key.visibility', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=118,
)


_KEYSET = _descriptor.Descriptor(
  name='KeySet',
  full_name='KeySet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keys', full_name='KeySet.keys', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=148,
)

_KEYSET.fields_by_name['keys'].message_type = _KEY
DESCRIPTOR.message_types_by_name['Key'] = _KEY
DESCRIPTOR.message_types_by_name['KeySet'] = _KEYSET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Key = _reflection.GeneratedProtocolMessageType('Key', (_message.Message,), {
  'DESCRIPTOR' : _KEY,
  '__module__' : 'accumulo.contrib.komorebidb.resources.komorebi_pb2'
  # @@protoc_insertion_point(class_scope:Key)
  })
_sym_db.RegisterMessage(Key)

KeySet = _reflection.GeneratedProtocolMessageType('KeySet', (_message.Message,), {
  'DESCRIPTOR' : _KEYSET,
  '__module__' : 'accumulo.contrib.komorebidb.resources.komorebi_pb2'
  # @@protoc_insertion_point(class_scope:KeySet)
  })
_sym_db.RegisterMessage(KeySet)


# @@protoc_insertion_point(module_scope)
