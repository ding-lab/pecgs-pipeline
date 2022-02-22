#!/bin/bash

python ../../src/compute1/generate_run_commands.py --sequencing-info  sequencing_info.txt run_list.txt /storage1/fs1/dinglab/Active/Projects/estorrs/pecgs-pipeline/examples/ht191/example_run

# if running this script from a non-compute1 system you can set a proxy run directory where the run directory will be written. You can then copy this directory to compute1 and start the run
# python ../../src/compute1/generate_run_commands.py --proxy-run-dir example_run --sequencing-info  sequencing_info.txt run_list.txt /storage1/fs1/dinglab/Active/Projects/estorrs/pecgs-pipeline/examples/ht191/example_run