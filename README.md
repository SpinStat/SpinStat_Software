
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright (c) 2025 Benedikt Zinn -->

# Development

## Setting up the repository workspace
Create a workspace directory somewhere (for me ~/ZephyrWorkspace/).

In the workspace:
- Create a python environment ('python3 -m venv .venv').
- Start the python environment ('source .venv/bin/activate').
- Install the python west package ('pip install west').
- Clone the SpinStat_Software repository('git clone git@github...').

Inside the new SpinStat_Software folder:
- Initialize west ('west init --local').
- Update west ('west update').

## Installing the ZephyrSDK
Inside the zephyr folder of the workspace (e.g. ~/ZephyrWorkspace/zephyr/), run 'west sdk install'.

