# Generated by rust2rpm 17
%bcond_with check

%global crate cbindgen

Name:           rust-%{crate}
Version:        0.24.3
Release:        1%{?dist}
Summary:        Tool for generating C bindings to Rust code

# Upstream license specification: MPL-2.0
License:        MPL-2.0
URL:            https://crates.io/crates/cbindgen
Source0:        https://github.com/mozilla/cbindgen/archive/refs/tags/v%{version}/%{crate}-%{version}.tar.gz
Source1:        vendor.tar.xz  
Source2:        cargo_config  

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
%if ! %{__cargo_skip_build}
BuildRequires:  (crate(clap/default) >= 2.0.0 with crate(clap/default) < 3.0.0)
BuildRequires:  (crate(heck/default) >= 0.3.0 with crate(heck/default) < 0.4.0)
BuildRequires:  (crate(indexmap/default) >= 1.0.0 with crate(indexmap/default) < 2.0.0)
BuildRequires:  (crate(log/default) >= 0.4.0 with crate(log/default) < 0.5.0)
BuildRequires:  (crate(proc-macro2/default) >= 1.0.0 with crate(proc-macro2/default) < 2.0.0)
BuildRequires:  (crate(quote/default) >= 1.0.0 with crate(quote/default) < 2.0.0)
BuildRequires:  (crate(serde/derive) >= 1.0.103 with crate(serde/derive) < 2.0.0)
BuildRequires:  (crate(serde_json/default) >= 1.0.0 with crate(serde_json/default) < 2.0.0)
BuildRequires:  (crate(syn/clone-impls) >= 1.0.3 with crate(syn/clone-impls) < 2.0.0)
BuildRequires:  (crate(syn/extra-traits) >= 1.0.3 with crate(syn/extra-traits) < 2.0.0)
BuildRequires:  (crate(syn/full) >= 1.0.3 with crate(syn/full) < 2.0.0)
BuildRequires:  (crate(syn/parsing) >= 1.0.3 with crate(syn/parsing) < 2.0.0)
BuildRequires:  (crate(syn/printing) >= 1.0.3 with crate(syn/printing) < 2.0.0)
BuildRequires:  (crate(tempfile/default) >= 3.0.0 with crate(tempfile/default) < 4.0.0)
BuildRequires:  (crate(toml/default) >= 0.5.0 with crate(toml/default) < 0.6.0)
%if %{with check}
BuildRequires:  (crate(serial_test/default) >= 0.5.0 with crate(serial_test/default) < 0.6.0)
%endif
%endif

%global _description %{expand:
Tool for generating C bindings to Rust code.}

%description %{_description}

%if ! %{__cargo_skip_build}
%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%doc README.md
%{_bindir}/cbindgen
%endif

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(cbindgen) = 0.18.0
Requires:       cargo
Requires:       (crate(heck/default) >= 0.3.0 with crate(heck/default) < 0.4.0)
Requires:       (crate(indexmap/default) >= 1.0.0 with crate(indexmap/default) < 2.0.0)
Requires:       (crate(log/default) >= 0.4.0 with crate(log/default) < 0.5.0)
Requires:       (crate(proc-macro2/default) >= 1.0.0 with crate(proc-macro2/default) < 2.0.0)
Requires:       (crate(quote/default) >= 1.0.0 with crate(quote/default) < 2.0.0)
Requires:       (crate(serde/derive) >= 1.0.103 with crate(serde/derive) < 2.0.0)
Requires:       (crate(serde_json/default) >= 1.0.0 with crate(serde_json/default) < 2.0.0)
Requires:       (crate(syn/parsing) >= 1.0.3 with crate(syn/parsing) < 2.0.0)
Requires:       (crate(tempfile/default) >= 3.0.0 with crate(tempfile/default) < 4.0.0)
Requires:       (crate(toml/default) >= 0.5.0 with crate(toml/default) < 0.6.0)

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(cbindgen/default) = 0.18.0
Requires:       cargo
Requires:       (crate(clap/default) >= 2.0.0 with crate(clap/default) < 3.0.0)
Requires:       crate(cbindgen) = 0.18.0

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+clap-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(cbindgen/clap) = 0.18.0
Requires:       cargo
Requires:       (crate(clap/default) >= 2.0.0 with crate(clap/default) < 3.0.0)
Requires:       crate(cbindgen) = 0.18.0

%description -n %{name}+clap-devel %{_description}

This package contains library source intended for building other packages
which use "clap" feature of "%{crate}" crate.

%files       -n %{name}+clap-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%setup -q -T -b 0 -n %{crate}-%{version}
%setup -q -D -T -a 1 -n %{crate}-%{version}
mkdir cargo-home
cp %{SOURCE2} cargo-home/config

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Wed Mar 24 2021 Bernhard Rosenkränzer <bero@lindev.ch> - 0.18.0-1
- Initial package
