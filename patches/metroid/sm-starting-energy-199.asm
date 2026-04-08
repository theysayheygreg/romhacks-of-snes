lorom

; Vanilla Super Metroid new-file state initializes current and max health here:
;   81:B2CD  LDA #$0063
;   81:B2D0  STA $09C4
;   81:B2D3  STA $09C2
; Change 99 starting energy to 199 for a visible low-risk gameplay artifact.

org $81B2CD
  lda #$00C7
