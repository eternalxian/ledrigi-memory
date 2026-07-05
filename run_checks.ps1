$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root
python memory_tool.py verify
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
python evaluate.py
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
python -m unittest discover -s tests -v
exit $LASTEXITCODE
