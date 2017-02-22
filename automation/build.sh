#!/bin/sh -ex

# Make sure the artifacts directory is empty:
artifacts_dir="${PWD}/exported-artifacts"
rm -rf "${artifacts_dir}" && mkdir -p "${artifacts_dir}"

# The name the package:
name="ovirt-engine-nodejs"

# Download the source:
spectool --get-files "${name}.spec"

# Make sure we remembered to update the version and/or release
if ! git show -- *.spec | \
    grep '^+\(Version\|Release\):'
then
    echo "Package version or release must be updated"
    exit 1
fi

# The Node.js build fails when a the directory where it runs has a very
# long name:
#
# execvp: printf: Argument list too long
#
# The reason for that is that the build process generates command line
# arguments with very long lists of files, and the total size exceeds
# the 128 KiB that the Linux kernel imposes for a single command line
# argument:
#
# http://lxr.free-electrons.com/source/include/uapi/linux/binfmts.h#L14
#
# This limit can't be changed (well, it can be, but requires to change
# and recompile the Kernel) so the only thing that we can do is try to
# use a shorted build directory. As the build runs inside a mock chroot
# that is discarded after the build, we can safely create a short
# directory in the root of the filesystem.
build_dir="/b"

# Build the source and binary packages:
rpmbuild \
  -ba \
  --define="_sourcedir ${PWD}" \
  --define="_srcrpmdir ${artifacts_dir}" \
  --define="_rpmdir ${artifacts_dir}" \
  --define="_builddir ${build_dir}" \
  "${name}.spec"
