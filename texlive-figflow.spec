# revision 21462
# category Package
# catalog-ctan /macros/plain/contrib/figflow
# catalog-date 2011-02-18 10:42:52 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-figflow
Version:	20170414
Release:	1
Summary:	Flow text around a figure
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/figflow
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/figflow.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/figflow.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides a Plain TeX macro \figflow that allows one to insert a
figure into an area inset into a paragraph. Command arguments
are width and height of the figure, and the figure (and its
caption) itself. Usage details are to be found in the TeX file
itself. The package does not work with LaTeX; packages such as
wrapfig, floatflt and picins support the needs of LaTeX users
in this area.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/figflow/figflow.tex
%doc %{_texmfdistdir}/doc/plain/figflow/README.figflow

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110218-2
+ Revision: 751838
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110218-1
+ Revision: 718435
- texlive-figflow
- texlive-figflow
- texlive-figflow
- texlive-figflow

