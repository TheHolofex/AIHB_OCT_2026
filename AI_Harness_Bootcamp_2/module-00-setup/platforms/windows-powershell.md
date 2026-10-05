# Windows PowerShell setup

Setup takes this Windows laptop from no course tools to a live readiness check, in which Oh My Pi writes one file you can verify. It has three parts. First you install Oh My Pi and pass the readiness check in Steps 1 to 9. Then you set up local Obsidian, and finally local n8n for Module 7. Plan for roughly 60 to 120 minutes for Steps 1 to 9 and about 20 to 30 minutes for Obsidian. The n8n time depends on downloads and restarts.

You need Git, Python 3.12 or newer, a browser, a plain text editor, local Obsidian, and the latest stable Oh My Pi release. The only provider key is `OPENROUTER_API_KEY`, and the course launcher selects `openrouter/anthropic/claude-sonnet-4.6`. Oh My Pi, Python, Git, Obsidian, the course checkout, and your key stay on native Windows. Module 7's n8n runs in Docker Desktop, controlled from an Ubuntu window under WSL 2. Use that Ubuntu window only for n8n. Don't install Node, npm, or another agent.

Open **Windows PowerShell** (version 5.1) from the Start menu as your ordinary user. Check with the device owner that you're allowed to install these tools. If an installer asks for administrator approval, use the owner's approved route. If policy denies an installer, stop and keep the message. Don't open an Administrator window to get around a denial.

To run a block, copy all of it, paste it into the PowerShell window, and press Enter if the prompt is still waiting. Most blocks are wrapped in `. { ... }`. That wrapper makes PowerShell read the whole block before it runs anything, so a failed check stops the rest of the block. A line that starts with `STOP:` or `HOLD:` names the problem. Go to [If a step stops](#if-a-step-stops) for that step, or start from the first failed check in [When setup stops](../shared/TROUBLESHOOTING.md).

## 1. Check this computer

This step checks Windows, PowerShell, free disk space, and your processor. It also looks for Git and a real Python 3.12 or newer, then lists anything you still need to install. Windows includes a Python shortcut that only opens the Microsoft Store, so the check skips anything under `WindowsApps` and asks each Python candidate for its actual path. Your Windows edition must still get security updates. WinGet, Microsoft's package installer, needs at least build 17763. See [WinGet requirements](https://learn.microsoft.com/en-us/windows/package-manager/winget/).

**Terminal: Windows PowerShell 5.1, ordinary user, opened from Start.**

```powershell
. {
  if ($env:OS -ne 'Windows_NT') { throw 'STOP: use native Windows.' }
  $ps = $PSVersionTable.PSVersion
  if ($PSVersionTable.PSEdition -ne 'Desktop' -or $ps.Major -ne 5 -or $ps.Minor -ne 1) { throw 'STOP: open Windows PowerShell 5.1 from Start.' }
  $os = Get-CimInstance -ClassName Win32_OperatingSystem -ErrorAction Stop
  if ([int]$os.BuildNumber -lt 17763) { throw 'STOP: this Windows build is older than 17763.' }
  $freeGb = [math]::Round((Get-PSDrive -Name $HOME.Substring(0, 1) -ErrorAction Stop).Free / 1GB, 1)
  if ($freeGb -lt 15) { throw ('STOP: ' + $freeGb + ' GB free on the home drive; free at least 15 GB.') }
  $archCode = (Get-CimInstance -ClassName Win32_Processor -ErrorAction Stop | Select-Object -First 1).Architecture
  if ($archCode -eq 12) {
    $asset = 'omp-windows-arm64.exe'
  } elseif ($archCode -eq 9) {
    $asset = 'omp-windows-x64.exe'
  } else {
    throw 'STOP: no published Oh My Pi binary matches this processor.'
  }
  $R = Join-Path $HOME 'Documents\AIHB_OCT_2026'
  $M = Join-Path $R 'AI_Harness_Bootcamp_2\module-00-setup'
  $missingTools = @()
  $git = Get-Command git -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
  if ($git) {
    $gitVersion = & $git.Source --version
    if ($LASTEXITCODE -ne 0) { throw 'STOP: the installed Git failed to run.' }
  } else {
    $missingTools += 'Git'
  }
  $PY = $null
  foreach ($candidate in @('py -3.12', 'py -3', 'python', 'python3')) {
    $parts = $candidate -split ' '
    $extra = @($parts | Select-Object -Skip 1)
    foreach ($cmd in @(Get-Command $parts[0] -CommandType Application -All -ErrorAction SilentlyContinue)) {
      if ($PY -or $cmd.Source -like '*\WindowsApps\*') { continue }
      $out = @(& $cmd.Source @extra -c 'import sys; sys.exit(1) if sys.version_info < (3,12) else print(sys.executable)' 2>$null)
      if ($LASTEXITCODE -eq 0 -and $out.Count -eq 1) {
        $exe = ([string]$out[0]).Trim()
        if ($exe -match '^[A-Za-z]:\\' -and $exe -notlike '*\WindowsApps\*' -and (Test-Path -LiteralPath $exe -PathType Leaf)) { $PY = $exe }
      }
    }
  }
  if (-not $PY) { $missingTools += 'Python 3.12+' }
  Write-Output ('WINDOWS ' + $os.Caption + ' build ' + $os.BuildNumber)
  Write-Output ('POWERSHELL ' + $ps)
  Write-Output ('FREE_GB ' + $freeGb)
  Write-Output ('OMP_ASSET ' + $asset)
  if ($git) { Write-Output ('GIT ' + $gitVersion) }
  if ($PY) { Write-Output ('PYTHON ' + $PY) }
  if (Get-Command winget -CommandType Application -ErrorAction SilentlyContinue) { Write-Output 'WINGET found' } else { Write-Output 'WINGET missing' }
  if ($missingTools.Count -eq 0) { Write-Output 'MISSING TOOLS: none' } else { Write-Output ('MISSING TOOLS: ' + ($missingTools -join ', ')) }
}
```

**Expected:** lines for Windows, PowerShell `5.1`, free space, and either `omp-windows-arm64.exe` or `omp-windows-x64.exe`, ending with `MISSING TOOLS: none` or a list of tools to install.

**Stop:** a `STOP:` line, or you aren't sure this Windows edition still gets updates or that installs are allowed.

**Recovery:** settle permission and support questions with the device owner first. For other stops, see [If a step stops](#steps-1-and-2-tools).

## 2. Install missing tools

Skip this step if Step 1 printed `MISSING TOOLS: none`. Otherwise WinGet installs only the missing tools: Git for the machine, which may ask for approval, and Python 3.12 for your user only. If WinGet shows source or package agreements, read them and accept only if you're authorized. See [WinGet install](https://learn.microsoft.com/en-us/windows/package-manager/winget/install).

**Terminal: Windows PowerShell 5.1, ordinary user, same window as Step 1.**

```powershell
. {
  if ($null -eq $missingTools) { throw 'STOP: run Step 1 in this window first.' }
  if ($missingTools.Count -eq 0) { Write-Output 'Nothing to install.'; return }
  if (-not (Get-Command winget -CommandType Application -ErrorAction SilentlyContinue)) { throw 'STOP: WinGet is missing.' }
  if ($missingTools -contains 'Git') {
    winget install --exact --id Git.Git --source winget
    if ($LASTEXITCODE -ne 0) { throw 'STOP: Git did not install. Keep the installer message.' }
  }
  if ($missingTools -contains 'Python 3.12+') {
    winget install --exact --id Python.Python.3.12 --source winget --scope user
    if ($LASTEXITCODE -ne 0) { throw 'STOP: Python did not install. Keep the installer message.' }
  }
  Write-Output 'INSTALLED: close every terminal window, open Windows PowerShell from Start, and run Step 1 again.'
}
```

**Expected:** each installer finishes and the last line starts with `INSTALLED:`. Close every terminal window, including Windows Terminal tabs and editor terminals, then open PowerShell from Start and run [Step 1](#1-check-this-computer) until it prints `MISSING TOOLS: none`.

**Stop:** a `STOP:` line, a denied approval prompt, or Step 1 still lists a tool after reopening.

**Recovery:** keep the installer message for the device owner. If WinGet is missing, see [If a step stops](#steps-1-and-2-tools).

## 3. Install Oh My Pi

This block resolves the latest stable release from the official GitHub endpoint once. It downloads the program and its published checksum file for that release into a new folder. A **checksum** is a file's fingerprint. The program runs only after its fingerprint matches the published one exactly. The block then copies it to `omp\omp.exe` under your local app data folder. If a different `omp.exe` is already there, it stops without replacing it. Finally, it saves that folder on your user **PATH**, the list of folders Windows searches when you type a command name. New terminals can then find `omp`. The fingerprint comes from Get-FileHash.

**Terminal: Windows PowerShell 5.1, ordinary user, same window as Step 1.**

```powershell
. {
  if (-not $asset) { throw 'STOP: run Step 1 in this window first.' }
  [Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12
  $destDir = Join-Path $env:LOCALAPPDATA 'omp'
  $dest = Join-Path $destDir 'omp.exe'
  foreach ($probe in @($destDir, $dest)) {
    if ((Test-Path -LiteralPath $probe) -and ((Get-Item -LiteralPath $probe -Force).Attributes -band [IO.FileAttributes]::ReparsePoint)) { throw ('STOP: ' + $probe + ' is a link. It was not followed.') }
  }
  $other = Get-Command omp -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
  if ($other -and $other.Source -ine $dest) { throw ('STOP: another omp is already on PATH at ' + $other.Source + '. It was not replaced.') }
  $download = Join-Path $env:LOCALAPPDATA ('omp-downloads\' + [guid]::NewGuid().ToString('n'))
  New-Item -ItemType Directory -Path $download -ErrorAction Stop | Out-Null
  $rel = & {
    $ProgressPreference = 'SilentlyContinue'
    Invoke-WebRequest -Uri 'https://api.github.com/repos/can1357/oh-my-pi/releases/latest' -UseBasicParsing -ErrorAction Stop | ConvertFrom-Json
  }
  if ($rel.draft -isnot [bool] -or $rel.draft -or $rel.prerelease -isnot [bool] -or $rel.prerelease) { throw 'STOP: latest release metadata is not a stable release' }
  $tag = [string]$rel.tag_name
  if ($tag -cnotmatch '^v[0-9]+\.[0-9]+\.[0-9]+$') { throw 'STOP: tag is not a stable release number' }
  $base = "https://github.com/can1357/oh-my-pi/releases/download/$tag"
  foreach ($name in @($asset, 'SHA256SUMS.txt')) {
    $matches = @($rel.assets | Where-Object { $_.name -ceq $name })
    if ($matches.Count -ne 1 -or $matches[0].browser_download_url -cne "$base/$name") { throw 'STOP: required release asset is missing or inconsistent' }
  }
  $rel | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $download 'release.json') -ErrorAction Stop
  Write-Output "RELEASE $tag"
  $sumsPath = Join-Path $download 'SHA256SUMS.txt'
  $binaryPath = Join-Path $download $asset
  & {
    $ProgressPreference = 'SilentlyContinue'
    Invoke-WebRequest -Uri ($base + '/SHA256SUMS.txt') -OutFile $sumsPath -UseBasicParsing -ErrorAction Stop
    Invoke-WebRequest -Uri ($base + '/' + $asset) -OutFile $binaryPath -UseBasicParsing -ErrorAction Stop
  }
  $lines = @(Get-Content -LiteralPath $sumsPath | Where-Object { ($_ -split '  ', 2)[1] -ceq $asset })
  if ($lines.Count -ne 1) { throw 'STOP: SHA256SUMS.txt has no single line for this file. Nothing was installed.' }
  $expected = ($lines[0] -split '  ', 2)[0]
  $actual = (Get-FileHash -LiteralPath $binaryPath -Algorithm SHA256).Hash.ToLowerInvariant()
  if ($expected -cnotmatch '^[0-9a-f]{64}$' -or $actual -cne $expected) { throw 'STOP: checksum did not match. Nothing was installed.' }
  Write-Output 'CHECKSUM OK'
  if (Test-Path -LiteralPath $dest) {
    $existing = Get-FileHash -LiteralPath $dest -Algorithm SHA256 -ErrorAction SilentlyContinue
    if (-not $existing -or $existing.Hash.ToLowerInvariant() -cne $actual) { throw 'STOP: a different omp.exe is already installed. It was not replaced.' }
    Write-Output 'KEPT the identical omp.exe already installed'
  } else {
    New-Item -ItemType Directory -Path $destDir -Force | Out-Null
    Copy-Item -LiteralPath $binaryPath -Destination $dest -ErrorAction Stop
  }
  $userPath = [Environment]::GetEnvironmentVariable('Path', 'User')
  $entries = @($userPath -split ';' | Where-Object { $_ })
  if ($entries -notcontains $destDir) {
    [Environment]::SetEnvironmentVariable('Path', ((@($destDir) + $entries) -join ';'), 'User')
    Write-Output 'PATH saved for new windows'
  }
  $env:Path = (@($destDir) + @($env:Path -split ';' | Where-Object { $_ -and $_ -ne $destDir })) -join ';'
  $found = (Get-Command omp -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1).Source
  if ($found -ine $dest) { throw 'STOP: omp resolves to a different or missing program.' }
  $expectedVer = 'omp/' + ($tag -replace '^v','')
  $version = @(& $dest --version)
  if ($LASTEXITCODE -ne 0 -or $version.Count -ne 1 -or ([string]$version[0]).Trim() -ne $expectedVer) { throw "STOP: omp --version did not print $expectedVer." }
  Write-Output ('OMP_VERSION ' + ([string]$version[0]).Trim())
}
```

**Expected:** `RELEASE <tag>`, `CHECKSUM OK`, then `OMP_VERSION omp/<semver>`. The version command is the first time the program runs, and it runs only after the fingerprint matched the selected release.

**Stop:** any `STOP:` line. A download, checksum, link, or existing-file stop changes nothing. A stop at the final path or version check comes after `omp.exe` was copied and your PATH was saved, and a rerun reports `KEPT the identical omp.exe already installed`.

**Recovery:** leave the download folder in place; running the block again uses a new folder. For a different existing `omp`, a link, or a blocked download, see [If a step stops](#step-3-oh-my-pi).

## 4. Get the course files

The course repository is private. This block checks whether your saved Git sign-in can read it, without asking for a password in the terminal. Then it clones the course into `Documents\AIHB_OCT_2026` in your home folder, or reuses a checkout of the same course already there. The clone keeps Git from changing line endings, the hidden character at the end of each line, because later checks compare exact bytes. The block reads three frozen course files and puts the checkout on hold if their line endings have changed. See [git ls-remote](https://git-scm.com/docs/git-ls-remote).

**Terminal: Windows PowerShell 5.1, ordinary user, same window as Step 1.**

```powershell
. {
  if (-not $R) { throw 'STOP: run Step 1 in this window first.' }
  $origin = 'https://github.com/TheHolofex/AIHB_OCT_2026.git'
  $savedPrompt = $env:GIT_TERMINAL_PROMPT
  $env:GIT_TERMINAL_PROMPT = '0'
  git ls-remote --exit-code $origin HEAD
  $access = $LASTEXITCODE
  if ($null -eq $savedPrompt) { Remove-Item Env:\GIT_TERMINAL_PROMPT } else { $env:GIT_TERMINAL_PROMPT = $savedPrompt }
  if ($access -ne 0) { throw 'STOP: GitHub access failed. Use "If GitHub access fails".' }
  Write-Output 'ACCESS OK'
  if (Test-Path -LiteralPath $R) {
    foreach ($probe in @($R, (Join-Path $R '.git'))) {
      if ((Test-Path -LiteralPath $probe) -and ((Get-Item -LiteralPath $probe -Force).Attributes -band [IO.FileAttributes]::ReparsePoint)) { throw 'STOP: the checkout or its .git folder is a link. It was not followed.' }
    }
    if (-not (Test-Path -LiteralPath (Join-Path $R '.git') -PathType Container)) { throw 'STOP: Documents\AIHB_OCT_2026 exists and is not a Git checkout. It was not changed.' }
    $remote = git -C $R remote get-url origin
    if ($LASTEXITCODE -ne 0 -or ([string]$remote).Trim() -ne $origin) { throw 'STOP: the existing checkout has a different origin. It was not changed.' }
    Write-Output 'CHECKOUT reused'
  } else {
    git -c core.autocrlf=false clone $origin $R
    if ($LASTEXITCODE -ne 0) { throw 'STOP: clone failed. Keep the message.' }
    Write-Output 'CHECKOUT cloned'
  }
  if (-not (Test-Path -LiteralPath (Join-Path $M 'shared\MODULE_00_LAB.md'))) { throw 'STOP: this checkout has no Module 0 lab. It was not changed.' }
  foreach ($rel in @('AI_Harness_Bootcamp_2\module-01-mission-thread\shared\case\SOURCE_MANIFEST.json', 'AI_Harness_Bootcamp_2\module-08-change-eval\shared\controls\policy.json', 'AI_Harness_Bootcamp_2\module-10-capstone\shared\baseline\run.json')) {
    $path = Join-Path $R $rel
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) { throw ('STOP: ' + $rel + ' is missing. The checkout was not changed.') }
    if ([Array]::IndexOf([IO.File]::ReadAllBytes($path), [byte]13) -ge 0) { throw 'HOLD: a frozen control has rewritten line endings. The checkout was not reset, cleaned, pulled, or renormalized.' }
  }
  Write-Output 'Line endings unchanged.'
  Write-Output ('COURSE ' + $R)
}
```

**Expected:** a commit ID followed by `HEAD`, then `ACCESS OK`, `CHECKOUT cloned` or `CHECKOUT reused`, `Line endings unchanged.`, and the course path.

**Stop:** `STOP: GitHub access failed`, any other `STOP:` line, or the line-ending `HOLD:`.

**Recovery:** for access, use the next subsection. For an existing folder or the line-ending hold, leave the folder untouched and see [If a step stops](#step-4-github-access-and-the-checkout).

### If GitHub access fails

Git for Windows includes Git Credential Manager, which signs you in to GitHub through a browser window and stores the sign-in in Windows Credential Manager. Run this command by itself. When the sign-in window opens, use the GitHub account that was invited to the course repository. That account is separate from your course-site password and your OpenRouter key.

**Terminal: Windows PowerShell 5.1, ordinary user, same window.**

```powershell
git ls-remote --exit-code https://github.com/TheHolofex/AIHB_OCT_2026.git HEAD
```

**Expected:** after you sign in, a commit ID followed by `HEAD`. Then run [Step 4](#4-get-the-course-files) again.

**Stop:** the window asks `Username for 'https://github.com'` instead of opening a sign-in window, or Git reports that the repository wasn't found.

**Recovery:** press Ctrl+C at a username prompt. Use the GitHub CLI route in [If a step stops](#step-4-github-access-and-the-checkout), and ask the repository owner to confirm your invitation.

## 5. Open a new window and confirm

Opening PowerShell from Start creates a new process, and a **process** is one running program with its own settings. A new process reads your saved PATH, but it should not have any key. Seeing `MISSING` here shows that no key was saved where new windows pick it up. Close every terminal window, including Windows Terminal tabs and editor terminals. Then open **Windows PowerShell** from Start. Don't type `powershell` inside an old window, because a child window inherits the parent's settings.

**Terminal: Windows PowerShell 5.1, ordinary user, newly opened from Start.**

```powershell
. {
  $R = Join-Path $HOME 'Documents\AIHB_OCT_2026'
  $M = Join-Path $R 'AI_Harness_Bootcamp_2\module-00-setup'
  $PY = $null
  foreach ($candidate in @('py -3.12', 'py -3', 'python', 'python3')) {
    $parts = $candidate -split ' '
    $extra = @($parts | Select-Object -Skip 1)
    foreach ($cmd in @(Get-Command $parts[0] -CommandType Application -All -ErrorAction SilentlyContinue)) {
      if ($PY -or $cmd.Source -like '*\WindowsApps\*') { continue }
      $out = @(& $cmd.Source @extra -c 'import sys; sys.exit(1) if sys.version_info < (3,12) else print(sys.executable)' 2>$null)
      if ($LASTEXITCODE -eq 0 -and $out.Count -eq 1) {
        $exe = ([string]$out[0]).Trim()
        if ($exe -match '^[A-Za-z]:\\' -and $exe -notlike '*\WindowsApps\*' -and (Test-Path -LiteralPath $exe -PathType Leaf)) { $PY = $exe }
      }
    }
  }
  if (-not $PY) { throw 'STOP: Python 3.12+ was not found in this window.' }
  if (-not (Test-Path -LiteralPath (Join-Path $M 'shared\MODULE_00_LAB.md'))) { throw 'STOP: the course checkout was not found. Run Step 4 first.' }
  $dest = Join-Path $env:LOCALAPPDATA 'omp\omp.exe'
  $found = (Get-Command omp -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1).Source
  if ($found -ine $dest) { throw 'STOP: omp is missing from PATH or points to a different program.' }
  $version = @(& $dest --version)
  $v = if ($version.Count -ge 1) { ([string]$version[0]).Trim() } else { '' }
  if ($LASTEXITCODE -ne 0 -or $version.Count -ne 1 -or ($v -notmatch '^omp/[0-9]+\.[0-9]+\.[0-9]+$')) { throw 'STOP: omp --version did not print a usable omp/<semver>.' }
  Write-Output ('OMP_VERSION ' + $v)
  Write-Output ('PYTHON ' + $PY)
  Write-Output ('COURSE ' + $R)
  if ([string]::IsNullOrEmpty($env:OPENROUTER_API_KEY)) { Write-Output 'MISSING' } else { Write-Output 'SET' }
}
```

**Expected:** `OMP_VERSION omp/<semver>`, the Python and course paths, and `MISSING` as the last line.

**Stop:** a `STOP:` line, or `SET` before you've typed a key in this window.

**Recovery:** if the window prints `SET`, don't print the variable; run the saved-key check in [If a step stops](#step-5-a-new-window). For a missing `omp`, make sure you opened this window from Start.

## 6. Enter your OpenRouter key

Run this command by itself. Type or paste your OpenRouter key at the hidden prompt, then press Enter. The command only waits for your input. Never put the key in a command, a file, a profile, or a chat. See [Use one OpenRouter key without putting it in your work](../shared/CREDENTIALS.md).

**Terminal: Windows PowerShell 5.1, ordinary user, same window as Step 5.**

```powershell
$secret = Read-Host -Prompt 'OpenRouter API key' -AsSecureString
```

**Expected:** the prompt returns, and the key isn't readable on screen. PowerShell may show asterisks, which is still hidden input.

**Stop:** the key appears as readable text, or you pasted it onto the command line instead of the prompt.

**Recovery:** revoke a displayed key with OpenRouter, then run this command again with the replacement.

## 7. Confirm the key is loaded

This block puts the hidden key into this terminal's environment only, clears the temporary copy, and prints `SET` or `MISSING`. To read the hidden value, it briefly uses a BSTR, an unmanaged string, then zeroes that memory with [ZeroFreeBSTR](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.interopservices.marshal.zerofreebstr). It writes nothing to a file, a profile, or your saved user settings.

**Terminal: Windows PowerShell 5.1, ordinary user, same window as Step 6.**

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

**Stop:** `MISSING`, an error, or any output that contains the key.

**Recovery:** run Step 6 and this block again in the same window. Don't check the key by printing the environment.

## 8. Run the readiness check

This block creates a fresh attempt folder under `course-evidence\reformation-qa` in your home folder, outside the course checkout. It writes a random token beside the work folder and copies the token into it. Then it runs the course launcher once. The launcher starts Oh My Pi with permission to write only `from-omp.txt`. Finally, the verifier checks that the file contains `omp works`, one space, and this attempt's token. It also checks that Oh My Pi's write receipt matches the file on disk. Don't create the evidence folder or `from-omp.txt` yourself.

**Terminal: Windows PowerShell 5.1, ordinary user, same window as Steps 5 to 7.**

```powershell
. {
  if (-not $PY -or -not $R -or -not $M) { throw 'STOP: run Step 5 in this window first.' }
  if ([string]::IsNullOrEmpty($env:OPENROUTER_API_KEY)) { throw 'STOP: the key is not loaded in this window. Repeat Steps 6 and 7.' }
  $attempt = Join-Path $HOME ('course-evidence\reformation-qa\' + [guid]::NewGuid().ToString('n') + '\module-00')
  $proof = Join-Path $attempt 'proof'
  $tokenFile = Join-Path $attempt 'run-token.txt'
  $evidence = Join-Path $attempt 'evidence'
  New-Item -ItemType Directory -Path $proof -ErrorAction Stop | Out-Null
  $bytes = New-Object byte[] 16
  [Security.Cryptography.RandomNumberGenerator]::Create().GetBytes($bytes)
  $utf8 = New-Object Text.UTF8Encoding $false
  [IO.File]::WriteAllText($tokenFile, (-join ($bytes | ForEach-Object { $_.ToString('x2') })), $utf8)
  Copy-Item -LiteralPath $tokenFile -Destination (Join-Path $proof 'run-token.txt') -ErrorAction Stop
  $promptFile = Join-Path $proof 'prompt.txt'
  [IO.File]::WriteAllText($promptFile, "Read run-token.txt with the course_read tool. Then write only from-omp.txt with the course_write tool. The file contents must be the words omp works, one space, and the exact token text from run-token.txt. Do not write any other file.`n", $utf8)
  Write-Output ('ATTEMPT ' + $attempt)
  & $PY (Join-Path $R 'shared\run_omp.py') --workdir $proof --prompt $promptFile --evidence $evidence --allow-write from-omp.txt
  $launchExit = $LASTEXITCODE
  Write-Output ('LAUNCH_EXIT ' + $launchExit)
  if ($launchExit -ne 0) { throw 'HOLD: the launcher did not succeed. Keep this attempt and read its message.' }
  & $PY (Join-Path $M 'shared\case\verify_tool_proof.py') $proof $tokenFile $evidence
  $verifyExit = $LASTEXITCODE
  Write-Output ('VERIFY_EXIT ' + $verifyExit)
  if ($verifyExit -ne 0) { throw 'HOLD: the readiness check did not pass. Keep this attempt.' }
}
```

**Expected:** the attempt path, `LAUNCH_EXIT 0`, the verifier's `READINESS CHECK PASS`, then `VERIFY_EXIT 0`. The launcher may print its own status line too, but that line alone doesn't complete the check.

**Stop:** `LAUNCH_EXIT` or `VERIFY_EXIT` other than `0`, or `READINESS CHECK HOLD`.

**Recovery:** keep the attempt folder and read the named failure. Running this block again makes a new attempt; see [If a step stops](#step-8-the-readiness-check).

## 9. Save the setup report and read the result

The setup report checks your prerequisites separately: Git, Python, Oh My Pi, the checkout, and whether this terminal has the key. It doesn't repeat the live write, so you need both `SETUP CHECK PASS` and `READINESS CHECK PASS`. Open `scripts\verify-setup.ps1` under the Module 0 folder in your text editor and read it before running it. Run this block only if you have permission to run the checker you've reviewed. Windows PowerShell's **execution policy** controls which scripts can run. First, the block checks for a restrictive policy explicitly set outside the Process scope, or an explicit Process restriction. If it finds one, it stops. If the current effective policy allows local scripts and no restrictive policy is set, it runs the checker directly. If no policy has been set anywhere on this computer, the default Restricted policy blocks scripts. In that case, the block runs the checker in a child PowerShell with `-ExecutionPolicy RemoteSigned`, only for that child process. See [about_Execution_Policies](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-5.1). Finally, the block reads `from-omp.txt` directly from disk.

**Terminal: Windows PowerShell 5.1, ordinary user, same window as Step 8.**

```powershell
. {
  if (-not $attempt -or -not $proof) { throw 'STOP: run Step 8 in this window first.' }
  $report = Join-Path $attempt 'setup-report.txt'
  $checker = Join-Path $M 'scripts\verify-setup.ps1'
  $list = Get-ExecutionPolicy -List
  $configured = @($list | Where-Object { $_.Scope -ne 'Process' -and [string]$_.ExecutionPolicy -ne 'Undefined' })
  $restrictiveConfigured = @($configured | Where-Object { [string]$_.ExecutionPolicy -in @('Restricted', 'AllSigned') })
  $processRestrictive = @($list | Where-Object { $_.Scope -eq 'Process' -and [string]$_.ExecutionPolicy -in @('Restricted', 'AllSigned') })
  $effective = [string](Get-ExecutionPolicy)
  $global:LASTEXITCODE = -1
  if ($restrictiveConfigured.Count -gt 0 -or $processRestrictive.Count -gt 0) {
    throw ('STOP: a restrictive execution policy is set on this computer (Get-ExecutionPolicy -List). Ask the device owner for an approved way to run the reviewed local course checker.')
  } elseif ($effective -notin @('Restricted', 'AllSigned')) {
    & $checker -Root $R -ResultsPath $report
  } elseif ($configured.Count -eq 0) {
    & (Join-Path $PSHOME 'powershell.exe') -NoProfile -ExecutionPolicy RemoteSigned -File $checker -Root $R -ResultsPath $report
  } else {
    throw ('STOP: execution policy ' + $effective + ' was set on this computer. Ask the device owner for an approved way to run the checker.')
  }
  $reportExit = $global:LASTEXITCODE
  Write-Output ('REPORT_EXIT ' + $reportExit)
  if ($reportExit -ne 0) { throw 'HOLD: the setup report found a problem. Fix its first FAIL line.' }
  if (-not (Test-Path -LiteralPath $report -PathType Leaf) -or -not ((Get-Content -LiteralPath $report -Tail 1) -like 'SETUP CHECK PASS*')) { throw 'HOLD: the setup report did not end with SETUP CHECK PASS.' }
  Get-Content -LiteralPath (Join-Path $proof 'from-omp.txt') -Raw -ErrorAction Stop
}
```

**Expected:** report lines ending in `SETUP CHECK PASS`, then `REPORT_EXIT 0`, then `omp works` followed by this attempt's token. The report never contains the key.

**Stop:** `STOP: a restrictive execution policy is set on this computer (Get-ExecutionPolicy -List)`, `SETUP CHECK HOLD`, a nonzero `REPORT_EXIT`, `HOLD: the setup report did not end with SETUP CHECK PASS.`, a message that running scripts is disabled or the file isn't signed, or file text that differs.

**Recovery:** fix the first `FAIL` line's `NEXT ACTION`, then run Step 8 again for a new attempt. For a policy block, see [If a step stops](#step-9-the-setup-report).

## Set up local Obsidian

Obsidian lets you follow links and edit notes in a **vault**, an ordinary folder of Markdown text files. You'll install it, open a fresh practice vault, and prove three things in the app window: links work, your saved edits reach the disk, and an edit made outside the app shows up while the vault is open. Keep this vault on the native Windows disk, outside the course checkout and any synced folder. Obsidian [stores plain local files and picks up outside changes](https://github.com/obsidianmd/obsidian-help/blob/master/en/Files%20and%20folders/How%20Obsidian%20stores%20data.md).

### Install Obsidian

First look for **Obsidian** in Start and in **Settings → Apps → Installed apps**. If it's already installed, keep it as it is, without upgrading or downgrading it, and skip this block. Otherwise the block downloads the official 1.13.7 Windows installer, which covers both x64 and ARM64. It checks the fingerprint published in the [release metadata](https://api.github.com/repos/obsidianmd/obsidian-releases/releases/tags/v1.13.7) and starts the installer only if it matches. When the installer asks who to install for, choose **Only for me**. Cancel if it asks to replace an existing installation or needs approval you don't have.

**Terminal: Windows PowerShell 5.1, ordinary user, same window as Step 9.**

```powershell
. {
  foreach ($existing in @((Join-Path $env:LOCALAPPDATA 'Programs\Obsidian\Obsidian.exe'), (Join-Path $env:ProgramFiles 'Obsidian\Obsidian.exe'))) {
    if (Test-Path -LiteralPath $existing) { Write-Output ('OBSIDIAN already installed at ' + $existing + '; kept as it is'); return }
  }
  [Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12
  $folder = Join-Path $env:LOCALAPPDATA ('obsidian-download-' + [guid]::NewGuid().ToString('n'))
  New-Item -ItemType Directory -Path $folder -ErrorAction Stop | Out-Null
  $installer = Join-Path $folder 'Obsidian-1.13.7.exe'
  Write-Output 'Downloading about 330 MB; this can take several minutes.'
  & {
    $ProgressPreference = 'SilentlyContinue'
    Invoke-WebRequest -Uri 'https://github.com/obsidianmd/obsidian-releases/releases/download/v1.13.7/Obsidian-1.13.7.exe' -OutFile $installer -UseBasicParsing -ErrorAction Stop
  }
  $hash = (Get-FileHash -LiteralPath $installer -Algorithm SHA256).Hash.ToLowerInvariant()
  if ($hash -cne 'f233dc24896b3f2d5f9e4b01111181a561d0760b2105f0a474024c5f3143a9bc') { throw 'Obsidian HOLD: checksum mismatch. The installer was not run.' }
  Write-Output 'OBSIDIAN CHECKSUM OK'
  $setup = Start-Process -FilePath $installer -PassThru
  $null = $setup.Handle
  $setup.WaitForExit()
  if ($setup.ExitCode -ne 0) { throw ('Obsidian HOLD: the installer exited with ' + $setup.ExitCode + '.') }
  Write-Output 'OBSIDIAN INSTALLED'
}
```

**Expected:** `OBSIDIAN already installed`, or `OBSIDIAN CHECKSUM OK` followed by `OBSIDIAN INSTALLED`. After that, **Start → Obsidian** opens the app window.

**Stop:** an `Obsidian HOLD:` line, an installer refusal, or no app window.

**Recovery:** never run a download whose checksum failed; running the block again uses a new folder. Keep any refusal message for the device owner and see [If a step stops](#local-obsidian-problems).

### Open the practice vault and save a reply

This block creates a fresh practice vault under your home folder and records the expected values outside the vault. It uses `$PY` and `$M` from Step 5; if you opened a new window, run the [Step 5](#5-open-a-new-window-and-confirm) block first.

**Terminal: Windows PowerShell 5.1, ordinary user, same window.**

```powershell
. {
  if (-not $PY -or -not $M) { throw 'Obsidian HOLD: run Step 5 in this window first.' }
  $ObsidianRoot = Join-Path $HOME ('obsidian-readiness-' + [guid]::NewGuid().ToString('n'))
  & $PY (Join-Path $M 'scripts\obsidian_readiness.py') initialize --root $ObsidianRoot
  if ($LASTEXITCODE -ne 0) { throw 'Obsidian HOLD: initialize failed; keep this attempt.' }
  Write-Output ('OBSIDIAN_ROOT ' + $ObsidianRoot)
}
```

**Expected:** `Created practice vault:` followed by a path ending in `\vault`, then the `OBSIDIAN_ROOT` line. Note both paths.

**Stop:** a `HOLD:` line or any helper error.

**Recovery:** keep the attempt and the message, and see [If a step stops](#local-obsidian-problems).

**Window: native Windows Obsidian, ordinary user.**

1. In the vault chooser, choose **Open folder as vault**. If a personal vault opens instead, use **Open another vault** and leave its files and settings alone. Select the exact folder printed after `Created practice vault:`, not its parent.
2. In this vault's **Settings → Community plugins**, keep **Restricted mode** on. Under **Settings → Core plugins**, turn **Sync** off if it's on. Don't sign in, install plugins, or connect a remote vault. Note the version shown in **Settings → General**, then close Settings.
3. Open **Start**. Switch to **Reading view** if the links aren't clickable, click **Token**, and read the token. Then follow **Reply** from Token.
4. Switch Reply to **Editing view**, type only the token on one line, and press **Ctrl+S**.
5. Open **Token** again in Reading view and leave it showing.

### Watch an outside edit and reopen

This block first checks that your saved reply matches the token. Only if it does, it changes Token on disk from outside Obsidian, while keeping your reply. Keep Token showing in Obsidian while it runs.

**Terminal: Windows PowerShell 5.1, ordinary user, same window.**

```powershell
. {
  if (-not $ObsidianRoot) { throw 'Obsidian HOLD: run the practice vault block in this window first.' }
  & $PY (Join-Path $M 'scripts\obsidian_readiness.py') check --root $ObsidianRoot
  if ($LASTEXITCODE -ne 0) { throw 'Obsidian HOLD: the saved reply did not match. Nothing was refreshed.' }
  & $PY (Join-Path $M 'scripts\obsidian_readiness.py') refresh --root $ObsidianRoot
  if ($LASTEXITCODE -ne 0) { throw 'Obsidian HOLD: refresh failed; keep this attempt.' }
}
```

**Expected:** `Token generation 1: initial token; external refresh not yet exercised` and `PASS: Obsidian file round-trip; GUI observation still required`, then `Source token rotated outside Obsidian; your saved reply was preserved.`

**Stop:** an `Obsidian HOLD:` line or a helper `HOLD:` line.

**Recovery:** in Obsidian, correct only Reply so it matches Token, save, and run this block again. Don't edit Start, Token, or the records outside `vault`.

**Window: native Windows Obsidian, same practice vault.** Before you close anything, look at Token and confirm its value changed while the vault was open. Follow **Reply**, replace the old value with the new one in Editing view, and press **Ctrl+S**. Close Obsidian, open it again from Start, and reopen the same vault if it doesn't reopen on its own. Open Reply and confirm the new value is still there.

**Terminal: Windows PowerShell 5.1, ordinary user, same window.**

```powershell
& $PY (Join-Path $M 'scripts\obsidian_readiness.py') check --root $ObsidianRoot
```

**Expected:** `Token generation 2: refreshed token; GUI observation still required`, the same `PASS:` line, and a new `Disk observation saved:` path.

**Stop:** a `HOLD:` line or a different result.

**Recovery:** confirm the vault path and the saved Reply in Obsidian, then run this check again. If Token changed only after a restart, see [If a step stops](#local-obsidian-problems).

### Record what you saw

In Notepad, create a new plain-text file named `gui-observation.txt` directly in the folder printed after `OBSIDIAN_ROOT`, beside `vault` rather than inside it. Write the date, your Windows build and processor, the Obsidian version, the exact vault path, and what happened at each point: following Start → Token → Reply, both saves, the outside change appearing while the vault was open, and Reply after reopening. Add the two `Disk observation saved:` paths and anything that failed.

Record **Obsidian READY** only if you saw every one of those actions in the app on this laptop and both checks passed. Otherwise record **Obsidian HOLD** and name the action that failed or that you didn't see. A helper `PASS` alone isn't enough. Keep this result separate from the Oh My Pi and n8n results.

## Local n8n for Module 7

n8n is a visual workflow editor. You'll run it locally in Docker Desktop, reach it only from this laptop at `http://localhost:5678`, and confirm that a saved workflow survives a stop and restart. The commands that control n8n run in an Ubuntu window under WSL 2, Windows' built-in Linux layer. Keep this result separate from `SETUP CHECK PASS` and `READINESS CHECK PASS`; Module 7 needs n8n ready.

Before you install anything, get the device owner's answers to three questions. First: does this laptop meet [Docker Desktop's Windows requirements](https://docs.docker.com/desktop/setup/install/windows-install/)? These include WSL 2.1.5 or newer, Windows 10 22H2 (build 19045) or Windows 11 23H2 (build 22631) or newer, 8 GB of RAM, hardware virtualization, and the Windows Server service (`LanmanServer`) set to Automatic. Windows on Arm uses an Early Access build. Second: does your use qualify under [Docker Desktop licensing](https://docs.docker.com/subscription/desktop-license/)? Third: may you run the [official n8n stack](https://raw.githubusercontent.com/n8n-io/n8n/master/docker/get-n8n-compose.yml)? Its sandbox runner uses privileged Docker-in-Docker. Keep n8n's Assistant off, and never enter a provider key into n8n.

### Check Windows, WSL, and Docker

This block reads your Windows build, memory, WSL version, installed Linux distributions, Docker, and whether anything already uses port 5678. It changes nothing.

**Terminal: Windows PowerShell 5.1, ordinary user, opened from Start.**

```powershell
. {
  $env:WSL_UTF8 = '1'
  $os = Get-CimInstance -ClassName Win32_OperatingSystem
  $ramGb = [math]::Round((Get-CimInstance -ClassName Win32_ComputerSystem).TotalPhysicalMemory / 1GB, 1)
  Write-Output ('WINDOWS ' + $os.Caption + ' build ' + $os.BuildNumber + ', RAM ' + $ramGb + ' GB')
  $server = Get-Service -Name LanmanServer
  Write-Output ('LANMANSERVER ' + $server.Status + ', ' + $server.StartType)
  wsl --version
  wsl --list --verbose
  if (Get-Command docker -CommandType Application -ErrorAction SilentlyContinue) { docker version; docker ps --all } else { Write-Output 'DOCKER not installed' }
  $listener = @(Get-NetTCPConnection -State Listen -LocalPort 5678 -ErrorAction SilentlyContinue)
  if ($listener.Count -eq 0) { Write-Output 'PORT 5678 free' } else { Write-Output ('PORT 5678 in use by process ' + $listener[0].OwningProcess) }
}
```

**Expected:** a build and memory that meet Docker's requirements, `LANMANSERVER Running, Automatic`, a WSL version of 2.1.5 or newer, and `PORT 5678 free`. The distribution list may show an existing `Ubuntu-24.04` or `Ubuntu-26.04` with VERSION `2`.

**Stop:** a requirement isn't met, `wsl --version` prints help text instead of a version, an Ubuntu shows VERSION `1`, Docker shows containers you don't recognize, or port 5678 is in use.

**Recovery:** settle each finding with the device owner, and keep every existing distribution, container, and volume. See [If a step stops](#local-n8n-problems).

### Install Ubuntu if you don't have it

If the list showed any Ubuntu with VERSION `2`, whatever its NAME, skip this block and open that one in the next section; the Ubuntu check there confirms its release. Install only if no Ubuntu is listed, or if the Ubuntu check reports a release other than 24.04 or 26.04. After the device owner approves, open PowerShell with **Run as administrator** and install the named release. New installs use WSL 2. See [Install WSL](https://learn.microsoft.com/en-us/windows/wsl/install).

**Terminal: Windows PowerShell, elevated with Run as administrator, owner-approved install only.**

```powershell
wsl --install -d Ubuntu-24.04
```

**Expected:** Ubuntu 24.04 installs, or Windows asks you to restart. When Ubuntu first opens, create an ordinary Linux username and password. The password doesn't show as you type.

**Stop:** an error, help text instead of an install, or a policy denial.

**Recovery:** keep the message and work through [Microsoft's install troubleshooting](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting#installation-issues) with the owner. Never reinstall or unregister a distribution that's already there.

### Open Ubuntu and check it

Open Ubuntu by its exact name and start in your Linux home folder. If you're using an Ubuntu that was already listed with a different NAME, such as `Ubuntu-26.04` or `Ubuntu`, replace `Ubuntu-24.04` in the command with that name.

**Terminal: Windows PowerShell 5.1, ordinary user, opened from Start.**

```powershell
wsl --distribution Ubuntu-24.04 --cd ~
```

**Expected:** an Ubuntu prompt as your ordinary Linux user. The rest of this part runs in that Ubuntu window.

**Stop:** the launch fails, or first-time user setup doesn't finish.

**Recovery:** keep the error and ask the owner to repair the distribution without resetting it.

This check confirms your Linux user, release, and free space. It also makes sure Ubuntu doesn't already have its own Docker Engine, because Docker warns against running that alongside Docker Desktop.

**Terminal: Ubuntu Bash, ordinary Linux user, the window you just opened.**

```bash
course_check_ubuntu() {
  local release avail_kb
  [ -n "${BASH_VERSION:-}" ] || { printf 'STOP: run this in Bash\n'; return 1; }
  [ "$(id -u)" -ne 0 ] || { printf 'STOP: use your ordinary Linux user, not root\n'; return 1; }
  case "$HOME" in /home/*) ;; *) printf 'STOP: your home must be under /home\n'; return 1 ;; esac
  release="$(. /etc/os-release && printf '%s:%s' "$ID" "$VERSION_ID")" || return 1
  case "$release" in
    ubuntu:24.04|ubuntu:26.04) ;;
    *) printf 'STOP: %s is not Ubuntu 24.04 or 26.04\n' "$release"; return 1 ;;
  esac
  avail_kb="$(df -Pk "$HOME" | awk 'NR == 2 { print $4 }')"
  [ "${avail_kb:-0}" -ge 26214400 ] || { printf 'STOP: less than 25 GB free in your Linux home\n'; return 1; }
  if dpkg-query -W -f='${Status}\n' docker-ce docker.io 2>/dev/null | grep -q 'ok installed'; then
    printf 'HOLD: Ubuntu already has its own Docker Engine; it was kept\n'; return 1
  fi
  command -v curl >/dev/null || { printf 'STOP: curl is missing\n'; return 1; }
  printf 'UBUNTU %s %s user %s, %s GB free\n' "$release" "$(uname -m)" "$(id -un)" "$((avail_kb / 1048576))"
}
course_check_ubuntu
```

**Expected:** one line such as `UBUNTU ubuntu:24.04 x86_64 user yourname, 180 GB free`.

**Stop:** a `STOP:` or `HOLD:` line.

**Recovery:** for missing `curl` or an existing Docker Engine, see [If a step stops](#local-n8n-problems). Never move course work under `/mnt/`.

### Install Docker Desktop and connect Ubuntu

**Window: Windows desktop, ordinary user.**

1. If the Windows check showed Docker already installed, keep that installation. If it's installed but not running, ask the owner before starting it, because starting Docker can restart containers that have a restart policy. See [Docker restart policies](https://docs.docker.com/engine/containers/start-containers-automatically/).
2. Otherwise download **Docker Desktop for Windows** for your processor from [Docker's Windows install page](https://docs.docker.com/desktop/setup/install/windows-install/) and run it. Use the installation mode the owner approves; the per-user mode needs no administrator rights. Select **Use WSL 2 instead of Hyper-V** if it's offered, select **Close** when it finishes, and restart Windows if asked.
3. Open **Docker Desktop** from Start. Read the agreement, and select **Accept** only if the licensing question is settled.
4. In **Settings → Resources → WSL Integration**, turn on the exact Ubuntu NAME you opened, then select **Apply & restart**.
5. Type `exit` in the Ubuntu window, then open Ubuntu again with the PowerShell box in [Open Ubuntu and check it](#open-ubuntu-and-check-it), so the window picks up Docker Desktop's connection.

### Create the n8n configuration

The official installer writes n8n's configuration into `n8n-course` in your Linux home without starting anything. This block first confirms that Ubuntu can reach Docker, that nothing is using port 5678, and that no `n8n-course` folder or Docker project exists yet. Then it downloads the installer to a review folder and checks that the installer reports version 1.4.0. It opens the installer in `less`, a pager that shows a file one screen at a time. Press **q** when you've read it, and type `INSTALL` to go ahead. The installer accepts the course's pinned n8n version and `--no-start`; see the [official one-line setup](https://docs.n8n.io/deploy/host-n8n/install-options/one-line-setup). The block then changes the one published port line from `'5678:5678'` to `'127.0.0.1:5678:5678'`, so only this laptop can reach the editor. Finally it records the Docker Compose project name `n8n-course`, the name Docker uses to group this stack's containers, volumes, and networks.

**Terminal: Ubuntu Bash, ordinary Linux user, the Ubuntu window you just reopened.**

```bash
course_n8n_configure() {
  local dir="$HOME/n8n-course" review approved found count
  [ "$(id -u)" -ne 0 ] || { printf 'HOLD: use your ordinary Linux user\n'; return 1; }
  if [ -e "$dir" ] || [ -L "$dir" ]; then
    printf 'HOLD: %s already exists; it was kept as it is\n' "$dir"; return 1
  fi
  if [ -n "${DOCKER_HOST:-}" ] || [ -n "${DOCKER_CONTEXT:-}" ]; then
    printf 'HOLD: DOCKER_HOST or DOCKER_CONTEXT is set; review it with the device owner\n'; return 1
  fi
  command -v docker >/dev/null || { printf 'HOLD: docker is not available in Ubuntu; turn on WSL Integration for this distribution in Docker Desktop\n'; return 1; }
  docker info >/dev/null || { printf 'HOLD: Ubuntu cannot reach Docker; check WSL Integration\n'; return 1; }
  docker compose version || return 1
  if ss -ltn 'sport = :5678' | grep -q LISTEN; then
    printf 'HOLD: port 5678 is already in use\n'; return 1
  fi
  found="$(docker ps -aq --filter label=com.docker.compose.project=n8n-course)" || return 1
  found="$found$(docker volume ls -q --filter label=com.docker.compose.project=n8n-course)" || return 1
  found="$found$(docker network ls -q --filter label=com.docker.compose.project=n8n-course)" || return 1
  [ -z "$found" ] || { printf 'HOLD: Docker already has an n8n-course project; it was kept\n'; return 1; }
  review="$(mktemp -d "$HOME/n8n-installer-review.XXXXXX")" || return 1
  curl -fsSL https://get.n8n.io -o "$review/get-n8n.sh" || { printf 'HOLD: download failed; nothing was run\n'; return 1; }
  grep -qx 'SCRIPT_VERSION="1.4.0"' "$review/get-n8n.sh" || { printf 'HOLD: installer version changed; nothing was run\n'; return 1; }
  less "$review/get-n8n.sh"
  read -r -p 'Type INSTALL to create the n8n configuration: ' approved
  [ "$approved" = INSTALL ] || { printf 'HOLD: not confirmed; nothing was run\n'; return 1; }
  N8N_DIR="$dir" sh "$review/get-n8n.sh" --version 2.41.5 --no-start || { printf 'HOLD: installer failed; its files were kept\n'; return 1; }
  count="$(grep -cF -- "- '5678:5678'" "$dir/compose.yml")"
  [ "$count" = 1 ] || { printf 'HOLD: expected one 5678 port line, found %s; compose.yml was not changed\n' "$count"; return 1; }
  sed -i "s/- '5678:5678'/- '127.0.0.1:5678:5678'/" "$dir/compose.yml" || return 1
  grep -qF -- "- '127.0.0.1:5678:5678'" "$dir/compose.yml" || { printf 'HOLD: the port binding was not saved\n'; return 1; }
  (umask 077; set -o noclobber; printf 'n8n-course\n' > "$dir/.course-project") || return 1
  printf 'N8N CONFIGURED %s, port 127.0.0.1:5678, project n8n-course\n' "$dir"
}
course_n8n_configure
```

**Expected:** the Docker Compose version, the installer in `less`, installer lines ending in `Not starting (--no-start)`, then `N8N CONFIGURED`. Nothing starts yet.

**Stop:** any `HOLD:` line.

**Recovery:** keep any folder or files the block made. Don't delete `n8n-course` or run the installer over it; see [If a step stops](#local-n8n-problems).

### Start n8n and inspect it

This helper runs Docker Compose with the recorded project name and the `n8n-course` files every time. If one of the listed variables is exported in your shell, it would override the saved settings, so the helper stops and prints only the variable's name. Define it in each new Ubuntu window before you control n8n.

**Terminal: Ubuntu Bash, ordinary Linux user, same Ubuntu window.**

```bash
course_n8n() {
  local variable conflict=0 project
  for variable in N8N_VERSION N8N_SANDBOX_VERSION N8N_RUNNERS_AUTH_TOKEN SEARXNG_SECRET COMPOSE_PROJECT_NAME COMPOSE_FILE COMPOSE_ENV_FILES COMPOSE_DISABLE_ENV_FILE COMPOSE_PROFILES; do
    if printenv "$variable" >/dev/null 2>&1; then
      printf 'HOLD: %s is exported in this shell\n' "$variable"
      conflict=1
    fi
  done
  [ "$conflict" -eq 0 ] || return 1
  if [ -L "$HOME/n8n-course/.course-project" ] || [ ! -f "$HOME/n8n-course/.course-project" ]; then
    printf 'HOLD: project record is missing or linked\n'; return 1
  fi
  project="$(cat "$HOME/n8n-course/.course-project")" || return 1
  case "$project" in
    ''|[!a-z0-9]*|*[!a-z0-9_-]*) printf 'HOLD: invalid project record\n'; return 1 ;;
  esac
  docker compose -p "$project" --env-file "$HOME/n8n-course/.env" -f "$HOME/n8n-course/compose.yml" "$@"
}
```

**Expected:** nothing prints. The helper is ready but hasn't started anything.

**Stop:** a later call prints a `HOLD:` line.

**Recovery:** ask the owner where the exported variable comes from, then open a clean Ubuntu window and define the helper again.

The first start downloads several images, which can take a while.

**Terminal: Ubuntu Bash, ordinary Linux user, same Ubuntu window.**

```bash
course_n8n up -d &&
  course_n8n ps --all &&
  course_n8n port n8n 5678 &&
  course_n8n exec -T n8n n8n --version
```

**Expected:** six services appear. `sandbox-certs` shows `Exited (0)` because it runs once, and the other five are running, healthy where a health check is shown. The port line is exactly `127.0.0.1:5678`, and n8n prints `2.41.5`.

**Stop:** a service is missing, restarting, or unhealthy; the port isn't `127.0.0.1:5678`; or the version differs.

**Recovery:** give the stack a minute to finish starting, then run the block again. If it still fails, keep the files and volumes and see [If a step stops](#local-n8n-problems).

### Save a blank workflow and confirm it persists

**Window: a Windows browser, ordinary user.**

1. Open **http://localhost:5678**. On a fresh instance, complete **Set up owner account** with local credentials. That account is the local instance owner, not an n8n Cloud account. Skip optional offers and leave the n8n Assistant off.
2. Select **Overview**, then **Build a workflow** or **Create workflow**. Click the title, name it **Module 7 Readiness**, and press Enter. The editor saves on its own. Leave the canvas blank and don't select **Publish**.
3. Reload the page and confirm the name and the blank canvas are still there.

Now stop and restart only this project. Stopping without `-v` keeps the named volumes that hold your workflow.

**Terminal: Ubuntu Bash, ordinary Linux user, same Ubuntu window.**

```bash
course_n8n down &&
  course_n8n up -d &&
  course_n8n ps --all &&
  course_n8n port n8n 5678 &&
  course_n8n exec -T n8n n8n --version
```

**Expected:** the containers stop and start again, with the same six-service state, `127.0.0.1:5678`, and `2.41.5` as before.

**Stop:** a stop or start error, or a different service state, port, or version.

**Recovery:** keep the files and volumes, fix the named error, and run the block again. Never add `-v` or prune volumes.

Reload **http://localhost:5678**, sign in as the same local owner if asked, and open **Module 7 Readiness**. Record **n8n READY** only if the version, the localhost-only port, the six-service state, and the saved workflow all survived the restart. Otherwise record **n8n HOLD** and name the failed check. Type `exit` to leave Ubuntu; Docker Desktop keeps n8n running.

In later sessions, check that Docker Desktop is running, open the same Ubuntu by name, define `course_n8n` again, and run the start block again: after a restart, n8n stays stopped until you start it, and the block starts it and checks it. Reuse the recorded `n8n-course` project. Never run `course_n8n_configure` again for an existing installation.

## If a step stops

Work through the first failure only, and keep its exact message. Keep every existing installation, checkout, vault, attempt folder, container, and volume while you fix it. [When setup stops](../shared/TROUBLESHOOTING.md) covers support packets and telling slow work from a stopped process.

### Steps 1 and 2: tools

- **PowerShell version stop:** you may be in PowerShell 7 (`pwsh`). Open **Windows PowerShell** from Start instead.
- **Low disk space:** free space on the drive that holds your home folder, then run Step 1 again.
- **No published binary for this processor:** save the message and ask for a supported laptop. Don't download the other architecture.
- **Python still missing after installing:** open **Settings → Apps → Advanced app settings → App execution aliases**, turn off the `python.exe` and `python3.exe` aliases, reopen PowerShell from Start, and run Step 1 again. Don't type a guessed Python path.
- **WinGet missing:** with the owner's approval, install only the missing tools from the official [Git for Windows installer](https://git-scm.com/downloads/win) and [Python Windows installer](https://www.python.org/downloads/windows/). For Python, choose 3.12 or newer, install for your user, and select **Add python.exe to PATH**.
- **Installer denied or failed:** keep the message for the device owner. Don't reinstall over an existing tool that fails for an unknown reason.

### Step 3: Oh My Pi

- **Download failed or checksum mismatch:** nothing was installed. A proxy or network inspection tool can change downloads, so ask the device owner about it rather than turning off a check. Running Step 3 again uses a new folder.
- **A different `omp.exe` is already installed, or another `omp` is on PATH:** keep it. Save the printed path and ask whoever installed it how to proceed. Don't overwrite, delete, or hide it.
- **A destination is a link:** your local app data may be redirected. Ask the owner for a local, unredirected location.
- **Windows blocks the verified program from starting:** save the message and ask the owner. Don't turn off a security control.

### Step 4: GitHub access and the checkout

- **Signed in to the wrong account:** open **Credential Manager → Windows Credentials** from the Start menu and remove only the `git:https://github.com` entry, then run the sign-in command again with the invited account.
- **No sign-in window appears:** use GitHub CLI with the three blocks below, then run Step 4 again.
- **`Documents\AIHB_OCT_2026` exists but isn't this course, or has a different origin:** leave it untouched, and choose another location only with the person who supports your machine.
- **Line-ending `HOLD:`:** don't edit or renormalize those files. After the person who supports your machine moves the folder aside, run Step 4 again so it makes a fresh copy.
- **Clone failed partway:** keep the partial folder and its message for support rather than deleting it.

If `gh` is already installed, this block only prints its version. The installer may ask for approval. See [GitHub CLI on Windows](https://github.com/cli/cli/blob/trunk/docs/install_windows.md).

**Terminal: Windows PowerShell 5.1, ordinary user, same window.**

```powershell
. {
  if (Get-Command gh -CommandType Application -ErrorAction SilentlyContinue) { gh --version; if ($LASTEXITCODE -ne 0) { throw 'STOP: the existing GitHub CLI failed. Keep its message.' }; return }
  if (-not (Get-Command winget -CommandType Application -ErrorAction SilentlyContinue)) { throw 'STOP: WinGet is missing; ask the device owner to install GitHub CLI.' }
  winget install --exact --id GitHub.cli --source winget
  if ($LASTEXITCODE -ne 0) { throw 'STOP: GitHub CLI did not install. Keep the message.' }
  Write-Output 'INSTALLED: close every terminal window, open Windows PowerShell from Start, and run Step 1 again.'
}
```

**Expected:** a `gh version` line, or `INSTALLED:`. After an install, reopen PowerShell from Start and run Step 1 before continuing.

**Stop:** a `STOP:` line or a denied approval.

**Recovery:** keep the message and ask the device owner to provide GitHub CLI.

Run the browser login by itself. Use the invited account, and when asked whether to authenticate Git with your GitHub credentials, choose **Yes**. Don't share the one-time code. See [gh auth login](https://cli.github.com/manual/gh_auth_login).

**Terminal: Windows PowerShell 5.1, ordinary user, same window.**

```powershell
gh auth login --hostname github.com --git-protocol https --web
```

**Expected:** the browser authorization completes and the command reports that you're logged in.

**Stop:** the wrong account, a denied authorization, or an error.

**Recovery:** fix the account or invitation with the repository owner before you log in again.

**Terminal: Windows PowerShell 5.1, ordinary user, same window.**

```powershell
gh auth status --hostname github.com
```

**Expected:** `Logged in to github.com account` with the invited account and `(keyring)`. Then run Step 4 again.

**Stop:** the wrong account, or a file path in place of `(keyring)`, which means the token is stored in a plain file.

**Recovery:** ask the device owner whether that storage is allowed before you continue. Don't add `--show-token` or share this output.

### Step 5: a new window

- **`omp` missing or a different program:** confirm you closed every window and opened PowerShell from Start. If it still fails, run Step 1 and Step 3 again; Step 3 keeps an identical `omp.exe` and saves PATH only if it's missing.
- **`SET` before you typed a key:** something supplies the key to new windows. This check looks for it in your saved environment and PowerShell profiles without printing the value.

**Terminal: Windows PowerShell 5.1, ordinary user, same window.**

```powershell
. {
  foreach ($scope in @('User', 'Machine')) {
    if (-not [string]::IsNullOrEmpty([Environment]::GetEnvironmentVariable('OPENROUTER_API_KEY', $scope))) { throw ('STOP: a saved ' + $scope + ' environment entry exists. The value was not printed.') }
  }
  foreach ($path in @($PROFILE.CurrentUserCurrentHost, $PROFILE.CurrentUserAllHosts, $PROFILE.AllUsersCurrentHost, $PROFILE.AllUsersAllHosts)) {
    if ($path -and (Test-Path -LiteralPath $path) -and (Select-String -LiteralPath $path -Pattern 'OPENROUTER_API_KEY' -SimpleMatch -Quiet)) { throw 'STOP: a PowerShell profile names the key variable. The line was not printed.' }
  }
  Write-Output 'No saved environment entry or profile reference was found.'
}
```

**Expected:** a `STOP:` line that names where the key is saved, or the no-entry line.

**Stop:** the no-entry line while new windows still print `SET` means another program supplies the key.

**Recovery:** revoke a key that was saved without authorization. For a Machine entry or a profile line, ask the owner to fix it. For a User entry, run the next block.

Run this only if the check named the **User** scope.

**Terminal: Windows PowerShell 5.1, ordinary user, same window.**

```powershell
[Environment]::SetEnvironmentVariable('OPENROUTER_API_KEY', $null, 'User')
```

**Expected:** no output and no key text.

**Stop:** the check didn't name the User scope.

**Recovery:** use the owner route for Machine or profile findings, then open a new window from Start and run Step 5 again.

### Steps 6 and 7: the key

- **The key appeared on screen or in a command:** revoke it with OpenRouter, then repeat Step 6 with the replacement.
- **`MISSING` after Step 7:** run Step 6 and Step 7 again in the same window. [Use one OpenRouter key without putting it in your work](../shared/CREDENTIALS.md) covers where the key must never go.

### Step 8: the readiness check

- **`LAUNCH_EXIT 2`:** a prerequisite failed before the live attempt, such as a missing key or `omp` not being on PATH, and the evidence folder wasn't created. Fix the named cause, then run Step 8 again for a new attempt.
- **`LAUNCH_EXIT 1`, `VERIFY_EXIT 1`, or `READINESS CHECK HOLD`:** the live attempt ran and failed. Keep both folders, read the `FAIL:` line or the launcher's message, and fix that cause. Common causes are a rejected key, an OpenRouter account problem, or a network block.
- Never write or edit `from-omp.txt` yourself, and never run the launcher again in the same attempt folder.

### Step 9: the setup report

- **`STOP: a restrictive execution policy is set on this computer (Get-ExecutionPolicy -List)`, running scripts is disabled, or the file isn't digitally signed:** a restrictive policy (on Machine/User or explicit Process) or other restriction is configured on this computer, or your organization manages it. The gate checks configured restrictive scopes before allowing any permissive run or child. Ask the device owner for an approved way to run the reviewed checker. Don't use `Bypass` or `Unrestricted`, change the policy yourself, unblock files, or paste the script's contents.
- **`SETUP CHECK HOLD`:** fix the first `FAIL` line's `NEXT ACTION`, then run Steps 8 and 9 again for a new attempt.
- **The report already exists:** the checker never overwrites a report. Run Step 8 again for a new attempt.

### Local Obsidian problems

- **Obsidian was already installed:** keep it, use it as it is, and record the version it shows.
- **The installer refuses, wants to replace an install, or needs approval:** cancel, record **Obsidian HOLD**, and keep the message for the owner. Don't delete a profile or reinstall over an app.
- **The check doesn't match:** in Obsidian, correct only Reply to match the current Token, save it, and check again. Don't edit Start, Token, or the records.
- **Token changed only after a restart:** that doesn't show a live refresh. With the correct vault open and Token showing, run the outside-edit block again, then repeat the edit, save, and reopen.

### Local n8n problems

- **Ubuntu already has its own Docker Engine:** keep it, and don't turn on Docker Desktop integration for that distribution until its owner has backed up its work and resolved the conflict.
- **Docker Desktop installed but stopped:** get the owner's approval before starting it.
- **`docker info` fails in Ubuntu:** check that WSL Integration is on for the exact distribution you opened, and that Docker Desktop is running.
- **`n8n-course` or a Docker project with that name already exists:** keep it, and ask its owner which project, version, and port it uses before you control it.
- **Port 5678 in use:** identify the owner of the listening process with the device owner. Don't stop processes or containers to free the port.
- **Installer version changed:** nothing ran. Ask the owner to review the new installer before you go on.
- **Services unhealthy or wrong version:** keep the result as HOLD. Don't change the pinned version, delete volumes, or disable services.

If `wsl --version` printed help text or a version below 2.1.5, update WSL after the owner approves. Save your work first, because the update can stop running Linux distributions.

**Terminal: Windows PowerShell, elevated with Run as administrator, owner-approved update only.**

```powershell
. {
  wsl --update
  if ($LASTEXITCODE -ne 0) { throw 'STOP: the WSL update failed. Keep the message.' }
  wsl --version
}
```

**Expected:** a WSL version of 2.1.5 or newer.

**Stop:** an error, a denial, or a request to restart.

**Recovery:** complete any approved restart, then run the Windows check again in an ordinary window.

If your Ubuntu shows VERSION `1`, the owner first makes a backup that can be restored, using [wsl --export](https://learn.microsoft.com/en-us/windows/wsl/basic-commands#export-a-distribution). Then convert that exact distribution: replace `Ubuntu-24.04` in the command with the NAME that shows VERSION `1` in your list.

**Terminal: Windows PowerShell 5.1, ordinary user, owner-approved conversion after a backup.**

```powershell
wsl --set-version Ubuntu-24.04 2
```

**Expected:** the conversion finishes, and `wsl --list --verbose` shows VERSION `2` for that name.

**Stop:** the conversion fails or the entry still shows `1`.

**Recovery:** keep the distribution and the backup, and ask the owner to resolve the error. Never unregister or reset a distribution to fix it.

If the Ubuntu check printed `STOP: curl is missing`, install only these packages after the owner approves. `sudo` asks for your Linux password, which doesn't show as you type.

**Terminal: Ubuntu Bash, ordinary Linux user with sudo, owner-approved packages only.**

```bash
sudo apt-get update && sudo apt-get install --no-upgrade curl ca-certificates
```

**Expected:** the packages install without removing or upgrading other packages. Then run the Ubuntu check again.

**Stop:** a policy denial, a package error, or a proposal to remove software.

**Recovery:** answer `n` at any removal proposal and keep the message for the owner. Don't weaken certificate checks.

## Local model (capstone) readiness lane

Ask staff for the approved native Windows `hf` and `llama-server` paths, then [check local-model readiness](../../module-10-capstone/shared/MODULE_10_LAB.md#check-local-model-readiness-before-downloading) before a download and again before launch. Use `&` with each quoted executable path. Missing tools, insufficient capacity, an occupied endpoint, or an unresolved failed rehearsal mean **Local model HOLD**; preserve your other readiness results and contact the device/support owner. Linux or PowerShell 7 observations do not establish native Windows PowerShell 5.1 operation.
