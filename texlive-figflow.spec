Name:		texlive-figflow
Version:	20110218
Release:	1
Summary:	Flow text around a figure
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/figflow
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/figflow.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/figflow.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
Provides a Plain TeX macro \figflow that allows one to insert a
figure into an area inset into a paragraph. Command arguments
are width and height of the figure, and the figure (and its
caption) itself. Usage details are to be found in the TeX file
itself. The package does not work with LaTeX; packages such as
wrapfig, floatflt and picins support the needs of LaTeX users
in this area.

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
%{_texmfdistdir}/tex/plain/figflow/figflow.tex
%doc %{_texmfdistdir}/doc/plain/figflow/README.figflow

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
