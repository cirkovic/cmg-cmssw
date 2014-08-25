void trainMVA_2lss(TString name) {
    TString Path = "/afs/cern.ch/work/c/cirkovic/TREES_250513_HADD";
    //gROOT->ProcessLine(".L ../../../python/plotter/functions.cc+");

    TFile *fOut = new TFile(name+".root","RECREATE");
    TMVA::Factory *factory = new TMVA::Factory(name, fOut, "!V:!Color");

    TFile *fSig = TFile::Open(Path+"/TTH122/ttHLepTreeProducerBase/ttHLepTreeProducerBase_tree.root");
    TTree *tSig = (TTree *) fSig->Get("ttHLepTreeProducerBase");
    tSig->AddFriend("sf/t", Path+"/2_finalmva_2lss_v2/evVarFriend_TTH122.root");
    factory->AddSignalTree(tSig, 1.0);
    fSig = TFile::Open(Path+"/TTH127/ttHLepTreeProducerBase/ttHLepTreeProducerBase_tree.root");
    tSig = (TTree *) fSig->Get("ttHLepTreeProducerBase");
    tSig->AddFriend("sf/t", Path+"/2_finalmva_2lss_v2/evVarFriend_TTH127.root");
    factory->AddSignalTree(tSig, 1.0);
    //fSig = TFile::Open(Path+"/TTH/ttHLepTreeProducerBase/ttHLepTreeProducerBase_tree.root");
    //tSig = (TTree *) fSig->Get("ttHLepTreeProducerBase");
    //factory->AddSignalTree(tSig, 1.0);

    TCut all = "nLepGood == 2 && LepGood1_charge == LepGood2_charge && nBJetMedium25 >= 1 && nJet25 >= 4 && LepGood2_pt > 20 && LepGood1_pt+LepGood2_pt+met > 100";
    if (name.Contains("ttW")) {
        TFile *fBkg = TFile::Open(Path+"/TTWJets/ttHLepTreeProducerBase/ttHLepTreeProducerBase_tree.root");
        TTree *tBkg = (TTree *) fBkg->Get("ttHLepTreeProducerBase");
        tBkg->AddFriend("sf/t", Path+"/2_finalmva_2lss_v2/evVarFriend_TTWJets.root");
        factory->AddBackgroundTree(tBkg, 1.0);
    } else if (name.Contains("ttbar")) {
        TFile *fBkg = TFile::Open(Path+"/TTJets/ttHLepTreeProducerBase/ttHLepTreeProducerBase_tree.root");
        TTree *tBkg = (TTree *) fBkg->Get("ttHLepTreeProducerBase");
        tBkg->AddFriend("sf/t", Path+"/2_finalmva_2lss_v2/evVarFriend_TTJets.root");
        factory->AddBackgroundTree(tBkg, 1.0);
        //fBkg = TFile::Open(Path+"/TTJets/ttHLepTreeProducerBase/ttHLepTreeProducerBase_tree.root");
        //tBkg = (TTree *) fBkg->Get("ttHLepTreeProducerBase");
        //factory->AddBackgroundTree(tBkg, 0.2);
    } else if (name.Contains("mix")) {
        TFile *fBkg1 = TFile::Open(Path+"/TTJets/ttHLepTreeProducerBase/ttHLepTreeProducerBase_tree.root");
        TTree *tBkg1 = (TTree *) fBkg1->Get("ttHLepTreeProducerBase");
        tBkg1->AddFriend("sf/t", Path+"/2_finalmva_2lss_v2/evVarFriend_TTJets.root");
        factory->AddBackgroundTree(tBkg1, 1.0);
        TFile *fBkg2 = TFile::Open(Path+"/TTWJets/ttHLepTreeProducerBase/ttHLepTreeProducerBase_tree.root");
        TTree *tBkg2 = (TTree *) fBkg2->Get("ttHLepTreeProducerBase");
        tBkg2->AddFriend("sf/t", Path+"/2_finalmva_2lss_v2/evVarFriend_TTWJets.root");
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

    //factory->AddSpectator("MVA_2LSS_4j_6var", 'F');
    // _vars_1_6
    factory->AddVariable("lep2AbsEta := min(abs(LepGood1_eta),abs(LepGood2_eta))", 'F');
    factory->AddVariable("lep2AbsEta := abs(LepGood2_eta)", 'F');
    factory->AddVariable("lep2Pt := LepGood2_pt", 'F');
    factory->AddVariable("MHT := mhtJet25", 'F');
    factory->AddVariable("mindr_lep2_jet := mindr_lep2_jet", 'F');
    factory->AddVariable("MT_met_lep1 := MT_met_lep1", 'F');
    factory->AddVariable("sum_pt := htJet25", 'F');

    // _vars_7_9 
    factory->AddVariable("avg_dr_jets := avg_dr_jet", 'F');
    factory->AddVariable("mindr_lep1_jet := mindr_lep1_jet", 'F');
    factory->AddVariable("MT_met_leplep := MT_met_leplep", 'F');

    // _var_10
    factory->AddVariable("numJets_float := nJet25", 'F');

    // _vars_11_15
    factory->AddVariable("b1_jet_pt := Jet1_pt", 'F');
    factory->AddVariable("b2_jet_pt := Jet2_pt", 'F');
    factory->AddVariable("lep1Pt := LepGood1_pt", 'F');
    factory->AddVariable("sum_pt-(sum_pz-abs(pz_of_everything)) := htJet25 - (sum_abspz - abs(sum_sgnpz))", 'F');
    factory->AddVariable("sum_pt/sum_pz := htJet25/sum_abspz", 'F');
    
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
