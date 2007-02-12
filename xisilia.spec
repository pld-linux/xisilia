Summary:	Cisilia's GTK+ front-end
Summary(pl.UTF-8):   Interfejs GTK+ do Cisili
Name:		xisilia
Version:	1.0.1
Release:	0.1
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.cisiar.org/proyectos/cisilia/files/versiones/tar/%{name}-%{version}.tar.gz
# Source0-md5:	fe6f7f6eaccac21b6c8bfd0c3136cfae
URL:		http://www.cisiar.org/
BuildRequires:	gtk+-devel >= 1.2.2
Requires:	cisilia >= 0.7.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is cisilia's GTK+ 1.2 front-end used to set the starting
parameters and to analyze the password recovery task statistics.

%description -l pl.UTF-8
Interfejs graficzny do cisili umożliwiający ustawianie parametrów,
przeglądanie statystyk z "odtwarzania" haseł.

%prep
%setup -q

%build
%configure

%{__make} \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
