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
<<<<<<< HEAD
curl -O https://raw.githubusercontent.com/galaxy-cli/income/main/income.sh
chmod +x income.sh
```

Or clone the repository:

```
git clone https://github.com/galaxy-cli/income.git
cd income
chmod +x income.sh
```

---

## Usage

Run the script from your terminal:

`./income.sh`

You will be interactively prompted to select the type of calculation:

```
Calculate income? [Y/N]
Calculate rent? [Y/N]
Calculate income brackets? [Y/N]
```

### Income Calculator

Estimate income based on:

- Annual salary → Calculates hourly, weekly, monthly
- Hourly wage → Calculates weekly, monthly, yearly

### Rent Calculator

Enter:

- Rent per month
- Your monthly income
- Number of roommates

The script outputs:

- Rent share per person
- Remaining income after rent
- Rent as a percentage of income

### Income Bracket Calculator

Enter a "middle class" benchmark income. Outputs standard bracket approximation:

- Working Poor
- Working
- Lower-Middle
- Middle
- Upper-Middle
- Upper
- Wealthy

### Investment Calculation

Enter values to calculate income investments:

- Monthly income
- Amount invested

---

## Example

=== Income Calculator ===
```
Calculate yearly income? [Y/N] Y
Annual income ($): 60,000

Income Breakdown:
Per hour: $125
Per week: $1,250
Per month: $5,000
Per year: $60,000
```
---

## How It Works

All math is basic Bash arithmetic. To handle floating point division (e.g., 1.5), the script uses `bc`.

User inputs are sanitized to allow commas for input clarity:

"1,000" → "1000"
clean="${var//,/}"

---
## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Author & Contact

**galaxy-cli**

GitHub: [https://github.com/galaxy-cli/income](https://github.com/galaxy-cli/incomen)

=======
python3 income.py --all
# Prompt: Run yearly income? [y/N]: y 120k/yr
```
>>>>>>> 76971fb (Full Python rewrite)
