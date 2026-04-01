lorom

; SMW U uses LDA.B #$04 at $009E24 when initializing a new save.
; Replace it with the internal value for a visible 9 starting lives gameplay test.
org $009E24
  db $A9, $08

org $00FFC0
  db "SMW START 09 LIVES  "
