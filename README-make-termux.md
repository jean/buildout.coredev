# Running buildout.coredev on Termux/Android

## Overview

These are the changes required to get `make install` and `make run` working on
Termux/Android. Some of these are committed to the repo; others must be
re-applied manually if the venv is recreated.

## Committed changes

### `stubs/robotframework-browser/`

`robotframework-browser` is a transitive test dependency (via
`plone.app.robotframework`) that requires a browser to function and cannot run
on Android. Its build also fails because `psutil` (one of its dependencies)
explicitly rejects the Android platform at build time.

A stub package is provided in `stubs/robotframework-browser/` that satisfies
the version requirement (19.10.1) without pulling in any dependencies.

It is referenced at the top of `requirements-test.txt`:

```
./stubs/robotframework-browser
```

## Manual patches (re-apply after venv recreation)

Android filesystems do not support hard links, so Python does not expose
`os.link`. Two packages in the Zope stack assume `os.link` is always available.

### `.venv/lib/python3.13/site-packages/ZODB/blob.py`

Around line 950, change:

```python
link_or_copy = os.link
```

to:

```python
# Android/Termux: os.link (hard links) is not supported on Android filesystems.
# Fall back to shutil.copy which has a compatible (src, dst) signature.
link_or_copy = os.link if hasattr(os, 'link') else shutil.copy
```

### `.venv/lib/python3.13/site-packages/zope/sendmail/queue.py`

Add `import shutil` to the imports, then around line 47, change:

```python
_os_link = os.link
```

to:

```python
# Android/Termux: os.link (hard links) is not supported on Android filesystems.
# Fall back to shutil.copy which has a compatible (src, dst) signature.
_os_link = os.link if hasattr(os, 'link') else shutil.copy
```
