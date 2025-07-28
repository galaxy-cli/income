# income · Personal Finance CLI Tool

**income** is a simple, interactive Bash script designed for quick personal finance calculations right from your terminal. Use it to estimate your income across timeframes, calculate rent affordability, and determine your income class — all without leaving the command line.

- Estimate income: hourly, weekly, monthly, yearly  
- Analyze rent affordability with or without roommates  
- Determine your income class bracket  

---

## Features

- Convert between hourly, weekly, monthly, and yearly income
- Check if your rent is reasonable based on your income
- Determine your income bracket (e.g., working class, wealthy)
- Validates user input for a clean, error-free experience

---

## Installation

Simply download the script and make it executable:

```
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

- Working class
- Lower middle class
- Middle class
- Upper middle class
- Upper class
- Wealthy

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

