# pywebview Fork

Fork of [r0x0r/pywebview](https://github.com/r0x0r/pywebview) with .NET 8 (coreclr) compatibility for Windows ARM64.

## Changes from upstream

- `OpenFolderDialog`: replaced `FileDialogNative` internals with `FolderBrowserDialog`
- WebView2 DLLs: updated to 1.0.3240 with `netcoreapp3.0` target
- `_is_chromium()`: skip .NET Framework registry check on coreclr
- `Microsoft.Win32.SystemEvents`: explicit `clr.AddReference` on coreclr

## Shipping

This is a git submodule of the tindex project. To ship changes:

1. Commit changes in this directory
2. Push to origin: `git push origin tindex`
   - Remote: `git@github.com-pywebview:smparkes/pywebview.git`
   - Branch: `tindex`
   - SSH key: `~/.ssh/id_pywebview`
3. Then in the parent tindex repo, stage the updated submodule pointer
