#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v21
# autospec commit: 0698adb
#
Name     : asciidoctor
Version  : 2.0.23
Release  : 6
URL      : https://github.com/asciidoctor/asciidoctor/archive/v2.0.23/asciidoctor-2.0.23.tar.gz
Source0  : https://github.com/asciidoctor/asciidoctor/archive/v2.0.23/asciidoctor-2.0.23.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: asciidoctor-bin = %{version}-%{release}
Requires: asciidoctor-license = %{version}-%{release}
Requires: ruby
BuildRequires : ruby
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
= Asciidoctor
Dan Allen <https://github.com/mojavelinux[@mojavelinux]>; Sarah White <https://github.com/graphitefriction[@graphitefriction]>
v2.0.23, 2024-05-17
// settings:
:idprefix:
:idseparator: -
:source-language: ruby
:language: {source-language}
ifndef::env-github[:icons: font]
ifdef::env-github[]
:status:
:caution-caption: :fire:
:important-caption: :exclamation:
:note-caption: :paperclip:
:tip-caption: :bulb:
:warning-caption: :warning:
endif::[]
// Variables:
:release-version: 2.0.23
// URIs:
:uri-org: https://github.com/asciidoctor
:uri-repo: {uri-org}/asciidoctor
:uri-asciidoctorj: {uri-org}/asciidoctorj
:uri-asciidoctorjs: {uri-org}/asciidoctor.js
:uri-project: https://asciidoctor.org
ifdef::env-site[:uri-project: link:]
:uri-docs: {uri-project}/docs
:uri-news: {uri-project}/news
:uri-manpage: {uri-project}/man/asciidoctor
:uri-issues: {uri-repo}/issues
:uri-contributors: {uri-repo}/graphs/contributors
:uri-rel-file-base: link:
:uri-rel-tree-base: link:
ifdef::env-site[]
:uri-rel-file-base: {uri-repo}/blob/HEAD/
:uri-rel-tree-base: {uri-repo}/tree/HEAD/
endif::[]
:uri-changelog: {uri-rel-file-base}CHANGELOG.adoc
:uri-contribute: {uri-rel-file-base}CONTRIBUTING.adoc
:uri-license: {uri-rel-file-base}LICENSE
:uri-tests: {uri-rel-tree-base}test
:uri-discuss: https://discuss.asciidoctor.org
:uri-chat: https://asciidoctor.zulipchat.com
:uri-rubygem: https://rubygems.org/gems/asciidoctor
:uri-what-is-asciidoc: {uri-docs}/what-is-asciidoc
:uri-user-manual: {uri-docs}/user-manual
:uri-install-docker: https://github.com/asciidoctor/docker-asciidoctor
//:uri-install-doc: {uri-docs}/install-toolchain
:uri-install-macos-doc: {uri-docs}/install-asciidoctor-macos
:uri-render-doc: {uri-docs}/render-documents
:uri-themes-doc: {uri-docs}/produce-custom-themes-using-asciidoctor-stylesheet-factory
:uri-gitscm-repo: https://github.com/git/git-scm.com
:uri-freesoftware: https://www.gnu.org/philosophy/free-sw.html
:uri-foundation: https://foundation.zurb.com
:uri-opal: https://opalrb.com
:uri-tilt: https://github.com/rtomayko/tilt
:uri-ruby: https://ruby-lang.org
// images:
:image-uri-screenshot: https://cdn.jsdelivr.net/gh/asciidoctor/asciidoctor/screenshot.png

%package bin
Summary: bin components for the asciidoctor package.
Group: Binaries
Requires: asciidoctor-license = %{version}-%{release}

%description bin
bin components for the asciidoctor package.


%package license
Summary: license components for the asciidoctor package.
Group: Default

%description license
license components for the asciidoctor package.


%prep
%setup -q -n asciidoctor-2.0.23
cd %{_builddir}/asciidoctor-2.0.23

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1736469635
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
gem build asciidoctor.gemspec; echo  %{?_smp_mflags}


%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1736469635
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/asciidoctor
cp %{_builddir}/asciidoctor-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/asciidoctor/9d157ff53ef9653004efadf1670c239286a8dd06 || :
export GOAMD64=v2
GOAMD64=v2
gem install --build-root %{buildroot} asciidoctor-*.gem

%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/3.4.0/cache/asciidoctor-2.0.23.gem
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/CHANGELOG.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/LICENSE
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/README-de.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/README-fr.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/README-jp.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/README-zh_CN.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/README.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/asciidoctor.gemspec
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/bin/asciidoctor
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-ar.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-be.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-bg.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-ca.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-cs.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-da.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-de.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-en.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-es.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-fa.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-fi.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-fr.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-hu.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-id.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-it.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-ja.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-ko.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-nb.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-nl.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-nn.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-pl.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-pt.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-pt_BR.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-ro.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-ru.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-sr.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-sr_Latn.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-sv.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-sw.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-th.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-tr.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-uk.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-vi.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-zh_CN.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes-zh_TW.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/locale/attributes.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/reference/syntax.adoc
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/stylesheets/asciidoctor-default.css
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/data/stylesheets/coderay-asciidoctor.css
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/abstract_block.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/abstract_node.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/attribute_list.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/block.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/callouts.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/cli.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/cli/invoker.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/cli/options.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/convert.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/converter.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/converter/composite.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/converter/docbook5.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/converter/html5.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/converter/manpage.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/converter/template.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/core_ext.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/core_ext/float/truncate.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/core_ext/hash/merge.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/core_ext/match_data/names.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/core_ext/nil_or_empty.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/core_ext/regexp/is_match.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/document.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/extensions.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/helpers.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/inline.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/list.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/load.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/logging.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/parser.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/path_resolver.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/reader.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/rouge_ext.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/rx.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/section.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/stylesheets.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/substitutors.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/syntax_highlighter.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/syntax_highlighter/coderay.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/syntax_highlighter/highlightjs.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/syntax_highlighter/html_pipeline.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/syntax_highlighter/prettify.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/syntax_highlighter/pygments.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/syntax_highlighter/rouge.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/table.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/timings.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/version.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/lib/asciidoctor/writer.rb
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/man/asciidoctor.1
/usr/lib64/ruby/gems/3.4.0/gems/asciidoctor-2.0.23/man/asciidoctor.adoc
/usr/lib64/ruby/gems/3.4.0/specifications/asciidoctor-2.0.23.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/asciidoctor

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/asciidoctor/9d157ff53ef9653004efadf1670c239286a8dd06
