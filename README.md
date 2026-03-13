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

> Supplementary Appendix A (formal proof that E[λ] → 0, to be incorporated in v3) is available in this repository.

---

## Preprint

Sakidja, R. (2026). *Light Curve Asymmetry in Rubin LSST Variable Stars: Candidate Evidence for T⁰ⁱ Momentum Flux Coupling in the Low-Velocity Galactic Regime.* Zenodo. https://doi.org/10.5281/zenodo.17959245

## Data

Alert stream data accessed via Lasair broker using filter `GravitationalWakeDipole_v1`. Proper motions from Gaia DR3 via VizieR.

## Status

Preliminary — Not Peer Reviewed. Version 3 pending new Rubin LSST data.
