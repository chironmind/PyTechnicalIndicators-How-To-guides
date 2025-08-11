from pytechnicalindicators import momentum_indicators as mi

# 53 example closing prices
data = [ 
    6037.59, 5970.84, 5906.94, 5881.63, 5868.55, 5942.47, 5975.38, 5909.03,
    5918.25, 5827.04, 5836.22, 5842.91, 5949.91, 5937.34, 5996.66, 6049.24,
    6086.37, 6118.71, 6101.24, 6012.28, 6067.70, 6039.31, 6071.17, 6040.53,
    5994.57, 6037.88, 6061.48, 6083.57, 6025.99, 6066.44, 6068.50, 6051.97,
    6115.07, 6114.63, 6129.58, 6144.15, 6117.52, 6013.13, 5983.25, 5955.25,
    5956.06, 5861.57, 5954.50, 5849.72, 5778.15, 5842.63, 5738.52, 5770.20,
    5614.56, 5572.07, 5599.30, 5521.52, 5638.94
]

period = 14
model = "smoothed_moving_average"  # options: "simple_moving_average", "smoothed_moving_average",
                                   #          "exponential_moving_average", "simple_moving_median",
                                   #          "simple_moving_mode"

# 1) Bulk: compute historical RSI values
rsi_series = mi.bulk.relative_strength_index(data, model, period)
print("Bulk RSIs:", rsi_series)

# 2) Single: compute the next/latest RSI when a new price arrives
new_price = 5769.21
data.append(new_price)

# For period=14, use the latest 14 prices for single RSI 
latest_window = data[-period:]
latest_rsi = mi.single.relative_strength_index(latest_window, model)
print("Single RSI:", latest_rsi)

