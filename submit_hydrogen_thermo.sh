#!/usr/bin/env bash
#SBATCH --job-name=h2-isotope-thermo
#SBATCH --partition=32core_partition
#SBATCH --array=0-2
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G
#SBATCH --time=01:00:00
#SBATCH --output=slurm-%A_%a.out
#SBATCH --error=slurm-%A_%a.err

set -euo pipefail
module load gaussian16/g16

inputs=(h2_thermo.gjf d2_thermo.gjf hd_thermo.gjf)
input="${inputs[$SLURM_ARRAY_TASK_ID]}"
g16 < "$input" > "${input%.gjf}.log"
