#!/usr/bin/env bash
#SBATCH --job-name=h2-isotope-pyscf
#SBATCH --partition=32core_partition
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --time=01:00:00
#SBATCH --output=pyscf-hydrogen-%j.out
#SBATCH --error=pyscf-hydrogen-%j.err

set -euo pipefail
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
/appl/share/maestro/maestro/.venv/bin/maestro-python hydrogen_isotope_thermo_pyscf.py
