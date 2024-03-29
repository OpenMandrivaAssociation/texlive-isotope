Name:		texlive-isotope
Version:	23711
Release:	2
Summary:	A package for typesetting isotopes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/isotope
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isotope.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isotope.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isotope.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a command \isotope for setting the atomic
weight and atomic number indications of isotopes. (The naive
way of doing the job with (La)TeX mathematics commands produces
an unsatisfactory result.).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/isotope/isotope.sty
%doc %{_texmfdistdir}/doc/latex/isotope/README
#- source
%doc %{_texmfdistdir}/source/latex/isotope/isotope.dtx
%doc %{_texmfdistdir}/source/latex/isotope/isotope.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
