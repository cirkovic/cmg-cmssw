import ROOT

#ROOT.gSystem.Load("libCMGToolsTTHAnalysis")
SignedImpactParameterComputer = ROOT.SignedImpactParameter()

def signedSip3D(lepton, vertex=None):
    if vertex is None:
        vertex = lepton.associatedVertex
    dir   = lepton.jet.momentum()         if hasattr(lepton,'jet')      else lepton.momentum()
    track = lepton.gsfTrack() if abs(lepton.pdgId()) == 11  else lepton.track()
    meas = SignedImpactParameterComputer.signedIP3D(track.get(), vertex, dir)
    return meas.significance()


def signedIp3D(lepton, vertex=None):
    if vertex is None:
        vertex = lepton.associatedVertex
    dir   = lepton.jet.momentum()         if hasattr(lepton,'jet')      else lepton.momentum()
    track = lepton.gsfTrack() if abs(lepton.pdgId()) == 11  else lepton.track()
    meas = SignedImpactParameterComputer.signedIP3D(track.get(), vertex, dir)
    return meas.value()

def twoTrackChi2(lepton1,lepton2):
    track1 = lepton1.gsfTrack() if abs(lepton1.pdgId()) == 11  else lepton1.track()
    track2 = lepton2.gsfTrack() if abs(lepton2.pdgId()) == 11  else lepton2.track()
    pair = SignedImpactParameterComputer.twoTrackChi2(track1.get(),track2.get())
    return (pair.first,pair.second)
