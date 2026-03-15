# GravitationalWakeDipole

A preliminary analysis of the first 8 days of Rubin Observatory LSST alert stream data, cross-matched with Gaia DR3 proper motions, testing whether stellar light curve asymmetry correlates with proper motion — as predicted by the off-diagonal T⁰ⁱ components of Einstein's stress-energy tensor.

**Primary result:** r=0.726, p=0.0022, 3.06σ across n=15 Variable Star candidates. Combined significance (Fisher, 2 formal tests): 3.30σ.

---

## Version 2

Extends the theoretical interpretation in three directions:

- The mechanism by which FFT-based N-body solvers filter ∇·T⁰ⁱ below the force softening scale is made explicit.
- The halo spin parameter λ(ρ_crit) falling monotonically across four orders of magnitude is identified as the accumulated numerical signature of this filtering.
- The per-star coupling constant (g = 0.0289 per km/s) is consistent within 16% with the orbit-integrated coupling constant from the SPARC companion paper, connecting the same T⁰ⁱ proportionality from pc to kpc scales with no free parameters.

## Supplementary Appendix A
Formal mathematical proof that E[λ] → 0 in the continuum limit. The proof demonstrates that any FFT Poisson solver is structurally incapable of producing net torque — not as an approximation, but as an algebraic identity: the force direction at each Fourier mode is locked to **k**, and **k** × **k** ≡ 0 exactly.

The apparent convergence of λ with simulation resolution is not convergence toward a physical answer. It is convergence toward the limit the identity guarantees. Resolution and erasure are the same event.

A.8 extends the argument to the Vlasov–Poisson precedent: plasma physics identified the same structural limitation in the 1930s and resolved it by pivoting to the full phase space distribution f(x,v,t). The FFT Poisson solver does not reach even the level of the electrostatic Vlasov–Poisson system — it discards T⁰ⁱ and gravitational Landau damping in the single step ρ = ∫f d³v.

> Supplementary Appendix A is available in this repository.

## Supplementary Appendix B
Full derivation of the x-axis placement for the three modern data points in Figure 4: Benson (2017), Li et al. (2022), and Shin-Uchuu (Ishiyama et al. 2021). All points are expressed in units of mean background density at z=0 for consistency with the Barnes & Efstathiou (1987) axis convention.

| Dataset | x-axis (× mean) | Method |
|---|---|---|
| Benson (2017) | 712 | FoF b=0.2 → 178/Ω_m, Millennium cosmology |
| Li et al. (2022) | 25,000 | 200 × (1+z)³ — Δ_200 mean density definition at z=4, cosmology-independent |
| Shin-Uchuu (2021) | 24,412 | 200 × E²(z=3.93) / Ω_m — Δ_200c, Planck 2015 |

No free parameters enter the placement of any data point. The Shin-Uchuu derivation is based on the script `lambda_conc.py`, which reads the halo catalog directly and is available in this repository.

---

## Preprint

Sakidja, R. (2026). *Light Curve Asymmetry in Rubin LSST Variable Stars: Candidate Evidence for T⁰ⁱ Momentum Flux Coupling in the Low-Velocity Galactic Regime.* Zenodo. https://doi.org/10.5281/zenodo.18895222

## Data

Alert stream data accessed via Lasair broker using filter `GravitationalWakeDipole_v1`. Proper motions from Gaia DR3 via VizieR.

## Status

Preliminary — Not Peer Reviewed. Version 3 pending new Rubin LSST data.
