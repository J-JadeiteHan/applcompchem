---
task: unsupported
engine: pyscf
error_class: none
outcome: workaround
wall_time_s: 5
n_atoms: 2
method: B3LYP
basis: 6-31G(d)
cores: 1
mode: slurm
---
Symptom: MAESTRO ThermoTask rejected isotope label `D`, and the catalog's IsotopeShiftTask provides isotope-shifted frequencies but not Gibbs free energy.

Attempts: A Gaussian16 array submission was attempted first but its compute-node module did not provide a `g16` command. A first PySCF module submission aborted because its CUDA runtime required a newer driver. The retry used the shared CPU PySCF environment on one Slurm core.

Result: Completed successfully on node4 in 5 s. The workflow optimized neutral singlet H2 at B3LYP/6-31G(d), evaluated its Hessian, and applied H/D nuclear masses and rotational symmetry numbers to the RRHO thermochemistry at 298.15 K and 1 atm. Gibbs free energies (Eh): H2 -1.176824729239; D2 -1.181427695023; HD -1.179682137444.

Context: The electronic energy and Born--Oppenheimer Hessian are isotope-independent; D2 and HD differ through the nuclear masses in vibrational, translational, and rotational partition functions. The H-H optimized separation was 0.74278835 Angstrom.
