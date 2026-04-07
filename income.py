import argparse
import sys
import re

# --- Utilities ---

def title(name):
    print(f"=== Calculate {name} ===")

def fmt(num, force_int=False):
    if force_int:
        return f"{round(num):,}"
    return f"{num:,.2f}".rstrip('0').rstrip('.') if num % 1 != 0 else f"{num:,.0f}"

def parse_smart_value(user_input):
    if not user_input: return None, None
    user_input = str(user_input).strip().lower()
    unit = 'mo' if 'mo' in user_input else 'yr' if 'yr' in user_input else None
    multiplier = 1000 if 'k' in user_input else 1
    clean_num_str = re.sub(r'[^\d.]', '', user_input.replace(',', ''))
    try:
        val = float(clean_num_str) * multiplier
        return val, unit
    except ValueError:
        return None, unit

def get_input(prompt, unit_label, allow_zero=False, is_pct=False, provided_val=None):
    if provided_val is not None:
        val, _ = parse_smart_value(str(provided_val))
        if val is not None: return val

    while True:
        user_input = input(f"{prompt} ({unit_label}) [? for help]: ").strip().lower()
        if user_input == '?':
            print(f"--- HELP: Enter a number. You can use 'k'. Units: {unit_label}")
            continue
        val, _ = parse_smart_value(user_input)
        if val is None:
            print("[!] Invalid input.")
            continue
        if not allow_zero and val <= 0:
            print("[!] Must be positive.")
            continue
        if is_pct and not (0 <= val <= 100):
            print("[!] Percent must be 0-100.")
            continue
        return val

def get_any_income(prompt, provided_val=None):
    if provided_val is not None:
        val, unit = parse_smart_value(str(provided_val))
        if val is not None and unit:
            return (val, val * 12) if unit == 'mo' else (val / 12, val)

    while True:
        user_input = input(f"{prompt} [? for help]: ").strip()
        if user_input == '?':
            print("--- HELP: Enter amount + /mo or /yr (e.g. 5k/mo or 100k/yr).")
            continue
        val, unit = parse_smart_value(user_input)
        if val is None:
            print("[!] Enter a valid amount.")
            continue
        while not unit:
            choice = input(f"[!] You entered {fmt(val)}. Is this [/mo] or [/yr]? ").strip().lower()
            if choice in ['1', 'mo', '/mo']: unit = 'mo'
            elif choice in ['2', 'yr', '/yr']: unit = 'yr'
        return (val, val * 12) if unit == 'mo' else (val / 12, val)

def print_result_table(rows, header=("Item", "Amount", "% of Total"), hour_mode=False):
    h1, h2, h3 = header
    print(f"\n{h1:<20} {h2:<12} {h3}")
    print("-" * 55)
    for label, val, pct in rows:
        if isinstance(pct, (int, float)):
            pct_str = f"{pct:>9.1f}%"
        elif pct is not None:
            pct_str = f"{pct:>10}"
        else:
            pct_str = ""
        is_hour = hour_mode and label == "Hour"
        val_str = f"${fmt(val, force_int=not is_hour):>10}" if isinstance(val, (int, float)) else f"{val:>11}"
        print(f"{label:<20} {val_str}  {pct_str}")

# --- Logic Modules ---

def calc_yearly(args=None):
    title("Year Income")
    _, y = get_any_income("Annual Income", args[0] if args else None)
    rows = [("Hour", y/52/40, None), ("Week", y/52, None), ("Month", y/12, None), ("Year", y, None)]
    print_result_table(rows, header=("Period", "Amount", ""), hour_mode=True)

def calc_monthly(args=None):
    title("Month Income")
    h = get_input("Wage", "hr", provided_val=args[0] if (args and len(args)>0) else None)
    w_hrs = get_input("Hours/wk", "wk", provided_val=args[1] if (args and len(args)>1) else None)
    w = h * w_hrs
    rows = [("Hour", h, None), ("Week", w, None), ("Month", (w*52)/12, None), ("Year", w*52, None)]
    print_result_table(rows, header=("Period", "Amount", ""), hour_mode=True)

def calc_rent(args=None):
    title("Rent")
    rent = get_input("Total Rent", "mo", provided_val=args[0] if (args and len(args)>0) else None)
    inc = get_input("Monthly Income", "mo", provided_val=args[1] if (args and len(args)>1) else None)
    roomies = int(get_input("Roommates", "ppl", True, provided_val=args[2] if (args and len(args)>2) else None))
    split = rent / (roomies + 1)
    rows = [
        ("Monthly Income", inc, 100.0),
        (f"Rent ({'Solo' if roomies==0 else 'Split'})", split, (split/inc)*100),
        ("Discretionary", inc - split, (1 - split/inc)*100)
    ]
    print_result_table(rows)

def calc_brackets(args=None):
    title("Class Bracket")
    _, mid = get_any_income("Middle class baseline", args[0] if args else None)
    scales = [
        ("Poor", 0.33), ("Working", 0.50), ("Lower Middle", 0.66),
        ("Middle", 1.00), ("Upper Middle", 1.50), ("Upper", 2.00), ("Wealthy", 3.00)
    ]
    rows = [(label, mid * mult, f"{mult:.2f}x") for label, mult in scales]
    print_result_table(rows, header=("Bracket", "Annual", "Mult"))

def calc_invest(args=None):
    title("Investment")
    mo_inc, _ = get_any_income("Gross Income", args[0] if (args and len(args)>0) else None)
    net_p = get_input("Net Pay", "%", is_pct=True, provided_val=args[1] if (args and len(args)>1) else None)
    net_mo = mo_inc * (net_p / 100)
    inv_p = get_input("Invested", "%", is_pct=True, provided_val=args[2] if (args and len(args)>2) else None)
    sav_p = get_input("Savings", "%", True, True, provided_val=args[3] if (args and len(args)>3) else None)
    if (inv_p + sav_p) > 100: sav_p = 100 - inv_p
    rows = [
        ("Net Pay", net_mo, net_p),
        ("  Invested", net_mo * (inv_p/100), inv_p),
        ("  Savings", net_mo * (sav_p/100), sav_p),
        ("  Fun Money", net_mo * ((100-inv_p-sav_p)/100), 100.0-inv_p-sav_p)
    ]
    print_result_table(rows)

# --- CLI Setup ---

def main():
    actions = {
        "yearly_income": calc_yearly,
        "monthly_income": calc_monthly,
        "monthly_rent": calc_rent,
        "income_bracket": calc_brackets,
        "investment": calc_invest
    }

    parser = argparse.ArgumentParser(description="Income Tool")
    for flag in actions.keys():
        parser.add_argument(f"--{flag.replace('_', '-')}", nargs='*', help=f"Calculate {flag}")
    parser.add_argument("--all", action="store_true")

    args = parser.parse_args()
    
    # Corrected check for presence of any argument
    if not args.all and all(v is None for v in vars(args).values() if v is not args.all):
        parser.print_help()
        return

    try:
        if args.all:
            for name, func in actions.items():
                prompt_str = f"Run {name.replace('_', ' ')}? [y/N]: "
                user_res = input(prompt_str).strip().split()
                if user_res and user_res[0].lower() == 'y':
                    extra_args = user_res[1:] if len(user_res) > 1 else None
                    func(extra_args)
                    print("")
        else:
            for flag, func in actions.items():
                val = getattr(args, flag)
                if val is not None:
                    func(val if len(val) > 0 else None)
    except KeyboardInterrupt:
        print("\n\n[!] Operation cancelled")
        sys.exit(0)

if __name__ == "__main__":
    main()