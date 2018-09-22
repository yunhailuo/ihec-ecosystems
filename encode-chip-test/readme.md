# ENCODE ChIP-Seq pipeline singularity wrapper

Note: This is out of date. 

## ENCODE ChIP-Seq pipeline

See https://github.com/ENCODE-DCC/chip-seq-pipeline2/


## Getting cromwell

Use http://www.epigenomes.ca/data/CEMT/resources/cromwell-30.2.jar

To get test data use: `python chip.py -get` (this will take a while). Update `ref_config.json` and then `python chip.py -refconfig` to generate hg38 configuaration files, followed by `python chip.py -pullimage` to generate the singularity image (this should take a few minites). `python chip.py -maketests` will generate the test configuration files. There should be `./singularity_test.sh` and `./testrun.sh` in the directory now. `chmod +x ./singularity_test.sh ./testrun.sh`, and then run the tests with `./singularity_test.sh ./v2/ihec/cemt0007_h3k4me3.json` and `./singularity_test.sh ./v2/ihec/cemt0007_h3k27me3.json` . 


The provided configuration files are for 75bp PET only. Standard configration files for SET and read lengths will be provided. Currently the only local mode is supported for singularity. Slurm support is on the way. The ENCODE documentation addresses both. 







