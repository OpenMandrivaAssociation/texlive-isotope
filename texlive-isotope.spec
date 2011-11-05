# revision 23711
# category Package
# catalog-ctan /macros/latex/contrib/isotope
# catalog-date 2011-08-26 17:57:53 +0200
# catalog-license lppl
# catalog-version v0.3
Name:		texlive-isotope
Version:	v0.3
Release:	1
Summary:	A package for typesetting isotopes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/isotope
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isotope.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isotope.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isotope.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides a command \isotope for setting the atomic
weight and atomic number indications of isotopes. (The naive
way of doing the job with (La)TeX mathematics commands produces
an unsatisfactory result.).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/isotope/isotope.sty
%doc %{_texmfdistdir}/doc/latex/isotope/README
#- source
%doc %{_texmfdistdir}/source/latex/isotope/isotope.dtx
%doc %{_texmfdistdir}/source/latex/isotope/isotope.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
