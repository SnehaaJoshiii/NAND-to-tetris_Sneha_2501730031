// Roll 2501730031: K = 31
// 20 rows tall, 64 pixels wide (4 screen words) at rows 31-50.

(START)
    @KBD
    D=M
    @CLEAR
    D;JEQ

    D=-1
    @fill
    M=D
    @DRAW
    0;JMP

(CLEAR)
    @0
    D=A
    @fill
    M=D

(DRAW)
    // 16384 + (32 * 31) = 17376
    @17376
    D=A
    @address
    M=D

    @20
    D=A
    @rows
    M=D

(ROW)
    @4
    D=A
    @columns
    M=D

(COLUMN)
    @fill
    D=M
    @address
    A=M
    M=D

    @address
    M=M+1
    @columns
    MD=M-1
    @COLUMN
    D;JGT

    @28
    D=A
    @address
    M=D+M

    @rows
    MD=M-1
    @ROW
    D;JGT

    @START
    0;JMP
