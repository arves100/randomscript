meta:
  id: item_proto
  file-extension: item_proto
  endian: le
  imports:
    - m2cryptedobject
seq:
  - id: header
    type: header
  - id: cryptedobject
    type: m2cryptedobject
    size: header.cryptedobject_size
    if: header.cryptedobject_size > 0
  - id: content
    if: header.cryptedobject_size == 0
    size-eos: true
types:
  header:
    seq:
      - id: magic
        type: u4
        enum: magictypes
      - id: version
        contents: [01,00,00,00]
        if: magic == magictypes::mipx
      - id: stride
        type: u4
        if: magic == magictypes::mipx
      - id: elements
        type: u4
      - id: cryptedobject_size
        type: u4
enums:
  magictypes:
    1481656653: mipx
    1414547789: mipt