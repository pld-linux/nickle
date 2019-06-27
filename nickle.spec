Summary:	Desk calculator language, similar to C
Summary(pl.UTF-8):	Język kalkulatora biurkowego podobny do C
Name:		nickle
Version:	2.84
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://nickle.org/release/%{name}-%{version}.tar.gz
# Source0-md5:	cf2a1e403698835a152e56b625857e07
URL:		http://nickle.org/
BuildRequires:	bison
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-style-dsssl
BuildRequires:	docbook-utils
BuildRequires:	flex
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	texlive-fonts-jknappen
# mathpazo/fplmr.tfm
BuildRequires:	texlive-fonts-other
BuildRequires:	texlive-jadetex
BuildRequires:	texlive-latex
# T2Acmr.fd
BuildRequires:	texlive-latex-cyrillic
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nickle is a programming language based prototyping environment with
powerful programming and scripting capabilities. Nickle supports a
variety of datatypes, especially arbitrary precision numbers. The
programming language vaguely resembles C. Some things in C which do
not translate easily are different, some design choices have been made
differently, and a very few features are simply missing.

Nickle provides the functionality of UNIX bc, dc and expr in
much-improved form. It is also an ideal environment for prototyping
complex algorithms. Nickle's scripting capabilities make it a nice
replacement for spreadsheets in some applications, and its numeric
features nicely complement the limited numeric functionality of
text-oriented languages such as AWK and PERL.

%description -l pl.UTF-8
Nickle to język programowania oparty na środowisku prototypowym z
potężnymi możliwościami programowania i skryptowania. Obsługuje wiele
różnych typów danych, w szczególności liczby dowolnej precyzji. Język
programowania w dużym stopniu przypomina C. Niektóre elementy w C,
które nie przekładają się bezpośrednio, są inne, część decyzji
projektowych się różni, brakuje bardzo nielicznych funkcji.

Nickle udostępnia funkcjonalność uniksowych poleceń bc, dc i expr w
bardzo udoskonalonej formie. Jest także idealnym środowiskiem do
tworzenia prototypów złożonych algorytmów. Możliwości skryptowe
czynią ten język przyjemnym zamiennikiem arkuszy kalkulacyjnych w
niektórych zastosowaniach, a możliwości obliczeniowe uzupełniają
ograniczoną funkcjonalność obliczeniową języków zorientowanych
tekstowo, takich jak AWK czy PERL.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}
mv -f $RPM_BUILD_ROOT%{_datadir}/nickle/examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_docdir}/nickle/nickle-tutorial.pdf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README README.name TODO doc/tutorial/nickle-tutorial.pdf
%attr(755,root,root) %{_bindir}/nickle
%{_includedir}/nickle
%{_datadir}/nickle
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man1/nickle.1*
