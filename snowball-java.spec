%{?scl:%scl_package snowball-java}
%{!?scl:%global pkg_name %{name}}

Name:		%{?scl_prefix}snowball-java
Version:	0
Release:	0.9.20130902%{?dist}
Summary:	Java stemming algorithm library
License:	BSD
URL:		http://snowball.tartarus.org/index.php
Source0:	http://snowball.tartarus.org/dist/libstemmer_java.tgz
# Custom pom file
Source1:	snowball-template-pom.xml
# http://snowball.tartarus.org/license.php
Source2:	snowball-notice.txt
# see http://snowball.tartarus.org/license.php
# http://www.opensource.org/licenses/bsd-license.html
Source3:	snowball-BSD-license.txt
# Build fix remove 'break;' 
Patch0:		snowball-remove-unreachable-statement.patch

BuildRequires:	%{?scl_prefix_maven}maven-local
%{?scl:Requires: %scl_runtime}

BuildArch:	noarch

%description
Snowball is a small string processing language
designed for creating stemming algorithms
for use in Information Retrieval.

This package contains all you need to include the
snowball stemming algorithms into a Java
project of your own. If you use this,
you don't need to use the snowball compiler,
or worry about the internals of the
stemmers in any way.

%package javadoc
Summary:	Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n libstemmer_java

%patch0 -p0

cp -p %{SOURCE1} pom.xml
sed -i "s|@VERSION@|%{version}|" pom.xml

cp -p %{SOURCE2} notice.txt
cp -p %{SOURCE3} license.txt
sed -i 's/\r//' license.txt notice.txt

%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_file : %{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%license license.txt notice.txt

%files javadoc -f .mfiles-javadoc
%license license.txt notice.txt

%changelog
* Wed Oct 12 2016 Tomas Repik <trepik@redhat.com> - 0-0.9.20130902
- use standard SCL macros

* Wed Jul 27 2016 Tomas Repik <trepik@redhat.com> - 0-0.8.20130902
- scl conversion

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20130902
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 30 2016 gil cattaneo <puntogil@libero.it> - 0-0.6.20130902
- rebuilt

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.20130902
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 11 2015 gil cattaneo <puntogil@libero.it> 0-0.4.20130902
- introduce license macro

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.20130902
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 0-0.2.20130902
- Use Requires: java-headless rebuild (#1067528)

* Mon Sep 02 2013 gil cattaneo <puntogil@libero.it> 0-0.1.20130902
- initial rpm
