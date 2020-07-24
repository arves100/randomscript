meta:
  id: attratr
  file-extension: attr.atr
  endian: le
seq:
  - id: header
    type: header
  - id: data
    type: u1
    repeat: expr
    repeat-expr: header.width * header.height
    enum: collisiontype
    doc: |
      While I calculate this as enumerator to make kaitai happy, they are
      actually bit-wise operations:
      Bit 0: None (You can't walk to it)
      Bit 1: Walkable
      Bit 2: Water (There's water on it)
      Bit 8: You can build a guild on that zone
types:
  header:
    seq:
      - id: magic
        contents: [0x4a, 0x0a]
      - id: width
        type: u2
      - id: height
        type: u2
enums:
  collisiontype:
    0: none
    1: walk
    2: water
    3: walk_water
    4: no_pvp
    5: no_pvp_walk
    6: no_pvp_water
    7: no_pvp_walk_water
    8: guild_build
    9: guild_build_walk
    10: guild_build_water
    11: guild_build_walk_water
    12: guild_build_no_pvp
    13: guild_build_no_pvp_walk
    14: guild_build_no_pvp_water
    15: guild_build_no_pvp_walk_water
