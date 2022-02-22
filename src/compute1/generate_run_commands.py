import argparse
import os
import logging

import pandas as pd

import wombat.pecgs as pecgs

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

parser = argparse.ArgumentParser()

parser.add_argument('run_list', type=str,
    help='Filepath of table containing run inputs.')

parser.add_argument('run_dir', type=str,
    help='Directory on compute1 that will be used for the pipeline runs.')

parser.add_argument('--sequencing-info', type=str,
    help='Sequencing info for fastqs if you want aligned bams to have correct metadata')

parser.add_argument('--input-config', type=str,
    help='YAML file containing inputs that will override the default pipeline parameters.')

parser.add_argument('--proxy-run-dir', type=str,
    help='Use if running this script on a system that is not compute1. Will write inputs to a proxy directory that can then be copied to compute1.')

parser.add_argument('--additional-volumes', type=str,
    help='Additional volumnes to map on compute1 on top of /storage1/fs1/dinglab and /scratch1/fs1/dinglab')


args = parser.parse_args()


def main():
    run_list = pd.read_csv(args.run_list, sep='\t', index_col='run_id')
    run_map = run_list.transpose().to_dict()
    run_map = {k: {c.replace('.filepath', ''): val
                   for c, val in v.items() if 'filepath' in c}
               for k, v in run_map.items()}

    if args.sequencing_info is not None:
        sequencing_info = pd.read_csv(
                args.sequencing_info, sep='\t', index_col='run_id')
    else:
        sequencing_info = None

    # get pecgs-pipeline root
    fp = os.path.realpath(__file__)
    tool_root = '/'.join(fp.split('/')[:-2])

    start_cmds, server_cmds, job_cmds = pecgs.from_run_list_TN_wxs_fq_T_rna_fq(
        run_map, args.run_dir, tool_root, sequencing_info=sequencing_info,
        proxy_run_dir=args.proxy_run_dir)


if __name__ == '__main__':
    main()