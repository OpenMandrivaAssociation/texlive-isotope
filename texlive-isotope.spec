# revision 23711
# category Package
# catalog-ctan /macros/latex/contrib/isotope
# catalog-date 2011-08-26 17:57:53 +0200
# catalog-license lppl
# catalog-version v0.3
Name:		texlive-isotope
Version:	v0.3
Release:	7
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> v0.3-2
+ Revision: 752846
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> v0.3-1
+ Revision: 718741
- texlive-isotope
- texlive-isotope
- texlive-isotope
- texlive-isotope

