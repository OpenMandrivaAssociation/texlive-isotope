%global tl_name isotope
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	A package for typesetting isotopes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/isotope
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/isotope.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/isotope.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/isotope.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a command \isotope for setting the atomic weight
and atomic number indications of isotopes. (The naive way of doing the
job with (La)TeX mathematics commands produces an unsatisfactory
result.)

