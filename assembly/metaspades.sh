#!/bin/bash
# conda install bioconda::spades
# https://ablab.github.io/spades/

eval "$(conda shell.bash hook)"
conda activate spades


BASEDIR="$1" # e.g. /home/jan/ms/1_mg; positional argument
READ_DIR="$2" # e.g. /home/reads_mg/1; positional argument
THREADS="$3" # e.g. 8; positional argument

SEQ_FILE_1_SUBSAMPLED=${READ_DIR}/concatenated_reads_subsampled/all_R1_PE.fastq
SEQ_FILE_2_SUBSAMPLED=${READ_DIR}/04_qc/concatenated_reads_subsampled/all_R2_PE.fastq
OUT_DIR_SUBSAMPLED=${BASEDIR}/06_assembly_metaspades/00_assembly/assembly_subsampled

SEQ_FILE_1=${READ_DIR}/concatenated_reads/all_R1_PE_full.fq.gz
SEQ_FILE_2=${READ_DIR}/concatenated_reads/all_R2_PE_full.fq.gz
OUT_DIR=${BASEDIR}/06_assembly_metaspades/00_assembly/assembly_full

# https://ablab.github.io/spades/running.html#basic-options
# https://ablab.github.io/spades/running.html#-meta-same-as-metaspadespy

# make a list of the files in the SEQ_DIR
# assembly with spades, note that "Currently metaSPAdes supports only a single short-read library which has to be paired-end "
# thus, we need to concatenate all the R1 and R2 files into one file each...

echo $BASEDIR


start_time=$(date +%s)

# and then run spades on those files
spades.py --meta \
    -1 $SEQ_FILE_1 \
    -2 $SEQ_FILE_2 \
    -o $OUT_DIR -t $THREADS 

end_time=$(date +%s)
elapsed_time=$((end_time - start_time))
echo "Duration $elapsed_time seconds"



# If you run a long calculation like metaspades in a standard VS Code integrated terminal and then close VS Code (or lose your internet connection), your job will typically be killed.

# When VS Code closes, it terminates the terminal session, which sends a hangup signal (SIGHUP) to all running child processes, terminating them immediately. While VS Code has a "terminal persistence" feature, it is highly unreliable for multi-day jobs.

# To safely run a 5-day calculation and allow yourself to close VS Code, you should use one of the following methods:

# 1. Use tmux (Highly Recommended)
# tmux is a terminal multiplexer that lets you create persistent terminal sessions.

# Type tmux in your VS Code terminal and press Enter. This opens a new persistent session.
# Run your script: metaspades.sh
# Detach from the session so it keeps running in the background: Press Ctrl + B, release, then press D.
# You can now safely close VS Code.
# When you come back, open a new terminal in VS Code and type tmux attach to see your running job.
# 2. Use screen
# If tmux isn't installed, screen does the exact same thing.

# Type screen.
# Run your script.
# Detach by pressing Ctrl + A, release, then D.
# Reattach later with screen -r.

# 3. Use nohup - also on python
# If you just want to run the command in the background and log the output without using a multiplexer, use nohup (no hangup) and & (run in background):


# nohup bash 00_scripts/metaspades.sh > metaspades_output.log 2>&1 &
# You can safely close VS Code immediately.
# To check on it later, you can watch the log file with tail -f metaspades_output.log.
# To see if it's still running, use htop or ps aux | grep metaspades.
# Summary: For a 5-day metaspades job, definitely use tmux or nohup before starting the script.

