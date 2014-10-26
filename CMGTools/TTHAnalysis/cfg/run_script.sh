pybatch.py -o OUTPUT_default run_susyMultilepton_cfg.py -b 'bsub -q 8nh -o std_output.txt -J JobName_default < batchScript.sh'
pybatch.py -o OUTPUT_shiftJEC_up run_susyMultilepton_shiftJEC_up_cfg.py -b 'bsub -q 8nh -o std_output.txt -J JobName_shiftJEC_up < batchScript.sh'
pybatch.py -o OUTPUT_shiftJEC_down run_susyMultilepton_shiftJEC_down_cfg.py -b 'bsub -q 8nh -o std_output.txt -J JobName_shiftJEC_down < batchScript.sh'

