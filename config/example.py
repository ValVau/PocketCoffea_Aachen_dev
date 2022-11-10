from pocket_coffea.lib.cuts import dilepton, SR, CR_top
from pocket_coffea.workflows.base import ttHbbBaseProcessor

cfg =  {

    "dataset" : {
        "jsons": ["datasets/RunIISummer20UL18_local.json"],
        "filter" : {
            "samples": ["ttHTobb"],
            "samples_exclude" : [],
            "year": ["2018"]
        }
    },

    # Input and output files
    "workflow" : ttHbbBaseProcessor,
    "output"   : "output/example",

    # Executor parameters
    "run_options" : {
        "executor"       : "futures",
        "workers"        : 12,
        "scaleout"       : 10,
        "partition"      : "standard",
        "walltime"       : "12:00:00",
        "mem_per_worker" : None, # GB
        "exclusive"      : True,
        "chunk"          : 50000,
        "max"            : None,
        "skipbadfiles"   : None,
        "voms"           : None
        "limit"          : 2,
     },

    # Cuts and plots settings
    "finalstate" : "dilepton",

    "cuts_definition" : {

       "baseline" : {
            "f" : dilepton,
            "tag": "dilepton_1"
       },
       "SR" : {
            "f" : SR,
            "tag": "SR_5"
       },
       "CR" : {
            "f" : CR_top,
            "tag": "CR_base"
       },

       "CRbb" : {
            "f" : CR_top,
            "tag": "CR_bb"
       },

    },

    "categories": {
        "SR" :  {"trigger","baseline",  "SR"},
        "CR1" : {"trigger", "CR"}, 
        "CR2" : {"trigger", "CRbb"},
    },

    "variables" : {
        "muon_pt" : {'binning' : {'n_or_arr' : 200, 'lo' : 0, 'hi' : 2000}, 'xlim' : (0,500),  'xlabel' : "$p_{T}^{\mu}$ [GeV]"},
        "muon_eta" : None,
        "muon_phi" : None,
        "electron_pt" : None,
        "electron_eta" : None,
        "electron_phi" : None,
        "jet_pt" : None,
        "jet_eta" : None,
        "jet_phi" : None,
        "nmuon" : None,
        "nelectron" : None,
        "nlep" : None,
        "nmuongood" : None,
        "nelectrongood" : None,
        "nlepgood" : None,
        "njet" : None,
        "nbjet" : None,
    },
    "variables2d" : {},
    "scale" : "log"
}
