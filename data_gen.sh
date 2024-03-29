#MSUB -N data_gen_and_train_single_agent
#MSUB -e logs/${MOAB_JOBID}.e
#MSUB -o logs/${MOAB_JOBID}.o
#MSUB -l nodes=1:ppn=4
#MSUB -l walltime=0:00:10:00
#MSUB -l pmem=16000mb
#MSUB -t [1-4]

cd /work/ws/nemo/fr_jf442-thesis-0/MTORL-DAC
source activate MTORL-DAC

#AGENT=${1:-exponential_decay}
AGENT=exponential_decay
ID=${1:-0}
NUM_RUNS=100
FC1=Ackley
FC2=Rastrigin
FC3=Rosenbrock
FC4=Sphere
VERSION=default
RESULTS_DIR="data_multi"

# Print some information about the job to STDOUT
echo "Workingdir: $(pwd)";
echo "Started at $(date)";
echo "Running job ${MOAB_JOBID} of user ${MOAB_USER} using ${MOAB_NODECOUNT} nodes on partition ${MOAB_PARTITION}";
echo "Setup: $AGENT $ID";


if [ ${MOAB_JOBARRAYINDEX} -eq 1 ]
then
    python data_gen.py --save_run_data --save_rep_buffer --env $FC1\_$VERSION --agent $AGENT --num_runs $NUM_RUNS --id $ID --results_dir $RESULTS_DIR
elif [ ${MOAB_JOBARRAYINDEX} -eq 2 ]
then
    python data_gen.py --save_run_data --save_rep_buffer --env $FC2\_$VERSION --agent $AGENT --num_runs $NUM_RUNS --id $ID --results_dir $RESULTS_DIR
elif [ ${MOAB_JOBARRAYINDEX} -eq 3 ]
then
    python data_gen.py --save_run_data --save_rep_buffer --env $FC3\_$VERSION --agent $AGENT --num_runs $NUM_RUNS --id $ID --results_dir $RESULTS_DIR
elif [ ${MOAB_JOBARRAYINDEX} -eq 4 ]
then
    python data_gen.py --save_run_data --save_rep_buffer --env $FC4\_$VERSION --agent $AGENT --num_runs $NUM_RUNS --id $ID --results_dir $RESULTS_DIR
fi

# Print some Information about the end-time to STDOUT
echo "DONE";
echo "Finished at $(date)";
