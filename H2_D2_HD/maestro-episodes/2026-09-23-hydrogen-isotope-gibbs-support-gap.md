---
task: unsupported
engine: none
error_class: support_gap
outcome: support_gap
method: B3LYP
basis: 6-31G(d)
mode: slurm
---
Symptom: The requested Gibbs free energies for H2, D2, and HD cannot be represented by ThermoTask because its SystemQM geometry parser rejects the isotope label `D`.

Attempts: Confirmed ThermoTask and selected Gaussian with DFT/B3LYP and 6-31G(d). Created H2, D2, and HD initial XYZ structures. MAESTRO suggested neutral H2 charge and singlet spin, then rejected D2 at the computed-charge stage with detail `'D'`. Searched the live catalog for isotope support; IsotopeShiftTask exists but produces isotope-shifted harmonic frequencies only, not thermochemistry or Gibbs free energy.

Result: MAESTRO currently lacks an isotope-aware Gibbs free-energy task for D2 and HD.

Context: User requested Gibbs free energies of H2, D2, and HD on idle compute cores rather than the login node, at the default 298.15 K and 1 atm unless otherwise specified.
