#!/bin/bash -l

# Job name
#$ -N <JOB_NAME>
# WD
#$ -wd /home/ucbthsc/Scratch/dir

# Force bash
#$ -S /bin/bash
# OpenMP threads
#$ -pe smp 12
# Memory
#$ -l mem=31G
# TMPDIR
#$ -l tmpfs=10G
# Wall time h:m:s
#$ -l h_rt=2:0:0
# Node types https://wiki.rc.ucl.ac.uk/wiki/Resource_Allocation
# #$ -ac allow=TU
#$ -M ucbthsc@ucl.ac.uk
#$ -m ae

# Do work in TMPDIR
cd $TMPDIR

# -----------------------------
# -- Enter job details below --
# -----------------------------

echo "JOB_STARTED"
echo $(/bin/date) > JOB_DATE

# module load python3/recommended



# Move output to Scratch
tar zcvf $HOME/Scratch/job_$JOB_ID.tar.gz $TMPDIR

echo "JOB_COMPLETED"
