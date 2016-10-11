%{?scl:%scl_package concurrent-trees}
%{!?scl:%global pkg_name %{name}}

Name:          %{?scl_prefix}concurrent-trees
Version:       2.5.0
Release:       4%{?dist}
Summary:       Concurrent Trees for Java
License:       ASL 2.0
URL:           https://github.com/npgall/%{pkg_name}/
Source0:       https://github.com/npgall/%{pkg_name}/archive/%{version}.tar.gz

BuildRequires: %{?scl_prefix_maven}maven-local
BuildRequires: %{?scl_prefix_java_common}junit
BuildRequires: %{?scl_prefix_maven}mvn(org.sonatype.oss:oss-parent:pom:)
%{?scl:Requires: %scl_runtime}

BuildArch:     noarch

%description
This library provides concurrent Radix Trees and
concurrent Suffix Trees for Java.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -qn %{pkg_name}-%{version}
rm -r documentation/javadoc
rm -r documentation/documents
rm documentation/images/dfs-comic.png

%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
# Unneeded tasks
%pom_remove_plugin :maven-release-plugin code
%pom_remove_plugin :maven-gpg-plugin code
%pom_remove_plugin :maven-javadoc-plugin code
# fedora 25
%pom_remove_plugin :maven-source-plugin code

%mvn_file :%{pkg_name} %{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_build -- -f code/pom.xml 
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc README.md documentation/
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Tue Oct 11 2016 Tomas Repik <trepik@redhat.com> - 2.5.0-4
- use standard SCL macros

* Tue Aug 09 2016 Tomas Repik <trepik@redhat.com> - 2.5.0-3
- scl conversion

* Tue Jun 21 2016 Tomas Repik <trepik@redhat.com> - 2.5.0-2
- remove maven-source-plugin causing failure

* Thu Apr 21 2016 Tomas Repik <trepik@redhat.com> - 2.5.0-1
- initial package

