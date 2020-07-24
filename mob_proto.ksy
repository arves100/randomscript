meta:
  id: mob_proto
  file-extension: mob_proto
  endian: le
  imports:
    - m2cryptedobject
seq:
  - id: header
    type: header
  - id: crypted_object
    type: m2cryptedobject
    if: header.cryptedobject_size > 0
    size: header.cryptedobject_size
  - id: content
    if: header.cryptedobject_size == 0
    size-eos: true
types:
  header:
    seq:
      - id: magic
        contents: 'MMPT'
      - id: elements
        type: u4
      - id: cryptedobject_size
        type: u4