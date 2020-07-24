meta:
  id: dmhashfile
  file-extension: hf
  endian: le
seq:
  - id: header
    type: header
  - id: files
    type: fileinfo
    repeat: expr
    repeat-expr: header.count
types:
  header:
    seq:
      - id: magic
        contents: [0x10, 0x00, 0x00, 0x00]
      - id: count
        type: u4
  fileinfo:
    seq:
      - id: magic
        contents: [0x01, 0x00, 0x00, 0x00]
      - id: size
        type: u4
      - id: size2
        type: u4
      - id: filename_hash
        type: u4
      - id: offset
        type: u8