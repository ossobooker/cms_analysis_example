# CMS Analysis example

Simple example on how to access CMS NanoAOD files and read some information from it.

Note: Assuming (1) the user have GRID certificate (2) registered to CMS VO.

More info:

https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid
https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideLcgAccess


![pyroot_example_nanoaod](https://github.com/ftorresd/pyroot_example_nanoaod/raw/main/content/pyroot_example_nanoaod.gif)


## Technicals

### Get the code

Download or clone (HTTPS) or clone (SSH)
```wget https://github.com/ftorresd/pyroot_example_nanoaod/archive/refs/heads/main.zip
unzip main.zip
cd pyroot_example_nanoaod-main
```

or

```
git clone https://github.com/ftorresd/pyroot_example_nanoaod.git
```

or

```
git clone git@github.com:ftorresd/pyroot_example_nanoaod.git
```

### Setup 
Execute once, every login.

```bash
source /cvmfs/sft.cern.ch/lcg/views/LCG_102/x86_64-centos7-gcc11-opt/setup.sh
voms-proxy-init --rfc --voms cms -valid 192:00
```

### Run the analysis code

```
python cms_analysis.py
```

### Output
Histograms will be saved at output_file.root.
