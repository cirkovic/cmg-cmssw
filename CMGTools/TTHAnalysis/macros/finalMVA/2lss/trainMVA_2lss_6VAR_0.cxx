void trainMVA_2lss(TString name) {
    TString Path = "/afs/cern.ch/work/c/cirkovic/TREES_53X_170714"";
    //gROOT->ProcessLine(".L ../../../python/plotter/functions.cc+");

    TFile *fOut = new TFile(name+".root","RECREATE");
    TMVA::Factory *factory = new TMVA::Factory(name, fOut, "!V:!Color");

    TFile *fSig = TFile::Open(Path+"/TTH/treeProducerSusyMultilepton/treeProducerSusyMultilepton_tree.root");
    TTree *tSig = (TTree *) fSig->Get("treeProducerSusyMultilepton");
    //tSig->AddFriend("sf/t", Path+"/2_finalmva_2lss_v2/evVarFriend_TTH122.root");
    factory->AddSignalTree(tSig, 1.0);
    //fSig = TFile::Open(Path+"/TTH127/ttHLepTreeProducerBase/ttHLepTreeProducerBase_tree.root");
    //tSig = (TTree *) fSig->Get("ttHLepTreeProducerBase");
    //tSig->AddFriend("sf/t", Path+"/2_finalmva_2lss_v2/evVarFriend_TTH127.root");
    //factory->AddSignalTree(tSig, 1.0);
    //fSig = TFile::Open(Path+"/TTH/ttHLepTreeProducerBase/ttHLepTreeProducerBase_tree.root");
    //tSig = (TTree *) fSig->Get("ttHLepTreeProducerBase");
    //factory->AddSignalTree(tSig, 1.0);

    TCut all = "nLepGood == 2 && LepGood1_charge == LepGood2_charge && nBJetMedium25 >= 1 && nJet25 >= 4 && LepGood2_pt > 20 && LepGood1_pt+LepGood2_pt+met > 100";
    if (name.Contains("ttW")) {
        TFile *fBkg = TFile::Open(Path+"/TTWJets/treeProducerSusyMultilepton/treeProducerSusyMultilepton_tree.root");
        TTree *tBkg = (TTree *) fBkg->Get("treeProducerSusyMultilepton");
        //tBkg->AddFriend("sf/t", "/afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/23-08-2014/3/1/evVarFriend_TTJetsSem.root");
        factory->AddBackgroundTree(tBkg, 1.0);
    } else if (name.Contains("ttbar")) {
        TFile *fBkg = TFile::Open(Path+"/TTJetsSem/treeProducerSusyMultilepton/treeProducerSusyMultilepton_tree.root");
        TTree *tBkg = (TTree *) fBkg->Get("treeProducerSusyMultilepton");
        //tBkg->AddFriend("sf/t", "/afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/23-08-2014/3/1/evVarFriend_TTJetsSem.root");
        factory->AddBackgroundTree(tBkg, 1.0);
        //fBkg = TFile::Open(Path+"/TTJets/ttHLepTreeProducerBase/ttHLepTreeProducerBase_tree.root");
        //tBkg = (TTree *) fBkg->Get("ttHLepTreeProducerBase");
        //factory->AddBackgroundTree(tBkg, 0.2);
    } else if (name.Contains("mix")) {
        TFile *fBkg1 = TFile::Open(Path+"/TTJetsSem/treeProducerSusyMultilepton/treeProducerSusyMultilepton_tree.root");
        TTree *tBkg1 = (TTree *) fBkg1->Get("treeProducerSusyMultilepton");
        factory->AddBackgroundTree(tBkg1, 1.0);
        TFile *fBkg2 = TFile::Open(Path+"/TTWJets/treeProducerSusyMultilepton/treeProducerSusyMultilepton_tree.root");
        TTree *tBkg2 = (TTree *) fBkg2->Get("treeProducerSusyMultilepton");
        factory->AddBackgroundTree(tBkg2, 1.0);
    } else  {
        std::cout << "Training not implemented " << std::endl;
        return;
    }

    if (name.Contains("_mm")) {
        all += "abs(LepGood1_pdgId) == 13 && abs(LepGood2_pdgId) == 13";
    } else if (name.Contains("_em")) {
        all += "abs(LepGood1_pdgId) != abs(LepGood2_pdgId)";
    } else if (name.Contains("_ee")) {
        all += "abs(LepGood1_pdgId) == 11 && abs(LepGood2_pdgId) == 11";
    }

    factory->AddVariable("abs(LepGood2_eta) := abs(LepGood2_eta)", 'F');
    factory->AddVariable("LepGood2_pt := LepGood2_pt", 'F');
    factory->AddVariable("mhtJet25 := mhtJet25", 'F');
    factory->AddVariable("mindr_lep2_jet := mindr_lep2_jet", 'F');
    factory->AddVariable("MT_met_lep1 := MT_met_lep1", 'F');
    factory->AddVariable("htJet25 := htJet25", 'F');
    
#endif

    factory->SetWeightExpression("1");
    factory->PrepareTrainingAndTestTree( all, all, "SplitMode=Random" );

    factory->BookMethod( TMVA::Types::kLD, "LD", "!H:!V:VarTransform=None:CreateMVAPdfs" );

    TString BDTGopt = "!H:!V:NTrees=200:BoostType=Grad:Shrinkage=0.10:!UseBaggedGrad:nCuts=200:nEventsMin=100:NNodesMax=5";

    BDTGopt += ":CreateMVAPdfs"; // Create Rarity distribution
    factory->BookMethod( TMVA::Types::kBDT, "BDTG", BDTGopt);

    factory->TrainAllMethods();
    factory->TestAllMethods();
    factory->EvaluateAllMethods();

    fOut->Close();
}
