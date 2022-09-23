from source_files import mc_chain
from source_files import data_chain
import tqdm
import json
import ROOT
# .....
# setup some ROOT stuff
ROOT.PyConfig.DisableRootLogon = True
ROOT.PyConfig.IgnoreCommandLineOptions = False
ROOT.gROOT.SetBatch(True)

# Load source files chains

# Config
# max number of events to be processed -> set to -1 to proccess all events
max_events = 25000
# max_events = -1 # max number of events to be processed -> set to -1 to proccess all events


# Declare histograms
# muons p_T
h_muon_pt_1_MC = ROOT.TH1F("h_muon_pt_1_MC", "; Muon pT ; Muons", 50, 0, 200)
# force the storage and computation of the sum of the square of weights per bin
# REF: https://root.cern.ch/doc/master/classTH1.html#associated-errors
h_muon_pt_1_MC.Sumw2()

h_muon_pt_2_MC = ROOT.TH1F("h_muon_pt_2_MC", "; Muon pT ; Muons", 50, 0, 200)
# force the storage and computation of the sum of the square of weights per bin
# REF: https://root.cern.ch/doc/master/classTH1.html#associated-errors
h_muon_pt_2_MC.Sumw2()


h_muon_pt_1_Data = ROOT.TH1F(
    "h_muon_pt_1_Data", "; Muon pT ; Muons", 50, 0, 200)
# force the storage and computation of the sum of the square of weights per bin
# REF: https://root.cern.ch/doc/master/classTH1.html#associated-errors
h_muon_pt_1_Data.Sumw2()

h_muon_pt_2_Data = ROOT.TH1F(
    "h_muon_pt_2_Data", "; Muon pT ; Muons", 50, 0, 200)
# force the storage and computation of the sum of the square of weights per bin
# REF: https://root.cern.ch/doc/master/classTH1.html#associated-errors
h_muon_pt_2_Data.Sumw2()

# total number of events in the file
n_events_data = data_chain.GetEntries()  # (REAL CMS DATA)
n_events_mc = mc_chain.GetEntries()

# Set the number of events for percentage calc
n_events_data_for_tqdm = n_events_data
if max_events >= 0:
    n_events_data_for_tqdm = max_events

# a correction factor applied in orther to not overflow the event list when running over all events
n_events_mc_for_tqdm = int(n_events_mc*0.8/3.)
if max_events >= 0:
    n_events_mc_for_tqdm = max_events


# calculating weight of MC data
# x-sec REF:
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat13TeV
# https://pdglive.lbl.gov/Particle.action?node=S043&init=0

Z_crosssection = 57094.5  # in pb
# this is the mean value of Branching Ratio to muon+nu and electron+nu
br_W_to_leptons = 0.0337
luminosity = 1  # in fb^-1
W_mc = (Z_crosssection*br_W_to_leptons*luminosity)/n_events_mc_for_tqdm

# weight for CMS data
W = 1

# print "--> Weights:"
# print "----> MC: " + str(W_mc)
# print "----> Data: " + str(W)


# loop over events and fill histograms
counter_data = 0

print("Processing CMS Data events...")

# Loop over Data events
for ievt, evt in tqdm.tqdm(enumerate(data_chain), desc="Events"):  # (REAL CMS DATA)
    if ievt+1 > max_events and max_events > 0:
        break
    if evt.nMuon >= 1:
        # loop over muons
        for i_muon in range(evt.nMuon):
            if i_muon == 0:
                h_muon_pt_1_Data.Fill(evt.Muon_pt[i_muon], W)
            if i_muon == 1:
                h_muon_pt_2_Data.Fill(evt.Muon_pt[i_muon], W)

    counter_data += W

print("-->> Event counts - DATA")
print("Total number of processed events: " + str(counter_data))


counter_mc = 0

print("Processing CMS MC events...")

# Loop over Data events
for ievt, evt in tqdm.tqdm(enumerate(mc_chain), desc="Events"):  # (SIMULATED CMS DATA)
    if ievt+1 > max_events and max_events > 0:
        break
    if evt.nMuon >= 1:
        # loop over muons
        for i_muon in range(evt.nMuon):
            if i_muon == 0:
                h_muon_pt_1_MC.Fill(evt.Muon_pt[i_muon], W)
            if i_muon == 1:
                h_muon_pt_2_MC.Fill(evt.Muon_pt[i_muon], W)

    counter_mc += W

print("-->> Event counts - MC")
print("Total number of processed events: " + str(counter_mc))


# Save histogram to a file
# Open a ROOT file and save the formula, function and histogram
output_file = ROOT.TFile('output_files/output_file.root', 'RECREATE')

h_muon_pt_1_MC.Print("all")
# Write histograms to file
h_muon_pt_1_Data.Write()
h_muon_pt_2_Data.Write()
h_muon_pt_1_MC.Write()
h_muon_pt_2_MC.Write()


# Close file
output_file.Close()

print("\nOutput histograms have been saved output_file.root")
