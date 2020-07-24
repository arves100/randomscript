meta:
  id: eterpackindex
  file-extension: eix
  endian: le
seq:
  - id: header
    type: header
  - id: files
    type: file_content
    repeat: expr
    repeat-expr: header.files
  - id: padding
    size-eos: true
types:
  header:
    seq:
      - id: magic
        contents: 'EPKD'
      - id: version
        contents: 
          - 0x02
          - 0x00
          - 0x00
          - 0x00
      - id: files
        type: u4
  file_content:
    seq:
      - id: id
        type: u4
      - id: name
        type: strz
        encoding: ks_c_5601-1987
        size: 161
      - id: padding
        size: 3
      - id: crc32_file_name
        type: u4
      - id: real_size
        type: u4
      - id: stored_size
        type: u4
      - id: crc32
        type: u4
      - id: stored_offset
        type: u4
      - id: compression_type
        type: u1
        enum: compression
      - id: padding_2
        size: 3
enums:
  compression:
    0: none
    1: lzo
    2: mcoz
    3: panama
    4: hybridcrypt
    5: hybridcrypt_unknown
    6: mcsp
