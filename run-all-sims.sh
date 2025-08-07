#!/usr/bin/env sh

USE_CORES=24

if command -v "parallel" > /dev/null; then
    temp_joint_file=$(mktemp)
    cat run-sim-*.sh > "$temp_joint_file"
    sed -i -e "/^#!/d" -e "/^[[:space:]]*$/d" "$temp_joint_file"
    parallel --jobs "$USE_CORES" < "$temp_joint_file"
    rm "$temp_joint_file"
else
    for f in run-sim-*.sh; do
        sh "$f"
    done
fi

sh clean-all-data.sh
