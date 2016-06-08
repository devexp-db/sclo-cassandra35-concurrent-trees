Name:          concurrent-trees
Version:       2.5.0
Release:       1%{?dist}
Summary:       Concurrent Trees for Java
License:       ASL 2.0
URL:           https://github.com/npgall/%{name}/
Source0:       https://github.com/npgall/%{name}/archive/%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:     noarch

%description
This library provides concurrent Radix Trees and
concurrent Suffix Trees for Java.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -qn %{name}-%{version}
rm -r documentation/javadoc
rm -r documentation/documents
rm documentation/images/dfs-comic.png

# Unneeded tasks
%pom_remove_plugin :maven-release-plugin code
%pom_remove_plugin :maven-gpg-plugin code
%pom_remove_plugin :maven-javadoc-plugin code

%mvn_file :%{name} %{name}

%build

%mvn_build -- -f code/pom.xml 

%install
%mvn_install

%files -f .mfiles
%doc README.md documentation/
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Thu Apr 21 2016 Tomas Repik <trepik@redhat.com> - 2.5.0-1
- initial package

