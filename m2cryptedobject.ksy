meta:
  id: m2cryptedobject
  endian: le
seq:
  - id: header
    type: header
  - id: magic_verification
    type: u4
    if: header.crypted_size == 0
    enum: cryptedmagic
  - id: crypted_magic_verification
    type: u4
    if: header.crypted_size != 0
  - id: crypted_content
    size: header.crypted_size
    if: header.crypted_size > 0
  - id: compressed_content
    size: header.compressed_size
    if: header.crypted_size == 0
types:
  header:
    seq:
      - id: magic
        type: u4
        enum: cryptedmagic
      - id: crypted_size
        type: u4
      - id: compressed_size
        type: u4
      - id: real_size
        type: u4
enums:
  cryptedmagic:
    1347633997: mcsp
    1515144013: mcoz