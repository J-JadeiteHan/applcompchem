#!/usr/bin/env python3
"""B3LYP/6-31G(d) RRHO Gibbs energies for H2 isotopologues at 298.15 K, 1 atm."""

from pathlib import Path
from types import MethodType
import json

import numpy as np
from scipy.optimize import minimize_scalar
from pyscf import dft, gto
from pyscf.hessian import thermo

TEMPERATURE = 298.15
PRESSURE_PA = 101325.0
ISOTOPOLOGUES = {
    "H2": (np.array([1.00782503223, 1.00782503223]), 2),
    "D2": (np.array([2.01410177812, 2.01410177812]), 2),
    "HD": (np.array([1.00782503223, 2.01410177812]), 1),
}


def make_mf(bond_angstrom):
    mol = gto.M(
        atom=f"H 0 0 {-bond_angstrom / 2}; H 0 0 {bond_angstrom / 2}",
        basis="6-31g(d)", unit="Angstrom", charge=0, spin=0, symmetry=False,
        verbose=4,
    )
    mf = dft.RKS(mol)
    mf.xc = "b3lyp"
    mf.conv_tol = 1e-10
    return mf


def energy_at(bond_angstrom):
    return make_mf(bond_angstrom).kernel()


opt = minimize_scalar(energy_at, bounds=(0.55, 1.10), method="bounded", options={"xatol": 1e-7})
if not opt.success:
    raise RuntimeError(opt.message)

mf = make_mf(opt.x)
energy = mf.kernel()
hessian = mf.Hessian().kernel()
results = {
    "method": "B3LYP/6-31G(d)",
    "temperature_K": TEMPERATURE,
    "pressure_Pa": PRESSURE_PA,
    "optimized_HH_distance_angstrom": float(opt.x),
    "electronic_energy_hartree": float(energy),
    "isotopologues": {},
}

for label, (masses, symmetry_number) in ISOTOPOLOGUES.items():
    vibrational = thermo.harmonic_analysis(mf.mol, hessian, mass=masses)
    original_mass_list = mf.mol.atom_mass_list
    original_symmetry_number = thermo.rotational_symmetry_number
    mf.mol.atom_mass_list = MethodType(lambda self, isotope_avg=True: masses, mf.mol)
    thermo.rotational_symmetry_number = lambda mol: symmetry_number
    try:
        thermal = thermo.thermo(mf, vibrational["freq_au"], TEMPERATURE, PRESSURE_PA)
    finally:
        mf.mol.atom_mass_list = original_mass_list
        thermo.rotational_symmetry_number = original_symmetry_number
    results["isotopologues"][label] = {
        "masses_u": masses.tolist(),
        "rotational_symmetry_number": symmetry_number,
        "harmonic_frequency_cm-1": [float(x.real) for x in vibrational["freq_wavenumber"]],
        "gibbs_free_energy_hartree": float(thermal["G_tot"][0]),
        "enthalpy_hartree": float(thermal["H_tot"][0]),
        "entropy_hartree_per_K": float(thermal["S_tot"][0]),
    }

Path("hydrogen_isotope_thermo_results.json").write_text(json.dumps(results, indent=2) + "\n")
for label, values in results["isotopologues"].items():
    print(f"{label:2s} G = {values['gibbs_free_energy_hartree']:.12f} Eh")
