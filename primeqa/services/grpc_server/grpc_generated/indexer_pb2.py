# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: indexer.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import parameter_pb2 as parameter__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rindexer.proto\x12\x05index\x1a\x0fparameter.proto\x1a\x1cgoogle/protobuf/struct.proto\"G\n\x07Indexer\x12\x12\n\nindexer_id\x18\x01 \x01(\t\x12(\n\nparameters\x18\x02 \x03(\x0b\x32\x14.parameter.Parameter\"\x14\n\x12GetIndexersRequest\"7\n\x13GetIndexersResponse\x12 \n\x08indexers\x18\x01 \x03(\x0b\x32\x0e.index.Indexer\"<\n\x08\x44ocument\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x13\n\x0b\x64ocument_id\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\x98\x01\n\x14GenerateIndexRequest\x12\x1f\n\x07indexer\x18\x01 \x01(\x0b\x32\x0e.index.Indexer\x12\"\n\tdocuments\x18\x02 \x03(\x0b\x32\x0f.index.Document\x12\x10\n\x08index_id\x18\x03 \x01(\t\x12)\n\x08metadata\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\"M\n\x15GenerateIndexResponse\x12\x10\n\x08index_id\x18\x01 \x01(\t\x12\"\n\x06status\x18\x02 \x01(\x0e\x32\x12.index.IndexStatus\")\n\x15GetIndexStatusRequest\x12\x10\n\x08index_id\x18\x01 \x01(\t\"9\n\x13IndexStatusResponse\x12\"\n\x06status\x18\x01 \x01(\x0e\x32\x12.index.IndexStatus\"(\n\x11GetIndexesRequest\x12\x13\n\x0b\x65ngine_type\x18\x01 \x01(\t\"s\n\x10IndexInformation\x12\x10\n\x08index_id\x18\x01 \x01(\t\x12\"\n\x06status\x18\x02 \x01(\x0e\x32\x12.index.IndexStatus\x12)\n\x08metadata\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\">\n\x12GetIndexesResponse\x12(\n\x07indexes\x18\x01 \x03(\x0b\x32\x17.index.IndexInformation*H\n\x0bIndexStatus\x12\t\n\x05READY\x10\x00\x12\x0c\n\x08INDEXING\x10\x01\x12\x13\n\x0f\x44OES_NOT_EXISTS\x10\x02\x12\x0b\n\x07\x43ORRUPT\x10\x03\x32\xb4\x02\n\x0fIndexingService\x12\x44\n\x0bGetIndexers\x12\x19.index.GetIndexersRequest\x1a\x1a.index.GetIndexersResponse\x12L\n\rGenerateIndex\x12\x1b.index.GenerateIndexRequest\x1a\x1c.index.GenerateIndexResponse(\x01\x12J\n\x0eGetIndexStatus\x12\x1c.index.GetIndexStatusRequest\x1a\x1a.index.IndexStatusResponse\x12\x41\n\nGetIndexes\x12\x18.index.GetIndexesRequest\x1a\x19.index.GetIndexesResponseb\x06proto3')

_INDEXSTATUS = DESCRIPTOR.enum_types_by_name['IndexStatus']
IndexStatus = enum_type_wrapper.EnumTypeWrapper(_INDEXSTATUS)
READY = 0
INDEXING = 1
DOES_NOT_EXISTS = 2
CORRUPT = 3


_INDEXER = DESCRIPTOR.message_types_by_name['Indexer']
_GETINDEXERSREQUEST = DESCRIPTOR.message_types_by_name['GetIndexersRequest']
_GETINDEXERSRESPONSE = DESCRIPTOR.message_types_by_name['GetIndexersResponse']
_DOCUMENT = DESCRIPTOR.message_types_by_name['Document']
_GENERATEINDEXREQUEST = DESCRIPTOR.message_types_by_name['GenerateIndexRequest']
_GENERATEINDEXRESPONSE = DESCRIPTOR.message_types_by_name['GenerateIndexResponse']
_GETINDEXSTATUSREQUEST = DESCRIPTOR.message_types_by_name['GetIndexStatusRequest']
_INDEXSTATUSRESPONSE = DESCRIPTOR.message_types_by_name['IndexStatusResponse']
_GETINDEXESREQUEST = DESCRIPTOR.message_types_by_name['GetIndexesRequest']
_INDEXINFORMATION = DESCRIPTOR.message_types_by_name['IndexInformation']
_GETINDEXESRESPONSE = DESCRIPTOR.message_types_by_name['GetIndexesResponse']
Indexer = _reflection.GeneratedProtocolMessageType('Indexer', (_message.Message,), {
  'DESCRIPTOR' : _INDEXER,
  '__module__' : 'indexer_pb2'
  # @@protoc_insertion_point(class_scope:index.Indexer)
  })
_sym_db.RegisterMessage(Indexer)

GetIndexersRequest = _reflection.GeneratedProtocolMessageType('GetIndexersRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETINDEXERSREQUEST,
  '__module__' : 'indexer_pb2'
  # @@protoc_insertion_point(class_scope:index.GetIndexersRequest)
  })
_sym_db.RegisterMessage(GetIndexersRequest)

GetIndexersResponse = _reflection.GeneratedProtocolMessageType('GetIndexersResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETINDEXERSRESPONSE,
  '__module__' : 'indexer_pb2'
  # @@protoc_insertion_point(class_scope:index.GetIndexersResponse)
  })
_sym_db.RegisterMessage(GetIndexersResponse)

Document = _reflection.GeneratedProtocolMessageType('Document', (_message.Message,), {
  'DESCRIPTOR' : _DOCUMENT,
  '__module__' : 'indexer_pb2'
  # @@protoc_insertion_point(class_scope:index.Document)
  })
_sym_db.RegisterMessage(Document)

GenerateIndexRequest = _reflection.GeneratedProtocolMessageType('GenerateIndexRequest', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEINDEXREQUEST,
  '__module__' : 'indexer_pb2'
  # @@protoc_insertion_point(class_scope:index.GenerateIndexRequest)
  })
_sym_db.RegisterMessage(GenerateIndexRequest)

GenerateIndexResponse = _reflection.GeneratedProtocolMessageType('GenerateIndexResponse', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEINDEXRESPONSE,
  '__module__' : 'indexer_pb2'
  # @@protoc_insertion_point(class_scope:index.GenerateIndexResponse)
  })
_sym_db.RegisterMessage(GenerateIndexResponse)

GetIndexStatusRequest = _reflection.GeneratedProtocolMessageType('GetIndexStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETINDEXSTATUSREQUEST,
  '__module__' : 'indexer_pb2'
  # @@protoc_insertion_point(class_scope:index.GetIndexStatusRequest)
  })
_sym_db.RegisterMessage(GetIndexStatusRequest)

IndexStatusResponse = _reflection.GeneratedProtocolMessageType('IndexStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _INDEXSTATUSRESPONSE,
  '__module__' : 'indexer_pb2'
  # @@protoc_insertion_point(class_scope:index.IndexStatusResponse)
  })
_sym_db.RegisterMessage(IndexStatusResponse)

GetIndexesRequest = _reflection.GeneratedProtocolMessageType('GetIndexesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETINDEXESREQUEST,
  '__module__' : 'indexer_pb2'
  # @@protoc_insertion_point(class_scope:index.GetIndexesRequest)
  })
_sym_db.RegisterMessage(GetIndexesRequest)

IndexInformation = _reflection.GeneratedProtocolMessageType('IndexInformation', (_message.Message,), {
  'DESCRIPTOR' : _INDEXINFORMATION,
  '__module__' : 'indexer_pb2'
  # @@protoc_insertion_point(class_scope:index.IndexInformation)
  })
_sym_db.RegisterMessage(IndexInformation)

GetIndexesResponse = _reflection.GeneratedProtocolMessageType('GetIndexesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETINDEXESRESPONSE,
  '__module__' : 'indexer_pb2'
  # @@protoc_insertion_point(class_scope:index.GetIndexesResponse)
  })
_sym_db.RegisterMessage(GetIndexesResponse)

_INDEXINGSERVICE = DESCRIPTOR.services_by_name['IndexingService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INDEXSTATUS._serialized_start=844
  _INDEXSTATUS._serialized_end=916
  _INDEXER._serialized_start=71
  _INDEXER._serialized_end=142
  _GETINDEXERSREQUEST._serialized_start=144
  _GETINDEXERSREQUEST._serialized_end=164
  _GETINDEXERSRESPONSE._serialized_start=166
  _GETINDEXERSRESPONSE._serialized_end=221
  _DOCUMENT._serialized_start=223
  _DOCUMENT._serialized_end=283
  _GENERATEINDEXREQUEST._serialized_start=286
  _GENERATEINDEXREQUEST._serialized_end=438
  _GENERATEINDEXRESPONSE._serialized_start=440
  _GENERATEINDEXRESPONSE._serialized_end=517
  _GETINDEXSTATUSREQUEST._serialized_start=519
  _GETINDEXSTATUSREQUEST._serialized_end=560
  _INDEXSTATUSRESPONSE._serialized_start=562
  _INDEXSTATUSRESPONSE._serialized_end=619
  _GETINDEXESREQUEST._serialized_start=621
  _GETINDEXESREQUEST._serialized_end=661
  _INDEXINFORMATION._serialized_start=663
  _INDEXINFORMATION._serialized_end=778
  _GETINDEXESRESPONSE._serialized_start=780
  _GETINDEXESRESPONSE._serialized_end=842
  _INDEXINGSERVICE._serialized_start=919
  _INDEXINGSERVICE._serialized_end=1227
# @@protoc_insertion_point(module_scope)
