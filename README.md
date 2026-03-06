# Gravitational Wake Dipole — Rubin LSST

**Candidate evidence for T⁰ⁱ momentum flux coupling in variable star light curves**

Ridwan Sakidja — Missouri State University — March 2026

---

## What this is

A preliminary analysis of the first 8 days of Rubin Observatory LSST alert stream data, cross-matched with Gaia DR3 proper motions, testing whether stellar light curve asymmetry correlates with proper motion — as predicted by the off-diagonal T⁰ⁱ components of Einstein's stress-energy tensor.

**Primary result:** r=0.726, p=0.0022, 3.06σ across n=15 Variable Star candidates. Combined significance (Fisher, 2 formal tests): 3.30σ.

---

## Files

| File | Description |
|------|-------------|
| `GravitationalWakeDipole_V1.ipynb` | Main analysis notebook — Gaia cross-match, statistics, figures |
| `ZTF_CMBDipole_NorthernTest_V1.ipynb` | ZTF non-detection control experiment |
| `lasair_425GravitationalWakeDipole_v1_filter_results.csv` | Raw Lasair alert stream output (n=121, 15 VS) |

---

## How to run

1. Open `GravitationalWakeDipole_V1.ipynb` in Google Colab
2. Run Cell 1 (install dependencies)
3. Upload the CSV when prompted in Cell 3
4. Run all cells in order

---

## Key numbers

| Test | Result | Status |
|------|--------|--------|
| Speed-asymmetry (Test 1) | r=0.726, p=0.0022, 3.06σ | Formal |
| Fall-rate suppression (Test 4) | p=0.0433, 2.02σ | Formal |
| Fisher combined (Tests 1+4) | p=0.00098, 3.30σ | — |
| CMB proximity | r=−0.570, 2.22σ | Exploratory |
| N/S contrast | 3.8× (n=1 North) | Observation only |

---

## Data source

- **Rubin LSST:** Lasair broker, filter `GravitationalWakeDipole_v1` (created 2026-03-02)
- **Proper motions:** Gaia DR3 via VizieR (I/355/gaiadr3)
- **CMB dipole:** Planck 2018, l=264°, b=+48°

---

## Preprint

Sakidja, R. (2026). *Light Curve Asymmetry in Rubin LSST Variable Stars: Candidate Evidence for T⁰ⁱ Momentum Flux Coupling in the Low-Velocity Galactic Regime.* Zenodo preprint. [link pending]
