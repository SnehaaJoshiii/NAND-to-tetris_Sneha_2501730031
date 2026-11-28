# Screenshot Guide

The `screenshots/` folder contains only images included in `Capstone_Report.pdf`.
Placeholder images and failed test captures have been removed.

## 1. Hardware Simulator

Open <https://nand2tetris.github.io/web-ide/chip/>.

For each test:

1. Select Project 5.
2. Turn **Builtin** off.
3. Open the matching HDL file.
4. Open the Test Script tab and load the `.tst` file.
5. Load the `.cmp` file if required.
6. Run the test.
7. Capture the whole browser window after the test finishes successfully.

Included in the report:

- `screenshots/CPU-tst-passed.png`
- `screenshots/ComputerAdd-tst-passed.png`
- `screenshots/ComputerMax-tst-passed.png`
- `screenshots/ComputerRect-tst-passed.png`

The Memory test screenshot is still pending.

## 2. Assembler

Run this in Terminal from `Project Files`:

```bash
python3 assembler.py Box.asm Box.hack
python3 assembler.py tests/Add.asm tests/Add.hack
python3 assembler.py tests/Max.asm tests/Max.hack
python3 assembler.py tests/Rect.asm tests/Rect.hack
python3 assembler.py tests/Pong.asm tests/Pong.hack
```

Included in the report: `screenshots/Assembler-verification.png`.

For the invalid test:

```bash
python3 assembler.py tests/Invalid.asm /tmp/invalid.hack
```

The expected output is:

```text
Line 2: invalid instruction
```

## 3. CPU Emulator

Open <https://nand2tetris.github.io/web-ide/cpu/>.

1. Load `Box.hack`.
2. Run the program.
3. Hold a key.
4. The captured key-held screenshot is `screenshots/Box-key-held.png`.
5. Release the key.
6. The captured cleared-screen screenshot is `screenshots/Box-key-released.png`.
