# Capstone Project: Make the Computer Draw a Box

**Name:** Sneha Joshi  
**Roll number:** 2501730031  
**Personal number:** K = 31

## Contents

- `CPU.hdl`, `Memory.hdl`, `Computer.hdl`: Hack computer implementation.
- `assembler.py`: two-pass Python assembler.
- `Box.asm`: key-controlled box program.
- `Box.hack`: `Box.asm` assembled by `assembler.py`.
- `tests/`: official sample programs and hardware test scripts.
- `REPORT.md`: short capstone report with computed parameters and test evidence.

## Run the assembler

```bash
python3 assembler.py Box.asm Box.hack
python3 assembler.py tests/Add.asm tests/Add.hack
python3 assembler.py tests/Max.asm tests/Max.hack
python3 assembler.py tests/Rect.asm tests/Rect.hack
python3 assembler.py tests/Pong.asm tests/Pong.hack
```

The implementation for K mod 3 = 1 reports invalid instructions in the form:

```text
Line 7: invalid instruction
```

## Run and capture the computer tests

Open the Nand2Tetris Web IDE at:

<https://nand2tetris.github.io/web-ide/chip/>

1. Use the Project 5 chip files for `CPU.hdl`, `Memory.hdl`, and `Computer.hdl`.
2. Turn **Builtin** off so the submitted chip implementations are tested.
3. Open `CPU.hdl`, `Memory.hdl`, or `Computer.hdl` in the HDL editor.
4. Load the matching test script from `tests/`:
   - `CPU.tst`
   - `Memory.tst`
   - `ComputerAdd.tst`
   - `ComputerMax.tst`
   - `ComputerRect.tst`
5. Load the matching comparison file when the web IDE requests it.
6. Run the test and take a screenshot only after the status shows successful/completed.
7. Save each screenshot in `screenshots/` using the test name.

## Run the box

Open:

<https://nand2tetris.github.io/web-ide/cpu/>

1. Load `Box.hack` using the folder/load control.
2. Run the program.
3. Hold any keyboard key. A 64-pixel-wide by 20-row box should appear at row 31.
4. Release the key. The box should disappear.
5. Save screenshots as:
   - `screenshots/Box-key-held.png`
   - `screenshots/Box-key-released.png`

The report template is `Capstone_Report.docx` or `Capstone_Report.pdf`. Replace the clearly labeled screenshot placeholders before submission.
