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

# Build the source and binary packages:
rpmbuild \
  -ba \
  --define="_sourcedir ${PWD}" \
  --define="_srcrpmdir ${artifacts_dir}" \
  --define="_rpmdir ${artifacts_dir}" \
  "${name}.spec"
