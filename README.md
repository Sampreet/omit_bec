# Cavity Detection of Persistent Current Chirality using Control-Probe Optomechanics

[![Version](https://img.shields.io/badge/version-1.1-red?style=for-the-badge)](#)

> A collection of all data and scripts for the work.

Author | Affiliation
------------ | -------------
[Sampreet Kalita](https://www.iitg.ac.in/stud/sampreet/) | Department of Physics, Indian Institute of Technology Guwahati, Assam 781039, India
[Pardeep Kumar](https://scholar.google.com/citations?user=CFIPlp8AAAAJ) | Max Planck Institute for the Science of Light, Staatsstraße 2, 91058 Erlangen, Germany
[Mishkatul Bhattacharya](https://scholar.google.com/citations?user=5gCcMuMAAAAJ) | School of Physics and Astronomy, Rochester Institute of Technology, 84 Lomb Memorial Drive, Rochester, New York 14623, USA
[Amarendra Kumar Sarma](https://www.iitg.ac.in/aksarma/) | Department of Physics, Indian Institute of Technology Guwahati, Assam 781039, India

## Structure of the Repository

```
ROOT_DIR/
|
├───data/
│   ├───foo-bar/
│   │   ├───baz_xyz.npz
│   │   └───...
│   └───...
|
│───scripts/
│   ├───foo-bar/
│   │   ├───baz.py
│   │   └───...
│   └───...
│
├───.gitignore
├───CHANGELOG.md
└───README.md
```

## Execution

### Installing Dependencies

The project requires `Python 3.8+` installed via the [Anaconda distribution](https://www.anaconda.com/products/individual). 
An extensive guide to set up your python environment same can be found [here](https://sampreet.github.io/python-for-physicists/modules/m01-getting-started/m01t01-setting-up-python.html).

Once the installation is complete and `conda` is configured, it is preferable to create a new conda environment (say `qom`) and activate it using:

```bash
conda create -n qom python=3
conda activate qom
```

This project uses [The Quantum Optomechanics Toolbox](https://github.com/Sampreet/qom) via Python Package Index using `pip`:

```bash
pip install -i https://test.pypi.org/simple/ qom
```

Alternatively, [clone](https://github.com/Sampreet/qom) or [download](https://github.com/Sampreet/qom/archive/refs/heads/master.zip) as `.zip` and extract the contents:
Now, execute the following from *outside* the top-level directory, `ROOT_DIR`, inside which `setup.py` is located:

```bash
pip install -e ROOT_DIR
```

### Running the Scripts

Make sure that the top-level directory, `ROOT_DIR` is in the same location as the `bec-systems` repository.

To run the scripts, navigate *inside* the top-level directory, `ROOT_DIR`, and execute:

```bash
python scripts/foo-bar/baz.py
```

Here, `foo-bar` is the name of the folder and  `baz.py` is the name of the file.