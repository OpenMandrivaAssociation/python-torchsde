Name:		python-torchsde
Version:	0.2.6
Release:	1
Summary:	SDE solvers and stochastic adjoints in PyTorch
License:	Apache-2.0
Group:		Development/Python
URL:		https://github.com/google-research/torchsde
Source0:	https://files.pythonhosted.org/packages/source/t/torchsde/torchsde-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
Requires:	python%{pyver}dist(trampoline)

%description
Stochastic differential equation solvers for PyTorch. ComfyUI uses
this for k-diffusion SDE samplers.

%files
%doc README.md
%license LICENSE
%{py_sitedir}/torchsde
%{py_sitedir}/torchsde-*.*-info
