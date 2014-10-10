void trainMVA_2lss(TString name) {
    TString Path = "/afs/cern.ch/work/c/cirkovic/Milos_02-10-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/cfg/TREES";
    //gROOT->ProcessLine(".L ../../../python/plotter/functions.cc+");

    TFile *fOut = new TFile(name+".root","RECREATE");
    TMVA::Factory *factory = new TMVA::Factory(name, fOut, "!V:!Color");

    TFile *fSig = TFile::Open(Path+"/TTHnlo_S14/treeProducerSusyMultilepton/treeProducerSusyMultilepton_tree.root");
    TTree *tSig = (TTree *) fSig->Get("treeProducerSusyMultilepton");
    tSig->AddFriend("sf/t", "/afs/cern.ch/work/c/cirkovic/Milos_08-10-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/macros/OUTPUT_081014_203308/evVarFriend_TTHnlo_S14.root");
    factory->AddSignalTree(tSig, 1.0);
    //fSig = TFile::Open(Path+"/TTH127/treeProducerSusyMultilepton/treeProducerSusyMultilepton_tree.root");
    //tSig = (TTree *) fSig->Get("treeProducerSusyMultilepton");
    //tSig->AddFriend("sf/t", Path+"/2_finalmva_2lss_v2/evVarFriend_TTH127.root");
    //factory->AddSignalTree(tSig, 1.0);
    //fSig = TFile::Open(Path+"/TTH/treeProducerSusyMultilepton/treeProducerSusyMultilepton_tree.root");
    //tSig = (TTree *) fSig->Get("treeProducerSusyMultilepton");
    //factory->AddSignalTree(tSig, 1.0);

    TCut all = "nLepGood == 2 && LepGood_charge[0] == LepGood_charge[1] && nBJetMedium25 >= 1 && nJet25 >= 4 && LepGood_pt[1] > 20 && LepGood_pt[0]+LepGood_pt[1]+met_pt > 100";
    if (name.Contains("ttW")) {
        TFile *fBkg = TFile::Open(Path+"/TTWJets/treeProducerSusyMultilepton/treeProducerSusyMultilepton_tree.root");
        TTree *tBkg = (TTree *) fBkg->Get("treeProducerSusyMultilepton");
        factory->AddBackgroundTree(tBkg, 1.0);
    } else if (name.Contains("ttbar")) {
        TFile *fBkg = TFile::Open(Path+"/TTJets_PUS14/treeProducerSusyMultilepton/treeProducerSusyMultilepton_tree.root");
        TTree *tBkg = (TTree *) fBkg->Get("treeProducerSusyMultilepton");
        tBkg->AddFriend("sf/t", "/afs/cern.ch/work/c/cirkovic/Milos_08-10-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/macros/OUTPUT_081014_203308/evVarFriend_TTJets_PUS14.root");
        factory->AddBackgroundTree(tBkg, 1.0);
        //fBkg = TFile::Open(Path+"/TTJets/treeProducerSusyMultilepton/treeProducerSusyMultilepton_tree.root");
        //tBkg = (TTree *) fBkg->Get("treeProducerSusyMultilepton");
        //factory->AddBackgroundTree(tBkg, 0.2);
    } else if (name.Contains("mix")) {
        TFile *fBkg1 = TFile::Open(Path+"/TTJets/treeProducerSusyMultilepton/treeProducerSusyMultilepton_tree.root");
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
        all += "abs(LepGood_pdgId[0]) == 13 && abs(LepGood_pdgId[1]) == 13";
    } else if (name.Contains("_em")) {
        all += "abs(LepGood_pdgId[0]) != abs(LepGood_pdgId[1])";
    } else if (name.Contains("_ee")) {
        all += "abs(LepGood_pdgId[0]) == 11 && abs(LepGood_pdgId[1]) == 11";
    }
/*
    //factory->AddSpectator("MVA_2LSS_4j_6var", 'F');

    // Dileptons
    //factory->AddVariable("lep2Pt := min(LepGood_pt[1], 200)", 'F');
    //factory->AddVariable("htll := min(LepGood_pt[0]+LepGood_pt[1], 400)", 'F');
    //factory->AddVariable("ptll := min(pt2l, 240)", 'F');
    //factory->AddVariable("mll := min(mass_2(LepGood_pt[0],LepGood_eta[0],LepGood_phi[0],LepGood_mass[0], LepGood_pt[1],LepGood_eta[1],LepGood_phi[1],LepGood_mass[1]), 240)", 'F');
    //factory->AddVariable("drll := min(deltaR(LepGood_eta[0],LepGood_phi[0], LepGood_eta[1],LepGood_phi[1]), 5)", 'F');

    // MET
    factory->AddVariable("mhtJet25 := min(mhtJet25, 300)", 'F');
    //factory->AddVariable("met_pt := min(met_pt, 300)", 'F');

    // Jets and HT
    factory->AddVariable("jet1Pt := min(Jet_pt[0], 300)", 'F');
    factory->AddVariable("jet2Pt := min(Jet_pt[1], 300)", 'F');
    //factory->AddVariable("jetptmin := min(Jet_pt[0],Jet_pt[1])", 'F');
    factory->AddVariable("htJet25 := min(htJet25, 1000)", 'F');

    // Centrality variables
    //factory->AddVariable("lepEta2max := max(abs(LepGood_eta[0]),abs(LepGood_eta[1]))", 'F');
    //factory->AddVariable("lepEta2min := min(abs(LepGood_eta[0]),abs(LepGood_eta[1]))", 'F');
    //factory->AddVariable("ptavgEta   := (abs(Jet_eta[0])*Jeo1_pt+abs(Jet_eta[1])*Jet_pt[1]+abs(LepGood_eta[0])*LepGood_pt[0]+abs(LepGood_eta[1])*LepGood_pt[1])/(Jet_pt[0]+Jet_pt[1]+LepGood_pt[0]+LepGood_pt[1])", 'F');

    //factory->AddVariable("ptavgEtaJets := (abs(Jet_eta[0])*Jet_pt[0]+abs(Jet_eta[1])*Jet_pt[1])/(Jet_pt[0]+Jet_pt[1])", 'F');

    factory->AddVariable("htJet25ratio1224Lep := (LepGood_pt[0]*(abs(LepGood_eta[0])<1.2) + LepGood_pt[1]*(abs(LepGood_eta[1])<1.2) + Jet_pt[0]*(abs(Jet_eta[0]) < 1.2) + Jet_pt[1]*(abs(Jet_eta[1]) < 1.2) + Jet_pt[2]*(abs(Jet_eta[2]) < 1.2) + Jet_pt[3]*(abs(Jet_eta[3]) < 1.2) + Jet_pt[4]*(abs(Jet_eta[4]) < 1.2) + Jet_pt[5]*(abs(Jet_eta[5]) < 1.2) + Jet_pt[6]*(abs(Jet_eta[6]) < 1.2) + Jet_pt[7]*(abs(Jet_eta[7]) < 1.2))/ (LepGood_pt[0] + LepGood_pt[1] + Jet_pt[0]*(abs(Jet_eta[0]) < 2.4) + Jet_pt[1]*(abs(Jet_eta[1]) < 2.4) + Jet_pt[2]*(abs(Jet_eta[2]) < 2.4) + Jet_pt[3]*(abs(Jet_eta[3]) < 2.4) + Jet_pt[4]*(abs(Jet_eta[4]) < 2.4) + Jet_pt[5]*(abs(Jet_eta[5]) < 2.4) + Jet_pt[6]*(abs(Jet_eta[6]) < 2.4) + Jet_pt[7]*(abs(Jet_eta[7]) < 2.4))", 'F');

  
    // Event reconstruction   
    //factory->AddVariable("bestMTopHad   := min(max(bestMTopHad,100),350)", 'F');
    factory->AddVariable("bestMTopHadPt := min(max(bestMTopHadPt,0),400)", 'F');
    //factory->AddVariable("mtW1 := mt_2(LepGood_pt[0],LepGood_phi[0],met_pt,met_phi)", 'F');
    
*/
    //factory->AddVariable("lep2AbsEta := min(abs(LepGood_eta[0]),abs(LepGood_eta[1]))", 'F');
    factory->AddVariable("lep2AbsEta := abs(LepGood_eta[1])", 'F');
    factory->AddVariable("lep2Pt := LepGood_pt[1]", 'F');
    factory->AddVariable("MHT := mhtJet25", 'F');
    factory->AddVariable("mindr_lep2_jet := mindr_lep2_jet", 'F');
    factory->AddVariable("MT_met_lep1 := MT_met_lep1", 'F');
    factory->AddVariable("sum_pt := htJet25", 'F');
    factory->AddVariable("avg_dr_jets := avg_dr_jet", 'F');
    factory->AddVariable("mindr_lep1_jet := mindr_lep1_jet", 'F');
    factory->AddVariable("MT_met_leplep := MT_met_leplep", 'F');
    factory->AddVariable("numJets_float := nJet25", 'F');
    factory->AddVariable("b1_jet_pt := (Jet_pt[0])if(nJet>=1)else(-1)", 'F');
    factory->AddVariable("b2_jet_pt := (Jet_pt[1])if(nJet>=2)else(-1)", 'F');
    factory->AddVariable("lep1Pt := LepGood_pt[0]", 'F');
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
