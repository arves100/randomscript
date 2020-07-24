meta:
  id: waterwtr
  file-extension: water.wtr
  endian: le
seq:
  - id: header
    type: header
  - id: water_map
    type: u1
    repeat: expr
    repeat-expr: header.width * header.height
  - id: water_height
    type: u4
    repeat: expr
    repeat-expr: header.height_number
types:
  header:
    seq:
      - id: magic
        contents: [0x32, 0x15]
      - id: width
        type: u2
      - id: height
        type: u2
      - id: height_number
        type: u1