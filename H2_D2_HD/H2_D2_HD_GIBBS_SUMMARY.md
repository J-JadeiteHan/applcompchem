# H2, D2, and HD Gibbs free-energy calculation

## Result

At 298.15 K and 1 atm, the B3LYP/6-31G(d) RRHO Gibbs free energies are:

| Molecule | Gibbs free energy (Eh) |
| --- | ---: |
| H2 | -1.176824729239 |
| D2 | -1.181427695023 |
| HD | -1.179682137444 |

The optimized H--H distance is 0.74278835 Angstrom. The electronic energy is
-1.175482410917 Eh.

## Isotope-exchange equilibrium constant

For the isotope-exchange reaction

`H2 + D2 <=> 2 HD`,

the calculated standard Gibbs free energy is

`Delta G° = 2G(HD) - G(H2) - G(D2) = -0.001111850626 Eh = -2.91916 kJ mol^-1`.

Using `K = exp(-Delta G° / RT)` at 298.15 K gives

`K = 3.2465`.

This value uses the same ideal-gas RRHO standard-state convention as the
underlying molecular Gibbs free energies.

## Method

The successful calculation used PySCF 2.14.0 with B3LYP/6-31G(d), optimized
neutral-singlet H2, evaluated its Hessian, and applied the H/D nuclear masses
and rotational symmetry numbers in the RRHO thermochemistry. Under the
Born--Oppenheimer approximation, the electronic energy and Hessian are shared
by the three isotopologues; their thermal corrections differ through mass.

The Slurm job ran on compute node `node4` with one CPU core and completed in
5 s. `hydrogen_isotope_thermo_results.json` contains the complete numerical
output and `hydrogen_isotope_thermo_pyscf.py` reproduces the successful run.

## Included files

This repository update also retains every file created for the earlier
Gaussian and PySCF submission attempts, including empty output logs and the
failed CUDA-based PySCF attempt, so the execution history is complete.
