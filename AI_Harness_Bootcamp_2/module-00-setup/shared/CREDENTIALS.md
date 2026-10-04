# Use one OpenRouter key without putting it in your work

Use the OpenRouter key you were given for `openrouter/anthropic/claude-sonnet-4.6`. An SDK cost estimate is not a bill, even when a local script reports it.

Keep the key in your approved password manager. Don't put it in a prompt, command argument, file, shell profile, Git setting, screenshot, chat, ticket, or evidence record. The launcher reads it from this process's environment and gives OMP an isolated configuration; you don't need another provider login.

## Keep repository access separate from model access

Get each kind of access separately:

- The **hosted-course password** opens the website but does not give you GitHub repository access.
- Your **GitHub account** needs read permission for the private `TheHolofex/AIHB_OCT_2026` repository. Accept the owner's invitation with the account you plan to use.
- Your **OpenRouter key** lets you send model requests, which OpenRouter bills to the key's account. It does not log you in to Git or GitHub.

In your platform guide, test read access to that exact repository with prompts disabled. If your approved Git credentials work, you don't need another login tool. Otherwise, follow the platform's GitHub CLI (`gh`) browser-login steps. GitHub CLI helps you reach the repository. It isn't another AI tool, and you don't need it to run OMP.

Before authorizing browser login, check the GitHub hostname, device code, and invited account. Then repeat the repository read check. Logging in alone doesn't grant permission. If the check fails, ask the owner to fix the invitation, organization approval, or network error. Don't log in again to try to gain permission.

[GitHub CLI prefers an operating-system credential store but can fall back to a plaintext file](https://cli.github.com/manual/gh_auth_login). Check which storage `gh auth status --hostname github.com` shows. Don't add `--show-token` or put authentication output in shared evidence. If device policy forbids that storage, stop and ask the device owner for approved storage or Git credentials. Don't use insecure storage. Only if fallback storage is needed and approved, follow the platform steps to set up `gh` as the Git credential helper for `github.com` alone.

## Enter the key through a hidden prompt

Choose your terminal's command. Paste only that command and press Enter. At the hidden prompt, type your OpenRouter key, which you enter in the terminal rather than save in a file, then press Enter. Don't paste the export or conversion commands while the prompt waits.

**Terminal: Bash or zsh, ordinary user.**

```bash
IFS= read -r -s OPENROUTER_API_KEY
```

**Terminal: PowerShell, ordinary user.**

```powershell
$secret = Read-Host 'OpenRouter key' -AsSecureString
```

**Expected:** The terminal accepts the key without displaying its value and returns to the ordinary prompt.

**Stop:** Characters are visible, the prompt is inaccessible with your access method, or you are unsure which program is receiving the input.

**Recovery:** Cancel input and close the terminal. If the key was exposed, revoke it in OpenRouter and get a replacement. Ask for an accessible approved input method; don't turn off masking.

## Make it available only to this process and its children

Wait until hidden input finishes. In PowerShell, the next block briefly converts the secure string to an environment value. It then clears and frees the temporary memory and disposes of the secure-string object.

**Terminal: Bash or zsh, ordinary user.**

```bash
export OPENROUTER_API_KEY
if [ -n "${OPENROUTER_API_KEY:-}" ]; then printf 'SET\n'; else printf 'MISSING\n'; fi
```

**Terminal: PowerShell, ordinary user.**

```powershell
$bstr = [IntPtr]::Zero
try {
  $bstr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secret)
  $env:OPENROUTER_API_KEY = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($bstr)
} finally {
  if ($bstr -ne [IntPtr]::Zero) { [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($bstr) }
  if ($secret) { $secret.Dispose() }
  Remove-Variable secret,bstr -ErrorAction SilentlyContinue
}
if ([string]::IsNullOrWhiteSpace($env:OPENROUTER_API_KEY)) { 'MISSING' } else { 'SET' }
```

**Expected:** Only `SET` prints. The key is present in this process; this doesn't check validity, credit, model availability, or a successful provider call.

**Stop:** The result is `MISSING`, conversion fails, or any key value appears in output.

**Recovery:** Re-enter the key through the hidden prompt. Revoke an exposed key first. Don't print the environment to troubleshoot.

## Check a separately opened terminal

Open a new terminal independently of the one where you entered the key. It should report `MISSING`. A child shell started from the first terminal can inherit its environment, so it isn't an independent check. `SET` alone doesn't mean the key was saved in a profile or leaked.

**Terminal: Bash or zsh, ordinary user, independently opened window.**

```bash
if [ -n "${OPENROUTER_API_KEY:-}" ]; then printf 'SET\n'; else printf 'MISSING\n'; fi
```

**Terminal: PowerShell, ordinary user, independently opened window.**

```powershell
if ([string]::IsNullOrWhiteSpace($env:OPENROUTER_API_KEY)) { 'MISSING' } else { 'SET' }
```

**Expected:** `MISSING` in an independent window. Enter the key again there when you need a paid turn.

**Stop:** If a new terminal window unexpectedly shows `SET`, find out why before describing the key as process-only.

**Recovery:** Check how the terminal started and whether an approved parent supplied the variable. Don't put profile or environment values in evidence. Revoke the key if you find an exposed or unauthorized saved copy.

## End access when you finish

Close the terminal to remove its process environment, or remove the variable from the current process:

**Terminal: Bash or zsh, ordinary user.**

```bash
unset OPENROUTER_API_KEY
```

**Terminal: PowerShell, ordinary user.**

```powershell
Remove-Item Env:OPENROUTER_API_KEY -ErrorAction SilentlyContinue
```

**Expected:** The presence-only check now reports `MISSING` in that process.

**Stop:** A child process may still have an inherited copy. Removing the variable doesn't revoke the provider key.

**Recovery:** Close those processes. Revoke the provider key if access must end everywhere or the value was exposed.

Record the provider/model identity, `omp/18.3.5`, whether the check showed `SET` or `MISSING`, and redacted run outcomes. Never save any part of the key. The current process environment limits persistence but doesn't shield it from other processes under your account.

Sources: [OpenRouter key settings](https://openrouter.ai/settings/keys), [Sonnet 4.6 through OpenRouter](https://openrouter.ai/anthropic/claude-sonnet-4.6), and [OMP model resolution at v18.3.5](https://github.com/can1357/oh-my-pi/blob/v18.3.5/docs/models.md).
