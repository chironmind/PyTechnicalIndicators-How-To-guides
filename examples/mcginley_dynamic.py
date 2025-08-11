import csv
import sys

from pytechnicalindicators import candle_indicators as ci

def load_prices_from_csv(path: str) -> list[float]:
    prices: list[float] = []
    with open(path, "r", newline="") as f:
        # Try to read as DictReader first (with a header)
        sample = f.read(4096)
        f.seek(0)
        has_header = "," in sample and any(ch.isalpha() for ch in sample.splitlines()[0])
        if has_header:
            reader = csv.DictReader(f)
            # Find a 'close' column in a case-insensitive way 
            close_key = None
            if reader.fieldnames:
                for k in reader.fieldnames:
                    if k and k.lower() == "close":
                        close_key = k 
                        break
            if close_key is None and reader.fieldnames:
                # Fallback to the first column if 'close' not found
                close_key = reader.fieldnames[0]
            for row in reader:
                try:
                    prices.append(float(row[close_key]))
                except (ValueError, TypeError, KeyError):
                    continue
        else:
            # No header: read first column only
            f.seek(0)
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    continue
                try:
                    prices.append(float(row[0]))
                except ValueError:
                    continue
    return prices

def main():
    if len(sys.argv) < 2:
        print("Usage: python choose_constant_model_type.py <path_to_csv>")
        sys.exit(1)

    csv_path = sys.argv[1]
    prices = load_prices_from_csv(csv_path)

    period = 5 
    deviation_model = "standard"     # or "standard_deviation"
    deviation_multiplier = 2.0 
    previous_mcginley_dynamic = 0.0  # none available on first run 

    # prices = load_prices_from_csv("data.csv")
    bands = ci.bulk.mcginley_dynamic_bands(
        prices,
        deviation_model,
        deviation_multiplier,
        previous_mcginley_dynamic,
        period,
    )

    print("Loaded", len(prices), "prices")
    print("Length of bands", len(bands))
    # bands is a list of tuples: (lower_band, mcginley_dynamic, upper_band)

    # Next price comes in
    new_price = 5689.24
    prices.append(new_price)

    last_mcginley_dynamic = bands[-1][1]  # previous McGinley Dynamic from bulk result

    # Use the last 'period' prices for the single calculation
    latest_window = prices[-period:]

    next_band = ci.single.mcginley_dynamic_bands(
        latest_window,
        deviation_model,
        deviation_multiplier,
        last_mcginley_dynamic,
    )

    lower, mid, upper = next_band
    print(f"Lower band {lower}, McGinley dynamic {mid}, upper band {upper}")

if __name__ == "__main__":
    main()

