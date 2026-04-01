lorom

; SMW U uses LDA.B #$04 at $009E26 when initializing a new save.
; Replace it with 9 starting lives for a visible but low-risk gameplay test.
org $009E26
  db $A9, $09

org $00FFC0
  db "SMW START 09 LIVES  "
