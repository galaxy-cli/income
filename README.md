# Income Tool CLI

A robust, "smart-parsing" financial utility for calculating income breakdowns, rent splits, class brackets, and investment goals. Designed for speed with support for natural language inputs and hybrid CLI/interactive flows.

## Features

- **Smart Parsing**: Supports shorthand like `65k`, `1,200/mo`, and `85k/yr`.
- **Hybrid Input**: Provide arguments directly via command line or follow interactive prompts.
- **Contextual Rounding**: High precision for hourly wages; clean whole numbers for annual/monthly views.
- **Frictionless Interface**: Use `?` at any prompt for instant help on expected units.

## Installation

Ensure you have Python 3.6+ installed. No external dependencies are required.
`python3 income.py --help`

1. Interactive ModeRun any module without arguments to be guided through the prompts.
`python3 income.py --monthly-rent`

2. Direct CLI ModeProvide values directly to skip prompts. Supports multiple arguments in order.
````
# Calculate wage: $44/hr at 40 hrs/wk
python3 income.py --monthly-income 44 40```
# Calculate rent split: $2500 rent, $6k income, 2 roommates
python3 income.py --monthly-rent 2500 6k 2
````

3. "The All" ModeWalk through every calculation in the suite. Supports "quick-fill" by providing data alongside the 'y' confirmation.
```
python3 income.py --all
# Prompt: Run yearly income? [y/N]: y 120k/yr