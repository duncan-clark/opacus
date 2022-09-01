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

class Mechanism(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        pass

    @classmethod
    @abc.abstractmethod
    def name(cls) -> str:
        """
        Accounting mechanism name
        """
        pass

    @abc.abstractmethod
    def compute_rdp(self, alpha : float) -> float:
        """
        Function to compute unsubsampled rdp for this mechanism for a given alpha
        """
        pass
