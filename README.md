# PyTechnicalIndicators How-To Guides

Welcome to the How-To Guides for PyTechnicalIndicators — Python bindings backed by the RustTI engine for fast, configurable technical analysis.

These guides are goal-oriented. They help you accomplish specific tasks with minimal theory and boilerplate. If you need deeper explanations or reference docs, see the links below.

---

## 🧭 What You’ll Find Here

- When to use bulk vs single functions: Understand when to use rolling series vs single-window calculations
  - [./bulk_vs_single.md](./bulk_vs_single.md)
- Choosing the right constant model type: Programmatically determine the best `constant_model_type`
  - [./choose_constant_model_type.md](./choose_constant_model_type.md)
- Choosing the right deviation model: Programmatically determine the best deviation model
  - [./choose_deviation_model.md](./choose_deviation_model.md)
- Choosing the right period: Programmatically determine the best period
  - [./choose_period.md](./choose_period.md)
- How to use the McGinley dynamic variation of functions
  - [./mcginley_dynamic.md](./mcginley_dynamic.md)

---

## ⚙️ Install

```bash
pip install pytechnicalindicators
```

Quick sanity check:

```python
from pytechnicalindicators import momentum_indicators as mi
prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
rsi = mi.bulk.relative_strength_index(prices, "smoothed_moving_average", 14)
print(rsi[-1])
```

---

## 📚 About This Repo

This repository collects practical, cut-to-the-chase guides for the PyTechnicalIndicators Python package.

Related resources:
- PyTechnicalIndicators repository: https://github.com/chironmind/PyTechnicalIndicators
- RustTI crate docs (engine under the hood): https://docs.rs/rust_ti/latest/rust_ti/

---

## 📚 More Documentation

This repository is part of a structured documentation suite:

- 📕 **Tutorials:** — [See here](https://github.com/ChironMind/PyTechnicalIndicators_Tutorials)
- 📘 **How-To Guides:** — You're here!
- ⏱️. **Benchmarks:** — [See here](https://github.com/ChironMind/PyTechnicalIndicators-Benchmarks)
- 📙 **Explanations:** — Coming soon
- 📗 **Reference:** — [See here](https://github.com/ChironMind/PyTechnicalIndicators/wiki)

---

## 💬 Contributing

Contributions, fixes, or new guides are welcome!
- Open an issue with your suggestion or question
- Submit a PR to add or improve a guide

---

## 🧠 New to PyTechnicalIndicators?

- Install the package (see above)
- Browse the guides listed here and start with “When to use bulk vs single”
- Many guides include a small CSV loader snippet to get you going quickly
