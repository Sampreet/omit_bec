# Pump-probe Cavity Optomechanics with a Rotating Atomic Superfluid in a Ring

[![Manuscript Version](https://img.shields.io/badge/version-3.5-red?style=for-the-badge)](https://doi.org/10.1103/PhysRevA.107.013525)
[![Toolbox Version](https://img.shields.io/badge/PhysRevA-107.013525-teal)]
[![Last Updated](https://img.shields.io/github/last-commit/sampreet/omit_bec?style=for-the-badge)](https://github.com/sampreet/omit_bec/blob/master/CHANGELOG.md)

> Phys. Rev. A 107, 013525 (2023)

Author | Affiliation
------------ | -------------
[Sampreet Kalita](https://www.iitg.ac.in/stud/sampreet/) | Department of Physics, Indian Institute of Technology Guwahati, Assam 781039, India
[Pardeep Kumar](https://scholar.google.com/citations?user=CFIPlp8AAAAJ) | Max Planck Institute for the Science of Light, Staatsstraße 2, 91058 Erlangen, Germany
[Rina Kanamoto](https://www.isc.meiji.ac.jp/~kanamoto/rinakanamoto_en.html) | Department of Physics, Meiji University, Kawasaki, Kanagawa 214-8571, Japan
[Mishkatul Bhattacharya](https://scholar.google.com/citations?user=5gCcMuMAAAAJ) | School of Physics and Astronomy, Rochester Institute of Technology, 84 Lomb Memorial Drive, Rochester, New York 14623, USA
[Amarendra Kumar Sarma](https://www.iitg.ac.in/aksarma/) | Department of Physics, Indian Institute of Technology Guwahati, Assam 781039, India

Contributing Part | SK | PK
------------ | ------------ | -------------
Literature review | 40% | 60%
Idea and formulation | 40% | 60%
Derivations of expressions | 70% | 30%
Parameter sweeping | 70% | 30%
Illustrations and plots | 60% | 40%
Results and discussion | 50% | 50%
Manuscript preparation | 60% | 40%

## About the Work

Atomic superfluids confined in a ring provide a remarkable paradigm for quantized circulation.
Very recently, a technique based on cavity optomechanics has been proposed [Kumar et al., Phys. Rev. Lett. 127, 113601 (2021)] for sensing and manipulating the rotation of a bosonic ring condensate with minimal destruction, in situ and in real time.
Here, we theoretically investigate other coherent interference effects that can be supported by the proposed configuration.
Specifically, in the presence of a strong control beam, we analyze the influence of atomic rotation on the transmission spectrum of a weak probe laser through a cavity containing a ring condensate.
We present a detailed study of the resulting narrow probe transmission profiles and group delay and show that they can be tuned by means of persistent currents.
Our results explore a facet of rotating matter waves and are relevant to applications such as atomtronics, sensing, and information processing.

## Notebooks

* [Approximated expressions for the Routh-Hurwitz Criteria for the Analysis of Stability of a BEC-OM System with a weak probe laser and a strong control laser containing OAM (BEC_10)](notebooks/bec_10_dynamical_stability_approx.ipynb)
* [Routh-Hurwitz Criteria for the Analysis of Stability of a BEC-OM System with a weak probe laser and a strong control laser containing OAM (BEC_10)](notebooks/bec_10_dynamical_stability.ipynb)
* [Calculation of Four-wave-mixing for a BEC-OM Model with a weak probe laser and a strong control laser containing OAM (BEC_10)](notebooks/bec_10_four_wave_mixing.ipynb)
* [Calculation of Optomechanically-induced Transparency for a BEC-OM Model with a weak probe laser and a strong control laser containing OAM (BEC_10)](notebooks/bec_10_induced_transparency.ipynb)
* [Approximated Expression for Transmission for a BEC-OM Model with a weak probe laser and a strong control laser containing OAM (BEC_10)](notebooks/bec_10_transmission_approx.ipynb)
* [Plots in the Latest Version of the Manuscript](notebooks/v3.5_qom-v1.0.1/plots.ipynb)

## Structure of the Repository

```
ROOT_DIR/
|
├───notebooks/
│   ├───bar/
│   │   ├───baz.ipynb
│   │   └───...
│   │
│   ├───foo_baz.ipynb
│   └───...
|
│───scripts/
│   ├───bar/
│   │   ├───baz.py
│   │   └───...
│   └───...
|
├───systems/
│   ├───__init__.py
│   ├───Foo.py
│   └───...
│
├───.gitignore
├───CHANGELOG.md
└───README.md
```

Here, `foo` represents the module or class and `bar` represents the version.

## Installing Dependencies

All numerical data and plots are obtained using the [Quantum Optomechanics Toolbox](https://github.com/sampreet/qom), an open-source Python framework to simulate optomechanical systems.
Refer to the [QOM toolbox documentation](https://sampreet.github.io/qom-docs/v1.0.1) for the steps to install this libary.

## Running the Scripts

To run the scripts, navigate *inside* the top-level directory, and execute:

```bash
python scripts/bar/baz.py
```

Here, `bar` is the name of the folder (containing the version information) inside `scripts` and `baz.py` is the name of the script (refer to the repository structure).