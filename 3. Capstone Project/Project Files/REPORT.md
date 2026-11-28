# Capstone Project Report

## 1. Student Details

- Name: Sneha Joshi
- Roll number: 2501730031
- Personal number: **K = 31** (last two digits of the roll number)

## 2. Calculated Box Parameters

- Starting row: **31**
- Height: **20 rows**
- Width multiplier: K mod 4 = 31 mod 4 = 3
- Width: 16 * (3 + 1) = **64 pixels**
- Horizontal size in screen words: 64 / 16 = **4 words**
- Starting screen address: SCREEN + 32 * 31 = 16384 + 992 = **17376**

The box occupies rows 31 through 50 and four consecutive screen words in each row.

## 3. Part A: Building the Hack Computer

`CPU.hdl` implements instruction decoding, the A-register, D-register, ALU selection, memory-write control, jump decisions, and the program counter. `Memory.hdl` maps RAM16K, Screen, and Keyboard according to the Hack memory map. `Computer.hdl` connects instruction ROM, CPU, and data memory.

Official test assets are included in `tests/`: `CPU.tst`, `Memory.tst`, `ComputerAdd.tst`, `ComputerMax.tst`, `ComputerRect.tst`, and their comparison files. Run these in the Nand2Tetris Hardware Simulator by loading each corresponding HDL chip and its test script.

## 4. Part B: Assembler

`assembler.py` performs the required first pass and second pass:

1. Removes comments and blank lines.
2. Records `(LABEL)` addresses.
3. Converts A-instructions and C-instructions to 16-bit machine code.
4. Allocates new variables at RAM address 16 and upward.
5. Resolves predefined symbols and labels.

Because K mod 3 = 1, invalid input produces a clear line-numbered error instead of a Python crash. The test `tests/Invalid.asm` produces `Line 2: invalid instruction`.

The assembler output was checked for `Add.asm`, `Max.asm`, and `Rect.asm`. Their generated `.hack` files match the official reference machine code included with the course. `Pong.asm` assembled successfully to a 27,483-line `.hack` file.

## 5. Part C: Box Program

`Box.asm` reads the keyboard at address 24576 on every frame. A key press selects `-1` using the valid C-instruction `D=-1`, while key release selects `0`. The program then draws or clears 20 rows of 4 screen words. It resumes key checking after each frame.

Run `python3 assembler.py Box.asm Box.hack`, load `Computer.hdl` and `Box.hack` in the CPU Emulator, and press any key while the program executes. A 64-pixel-wide by 20-row box should appear beginning at row 31. Releasing the key should clear it.

## 6. Mistake Fixed

One implementation mistake was in the memory-mapped output selection: the screen and keyboard regions were initially not separated correctly from RAM. I corrected `Memory.hdl` by splitting the address at bit 14, routing RAM for address 14 = 0, and routing Screen or Keyboard for address 14 = 1 using address bit 13. I also corrected the box fill constant to use `D=-1`; `@-1` is not a valid Hack A-instruction and was treated as a variable. These changes prevent the display from showing a stray line instead of the filled box.

## 7. How to Run

Assembler verification is run from this folder with:

```bash
python3 assembler.py Box.asm Box.hack
python3 assembler.py tests/Add.asm tests/Add.hack
python3 assembler.py tests/Max.asm tests/Max.hack
python3 assembler.py tests/Rect.asm tests/Rect.hack
python3 assembler.py tests/Pong.asm tests/Pong.hack
```

For HDL tests, open the Hardware Simulator in the [Nand2Tetris Web IDE](https://nand2tetris.github.io/web-ide/chip/), switch **Builtin** off, open each HDL file, load its test script from `tests/`, and save the successful screen.

For the box, open the [CPU Emulator Web IDE](https://nand2tetris.github.io/web-ide/cpu/), load `Box.hack`, run it, hold a key to draw the box, and release it to erase the box.
