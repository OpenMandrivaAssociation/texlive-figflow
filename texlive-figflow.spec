%global tl_name figflow
%global tl_revision 21462

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Flow text around a figure
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/contrib/figflow
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/figflow.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/figflow.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides a Plain TeX macro \figflow that allows one to insert a figure
into an area inset into a paragraph. Command arguments are width and
height of the figure, and the figure (and its caption) itself. Usage
details are to be found in the TeX file itself. The package does not
work with LaTeX; packages such as wrapfig, floatflt and picins support
the needs of LaTeX users in this area.

