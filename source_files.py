import ROOT

# Create a Chain of filles to analyze

# MC
mc_chain = ROOT.TChain("Events")
print("--> Adding MC files to chain...")
# Dataset: /DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM
# List all files:
# dasgoclient -query="file dataset=/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"

# mc_chain.Add("root://cms-xrd-global.cern.ch///store/mc/RunIISummer20UL18NanoAODv2/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/106X_upgrade2018_realistic_v15_L1v1-v1/00000/B81103CC-8168-3F46-AEC4-6CEF3012FC8A.root")
mc_chain.Add("/eos/cms/store/mc/RunIISummer20UL18NanoAODv9/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/230000/55E96D77-D756-814A-8FF8-D4CD4EACCA76.root")
# mc_chain.Add("root://cms-xrd-global.cern.ch///store/mc/RunIISummer20UL18NanoAODv9/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/230000/55E96D77-D756-814A-8FF8-D4CD4EACCA76.root")


# Data
data_chain = ROOT.TChain("Events")
print("--> Adding Data files to chain...")
# Dataset: /SingleMuon/Run2018D-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD
# List all files.
# dasgoclient -query="file dataset=/SingleMuon/Run2018D-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD"

data_chain.Add(
    "/eos/cms/store/data/Run2018D/SingleMuon/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/130000/195BC720-372C-6943-849A-A6D5A2CE81A8.root")
# data_chain.Add(
#     "root://cms-xrd-global.cern.ch///store/data/Run2018D/SingleMuon/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/130000/195BC720-372C-6943-849A-A6D5A2CE81A8.root")
