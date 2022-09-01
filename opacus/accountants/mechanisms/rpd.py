# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import abc
from collections import OrderedDict
from copy import deepcopy
from typing import Any, Callable, Mapping, TypeVar
from analysis import _log_add
from mechanism import Mechanism
import numpy as np

class GaussianMechanism(Mechanism):
    def __init__(self,sigma):
        """
        sigma : std of gaussian noise normalized by L2 sensitivity
        """
        self.sigma = sigma

    @classmethod
    def name(self) -> str:
        return("Gaussian Mechanism")

    def compute_rdp(self, alpha : float) -> float:
        return alpha / (2*self.sigma**2)

class LaplaceMechanism(Mechanism):
    def __init__(self,l_param):
        """
        # Assumes that the function has L2 sensitivity = 1
        l_param (lambda) :
        """
        self.l_param = l_param

    @classmethod
    def name(self) -> str:
        return("Laplace Mechanism")

    def compute_rdp(self, alpha : float) -> float:
        if alpha >= 1:
            #_log_add(x,y) does log(exp(x) + exp(y))
            return (1/(alpha-1)) * _log_add(
                ((alpha-1)/self.l_param) + np.log((alpha)/(2*alpha -1)),
                ((-alpha)/self.l_param)  + np.log((alpha -1)/(2*alpha -1))
                )
        else:
           raise(ValueError, "attempting to compute RDP for alpha <1")
