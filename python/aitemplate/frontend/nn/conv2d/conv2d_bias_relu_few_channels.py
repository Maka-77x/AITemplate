#  Copyright (c) Meta Platforms, Inc. and affiliates.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
"""
conv2d bias relu for few channels
"""

from aitemplate.frontend.nn.conv2d.special_conv2d_bias_act import SpecialConv2dBiasAct


class Conv2dBiasReluFewChannels(SpecialConv2dBiasAct):
    r"""Applies 2D convolution with bias + relu for few channels.

    This layer equals to Conv2dBiasRelu but has improved performance for in_channels < 8.
    """

    def __init__(
        self,
        in_channels,
        out_channels,
        kernel_size,
        stride,
        padding=0,
        dilation=1,
        auto_padding=True,
        dtype="float16",
    ):
        super().__init__(
            "conv2d_bias_relu_few_channels",
            in_channels,
            out_channels,
            kernel_size,
            stride,
            padding,
            dilation,
            auto_padding,
            dtype,
        )
