#!/usr/bin/python

import numpy as np
from lib.BinaryClassifier import BinaryClassifier


class McBinaryClassifier(BinaryClassifier):
    def __init__(self, Features, Labels, TestFeatures, TestLabels, Iteration):
        super(McBinaryClassifier, self).__init__(Features, Labels, TestFeatures, TestLabels, Iteration)
        self.Fxy = {}

    def InitWV (self):
        ClsNum = max (self.Classes) + 1
        W = np.array([0] * len(self.Features[0]) * ClsNum)
        return W

    def BinaryClass(self, Labels):
        return Labels

    def Predict (self, x):
        self.Fxy = {}
    
        ClsNum = max (self.Classes) + 1
        FNum   = len(self.Features[0])  
        
        ArgMax = 0
        MaxCls = 0
        for C in self.Classes:
            FVector = [0] * FNum * ClsNum
            FVector[C * FNum: (C * FNum + FNum)] = x
            
            self.Fxy[C] = np.array(FVector)
            
            Arg = np.dot(self.W, np.array(FVector))
            if Arg > ArgMax:
                ArgMax = Arg
                MaxCls = C
        return MaxCls
          
    def UpdateWeight (self, x, y, Pred):
        print ("UpdateWeight...")

                    
        



    
