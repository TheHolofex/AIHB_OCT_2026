# Windows PowerShell setup

Set up the course tools on native Windows, then run a readiness check in which Oh My Pi writes one file. Plan for roughly 60 to 120 minutes for the native setup, though that is only an estimate. The n8n bridge may take more time to install and restart. Open **Windows PowerShell 5.1** from the Start menu on native Windows as an ordinary user. Installers may need an approved elevation prompt; if administrator credentials are required, follow the device owner's approved route.

You need Git, Python 3.12 or newer, a browser, an ordinary text editor, local Obsidian, and Oh My Pi 18.3.5. The only provider key is `OPENROUTER_API_KEY`, and the course launcher selects `openrouter/anthropic/claude-sonnet-4.6`. Module 7 also needs local n8n 2.41.5 through Docker Desktop and a named Ubuntu WSL 2 bridge, described below. Keep OMP, Python, Git, Obsidian and its vault, the checkout, evidence, and credentials on native Windows; use Ubuntu only for n8n installation and lifecycle commands. You do not install Node, npm, or another agent.

A checksum is a fingerprint of a file. You compare the fingerprint of the downloaded program with the fingerprint published beside it, and you do that before the program is allowed to run. PATH is the list of folders Windows searches when you type a command name.

If a company policy denies an installer, stop and save the message. Do not open an Administrator window to get around that denial. When a step stops, start from the first failed check in [When setup stops](../shared/TROUBLESHOOTING.md).

## Check the disk and the processor

Check with the device owner that these installations are allowed. Your Windows release and edition must still be supported under your device's servicing arrangement. WinGet requires at least Windows 10 version 1809, build 17763, but meeting that minimum does not make an unsupported release supported. Windows 10 is not ruled out simply because it is not Windows 11, as long as it has applicable ongoing support. If you are unsure about the edition or support lifecycle, ask the device owner. See [WinGet requirements](https://learn.microsoft.com/en-us/windows/package-manager/winget/).

Check the OS/build, Windows PowerShell version, and whether WinGet is available. You also need enough free space for Git, Python, and the course checkout, plus a Windows binary that matches your processor. Windows reports the processor code: 12 means ARM64 and 9 means x64. The program running this check can report a different architecture, so use the processor code instead.

**Terminal: Windows PowerShell 5.1, ordinary user, same window.**

```powershell
$ErrorActionPreference = 'Stop'
if ($env:OS -ne 'Windows_NT') { throw 'STOP: use native Windows.' }
$PSVersionTable
if ($PSVersionTable.PSEdition -ne 'Desktop' -or $PSVersionTable.PSVersion.Major -ne 5 -or $PSVersionTable.PSVersion.Minor -ne 1) {
  throw 'STOP: open Windows PowerShell 5.1 from Start.'
}
$os = Get-CimInstance -ClassName Win32_OperatingSystem
$os | Select-Object Caption, Version, BuildNumber
if ([int]$os.BuildNumber -lt 17763) { throw 'STOP: this OS is below the WinGet technical floor.' }
$winget = Get-Command winget -CommandType Application -ErrorAction SilentlyContinue
if ($winget) {
  & $winget.Source --version
  if ($LASTEXITCODE -ne 0) { throw 'STOP: WinGet failed. Keep its message.' }
} else { Write-Output 'WinGet MISSING: use the approved official-installer recovery if needed.' }
$driveName = ([IO.Path]::GetPathRoot($HOME).TrimEnd('\'))[0]
$freeGb = (Get-PSDrive -Name $driveName).Free / 1GB
Write-Output ("free GB: " + [math]::Round($freeGb, 1))
if ($freeGb -lt 15) { throw 'STOP: free at least 15 GB on the home drive.' }
$archCode = (Get-CimInstance -ClassName Win32_Processor | Select-Object -First 1).Architecture
if ($archCode -eq 12) {
  $asset = 'omp-windows-arm64.exe'
} elseif ($archCode -eq 9) {
  $asset = 'omp-windows-x64.exe'
} else {
  throw 'STOP: this processor does not have a published course binary.'
}
Write-Output $asset
```

**Expected:** a supported Windows edition/build, Desktop PowerShell 5.1, a WinGet version or explicit missing notice, free space of at least 15 GB, then either `omp-windows-arm64.exe` or `omp-windows-x64.exe`.

**Stop:** installation permission or OS support is uncertain, the OS/shell check fails, free space is under 15 GB, the processor query fails, or the script stops because no published binary matches.

**Recovery:** resolve an OS/support or installation-permission question with the device owner before continuing. For low disk space, free space on the home drive and check again. For an unsupported processor, save the stop message and ask support for a supported machine. Do not download the other architecture and hope it runs.

The architecture numbers are documented with [Win32_Processor](https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-processor).

## Resolve the real Python 3.12 executable

Check Git, then try each Python candidate until one runs as version 3.12 or newer. This check skips Store aliases and reparse points (links or redirects). After a candidate passes the version check, it accepts an absolute `sys.executable` path and checks that executable too. If `py -3.12` is absent or `python` is too old, a later candidate may still work. See [Python for Windows](https://docs.python.org/3.12/using/windows.html) for the launcher.

Paste this whole block in each newly opened setup window to recreate `$PY`, `$R`, and `$M` and check Git again.

**Terminal: Windows PowerShell 5.1, ordinary user, same window or newly opened from Start after a restart.**

```powershell
$ErrorActionPreference = 'Stop'
$R = Join-Path $HOME 'Documents\AIHB_OCT_2026'
$M = Join-Path $R 'AI_Harness_Bootcamp_2\module-00-setup'
$gitReady = $false
$gitCmd = Get-Command git -CommandType Application -ErrorAction SilentlyContinue
if ($gitCmd) {
  & $gitCmd.Source --version
  if ($LASTEXITCODE -ne 0) { throw 'STOP: existing Git failed; preserve the message before repair.' }
  $gitReady = $true
} else { Write-Output 'Git MISSING' }
function Find-CoursePython {
  $candidates = @()
  $pyLaunchers = @(Get-Command py -CommandType Application -All -ErrorAction SilentlyContinue)
  foreach ($cmd in $pyLaunchers) {
    $candidates += @{ Exe = $cmd.Source; Args = @('-3.12') }
    $candidates += @{ Exe = $cmd.Source; Args = @('-3') }
  }
  foreach ($name in @('python3.12', 'python', 'python3')) {
    foreach ($cmd in @(Get-Command $name -CommandType Application -All -ErrorAction SilentlyContinue)) {
      $candidates += @{ Exe = $cmd.Source; Args = @() }
    }
  }
  foreach ($candidate in $candidates) {
    $exe = $candidate.Exe
    if ($exe -like '*\WindowsApps\*') { continue }
    $item = Get-Item -LiteralPath $exe -Force
    if ($item.PSIsContainer -or ($item.Attributes -band [IO.FileAttributes]::ReparsePoint)) { continue }
    $argsForPython = @($candidate.Args) + @('-c', 'import sys; sys.exit(1) if sys.version_info < (3,12) else print(sys.executable)')
    $output = @(& $exe @argsForPython)
    if ($LASTEXITCODE -ne 0) { continue }
    if ($output.Count -ne 1 -or [string]::IsNullOrWhiteSpace([string]$output[0])) { continue }
    $resolved = ([string]$output[0]).Trim()
    if ($resolved -notmatch '^[A-Za-z]:\\' -or $resolved -like '*\WindowsApps\*') { continue }
    if (-not (Test-Path -LiteralPath $resolved -PathType Leaf)) { continue }
    $item = Get-Item -LiteralPath $resolved -Force
    if ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) { continue }
    $confirmed = @(& $resolved -c 'import sys; sys.exit(1) if sys.version_info < (3,12) else print(sys.executable)')
    if ($LASTEXITCODE -ne 0) { continue }
    if ($confirmed.Count -ne 1 -or ([string]$confirmed[0]).Trim() -ine $resolved) { continue }
    return $resolved
  }
  return $null
}
$PY = Find-CoursePython
if ($PY) {
  Write-Output $PY
  & $PY --version
  if ($LASTEXITCODE -ne 0) { throw 'STOP: resolved Python failed its version command.' }
} else { Write-Output 'Python 3.12+ MISSING' }
```

**Expected:** Git’s version and an absolute Python path followed by Python 3.12 or newer, or a specific `MISSING` line for a prerequisite to install. Failed candidate messages can appear before a later suitable Python is found.

**Stop:** an existing Git fails, or no suitable Python is found after installation. Do not continue to downloads or cloning with a missing prerequisite.

**Recovery:** install only the missing prerequisite below. If Python still resolves only to a Store alias, use Settings → Apps → Advanced app settings → App execution aliases to turn off the `python.exe` and `python3.exe` aliases, then reopen and resolve again. Do not type a guessed `$PY` path.

## Install Git and Python for your user

Install only the prerequisites that are missing; skip this block if both tools passed. Although you start as an ordinary user, Git may need an approved machine installation. When WinGet asks about source or package agreements, review them and accept only if you are authorized. Git's installer may ask for elevation, while Python requests a user install. If the package cannot install at the requested scope, approval is denied, or policy blocks the installation, stop and ask the device owner to provide the approved installation. Do not switch to Administrator to bypass policy. See [WinGet install options](https://learn.microsoft.com/en-us/windows/package-manager/winget/install).

Install only the tools marked missing by the preceding block.

**Terminal: Windows PowerShell 5.1, ordinary user, same window.**

```powershell
if (-not (Get-Command winget -CommandType Application -ErrorAction SilentlyContinue)) {
  throw 'STOP: WinGet is missing. Use the official-installer recovery.'
}
if (-not $gitReady) {
  winget install --exact --id Git.Git --source winget
  if ($LASTEXITCODE -ne 0) { throw 'STOP: Git installation did not succeed. Keep the installer message.' }
}
if (-not $PY) {
  winget install --exact --id Python.Python.3.12 --source winget --scope user
  if ($LASTEXITCODE -ne 0) { throw 'STOP: Python installation did not succeed. Keep the installer message.' }
}
```

**Expected:** each needed installer exits successfully. Suitable existing tools are skipped.

**Stop:** any nonzero installer exit, including an already-installed message when the tool still failed discovery, or any denied permission/policy prompt.

**Recovery:** keep the message and work with the device owner to fix the problem it names. If only WinGet is unavailable, use the approved official [Git for Windows installer](https://git-scm.com/downloads/win) and [Python Windows installer](https://www.python.org/downloads/windows/) for missing tools only. Choose Python 3.12 or newer, install it for the current user, and select **Add python.exe to PATH**. Do not reinstall over an existing installation that conflicts for an unknown reason.

After any PATH-changing installer, close **all terminal windows**, including Windows Terminal and editor terminals. Open **Windows PowerShell** again through **Start**. A new tab can inherit the old environment. Repeat the full [Git and Python resolver](#resolve-the-real-python-312-executable) in that new window; it also recreates `$R` and `$M`. Continue only after both tools pass.

## Download Oh My Pi and verify it before it can run

Download the selected binary and `SHA256SUMS.txt` from the pinned release into a new folder for this attempt alone. The published file lists a lowercase SHA-256 fingerprint, two spaces, and then the exact filename. Do not copy or run the program unless that exact line matches the file you downloaded.

The release page is [Oh My Pi v18.3.5](https://github.com/can1357/oh-my-pi/releases/tag/v18.3.5). `Get-FileHash` is the Windows command that computes the fingerprint: [Get-FileHash](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-filehash).

**Terminal: Windows PowerShell 5.1, ordinary user, same window.**

```powershell
$ErrorActionPreference = 'Stop'
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
if (-not $env:LOCALAPPDATA) { throw 'STOP: LOCALAPPDATA is not set.' }
$archCode = (Get-CimInstance -ClassName Win32_Processor | Select-Object -First 1).Architecture
if ($archCode -eq 12) {
  $asset = 'omp-windows-arm64.exe'
} elseif ($archCode -eq 9) {
  $asset = 'omp-windows-x64.exe'
} else {
  throw 'STOP: this processor does not have a published course binary.'
}
$downloadParent = Join-Path $env:LOCALAPPDATA 'omp-downloads'
if (Test-Path -LiteralPath $downloadParent) {
  $parentItem = Get-Item -LiteralPath $downloadParent -Force
  if ($parentItem.Attributes -band [IO.FileAttributes]::ReparsePoint) {
    throw 'STOP: the download parent is a link. Nothing was downloaded.'
  }
} else {
  New-Item -ItemType Directory -Path $downloadParent | Out-Null
}
$download = Join-Path $downloadParent ([guid]::NewGuid().ToString('n'))
New-Item -ItemType Directory -Path $download | Out-Null
$base = 'https://github.com/can1357/oh-my-pi/releases/download/v18.3.5'
$sumsPath = Join-Path $download 'SHA256SUMS.txt'
$binaryPath = Join-Path $download $asset
Invoke-WebRequest -Uri ($base + '/SHA256SUMS.txt') -OutFile $sumsPath -UseBasicParsing
Invoke-WebRequest -Uri ($base + '/' + $asset) -OutFile $binaryPath -UseBasicParsing
if (-not (Test-Path -LiteralPath $sumsPath) -or -not (Test-Path -LiteralPath $binaryPath)) {
  throw 'STOP: a download is missing. Nothing was installed.'
}
$matches = @(Get-Content -LiteralPath $sumsPath | Where-Object {
  $pair = $_ -split '  ', 2
  $pair.Length -eq 2 -and $pair[1] -ceq $asset
})
if ($matches.Count -ne 1) { throw 'STOP: the checksum file has no single exact line for the selected file. Nothing was installed.' }
$expected = ($matches[0] -split '  ', 2)[0]
if ($expected -cnotmatch '^[0-9a-f]{64}$') { throw 'STOP: the checksum line is not a SHA-256 value. Nothing was installed.' }
$actual = (Get-FileHash -LiteralPath $binaryPath -Algorithm SHA256).Hash.ToLowerInvariant()
if ($actual -ne $expected) { throw 'STOP: checksum failed. Nothing was installed.' }
$destDir = Join-Path $env:LOCALAPPDATA 'omp'
$dest = Join-Path $destDir 'omp.exe'
foreach ($probe in @($destDir, $dest)) {
  if (Test-Path -LiteralPath $probe) {
    $probeItem = Get-Item -LiteralPath $probe -Force
    if ($probeItem.Attributes -band [IO.FileAttributes]::ReparsePoint) {
      throw 'STOP: the destination is a symlink or junction. It was not replaced.'
    }
  }
}
if (Test-Path -LiteralPath $dest) {
  $destItem = Get-Item -LiteralPath $dest -Force
  if ($destItem.PSIsContainer) { throw 'STOP: the destination is a folder. It was not replaced.' }
  $existing = (Get-FileHash -LiteralPath $dest -Algorithm SHA256).Hash.ToLowerInvariant()
  if ($existing -ne $actual) { throw 'STOP: a different file is already at the destination. It was not replaced.' }
} else {
  if (-not (Test-Path -LiteralPath $destDir)) {
    New-Item -ItemType Directory -Path $destDir | Out-Null
  }
  Copy-Item -LiteralPath $binaryPath -Destination $dest
}
Write-Output $download
Write-Output $dest
$ompVersion = @(& $dest --version)
if ($LASTEXITCODE -ne 0) { throw 'STOP: OMP version command failed.' }
if ($ompVersion.Count -ne 1 -or ([string]$ompVersion[0]).Trim() -ne 'omp/18.3.5') { throw 'STOP: OMP version differs from omp/18.3.5.' }
Write-Output $ompVersion
```

**Expected:** the download folder path, the destination path ending in `\omp\omp.exe` under your local app data, and a version line `omp/18.3.5`. That version command is the first time the program runs, and it runs only after the fingerprint matched.

**Stop:** the script stops on a failed download, a missing or extra checksum line, a fingerprint mismatch, a symlink or junction, or a different file already at the destination. The destination is left untouched in those cases.

**Recovery:** leave the download folder in place. Fix the cause named in the stop line before running the block again; the next run makes a new download folder. Do not copy the binary into place yourself or delete a different existing `omp.exe`. If Windows blocks the verified file from starting, save the message and stop rather than turning off a security control.

## Save the program folder on your user PATH

The launcher finds `omp` by name. Save the destination folder in your user PATH so a later window can find the same binary. It does not store the API key.

**Terminal: Windows PowerShell 5.1, ordinary user, same window.**

```powershell
$ompDir = Join-Path $env:LOCALAPPDATA 'omp'
$dest = Join-Path $ompDir 'omp.exe'
if (-not (Test-Path -LiteralPath $dest)) { throw 'STOP: the verified binary is not at the destination.' }
$otherOmp = Get-Command omp -CommandType Application -ErrorAction SilentlyContinue
if ($otherOmp -and $otherOmp.Source -ine $dest) { throw 'STOP: another omp is already on PATH. It was not hidden or replaced.' }
$current = [Environment]::GetEnvironmentVariable('Path', 'User')
$entries = @($current -split ';')
if ($entries -ccontains $ompDir) {
  $updated = $current
} elseif ([string]::IsNullOrEmpty($current)) {
  $updated = $ompDir
} else {
  $updated = $ompDir + ';' + $current
}
[Environment]::SetEnvironmentVariable('Path', $updated, 'User')
$env:Path = $ompDir + ';' + $env:Path
$found = (Get-Command omp -ErrorAction SilentlyContinue).Source
if ($found -ine $dest) { throw 'STOP: omp resolves to a different or missing program. Preserve that installation.' }
Write-Output $found
```

**Expected:** the printed path is the same `\omp\omp.exe` path under local app data.

**Stop:** the command is not found, or the found path is a different file.

**Recovery:** run the download block again only if the destination file is missing. If a different `omp` is found, do not overwrite it. Save the printed path and stop. PATH changes are documented in [about_Environment_Variables](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables).

## Check private GitHub access before cloning

Check whether your existing Git credentials can read the private course repository. This check turns off Git terminal prompts temporarily, then restores the setting this process had before. If access works, skip GitHub CLI and keep your working credentials and helpers. See [git ls-remote](https://git-scm.com/docs/git-ls-remote).

**Terminal: Windows PowerShell 5.1, ordinary user, same window.**

```powershell
$savedGitPrompt = [Environment]::GetEnvironmentVariable('GIT_TERMINAL_PROMPT', 'Process')
try {
  $env:GIT_TERMINAL_PROMPT = '0'
  git ls-remote --exit-code https://github.com/TheHolofex/AIHB_OCT_2026.git HEAD
  if ($LASTEXITCODE -ne 0) { throw 'STOP: repository access failed. Keep the message; use the access recovery.' }
} finally {
  if ($null -eq $savedGitPrompt) {
    Remove-Item Env:\GIT_TERMINAL_PROMPT -ErrorAction SilentlyContinue
  } else {
    [Environment]::SetEnvironmentVariable('GIT_TERMINAL_PROMPT', $savedGitPrompt, 'Process')
  }
}
Write-Output 'Repository access confirmed.'
```

**Expected:** a commit identifier and `HEAD`, then `Repository access confirmed.`

**Stop:** any nonzero exit, denied access, or repository-not-found message. This is an access prerequisite, not a local folder permission problem.

**Recovery:** keep the message. Fix a network problem first if the message names one; if your credentials are missing or unsuitable, use the fallback below. You also need the repository owner's invitation and any organization approval. Logging in alone will not give you access.

### Install GitHub CLI only for failed access

If `gh` is already installed, skip the installation. Review the official installer's approval prompt: this package may ask for administrator elevation and may not install just for your user. If approval or policy blocks it, stop and use the device owner's approved route. See [GitHub CLI’s Windows installation instructions](https://raw.githubusercontent.com/cli/cli/trunk/docs/install_windows.md) for the command and restart requirement.

**Terminal: Windows PowerShell 5.1, ordinary user, same window.**

```powershell
if (Get-Command gh -CommandType Application -ErrorAction SilentlyContinue) {
  gh --version
  if ($LASTEXITCODE -ne 0) { throw 'STOP: existing GitHub CLI failed. Preserve its message.' }
} else {
  if (-not (Get-Command winget -CommandType Application -ErrorAction SilentlyContinue)) {
    throw 'STOP: ask the device owner to provision official GitHub CLI; WinGet is unavailable.'
  }
  winget install --exact --id GitHub.cli --source winget
  if ($LASTEXITCODE -ne 0) { throw 'STOP: GitHub CLI installation failed. Keep the message.' }
}
```

**Expected:** an existing GitHub CLI version, or a successful official installation.

**Stop:** any nonzero exit, denied approval, or policy restriction.

**Recovery:** keep the failure message and ask the device owner to resolve the installation problem it names. After installation, close **all terminal windows** and reopen **Windows PowerShell through Start**, not in a new tab. Run the full [Git and Python resolver](#resolve-the-real-python-312-executable) again to set `$R`, `$M`, and the real `$PY` and check Git. Do not continue if a prerequisite is missing.

### Authorize the invited GitHub account

Run the browser login. GitHub CLI will show a device code and ask you to open a browser to authorize access. Make sure the browser is using the GitHub account invited to this repository. These GitHub credentials are separate from your course-site password and OpenRouter key. If login asks you to configure Git credentials, choose **No**. Check how they are stored first, then configure the host in the later block.

GitHub CLI prefers the OS credential store but may fall back to a plaintext file. Do not use `--insecure-storage`. See [gh auth login](https://cli.github.com/manual/gh_auth_login).

**Terminal: Windows PowerShell 5.1, ordinary user, same window after resolving tools following any restart.**

```powershell
gh auth login --hostname github.com --git-protocol https --web
if ($LASTEXITCODE -ne 0) { throw 'STOP: GitHub login failed. Do not configure Git yet.' }
```

**Expected:** browser authorization completes for the invited account and login exits successfully.

**Stop:** wrong account, denied authorization, or a nonzero exit.

**Recovery:** correct the account or invitation with the repository owner before another login. Do not share the device code or authentication output.

Inspect account and storage locally, without displaying a token. See [gh auth status](https://cli.github.com/manual/gh_auth_status).

**Terminal: Windows PowerShell 5.1, ordinary user, same window.**

```powershell
gh auth status --hostname github.com
if ($LASTEXITCODE -ne 0) { throw 'STOP: GitHub authentication status failed.' }
```

**Expected:** the correct active account and credential storage allowed by your device policy. Do not share this output or add `--show-token`.

**Stop:** wrong account, failed status, unapproved storage, or uncertainty about whether reported storage is approved.

**Recovery:** ask the device owner to provision approved credential storage or credentials. Do not proceed with plaintext fallback unless the device policy explicitly approves that storage.

Configure Git for `github.com` only after the status and storage check passes. See [gh auth setup-git](https://cli.github.com/manual/gh_auth_setup-git).

**Terminal: Windows PowerShell 5.1, ordinary user, same window.**

```powershell
gh auth setup-git --hostname github.com
if ($LASTEXITCODE -ne 0) { throw 'STOP: Git credential setup failed.' }
```

**Expected:** exit zero; the command may print nothing.

**Stop:** any nonzero exit. Do not add `--force`.

**Recovery:** work with the device owner to fix the reported credential problem. Before cloning, run the exact [disabled-prompt repository access block](#check-private-github-access-before-cloning) again. Continue only if it prints `Repository access confirmed.` If it still fails, keep the message and ask the repository owner to confirm the invitation and organization approval. Do not keep repeating login without checking the cause.

## Use the course checkout, or clone it once

Use or clone the course at `$HOME\Documents\AIHB_OCT_2026` after repository access passes. If a checkout of the course is already there, the command uses it as it is; it leaves a different folder at that path alone.

Git may change line endings when it copies text files. A line ending is the hidden character at the end of a line. Later checks compare the exact bytes, so this change can make a frozen control look different even when its words have not changed. The copy command turns off that change for this command only; it does not save a Git setting. It also does not reset, clean, pull, or renormalize an existing folder. The published course marks these text files so a later fresh copy keeps their published line endings too.

Once the copy has been found or made, this step reads three frozen controls: the Module 1 source manifest, the Module 8 policy file, and the Module 10 restore control. If any contains a carriage return, this copy's line endings were already rewritten. Put the result on hold, leave the folder untouched, and get an intact fresh copy. Do not use this step to repair the existing files.

**Terminal: Windows PowerShell 5.1, ordinary user, same window.**

```powershell
$R = Join-Path $HOME 'Documents\AIHB_OCT_2026'
$origin = 'https://github.com/TheHolofex/AIHB_OCT_2026.git'
$usingExisting = $false
if (Test-Path -LiteralPath $R) {
  foreach ($probe in @($R, (Join-Path $R '.git'))) {
    if (Test-Path -LiteralPath $probe) {
      $item = Get-Item -LiteralPath $probe -Force
      if ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) { throw 'STOP: checkout or .git is a link. It was not followed.' }
    }
  }
  if (-not (Test-Path -LiteralPath (Join-Path $R '.git') -PathType Container)) {
    throw 'STOP: the home folder already has AIHB_OCT_2026, and it is not a Git checkout. It was not replaced.'
  }
  $remote = (& git -C $R remote get-url origin)
  if ($LASTEXITCODE -ne 0) { throw 'STOP: Git could not read the existing origin.' }
  if ([string]::IsNullOrWhiteSpace([string]$remote) -or ([string]$remote).Trim() -ne $origin) {
    throw 'STOP: that checkout has a different origin. It was not replaced, reset, pulled, or cleaned.'
  }
  & git -C $R rev-parse --verify HEAD
  if ($LASTEXITCODE -ne 0) { throw 'STOP: existing checkout has no valid HEAD. Keep it unchanged.' }
  $usingExisting = $true
} else {
  & git -c core.autocrlf=false clone $origin $R
  if ($LASTEXITCODE -ne 0) { throw 'STOP: clone failed. No partial folder was cleaned up by this step.' }
}
$M = Join-Path $R 'AI_Harness_Bootcamp_2\module-00-setup'
$lab = Join-Path $M 'shared\MODULE_00_LAB.md'
if (-not (Test-Path -LiteralPath $lab)) {
  throw 'STOP: this checkout does not contain the Module 0 lab. It was not reset, pulled, or cleaned.'
}
$frozen = @(
  'AI_Harness_Bootcamp_2\module-01-mission-thread\shared\case\SOURCE_MANIFEST.json',
  'AI_Harness_Bootcamp_2\module-08-change-eval\shared\controls\policy.json',
  'AI_Harness_Bootcamp_2\module-10-capstone\shared\baseline\run.json'
)
foreach ($rel in $frozen) {
  $path = Join-Path $R $rel
  if (-not (Test-Path -LiteralPath $path)) {
    throw 'STOP: a frozen control is missing. The checkout was not reset, pulled, or cleaned.'
  }
  $item = Get-Item -LiteralPath $path -Force
  if ($item.PSIsContainer -or ($item.Attributes -band [IO.FileAttributes]::ReparsePoint)) {
    throw 'STOP: a frozen control is a folder or a link. It was not followed or changed.'
  }
  $bytes = [IO.File]::ReadAllBytes($path)
  if ([Array]::IndexOf($bytes, [byte]13) -ge 0) {
    throw 'HOLD: a frozen control has rewritten line endings. The checkout was not reset, cleaned, pulled, or renormalized.'
  }
}
if ($usingExisting) {
  Write-Output 'Using the existing course checkout.'
} else {
  Write-Output 'Cloned the course checkout.'
}
Write-Output 'Line endings unchanged.'
Write-Output $R
Write-Output $M
```

**Expected:** either `Using the existing course checkout.` or `Cloned the course checkout.`, then `Line endings unchanged.`, then the absolute course path and the Module 0 path.

**Stop:** the folder exists but is not the course origin, Git cannot read the origin, the clone fails, the lab file is missing, a frozen control is missing or is a folder or link, or a frozen control contains a rewritten line ending. The hold line is `HOLD: a frozen control has rewritten line endings. The checkout was not reset, cleaned, pulled, or renormalized.`

**Recovery:** leave the existing folder in place. If it is the wrong project, choose a different computer folder only with the person who supports your machine; do not delete, reset, pull, or clean this one. If the hold names rewritten line endings, do not edit those files and do not renormalize them. Ask the person who supports your machine before moving the folder aside. After `$HOME\Documents\AIHB_OCT_2026` is no longer occupied, run this block again so the new copy is intact. If a copy you just made still prints that hold, stop and save the message. If the clone failed before creating the folder, correct the reported access or network problem before another attempt. If a partial folder was created and it is not a valid course checkout, stop and save the Git message. The one-command setting is documented in [Git core.autocrlf](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coreautocrlf).

`$R` and `$M` belong to this window. You will set them again in the window that runs the readiness check.

## Enter the key without showing it

Type the key at the hidden prompt and press Enter. The command only waits for your input; it does nothing else. Do not paste the key into the command, a file, a profile, or a chat. See [Connect the course account without leaking a key](../shared/CREDENTIALS.md) for the rules on where the key must not go.

**Terminal: Windows PowerShell 5.1, ordinary user, same window.**

```powershell
$secret = Read-Host -Prompt 'OpenRouter API key' -AsSecureString
```

**Expected:** the prompt returns, and the key does not appear as readable text. Windows PowerShell may show asterisks. That is still hidden input.

**Stop:** the key appears in readable text, or you pasted it into the command line instead of the prompt.

**Recovery:** if the key was displayed or pasted into a command, revoke it with the provider, use the replacement, and run only this command again. Do not continue with a key that has been displayed.

## Load the key into this process only

Load the hidden value into this process. The command makes it a process environment variable, clears the temporary copy, and prints only `SET` or `MISSING`. A SecureString holds the value you entered at the hidden prompt. To convert it, the command briefly uses a BSTR (an unmanaged string) and then zeroes that memory. It does not write the key to a file, a profile, or your saved user environment.

The conversion and zeroing methods are [SecureStringToBSTR](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.interopservices.marshal.securestringtobstr) and [ZeroFreeBSTR](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.interopservices.marshal.zerofreebstr).

**Terminal: Windows PowerShell 5.1, ordinary user, same window.**

```powershell
$bstr = [IntPtr]::Zero
$plain = $null
try {
  if ($null -eq $secret) { throw 'STOP: run the hidden read in this window first.' }
  $bstr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secret)
  $plain = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($bstr)
  if ([string]::IsNullOrWhiteSpace($plain)) {
    Write-Output 'MISSING'
  } else {
    $env:OPENROUTER_API_KEY = $plain
    Write-Output 'SET'
  }
} finally {
  if ($bstr -ne [IntPtr]::Zero) {
    [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($bstr)
  }
  $plain = $null
  if ($null -ne $secret) { $secret.Dispose() }
  $secret = $null
}
```

**Expected:** `SET`.

**Stop:** `MISSING`, an error before either word, or any output that contains the key.

**Recovery:** run the hidden-read command again in this same window, then run this command again. Do not check the key by printing the environment. Do not save it with `SetEnvironmentVariable`.

## Open an independent window and read the difference

A new window opened from the Start menu is a new process, so it should not have the key you loaded only into the earlier window. A child process is different: if you type `powershell` in the window holding the key, the child can inherit it. Seeing `SET` in that child does not mean the key was saved in a profile or file. On its own, `SET` also does not show whether the key was saved, exposed, or accepted for authentication. Seeing `MISSING` in a new terminal window opened from Start checks that the new process did not receive a saved key.

Once you have seen `SET`, close all terminal windows, including Windows Terminal and editor terminals, then open Windows PowerShell again through Start. A new tab may keep the old PATH, so do not type `powershell` in the old window either. The new window will not have `$PY`, `$R`, or `$M`. Run the full [Git and Python resolver](#resolve-the-real-python-312-executable) there to set `$R`, `$M`, and `$PY` again and check Git. Do not repair PATH in this new window.

**Terminal: Windows PowerShell 5.1, ordinary user, newly opened from Start; Git and Python resolved here.**

```powershell
$dest = Join-Path $env:LOCALAPPDATA 'omp\omp.exe'
$found = (Get-Command omp -ErrorAction SilentlyContinue).Source
if ($found -ine $dest) { throw 'STOP: omp resolves to a different or missing program. Preserve that installation.' }
Write-Output $found
$ompVersion = @(& $dest --version)
if ($LASTEXITCODE -ne 0) { throw 'STOP: OMP version command failed.' }
if ($ompVersion.Count -ne 1 -or ([string]$ompVersion[0]).Trim() -ne 'omp/18.3.5') { throw 'STOP: OMP version differs from omp/18.3.5.' }
Write-Output $ompVersion
if ([string]::IsNullOrWhiteSpace($env:OPENROUTER_API_KEY)) { Write-Output 'MISSING' } else { Write-Output 'SET' }
```

**Expected:** the found path is the verified `\omp\omp.exe`, the version line is `omp/18.3.5`, and the last line is `MISSING`.

**Stop:** the command is missing, the path differs, the version differs, or a window you opened fresh from the Start menu prints `SET` before you type a key.

**Recovery:** if the program path or version is wrong, return to the install step and do not overwrite a different file. If this window, opened fresh from the Start menu, prints `SET`, run the next check before you enter a key. Do not print the variable.

## Check for a saved key without displaying it

Run this only if the independent window printed `SET` before you entered a key. It checks the saved environment and PowerShell profiles for the variable name without printing its value or a matching line.

**Terminal: Windows PowerShell 5.1, ordinary user, same window.**

```powershell
foreach ($scope in @('User', 'Machine')) {
  $saved = [Environment]::GetEnvironmentVariable('OPENROUTER_API_KEY', $scope)
  if (-not [string]::IsNullOrEmpty($saved)) {
    $saved = $null
    throw ('STOP: a saved ' + $scope + ' environment entry exists. The value was not printed.')
  }
}
$profiles = @(
  $PROFILE.CurrentUserCurrentHost,
  $PROFILE.CurrentUserAllHosts,
  $PROFILE.AllUsersCurrentHost,
  $PROFILE.AllUsersAllHosts
)
foreach ($path in $profiles) {
  if ($path -and (Test-Path -LiteralPath $path)) {
    if (Select-String -LiteralPath $path -Pattern 'OPENROUTER_API_KEY' -SimpleMatch -Quiet) {
      throw 'STOP: a PowerShell profile names the key variable. The line was not printed.'
    }
  }
}
Write-Output 'No saved environment entry or profile reference was found.'
```

**Expected:** a saved-entry or profile stop identifies a possible source. If neither is found, the line is `No saved environment entry or profile reference was found.`

**Stop:** if the check finds a saved entry or a profile reference. Also stop if the independent window printed `SET` but this check finds nothing: something else is supplying the variable, and you still must not print it.

**Recovery:** find the source before changing it. A profile may mention the variable only to check whether it exists; an approved parent process may also pass it along. Inspect locally without copying any value. Revoke the key if you find that it was exposed or saved without authorization. If the check names an unauthorized User-scope entry, remove only that entry below. For a Machine-scope entry or a profile assignment, ask the device owner to approve the fix; do not delete a profile or change machine settings without knowing what they do. Once the cause is resolved, open another window from Start and repeat the check that shows only whether the key is present.

Remove only the saved User entry identified by the preceding check.

**Terminal: Windows PowerShell 5.1, ordinary user, same window.**

```powershell
[Environment]::SetEnvironmentVariable('OPENROUTER_API_KEY', $null, 'User')
Write-Output 'User environment name cleared. The value was not printed.'
```

**Expected:** the cleared line, and no key text.

**Stop:** you did not first see a stop line that named the User scope, or the key appears in the output.

**Recovery:** run this only after the check names the User scope. For a Machine scope or profile finding, use the recovery in the previous step instead of this command.

## Enter the key again in the new window

Run the readiness check in the new terminal window opened from Start, because its PATH comes from your saved user setting. The key will not be there, so repeat the hidden read and then the separate conversion. Do not skip the read or paste the key into the conversion command.

**Terminal: Windows PowerShell 5.1, ordinary user, same window.**

```powershell
$secret = Read-Host -Prompt 'OpenRouter API key' -AsSecureString
```

**Expected:** the prompt returns, and the key is not readable on screen.

**Stop:** the key is visible as readable text.

**Recovery:** revoke a displayed key, then run this read again.

Load the hidden value into this PowerShell process, then clear the temporary copy.

**Terminal: Windows PowerShell 5.1, ordinary user, same window.**

```powershell
$bstr = [IntPtr]::Zero
$plain = $null
try {
  if ($null -eq $secret) { throw 'STOP: run the hidden read in this window first.' }
  $bstr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secret)
  $plain = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($bstr)
  if ([string]::IsNullOrWhiteSpace($plain)) {
    Write-Output 'MISSING'
  } else {
    $env:OPENROUTER_API_KEY = $plain
    Write-Output 'SET'
  }
} finally {
  if ($bstr -ne [IntPtr]::Zero) {
    [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($bstr)
  }
  $plain = $null
  if ($null -ne $secret) { $secret.Dispose() }
  $secret = $null
}
```

**Expected:** `SET`.

**Stop:** `MISSING`, or any output that contains the key.

**Recovery:** run the hidden read and this conversion again in this window. Do not continue to the readiness check on `MISSING`.

## Prepare a fresh readiness check

Create a fresh work folder outside the course checkout for one attempt. The model will read a token and write only `from-omp.txt`. Python's secrets module creates the token outside the work folder, then copies it in so the model has to read it. For now, the evidence folder is only a path: don't create that folder or `from-omp.txt` yourself.

Run the full Git and Python resolver in this window before this block, because `$PY` from an earlier window won't be here. This block sets `$R` and `$M` again. Stay in this window through the checker and report. A new Start-menu window won't keep `$PY`, `$R`, `$M`, `$attempt`, or the key.

Windows PowerShell removes quotation marks inside a short `-c` program before Python sees them. Instead, the programs below reach Python through standard input (the text piped into a program), with each file path passed as a separate argument. That keeps the quotation marks in the program. These programs write UTF-8 text without printing the token. This block also stops if a frozen control was rewritten; it does not repair that copy. See [about_Quoting_Rules](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_quoting_rules?view=powershell-5.1) for the quoting rules. `$OutputEncoding` controls how PowerShell encodes the text it sends; see [about_Preference_Variables](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_preference_variables?view=powershell-5.1).

**Terminal: Windows PowerShell 5.1, ordinary user, same window.**

```powershell
if (-not $PY) { throw 'STOP: resolve Python again in this window before the readiness check.' }
$R = Join-Path $HOME 'Documents\AIHB_OCT_2026'
$M = Join-Path $R 'AI_Harness_Bootcamp_2\module-00-setup'
$frozen = @(
  'AI_Harness_Bootcamp_2\module-01-mission-thread\shared\case\SOURCE_MANIFEST.json',
  'AI_Harness_Bootcamp_2\module-08-change-eval\shared\controls\policy.json',
  'AI_Harness_Bootcamp_2\module-10-capstone\shared\baseline\run.json'
)
foreach ($rel in $frozen) {
  $path = Join-Path $R $rel
  if (-not (Test-Path -LiteralPath $path)) {
    throw 'STOP: a frozen control is missing. Nothing was created for this readiness check.'
  }
  $item = Get-Item -LiteralPath $path -Force
  if ($item.PSIsContainer -or ($item.Attributes -band [IO.FileAttributes]::ReparsePoint)) {
    throw 'STOP: a frozen control is a folder or a link. It was not followed or changed.'
  }
  $bytes = [IO.File]::ReadAllBytes($path)
  if ([Array]::IndexOf($bytes, [byte]13) -ge 0) {
    throw 'HOLD: a frozen control has rewritten line endings. Nothing was created, and the checkout was not changed.'
  }
}
$runId = [guid]::NewGuid().ToString('n')
$run = Join-Path (Join-Path $HOME 'course-evidence\reformation-qa') $runId
$attempt = Join-Path $run 'module-00'
$proof = Join-Path $attempt 'proof'
$tokenFile = Join-Path $attempt 'run-token.txt'
$evidence = Join-Path $attempt ('evidence-' + [guid]::NewGuid().ToString('n'))
if ((Test-Path -LiteralPath $proof) -or (Test-Path -LiteralPath $tokenFile) -or (Test-Path -LiteralPath $evidence)) {
  throw 'STOP: an attempt path already exists. Nothing was overwritten.'
}
New-Item -ItemType Directory -Path $proof | Out-Null
$savedOutputEncoding = $OutputEncoding
$OutputEncoding = [System.Text.UTF8Encoding]::new($false)
try {
@'
import pathlib, secrets, sys
pathlib.Path(sys.argv[1]).write_text(secrets.token_hex(16) + "\n", encoding="utf-8")
'@ | & $PY - $tokenFile
if ($LASTEXITCODE -ne 0) { throw 'STOP: the token file was not written.' }
Copy-Item -LiteralPath $tokenFile -Destination (Join-Path $proof 'run-token.txt')
$promptFile = Join-Path $proof 'prompt.txt'
@'
import pathlib, sys
pathlib.Path(sys.argv[1]).write_text("Use only the course_read and course_write tools. Do not use any other tool.\nUse course_read to read the file run-token.txt in your work directory. The token is the exact text of that file, with surrounding space removed.\nUse course_write to write only the file from-omp.txt. The entire file must be the two words omp works, then one space, then that exact token. Do not write any other file.\n", encoding="utf-8")
'@ | & $PY - $promptFile
if ($LASTEXITCODE -ne 0) { throw 'STOP: the prompt file was not written.' }
} finally {
  $OutputEncoding = $savedOutputEncoding
}
Write-Output $proof
Write-Output $tokenFile
Write-Output $evidence
Write-Output ('evidence exists now: ' + (Test-Path -LiteralPath $evidence))
```

**Expected:** three absolute paths, then `evidence exists now: False`. The token value is not printed.

**Stop:** Python is missing, a frozen control is missing or rewritten, a path already exists, a file cannot be written, or the evidence line is `True`. The line-ending hold is `HOLD: a frozen control has rewritten line endings. Nothing was created, and the checkout was not changed.`

**Recovery:** If the stop says to resolve Python, run that block in this window, then run this block again. If the hold names rewritten line endings, return to the checkout step without editing the course files. Leave any partial attempt in place, and run this block again only after the checkout hold is cleared so the new attempt gets new paths. Don't delete the course checkout or create the evidence folder or `from-omp.txt` by hand.

## Ask for the one permitted write

Run the launcher once. It starts the pinned Oh My Pi binary with permission to write only `from-omp.txt` and reads the key from this PowerShell process. If the key is missing, the launcher stops before creating the evidence folder. If the live attempt fails, it keeps the evidence it created. Don't run the launcher again against a work folder that already contains `from-omp.txt`.

**Terminal: Windows PowerShell 5.1, ordinary user, same window.**

```powershell
$launcher = Join-Path $R 'shared\run_omp.py'
if (Test-Path -LiteralPath $evidence) { throw 'STOP: the evidence path already exists. Choose a new attempt.' }
if (Test-Path -LiteralPath (Join-Path $proof 'from-omp.txt')) { throw 'STOP: the work folder already has a write. Keep it and start a new attempt.' }
& $PY $launcher --workdir $proof --prompt $promptFile --evidence $evidence --allow-write 'from-omp.txt'
if ($LASTEXITCODE -ne 0) { throw ('HOLD: launcher exit ' + $LASTEXITCODE + '. Preserve this attempt and correct the reported cause.') }
Write-Output 'launcher exit 0'
if (-not (Test-Path -LiteralPath $evidence -PathType Container)) { throw 'HOLD: launcher produced no evidence folder.' }
Write-Output ('evidence exists after launch: ' + (Test-Path -LiteralPath $evidence))
```

**Expected:** the launcher finishes, the exit line is `launcher exit 0`, and the evidence folder now exists. The launcher may also print a status line of its own. That line does not complete the readiness check.

**Stop:** exit 2, especially with a missing-key hold, means a prerequisite failed. The evidence folder should still be absent, and you must not invent the result file. Exit 1 means the live attempt failed. Exit 0 with no evidence folder is also a stop.

**Recovery:** On exit 2 with no evidence folder, correct the named prerequisite. Enter the key again only if the message says it's missing, then return to “Prepare a fresh readiness check” with new paths. On exit 1, or if `from-omp.txt` already exists, keep both folders and correct the specific failure named in the evidence before preparing a fresh readiness check. Don't retry in the same work folder or write `from-omp.txt` yourself.

## Check the write against the token and the receipt

Run the checker with the work folder, the token file outside it, and the evidence folder. It passes only if `from-omp.txt` contains `omp works`, one space, and this run's token, and the `course_write` receipt agrees with the file on disk.

**Terminal: Windows PowerShell 5.1, ordinary user, same window.**

```powershell
$checker = Join-Path $M 'shared\case\verify_tool_proof.py'
& $PY $checker $proof $tokenFile $evidence
if ($LASTEXITCODE -ne 0) { throw ('HOLD: checker exit ' + $LASTEXITCODE + '. Preserve this attempt.') }
Write-Output 'checker exit 0'
```

**Expected:** the checker's last result line is `READINESS CHECK PASS`, and the exit line is `checker exit 0`.

**Stop:** The last result line is `READINESS CHECK HOLD`, the checker exits nonzero, or the result file is missing. Creating the file yourself does not count as a pass.

**Recovery:** keep this attempt. Correct the specific failure named by the checker before returning to “Prepare a fresh readiness check” with new folders. Do not edit `from-omp.txt` to make the words match.

## Read the actual file on disk

Open the file from disk separately from the receipt check. The model saying it wrote a file doesn't show what's on disk.

**Terminal: Windows PowerShell 5.1, ordinary user, same independent window.**

```powershell
Get-Content -LiteralPath (Join-Path $proof 'from-omp.txt') -Raw -ErrorAction Stop
```

**Expected:** `omp works` followed by one space and this attempt's token, as checked by `READINESS CHECK PASS`. The checker also checks the real receipts and the pinned OMP, provider, and model identities.

**Stop:** the file cannot be read or the content differs.

**Recovery:** Keep this attempt and resolve the reported file or evidence problem before creating a new one. Don't edit the file to make it pass.

## Record prerequisites, not the live turn

This report checks whether Git, Python, Oh My Pi, the checkout, and the key are present in this process. A passing report checks those prerequisites, not the live write; the readiness check you already ran checks the write. Local changes in the checkout are no reason to reset, pull, or clean it. Stay in this PowerShell window for the report: `$R`, `$M`, and `$attempt` are set here, but a new Start-menu window has none of them or the key.

Open `$M\scripts\verify-setup.ps1` in your text editor and review the local checker before running it. Inspect the effective policy and its scopes. See [PowerShell 5.1 execution policies](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-5.1).

**Terminal: Windows PowerShell 5.1, ordinary user, same proof window.**

```powershell
Get-ExecutionPolicy
Get-ExecutionPolicy -List | Format-Table -AutoSize
```

**Expected:** the effective policy and five scope settings. If the effective policy allows this reviewed checker to run, run the report below unchanged. A permissive managed policy is not, by itself, a reason to stop.

**Stop:** an organizational policy, intentional restriction, or signing requirement blocks this checker, or you cannot determine whether running it is authorized.

**Recovery:** Ask the device owner for an approved signed checker or approved way to run it. Don't change an intentional restriction or signing requirement, unblock files, paste script contents, or run an in-memory copy to get around the policy.

Use the following optional block **only** when all scopes are `Undefined`, the effective policy is the unmanaged default `Restricted`, and you have **explicit permission to run this reviewed local course checker**. The absence of Group Policy is not consent. If those conditions do not all hold, skip this block. The ordinary confirmation prompt remains visible: read it and answer **Y** only under that explicit permission; otherwise answer **N** and stop.

Temporarily permit the approved local checker in this process only.

**Terminal: Windows PowerShell 5.1, ordinary user, same proof window; only under the conditions above.**

```powershell
$effective = Get-ExecutionPolicy
$scopes = @(Get-ExecutionPolicy -List)
if ($effective -ne 'Restricted' -or @($scopes | Where-Object { $_.ExecutionPolicy -ne 'Undefined' }).Count -ne 0) {
  throw 'STOP: this is not the unmanaged default restriction. Use the owner-approved route.'
}
$permission = Read-Host 'Do you have explicit permission to run the reviewed local course checker? Type YES to confirm'
if ($permission -cne 'YES') { throw 'STOP: explicit permission was not confirmed.' }
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
$effective = Get-ExecutionPolicy
Write-Output ('Effective policy: ' + $effective)
if ($effective -ne 'RemoteSigned') { throw 'STOP: the effective policy did not permit the approved local checker.' }
```

**Expected:** after your visible confirmation, `Effective policy: RemoteSigned`. Closing this PowerShell process ends this temporary setting; close any child processes too.

**Stop:** permission is absent, a scope is configured, confirmation is declined, or the effective policy differs. A signing or organizational restriction still means stop.

**Recovery:** keep the policy output and use the device owner’s approved route. Do not use `-Force`, `Bypass`, `Unrestricted`, or a CurrentUser/LocalMachine policy write.

Run the checker directly and save its separate prerequisite report.

**Terminal: Windows PowerShell 5.1, ordinary user, same proof window.**

```powershell
$report = Join-Path $attempt 'setup-report.txt'
if (Test-Path -LiteralPath $report) { throw 'STOP: the report path already exists. It was not overwritten.' }
& (Join-Path $M 'scripts\verify-setup.ps1') -Root $R -ResultsPath $report
if ($LASTEXITCODE -ne 0) { throw ('HOLD: report exit ' + $LASTEXITCODE + '. Preserve the report and correct its first failed prerequisite.') }
Write-Output 'report exit 0'
Write-Output $report
```

**Expected:** `report exit 0`, a report file path, and a last report line that begins `SETUP CHECK PASS`. The report does not contain the key.

**Stop:** the script is blocked by execution policy, exits nonzero, reports `SETUP CHECK HOLD`, the report path already exists, or the report contains the key. A hold in this report concerns a prerequisite. Editing the result file won't fix it, and a pass in this report does not replace `READINESS CHECK PASS`.

**Recovery:** Fix the first failed prerequisite named in the report. If the old report file exists, choose a new report path before running the report command again. Don't reset, pull, or clean the checkout because the report mentions local changes. Continue only after both `SETUP CHECK PASS` and `READINESS CHECK PASS`, and after reading the file separately from disk.


## Set up local Obsidian

Obsidian lets you follow links and edit notes in a **vault**, an ordinary folder of Markdown text files. Allow about 20–30 minutes for installation and the file round-trip below; download time varies. Keep this vault on the native Windows disk alongside your native Python workflow, outside the checkout and any synced folder. It does not belong in n8n’s Ubuntu home. [Obsidian stores local files and refreshes external edits](https://github.com/obsidianmd/obsidian-help/blob/master/en/Files%20and%20folders/How%20Obsidian%20stores%20data.md).

### Preserve an existing app, or install the verified Windows release

First look for **Obsidian** in **Start** and **Settings → Apps → Installed apps**. If it's there, open it normally and leave its installation, profile, and personal vaults in place. Skip the download and installer blocks; don't upgrade or downgrade it to match this guide. When you open the practice vault, record the version shown in Obsidian's Settings. If you're unsure where the installation came from or whether it's in good condition, record **Obsidian HOLD** and ask the device owner to resolve it without replacing it.

Only when Obsidian is absent, obtain approval for a current-user installation. The reference download is the official universal Windows 1.13.7 EXE for x64 and ARM64. The fingerprint below comes from the [official release metadata](https://api.github.com/repos/obsidianmd/obsidian-releases/releases/tags/v1.13.7). The [vendor’s Windows instructions](https://github.com/obsidianmd/obsidian-help/blob/master/en/Getting%20started/Download%20and%20install%20Obsidian.md) use the universal installer.

**Terminal: Windows PowerShell 5.1, ordinary user, same native proof window.**

```powershell
$ErrorActionPreference = 'Stop'
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
if (-not $env:LOCALAPPDATA) { throw 'Obsidian HOLD: LOCALAPPDATA is missing.' }
if ((Get-Item -LiteralPath $env:LOCALAPPDATA -Force).Attributes -band [IO.FileAttributes]::ReparsePoint) {
  throw 'Obsidian HOLD: local app data is redirected; ask the owner for a local route.'
}
$ObsidianDownload = Join-Path $env:LOCALAPPDATA ('obsidian-download-' + [guid]::NewGuid().ToString('n'))
New-Item -ItemType Directory -Path $ObsidianDownload -ErrorAction Stop | Out-Null
$ObsidianInstaller = Join-Path $ObsidianDownload 'Obsidian-1.13.7.exe'
Invoke-WebRequest -Uri 'https://github.com/obsidianmd/obsidian-releases/releases/download/v1.13.7/Obsidian-1.13.7.exe' -OutFile $ObsidianInstaller -UseBasicParsing
$ObsidianHash = (Get-FileHash -LiteralPath $ObsidianInstaller -Algorithm SHA256).Hash.ToLowerInvariant()
if ($ObsidianHash -cne 'f233dc24896b3f2d5f9e4b01111181a561d0760b2105f0a474024c5f3143a9bc') {
  throw 'Obsidian HOLD: checksum mismatch. Do not run this file.'
}
Write-Output $ObsidianInstaller
Write-Output 'Obsidian download checksum matched; installer has not run.'
```

**Expected:** the fresh download path and checksum-match message. **HOLD:** failed download, redirected location, or fingerprint mismatch. **Recovery:** keep that attempt and resolve the named failure; a retry uses a fresh folder. Never execute the failed download.

After the match, run this separate installer step. Choose **Only for me** if the installer asks who should receive the installation, and use the offered current-user location only if it is empty. Cancel if it detects an existing installation, requests a replacement, or requires unapproved elevation. Do not select an all-users route to get around a policy denial. [Start-Process](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/start-process?view=powershell-5.1) starts this installer with your ordinary-user context.

**Terminal: Windows PowerShell 5.1, ordinary user, same window; approved fresh install only.**

```powershell
if (-not $ObsidianInstaller) { throw 'Obsidian HOLD: verify the fresh download first.' }
if ((Get-FileHash -LiteralPath $ObsidianInstaller -Algorithm SHA256).Hash.ToLowerInvariant() -cne 'f233dc24896b3f2d5f9e4b01111181a561d0760b2105f0a474024c5f3143a9bc') {
  throw 'Obsidian HOLD: installer bytes changed. Do not run it.'
}
$ObsidianInstallProcess = Start-Process -FilePath $ObsidianInstaller -PassThru -Wait
if ($ObsidianInstallProcess.ExitCode -ne 0) { throw 'Obsidian HOLD: installer did not finish successfully.' }
```

**Expected:** the installer completes and **Start → Obsidian** opens a real application window. **HOLD:** a refusal, an unexpected existing app, an unsuccessful installer exit, or no window. **Recovery:** Keep the message for the device owner. Don't delete a profile, reinstall over an existing app, or disable a Windows security control.

### Open the exact practice vault and save a linked reply

This creates a fresh vault and records expected values outside it. Use the native `$PY`, `$R`, and `$M` from this page. If you reopened PowerShell, rerun [the Python resolver](#resolve-the-real-python-312-executable) first. No provider call or key entry is needed here.

**Terminal: Windows PowerShell 5.1, ordinary user, same native window.**

```powershell
if (-not $PY -or -not $M) { throw 'Obsidian HOLD: restore the native Python and course paths first.' }
$ObsidianHelper = Join-Path $M 'scripts\obsidian_readiness.py'
if (-not (Test-Path -LiteralPath $ObsidianHelper -PathType Leaf)) { throw 'Obsidian HOLD: course helper is missing.' }
$ObsidianRoot = Join-Path $HOME ('obsidian-readiness-' + [guid]::NewGuid().ToString('n'))
& $PY $ObsidianHelper initialize --root $ObsidianRoot
if ($LASTEXITCODE -ne 0) { throw 'Obsidian HOLD: initialize failed; preserve this attempt.' }
$ObsidianVault = Join-Path $ObsidianRoot 'vault'
Write-Output $ObsidianRoot
Write-Output $ObsidianVault
```

**Expected:** `Created practice vault:` names exactly the printed `$ObsidianVault`, with `Start`, `Token`, and a blank `Reply`. Save the printed root path for this attempt. **HOLD:** any helper error, missing helper, or redirected/synced home. **Recovery:** keep the attempt; ask the owner to provide a complete checkout or an approved local, unsynced home location. Do not initialize inside an existing vault or copy the vault to WSL.

**Window: native Windows Obsidian, ordinary user.**

1. In the vault chooser, choose **Open folder as vault → Open**. If a personal vault is open, use **Open another vault** first; leave its files and settings intact. Select the exact folder printed as `$ObsidianVault`, not its parent or the course checkout.
2. In this practice vault’s **Settings → Community plugins**, leave **Restricted mode** on; turn it on for this vault if it is off. Under **Settings → Core plugins**, turn **Sync** off if it is on. Do not sign in, connect a remote vault, install a plugin, or configure MCP. In **Settings → General**, record the installed version, then close Settings.
3. Open **Start** in the file list. Switch to **Reading view** through the note’s view control if needed so the links are clickable. Click **Token**, read its current token, then follow **Reply** from Token.
4. Switch Reply to **Editing view** using its view control. Enter only the token you read, on one line, with no heading, quote marks, or explanation. Press **Ctrl+S** and wait for the note to save.

**Expected:** both links open existing notes, and Reply contains the token you saw. **HOLD:** the wrong vault, a missing note or link, blocked editing, or unavailable settings. **Recovery:** Reopen the exact printed vault and check the named issue. Don't enter the reply from a terminal or use a text editor instead of doing the work in the app window.

**Terminal: Windows PowerShell 5.1, ordinary user, same native window.**

```powershell
& $PY $ObsidianHelper check --root $ObsidianRoot
if ($LASTEXITCODE -ne 0) { throw 'Obsidian HOLD: initial saved reply did not pass.' }
```

**Expected:** `Token generation 1: initial token; external refresh not yet exercised` and `PASS: Obsidian file round-trip; GUI observation still required`, plus a new disk-record path. **HOLD:** any other result. **Recovery:** In Obsidian, correct only Reply to match the current Token, save, and rerun `check`; keep every record. Don't edit Start, Token, or the expected-value records to force a match.

### Observe an outside edit, save again, and reopen

Keep the practice vault open and show **Token** in Reading view. The next command changes Token on disk while keeping your old Reply.

**Terminal: Windows PowerShell 5.1, ordinary user, same native window.**

```powershell
& $PY $ObsidianHelper refresh --root $ObsidianRoot
if ($LASTEXITCODE -ne 0) { throw 'Obsidian HOLD: external refresh failed; preserve this attempt.' }
```

**Expected:** `Source token rotated outside Obsidian; your saved reply was preserved.` **HOLD:** a helper error. **Recovery:** keep the attempt and the error for support; do not overwrite its records or reinitialize it.

**Window: native Windows Obsidian, same practice vault.** Return to Token, which is still open, and check that its value has changed before you close or reopen anything. Follow **Reply**, replace the old value with the new value in Editing view, and press **Ctrl+S**. Close only this practice-vault window. Open Obsidian from Start again and reopen the exact `$ObsidianVault` through the vault chooser if it did not reopen automatically. Open Reply and confirm the new value remains.

**Expected:** the outside edit appears in the open app, and your second saved reply survives reopening. **HOLD:** stale Token, unsaved Reply, or a different reopened vault. **Recovery:** record what failed and the exact path. Seeing the new token only after a restart doesn't show that Obsidian refreshed while open; fix the cause, run another `refresh` while the correct vault is open, then repeat the GUI edit, save, and reopen steps.

**Terminal: Windows PowerShell 5.1, ordinary user, same native window.**

```powershell
& $PY $ObsidianHelper check --root $ObsidianRoot
if ($LASTEXITCODE -ne 0) { throw 'Obsidian HOLD: reopened saved reply did not pass.' }
```

**Expected:** a refreshed token generation, the same qualified PASS line, and a new record path. **HOLD:** mismatch or helper failure. **Recovery:** confirm the exact vault and saved Reply in Obsidian, keep the record of what failed, and repeat the failed step.

In Notepad, save a new plain-text file named `gui-observation.txt` directly in the printed `$ObsidianRoot`, outside `vault`. Use **Save As**, choose **All files**, and don't replace an existing record. Write down the date, native Windows build/architecture, Obsidian version, exact vault path, what you saw when you followed Start → Token → Reply, both edits and saves, the outside change appearing in the open app, and the reopened Reply. Include the two paths for the files read from disk and any remaining failure. Attach screenshots only of the practice vault if useful; don't include keys or unrelated personal windows.

Record **Obsidian READY** only if you saw those actions on this laptop and both checks of the files on disk passed. Otherwise record **Obsidian HOLD** and name the action that failed or was unobserved. A helper PASS or an `.obsidian` folder alone isn't enough. Keep this result separate from OMP and n8n; an Obsidian HOLD doesn't erase either existing result. What happened in macOS or WSL doesn't confirm how the native Windows app works on this laptop.

## Prepare local n8n for Module 7

Open the local visual workflow editor and confirm that a saved workflow remains after you stop and restart it. Keep this result separate from `SETUP CHECK PASS` and the live OMP `READINESS CHECK PASS`. An n8n HOLD does not erase an OMP pass, but Module 7 needs n8n ready. The time needed for installation and image downloads varies with the device and network.

### Check the Windows host and approvals

[Microsoft’s simplified WSL installation](https://learn.microsoft.com/en-us/windows/wsl/install) requires Windows 10 build 19041+ or Windows 11. Docker’s current WSL backend requirements are stricter: WSL package 2.1.5+, Windows 10 22H2 build 19045 or Windows 11 23H2 build 22631+, a supported edition and servicing status, 8 GB RAM, SLAT, hardware virtualization enabled, and the Windows Server service (`LanmanServer`) enabled with Automatic startup. Docker lists Enterprise, Pro, and Education in its requirements and separately discusses Home for Linux containers; have the owner confirm eligibility for the exact host. Windows Server is unsupported. See [Docker’s current Windows requirements](https://docs.docker.com/desktop/setup/install/windows-install/) before downloading. Passing the earlier native-tool or Microsoft WSL floor alone is insufficient.

On Windows Arm, choose the **Arm (Early Access)** download only if the owner approves its Early Access status; Windows containers are unsupported. Published arm64 images do not show that this course stack works on a Windows Arm laptop. Keep n8n on HOLD until this device passes the checks below. An x64 host must pass them too.

Ask the device owner to confirm [Docker Desktop licensing](https://docs.docker.com/subscription-billing/desktop-license/). It's free for personal use, education, non-commercial open source, and qualifying small businesses (fewer than 250 employees AND under $10 million revenue). Professional use outside those limits and use by government entities require a paid subscription. Don't assume a work laptop qualifies because this is a class.

The [official stack](https://raw.githubusercontent.com/n8n-io/n8n/master/docker/get-n8n-compose.yml) includes `n8n`, `runners`, `sandbox-certs`, `sandbox-api`, `sandbox-runner-1`, and `searxng`. The sandbox runner uses privileged Docker-in-Docker. Obtain owner approval for that privilege and ordinary-user Docker access before starting it. Keep Assistant off; do not enter a provider key into n8n.

Check existing Docker work and the Windows port before changing settings. If Docker Desktop is already running, open its window and check **Containers**. If it's installed but stopped, ask the owner to review and approve what starting it might do to existing work before you launch it. Starting its daemon can restart unrelated containers, even ones stopped by hand that have an `always` policy; see [Docker restart policies](https://docs.docker.com/engine/containers/start-containers-automatically/). After approval, launch Desktop and check its containers. Don't stop them to make room.

**Terminal: Windows PowerShell, ordinary user, new inspection window.**

```powershell
Get-ComputerInfo -ErrorAction Stop | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber, CsTotalPhysicalMemory
Get-Service -Name LanmanServer -ErrorAction Stop | Select-Object Name, Status, StartType
wsl --version
Write-Output ('WSL version exit: ' + $LASTEXITCODE)
wsl --list --verbose
Write-Output ('Distribution list exit: ' + $LASTEXITCODE)
if (Get-Command docker -CommandType Application -ErrorAction SilentlyContinue) {
  docker context ls
  docker info
  docker compose version
  docker ps --all
  docker volume ls
} else { Write-Output 'Docker CLI absent; inspect installed apps before installing.' }
Get-NetTCPConnection -State Listen -ErrorAction Stop | Where-Object LocalPort -eq 5678 | Select-Object LocalAddress, LocalPort, OwningProcess
```

**Expected:** you've recorded the host and WSL versions without changing the distributions. You've recorded the Docker inventory or noted that Docker is absent. For a fresh installation, nothing is listening on port 5678. An existing course instance may already use that port.

**Stop:** licensing, privileges, host support, virtualization, or WSL approval is unresolved; Docker points to an unexpected/remote engine; existing applications or port ownership are unclear; any inspection fails.

**Recovery:** work through the specific finding with the owner. Keep all applications, containers, volumes, checkouts, and earlier attempts. Don't kill a process, prune Docker, reset Desktop, or change contexts without knowing their effects. If a WSL/Docker prerequisite is denied, record **n8n HOLD** separately from OMP readiness.

### Select Ubuntu for the n8n bridge only

Keep any suitable existing Ubuntu 24.04 or 26.04 WSL 2 distribution; never unregister it. Leave all native Windows paths and credentials from earlier steps where they are. Don't clone the course again, install Linux OMP/Python/Git, copy keys, or move native files. Use this Ubuntu home only for the separate n8n setup. Check `wsl --list --online` before a new install. If WSL is missing or blocked, have the owner resolve the installation prerequisite first and record a policy denial as n8n HOLD.

### Install Ubuntu only when a suitable distribution is absent

If you already have a suitable Ubuntu, skip this section. If you don't know an installed Ubuntu's release, select it by its exact name and launch it using the steps below before you decide to install anything. For a new install, first check that the online list includes the exact NAME `Ubuntu-24.04`; don't use the changing `Ubuntu` alias. After the owner approves the install, open PowerShell with **Run as administrator**.

Install the named release. Microsoft's `--install` command creates new distributions as WSL 2. The command `wsl --set-default-version 2` sets the default for **new** distributions only; it won't convert an existing WSL 1 installation.

**Terminal: Windows PowerShell, elevated, newly opened for the approved installation.**

```powershell
wsl --list --online
if ($LASTEXITCODE -ne 0) { throw 'STOP: online list failed.' }
$CourseInstallName = Read-Host 'Type Ubuntu-24.04 only if that exact NAME appears in the online list'
if ($CourseInstallName -cne 'Ubuntu-24.04') { throw 'STOP: the exact pinned distribution was not confirmed.' }
wsl --install -d Ubuntu-24.04
if ($LASTEXITCODE -ne 0) { throw 'STOP: preserve the install message; complete any requested restart before rechecking.' }
```

**Expected:** Ubuntu-24.04 installs, or Windows requests a restart. Save open work and restart Windows when requested. Do not paste Linux commands into PowerShell. If installation opens Ubuntu and asks for a username, create an ordinary Linux username and password there; password characters are invisible. Wait until that setup finishes before continuing.

**Stop:** the exact release is unavailable, help text appears instead of installation, or installation fails.

**Recovery:** Keep the message and work through [Microsoft’s installation troubleshooting](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting#installation-issues) with the owner. If Windows asked you to restart, check the installed list again before doing anything else. Don't reinstall a distribution that's already there.

### Select the exact distribution

After any restart, open a regular Windows PowerShell window. At the prompt, enter the exact installed NAME, even if it isn't `Ubuntu-24.04`. That way you keep an existing Ubuntu 26.04 or another valid Ubuntu installation with a different name.

**Terminal: Windows PowerShell, ordinary user, newly opened from Start.**

```powershell
wsl --list --verbose
if ($LASTEXITCODE -ne 0) { throw 'STOP: could not inspect installed distributions.' }
$CourseDistroNames = @(wsl --list --quiet)
if ($LASTEXITCODE -ne 0) { throw 'STOP: could not read distribution names.' }
$CourseDistroNames = @($CourseDistroNames | ForEach-Object { ($_ -replace "`0", '').Trim() } | Where-Object { $_ })
$CourseDistro = Read-Host 'Enter the exact installed Ubuntu NAME you intend to use'
if ($CourseDistroNames -cnotcontains $CourseDistro) { throw 'STOP: that exact name is not installed.' }
$CourseWslVersion = Read-Host 'Enter the VERSION shown for that exact NAME in the verbose list'
if ($CourseWslVersion -notin @('1', '2')) { throw 'STOP: inspect the VERSION column again.' }
```

**Expected:** the name matches an installed entry, and its VERSION is `2`.

**Stop:** the selected name is absent, its release is unknown, or its VERSION is `1`.

**Recovery:** You can launch the named distribution below to check an unknown release, but don't continue to Docker integration until the Linux release check passes. If its VERSION is `1`, use the separate approved conversion below. Setting a default doesn't convert an existing distribution.

#### Convert an existing WSL 1 distribution only with approval

If the selected entry already shows VERSION `2`, skip this step. Conversion can take time or fail, so ask the owner to approve it and make a backup you can restore first, using [Microsoft's export and import commands](https://learn.microsoft.com/en-us/windows/wsl/basic-commands#export-a-distribution). The owner picks a new destination with enough space, exports the exact selected distribution, and checks that the backup can be used before conversion. Keep both the original and the backup.

Convert only the name validated in the preceding block, after backup confirmation.

**Terminal: Windows PowerShell, ordinary user, same selection window; owner-approved conversion only.**

```powershell
if (-not $CourseDistro -or $CourseDistroNames -cnotcontains $CourseDistro -or $CourseWslVersion -ne '1') { throw 'STOP: select and validate the WSL 1 entry first.' }
$CourseConversion = Read-Host 'Type BACKUP READY only after the owner approves conversion and confirms a recoverable backup'
if ($CourseConversion -cne 'BACKUP READY') { throw 'STOP: conversion is not approved and backed up.' }
wsl --set-version $CourseDistro 2
if ($LASTEXITCODE -ne 0) { throw 'STOP: preserve the conversion error and backup.' }
wsl --list --verbose
if ($LASTEXITCODE -ne 0) { throw 'STOP: could not verify the converted distribution.' }
```

**Expected:** the exact selected NAME now shows VERSION `2`.

**Stop:** conversion fails or the entry still shows `1`.

**Recovery:** keep the distribution and backup intact and ask the owner to resolve the reported failure. Never unregister or reset as a repair.

### Launch and verify Ubuntu

Before launching, check that the exact selected NAME shows VERSION `2` in the Windows list. If Ubuntu asks for a Linux username and password on first launch, enter them now. Choose a regular username; no characters appear as you type the password. If this installation already has a user, keep that user.

Launch the selected distribution by name, starting at its Linux home.

**Terminal: Windows PowerShell, ordinary user, same selection window.**

```powershell
if (-not $CourseDistro -or $CourseDistroNames -cnotcontains $CourseDistro) { throw 'STOP: select the installed distribution first.' }
wsl --distribution $CourseDistro --cd ~
if ($LASTEXITCODE -ne 0) { throw 'STOP: the named Ubuntu session returned an error.' }
```

**Expected:** Ubuntu opens as your ordinary Linux user. The PowerShell exit check runs when you leave Ubuntu.

**Stop:** launch fails or first-user setup does not finish.

**Recovery:** keep the error and ask the owner to repair the selected distribution without resetting it.

Check the user, home, release, shell, and processor inside that Ubuntu window.

**Terminal: Ubuntu Bash, ordinary Linux user, newly launched named distribution.**

```bash
course_check_wsl_host() {
  [ -n "${BASH_VERSION:-}" ] && [ "$(id -u)" -ne 0 ] || { printf 'STOP: use Bash as your ordinary Linux user\n'; return 1; }
  whoami && cd "$HOME" && pwd -P || return 1
  case "$(pwd -P)" in /home/*) ;; *) printf 'STOP: home must be under Linux /home\n'; return 1 ;; esac
  [ "$HOME" = "$(pwd -P)" ] && [ -w "$HOME" ] || { printf 'STOP: home is redirected or not writable\n'; return 1; }
  cat /etc/os-release || return 1
  . /etc/os-release
  case "$ID:$VERSION_ID" in ubuntu:24.04|ubuntu:26.04) ;; *) printf 'STOP: use supported Ubuntu 24.04 or 26.04\n'; return 1 ;; esac
  case "$(uname -m)" in x86_64|aarch64|arm64) uname -m ;; *) printf 'STOP: unsupported processor\n'; return 1 ;; esac
  df -h "$HOME"
}
course_check_wsl_host
```

**Expected:** Your regular username, a writable `/home/` path, Ubuntu `24.04` or `26.04`, and `x86_64` or `aarch64`/`arm64`. Use `df` to check available space only: you need at least 25 GB for this route, plus space for Docker images and volumes on the Windows drive. The mount-point column does not have to start with `/home`.

**Stop:** root user, unsupported release/processor, redirected home, failed command, or less than 25 GB available.

**Recovery:** Choose the correct existing Ubuntu user and distribution, or ask the owner to set up a supported one. If space is low, free space in the Linux filesystem; don't move course work under `/mnt/`.


### Update WSL only if Docker requires it

Skip this step when the recorded WSL package version meets the Docker requirement. A distribution’s VERSION `2` is not the WSL package version. For an old inbox WSL with no version output, or a package below 2.1.5, obtain owner approval for the update. Save work in every WSL distribution and Docker application; updates or restarts can interrupt them. Do not use a blanket WSL shutdown while other work is running.

**Terminal: Windows PowerShell, elevated only for the owner-approved WSL update.**

```powershell
wsl --update
if ($LASTEXITCODE -ne 0) { throw 'STOP: preserve the WSL update message.' }
wsl --version
if ($LASTEXITCODE -ne 0) { throw 'STOP: WSL package version is still unavailable.' }
wsl --list --verbose
if ($LASTEXITCODE -ne 0) { throw 'STOP: could not recheck distributions.' }
```

**Expected:** WSL package 2.1.5 or newer and the selected Ubuntu still present as VERSION `2`.

**Stop:** update denied, failed, or requests a restart; the selected distribution changed or the version is still too old.

**Recovery:** save the output and complete any owner-approved restart before rechecking in a fresh ordinary PowerShell window. Re-select the exact distribution name afterward. Never unregister, reset, or reinstall an existing distribution to repair a version check. See [Microsoft’s WSL commands](https://learn.microsoft.com/en-us/windows/wsl/basic-commands).

### Connect Docker Desktop to the selected Ubuntu

First run the Ubuntu package/process inspection below and resolve any independent Docker installation with its owner. Then install only a missing, approved **Docker Desktop for Windows**, from the official Windows download page above, matching the host processor. In the installer select **Use WSL 2 instead of Hyper-V** when offered. Follow the owner’s installation mode and elevation policy, select **Close** when complete, and save work before any required Windows restart. Existing Desktop installations stay in place.

Before enabling integration, run the Ubuntu package/process inspection below and resolve any existing independent daemon. Open **Start → Docker Desktop**. Review the agreement and select **Accept** only after licensing approval. Under **Settings → General**, select **Use WSL 2 based engine** if shown (it can be enabled automatically). Under **Settings → Resources → WSL Integration**, enable the exact Ubuntu NAME you recorded; do not rely on the default-distribution checkbox. Select **Apply** (or **Apply & restart**, if that is the displayed button) after saving affected work. If WSL Integration is missing, use the Docker taskbar menu’s **Switch to Linux containers** with owner approval; switching can interrupt existing work. Expected state: Desktop’s engine is running, using Linux containers, with integration enabled for that exact distro. See [Docker WSL integration](https://docs.docker.com/desktop/features/wsl/).

Do not install Docker Engine inside Ubuntu. If Ubuntu already has its own Docker Engine/CLI, stop and have its owner inventory and back up that work and resolve the conflict before enabling Desktop integration. Docker warns against running both installations. Do not uninstall or migrate the existing daemon as an automatic repair. If the installer later suggests `get.docker.com`, do not follow that suggestion on this route.

Open the selected Ubuntu by its exact NAME using the named launch procedure above. Use the same ordinary Linux user and Linux `$HOME` each time. Before enabling integration, inspect that Ubuntu’s installed packages and processes with the owner to identify any existing independent Docker daemon. Do not start or remove one.

**Terminal: Ubuntu Bash, ordinary Linux user, selected distribution; before installing Desktop or enabling integration.**

```bash
dpkg-query -W -f='${binary:Package} ${Status}\n' docker-ce docker-ce-cli docker.io containerd.io 2>/dev/null
pgrep -a dockerd
```

**Expected:** Ubuntu has no separately installed Docker Engine/CLI packages and no `dockerd`; the checks can return nonzero when packages or processes are absent. **Stop:** an installed package, daemon, or unclear result may mean Docker is already installed. **Recovery:** ask the owner to check for custom installations too and keep their containers and volumes while resolving the conflict. These checks cannot rule out a daemon installed by hand.

Check `curl --version` and the certificate bundle in the inspection block below. If either is missing, use this package step only after owner approval; skip it when both are present.

**Terminal: Ubuntu Bash, ordinary Linux user, selected distribution; approved missing packages only.**

```bash
sudo apt-get update && sudo apt-get install --no-upgrade curl ca-certificates
```

**Expected:** the missing download prerequisites are installed; existing packages are not upgraded by the install command. **Stop:** policy denial, package failure, or a proposal to remove existing software. **Recovery:** keep the message and resolve it with the owner; do not weaken certificate verification or install a Docker daemon. Then repeat the following inspection.

**Terminal: Ubuntu Bash, ordinary Linux user, selected WSL 2 distribution.**

```bash
course_n8n_inspect() {
  [ -n "${BASH_VERSION:-}" ] && [ "$(id -u)" -ne 0 ] || return 1
  cd "$HOME" || return 1
  case "$HOME" in /home/*) ;; *) printf 'HOLD: use your Linux home\n'; return 1 ;; esac
  [ "$(pwd -P)" = "$HOME" ] || return 1
  curl --version || return 1
  [ -s /etc/ssl/certs/ca-certificates.crt ] || return 1
  if [ -n "${DOCKER_HOST:-}" ] || [ -n "${DOCKER_CONTEXT:-}" ]; then
    printf 'HOLD: Docker override is set; review privately with owner\n'; return 1
  fi
  docker context ls || return 1
  docker info || return 1
  docker compose version || return 1
  docker ps --all || return 1
  docker volume ls || return 1
  ss -ltn 'sport = :5678' || return 1
  df -h "$HOME" || return 1
  printf 'Intended destination: %s/n8n-course\n' "$HOME"
  if [ -e "$HOME/n8n-course" ] || [ -L "$HOME/n8n-course" ]; then
    printf 'EXISTING destination: preserve it; do not run installer\n'
  else
    printf 'FRESH destination: absent\n'
  fi
}
course_n8n_inspect
```

**Expected:** `docker info` works for the approved Docker Desktop Linux engine when you run it as this ordinary user, and `docker compose version` works too. The modern plugin may report version 5; it doesn't have to start with `2.`. The Docker inventory matches the owner's known work, the destination is outside the checkout, and port 5678 is free for a fresh instance in both Windows and Ubuntu.

**Stop:** any command fails, Linux-home identity differs, an engine/context is unexpected, a Docker override is set, an unknown port listener exists, or there isn't enough storage for the full stack.

**Recovery:** review the integration and context with the owner, then try again in the intended Ubuntu shell. Never use `sudo` for the n8n installer, make the Docker socket world-writable, or start a second Ubuntu daemon. Seeing a CLI version doesn't show that you can reach the daemon. Keep an existing destination, even if incomplete, and ask its owner to identify its Compose project, data, version, and port. Use the lifecycle steps below only after confirming this is the intended course installation. A different version means HOLD until the owner resolves it; it isn't permission to repin or upgrade.

### Create the fresh n8n configuration

Choose one installation method below only if the earlier checks passed and `$HOME/n8n-course` does not exist. The [official one-line setup](https://docs.n8n.io/deploy/host-n8n/install-options/one-line-setup) accepts the course's specified version `2.41.5` and `--no-start`. The [reviewed installer source](https://raw.githubusercontent.com/n8n-io/n8n/master/docker/get-n8n.sh) is version `1.4.0`, but the live URL can change. Prefer downloading and reviewing it so you can check the version before running it. If the installer says “existing install”, that message tells you neither the version nor whether n8n is ready.

**Terminal: Ubuntu Bash, ordinary Linux user, same selected distribution; one-line option.**

```bash
(
  set -o pipefail
  if [ -e "$HOME/n8n-course" ] || [ -L "$HOME/n8n-course" ]; then
    printf 'HOLD: destination exists; preserved\n' >&2; exit 1
  fi
  curl -fsSL https://get.n8n.io | N8N_DIR="$HOME/n8n-course" sh -s -- --version 2.41.5 --no-start
)
```

**Expected:** successful completion creates configuration under Linux `$HOME/n8n-course` without starting containers. Bash `pipefail` reports a failed download even if the shell side exits successfully.

**Stop:** any download/installer failure, changed installer version, missing configuration, or existing-install notice. A streamed script can partially execute before a download failure.

**Recovery:** keep partial files and messages for owner review. Do not rerun over them, delete them, or use upgrade/uninstall flags. The following alternative downloads completely before execution; use it instead of the one-line option, not afterward.

**Terminal: Ubuntu Bash, ordinary Linux user, same selected distribution; download-and-review alternative.**

```bash
course_n8n_review_install() {
  local review_dir approved
  if [ -e "$HOME/n8n-course" ] || [ -L "$HOME/n8n-course" ]; then
    printf 'HOLD: destination exists; preserved\n'; return 1
  fi
  review_dir="$(mktemp -d "$HOME/n8n-installer-review.XXXXXX")" || return 1
  curl -fsSL https://get.n8n.io -o "$review_dir/get-n8n.sh" || {
    printf 'HOLD: incomplete download kept at %s; do not execute it\n' "$review_dir"; return 1;
  }
  [ -s "$review_dir/get-n8n.sh" ] || return 1
  grep -qx 'SCRIPT_VERSION="1.4.0"' "$review_dir/get-n8n.sh" || {
    printf 'HOLD: installer version changed; owner review needed\n'; return 1;
  }
  less "$review_dir/get-n8n.sh" || return 1
  read -r -p 'After reviewing, type INSTALL to create the fresh configuration: ' approved
  [ "$approved" = INSTALL ] || return 1
  N8N_DIR="$HOME/n8n-course" sh "$review_dir/get-n8n.sh" --version 2.41.5 --no-start
}
course_n8n_review_install
```

**Expected:** a completed download, installer version `1.4.0`, review in `less` (press **q** to leave), then fresh configuration after confirmation; no containers start.

**Stop:** failed or empty download, changed script version, denied review, installer failure, or an existing destination.

**Recovery:** keep the review folder and partial setup. Resolve the specific failure with the owner. Do not execute a partial download or overwrite an existing installation.

### Bind the editor to this laptop before starting

In your normal text editor, use **File → Open** to open the selected distro’s Linux `$HOME/n8n-course/compose.yml` (Windows editors can reach it through `\\wsl.localhost\<exact-distro-name>\home\<linux-user>\n8n-course\compose.yml`). Under the `n8n` service’s `ports`, change only `'5678:5678'` to `'127.0.0.1:5678:5678'`, then **File → Save**. Keep all six services. Do not open/share `.env`, paste it into chat, or run a resolved `docker compose config` dump; it contains secrets. No course checkout file or provider key belongs in this n8n configuration.

**Expected:** the saved n8n port is exactly `127.0.0.1:5678:5678`; no other service publishes a port. **Stop:** the file differs from the expected stack, already belongs to another installation, or cannot be saved. **Recovery:** keep it and review with the owner before starting; do not replace a preexisting Compose file.

### Record the fresh project name

A Compose project name tells Docker which containers, volumes, and networks belong to this stack. The file path alone doesn't set that name; see [Docker project names](https://docs.docker.com/compose/how-tos/project-name/). For a genuinely fresh configuration, agree on an unused name with the owner before starting. Use lowercase ASCII letters, digits, underscores, and hyphens, beginning with a letter or digit. If an installation already exists, keep its actual project identity and leave its lifecycle with the owner; don't register it as a fresh project.

**Terminal: Ubuntu Bash, ordinary Linux user, same selected distribution; fresh configuration only.**

```bash
course_n8n_identify() {
  local project containers volumes networks
  local LC_ALL=C
  if [ -e "$HOME/n8n-course/.course-project" ] || [ -L "$HOME/n8n-course/.course-project" ]; then
    printf 'HOLD: project record exists; preserve it\n'; return 1
  fi
  printf 'Enter the owner-approved unused project name: '
  IFS= read -r project || return 1
  case "$project" in
    ''|[!a-z0-9]*|*[!a-z0-9_-]*) printf 'HOLD: invalid project name\n'; return 1 ;;
  esac
  containers="$(docker ps -aq --filter "label=com.docker.compose.project=$project")" || {
    printf 'HOLD: container inspection failed\n'; return 1;
  }
  volumes="$(docker volume ls -q --filter "label=com.docker.compose.project=$project")" || {
    printf 'HOLD: volume inspection failed\n'; return 1;
  }
  networks="$(docker network ls -q --filter "label=com.docker.compose.project=$project")" || {
    printf 'HOLD: network inspection failed\n'; return 1;
  }
  if [ -n "$containers" ] || [ -n "$volumes" ] || [ -n "$networks" ]; then
    printf 'HOLD: project name already has Docker resources\n'; return 1
  fi
  (umask 077; set -o noclobber; printf '%s\n' "$project" > "$HOME/n8n-course/.course-project") || {
    printf 'HOLD: could not create project record; preserve existing files\n'; return 1;
  }
  printf 'Project name recorded\n'
}
course_n8n_identify
```

**Expected:** all three inspections succeed without finding resources for the approved name, and `.course-project` is created without overwriting a file or symlink. **Stop:** an invalid name, existing resource or record, inspection failure, or failed write. **Recovery:** keep the resources and files and review the finding with the owner. Do not remove resources or rename an existing installation.

### Use the recorded project and configuration

Define this helper in the same Ubuntu shell. It explicitly selects the recorded project, `.env`, and `compose.yml`. [Exported variables override `.env`](https://docs.docker.com/compose/how-tos/environment-variables/variable-interpolation/), even when you give the file path. If any listed override is exported, even with an empty value, the helper stops and prints only its name, not its value.

**Terminal: Ubuntu Bash, ordinary Linux user, same selected distribution.**

```bash
course_n8n() {
  local variable project
  local LC_ALL=C
  for variable in N8N_VERSION N8N_SANDBOX_VERSION N8N_RUNNERS_AUTH_TOKEN SEARXNG_SECRET COMPOSE_PROJECT_NAME COMPOSE_FILE COMPOSE_ENV_FILES COMPOSE_DISABLE_ENV_FILE COMPOSE_PROFILES; do
    if printenv "$variable" >/dev/null 2>&1; then
      printf '%s HOLD\n' "$variable"; return 1
    fi
  done
  if [ ! -f "$HOME/n8n-course/.course-project" ] || [ -L "$HOME/n8n-course/.course-project" ]; then
    printf 'HOLD: project record missing or not a regular file\n'; return 1
  fi
  project="$(cat "$HOME/n8n-course/.course-project")" || {
    printf 'HOLD: could not read project record\n'; return 1;
  }
  case "$project" in
    ''|[!a-z0-9]*|*[!a-z0-9_-]*) printf 'HOLD: invalid project record\n'; return 1 ;;
  esac
  docker compose -p "$project" --env-file "$HOME/n8n-course/.env" -f "$HOME/n8n-course/compose.yml" "$@"
}
```

**Expected:** the helper is defined but starts nothing until you call it. **Stop:** a later call reports HOLD or fails. **Recovery:** ask the owner to resolve exported overrides in a clean shell. Then check the approved Docker engine/context and define the helper again. Don't automatically unset variables, rewrite configuration, or recreate a missing project record for an existing installation.

Start only after identity creation succeeds.

**Terminal: Ubuntu Bash, ordinary Linux user, same selected distribution.**

```bash
course_n8n up -d
```

**Expected:** the full stack starts; initial image pulls can take several minutes. **Stop:** a pull, privilege, port, or startup error. **Recovery:** keep configuration and volumes, resolve the named problem with the owner, and retry only this start after correction. Do not reset or reinstall.

**Terminal: Ubuntu Bash, ordinary Linux user, same selected distribution.**

```bash
course_n8n ps --all
course_n8n port n8n 5678
course_n8n exec n8n n8n --version
```

**Expected:** all six services appear. `sandbox-certs` has finished successfully as a one-shot service, `Exited (0)`; the other five are running, with healthy status wherever health checks are shown. The port output is exactly `127.0.0.1:5678`, and n8n reports `2.41.5`. **Stop:** a service is missing, restarting, or unhealthy; the certificate service failed; the port is public; a command failed; or n8n reports another version. **Recovery:** give initialization time to finish, then check again. If the problem persists, keep the result at HOLD. Review errors privately without exposing secrets, and don't change the pinned version, delete volumes, or disable services to force a pass.

### Save a blank workflow and prove it persists

In the Windows browser, open **http://localhost:5678**. For a fresh instance, complete **Set up owner account** with local credentials and select **Next**. This creates the local instance owner, not an n8n Cloud account. If a login page appears for an existing instance, use its existing owner login; do not reset it. Skip optional offers and surveys where offered. No external account, provider key, or paid activation is required. Leave **n8n Assistant** off.

Select **Overview**, then **Build a workflow** on a fresh instance or **Create workflow** when workflows already exist. Click the workflow title, name it **Module 7 Readiness**, and press **Enter**. The editor saves automatically; do not look for a required Save button. Leave the canvas blank and do not select **Publish**. Reload the browser page and confirm the name and blank canvas remain. Keep an existing workflow with that name; choose a distinct readiness name if it contains work.

**Expected:** local owner access, saved blank workflow, Assistant off, and workflow unpublished/inactive. **Stop:** Cloud signup, provider-key/payment request, wrong instance, missing saved workflow, or unavailable editor. **Recovery:** check the address and the inspected port/project with the owner. Keep the existing account and workflows; do not create another instance to hide a failure.

Stop only this confirmed course Compose project. This keeps its named volumes and workflow data.

**Terminal: Ubuntu Bash, ordinary Linux user, same selected distribution.**

```bash
course_n8n down
```

**Expected:** this project’s containers stop and are removed; volumes remain. **Stop:** command failure or evidence this is another owner’s project. **Recovery:** keep the output and confirm project ownership. Never add `-v` or run a volume prune.

**Terminal: Ubuntu Bash, ordinary Linux user, same selected distribution.**

```bash
course_n8n up -d
```

**Expected:** the same project starts again using its saved data. **Stop:** startup failure. **Recovery:** keep files/volumes, resolve the specific error, and repeat the service/version/port inspection above.

Repeat that inspection after restart. Reload **http://localhost:5678**, sign in with the same local owner if needed, and reopen **Module 7 Readiness**. Record **n8n READY** only when the correct version, localhost-only port, six-service state, and saved workflow all survive the restart. Otherwise record **n8n HOLD** with the failed check, separately from both OMP results.

In later sessions, check whether Desktop is running first. If it's stopped, get the owner's approval for the effects of starting it on existing work before you launch it. Open the same Ubuntu distribution as the same ordinary user, check the approved Docker engine/context, and define `course_n8n` again. Reuse `.course-project`; never rerun `course_n8n_identify` or create another project for a restart. Don't reset, uninstall, or upgrade anything on this path.

### Return to native PowerShell

After the n8n check, leave Ubuntu. Docker Desktop can keep the stack running for browser use.

**Terminal: Ubuntu Bash, ordinary Linux user, the bridge launched from PowerShell.**

```bash
exit
```

**Expected:** the native `PS ...>` prompt returns. **Stop:** the shell shown is not PowerShell or the named Ubuntu launch reported an error. **Recovery:** Open **Windows PowerShell 5.1** from Start and use the earlier native path-assignment and readiness procedures as needed. Your native OMP binary, Python, Git checkout, evidence, and credentials stay where they were; don't move them into Ubuntu or enter the provider key there. Reopen the same named Ubuntu only when you need n8n lifecycle commands.
