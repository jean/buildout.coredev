#!/bin/sh
set -eu

site=$(.venv/bin/python -c 'import site; print(site.getsitepackages()[0])')

apply_patch()
{
    patch_file=$1

    if patch --dry-run -d "$site" -p1 < "$patch_file" >/dev/null 2>&1; then
        patch -d "$site" -p1 < "$patch_file"
    elif patch --dry-run --reverse -d "$site" -p1 < "$patch_file" >/dev/null 2>&1; then
        echo "Already applied: $patch_file"
    else
        echo "Cannot apply: $patch_file" >&2
        return 1
    fi
}

apply_patch ./patches/ZODB-termux-no-hardlinks.patch
apply_patch ./patches/zope-sendmail-termux-no-hardlinks.patch
