"""
Extract median lambda vs concentration from Shin-Uchuu z~4.
Concentration c = Rvir/rs is a proxy for inner overdensity.
High concentration halos probe the high rho_crit regime.
"""
import h5py
import numpy as np
import csv

FILENAME = "ShinUchuu_halolist_3p93_m200c1e9.h5"

# Planck 2015 cosmology
OMEGA_M = 0.3089
OMEGA_L = 0.6911
H0 = 67.74
h = H0 / 100.0
Z_SNAP = 3.93

# Critical density at z=3.93 in M_sun/h / (Mpc/h)^3
E2 = OMEGA_M * (1 + Z_SNAP)**3 + OMEGA_L
RHO_CRIT_0 = 2.775e11
rho_crit_h = RHO_CRIT_0 * E2  # M_sun/h / (Mpc/h)^3
rho_mean_h = rho_crit_h * OMEGA_M

print(f"z = {Z_SNAP}")
print(f"rho_crit = {rho_crit_h:.3e} M_sun/h/(Mpc/h)^3")
print(f"rho_mean = {rho_mean_h:.3e} M_sun/h/(Mpc/h)^3\n")

with h5py.File(FILENAME, 'r') as f:
    keys = list(f.keys())
    g = f[keys[0]] if len(keys)==1 and isinstance(f[keys[0]], h5py.Group) else f
    spin    = g['Spin'][:]
    mvir    = g['Mvir'][:]
    rvir    = g['Rvir'][:]   # kpc/h
    rs      = g['rs'][:]     # kpc/h (NFW scale radius)
    m200c   = g['M200c'][:]
    m500c   = g['M500c'][:]
    m2500c  = g['M2500c'][:]
    pid     = g['pid'][:]    # -1 = distinct halo, else subhalo

# Convert Rvir and rs to Mpc/h
rvir_mpc = rvir / 1000.0
rs_mpc   = rs   / 1000.0

# Concentration c = Rvir / rs
valid = (rs_mpc > 0) & (rvir_mpc > 0) & (pid == -1)  # distinct halos only
conc = np.zeros(len(spin))
conc[valid] = rvir_mpc[valid] / rs_mpc[valid]

print(f"Total halos: {len(spin):,}")
print(f"Distinct halos (pid=-1): {valid.sum():,}")
print(f"Concentration range: {conc[valid].min():.1f} to {conc[valid].max():.1f}")
print(f"Median concentration: {np.median(conc[valid]):.2f}\n")

# For NFW profile, the mean overdensity within Rvir relative to rho_mean is:
# delta_vir = (4/3 pi Rvir^3 * rho_vir) / (4/3 pi Rvir^3 * rho_mean)
# But we can compute the EFFECTIVE overdensity at the scale radius:
# rho_s = M200c / (4*pi*rs^3 * [ln(1+c) - c/(1+c)])
# The overdensity at 0.1*Rvir (inner halo) scales as ~200*c^2/(g(c)*something)

# Simpler: compute overdensity of M2500c sphere directly
# R2500c from M2500c: M2500c = (4/3)*pi*R2500c^3 * 2500 * rho_crit
# R2500c = (M2500c / (2500 * rho_crit * 4pi/3))^(1/3)

valid2 = valid & (m2500c > 0)
R2500c = (m2500c[valid2] / (2500.0 * rho_crit_h * (4.0/3.0) * np.pi))**(1.0/3.0)  # Mpc/h

# Mean density within R2500c relative to mean background
rho_inner = m2500c[valid2] / ((4.0/3.0) * np.pi * R2500c**3)
od_inner = rho_inner / rho_mean_h

print(f"Halos with M2500c > 0: {valid2.sum():,}")
print(f"Overdensity within R2500c relative to mean: {od_inner.min():.0f} to {od_inner.max():.0f}")
print(f"Median: {np.median(od_inner):.0f}\n")

# Now bin lambda by overdensity within R2500c
spin_v2 = spin[valid2]

print(f"{'od_threshold':>14} {'N_halos':>10} {'median_lambda':>15} {'mean_lambda':>13}")
print("-"*55)

thresholds = [1800, 5000, 10000, 20000, 50000, 100000]
results = []
for t in thresholds:
    mask = od_inner >= t
    n = mask.sum()
    if n > 10:
        med  = float(np.median(spin_v2[mask]))
        mean = float(np.mean(spin_v2[mask]))
        std  = float(np.std(spin_v2[mask]))
        print(f"{t:>14,} {n:>10,} {med:>15.4f} {mean:>13.4f}")
        results.append({'od_threshold': t, 'N': int(n),
                        'median_lambda': med, 'mean_lambda': mean,
                        'std_lambda': std, 'z': Z_SNAP,
                        'sim': 'ShinUchuu_DM', 'od_definition': 'within_R2500c_vs_mean'})
    else:
        print(f"{t:>14,} {n:>10,}   insufficient halos")

print()
print("Ref: Li et al. (2022) lambda_DM=0.0255 at rho~1800x mean (virial)")
print("Note: od here is rho within R2500c / rho_mean — probes higher densities")

if results:
    with open('ShinUchuu_lambda_od.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=results[0].keys())
        w.writeheader(); w.writerows(results)
    print("Saved to ShinUchuu_lambda_od.csv")
