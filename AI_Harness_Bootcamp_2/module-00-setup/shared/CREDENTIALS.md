# Use one OpenRouter key without putting it in your work

Use the OpenRouter key you were given for `openrouter/anthropic/claude-sonnet-4.6`. An SDK cost estimate is not a bill, even when a local script reports it.

Keep the key in your approved password manager. Do not put it in a prompt, command argument, file, shell profile, Git setting, screenshot, chat, ticket, or evidence record. The course launcher reads it from the current process environment and gives OMP its own isolated configuration; you do not need another provider login.

## Keep repository access separate from model access

Three kinds of access serve different purposes:

- The **hosted-course password** opens the website but does not give you GitHub repository access.
- Your **GitHub account** needs read permission for the private `TheHolofex/AIHB_OCT_2026` repository. Accept the owner's invitation with the account you plan to use.
- Your **OpenRouter key** lets you send model requests, which OpenRouter bills to the key's account. It does not log you in to Git or GitHub.

Each platform first checks whether your existing approved Git credentials can read the exact repository without prompting in the terminal. If they can, keep using them. If they cannot, follow the platform's GitHub CLI (`gh`) steps to log in through your browser. `gh` helps with repository access; it is not another AI tool or needed to run OMP.

Before authorizing browser login, check the GitHub hostname, device code, and invited account. Then check that you can read the exact repository; login alone does not show you have permission. If the read check still fails, work with the responsible owner to fix the invitation, organization approval, or network error. Logging in again cannot grant permission.

[GitHub CLI prefers an operating-system credential store but can fall back to a plaintext file](https://cli.github.com/manual/gh_auth_login). Check where `gh auth status --hostname github.com` says the credentials are stored, but do not add `--show-token` or copy authentication output into shared evidence. If device policy does not allow that storage, stop and ask the device owner to set up approved storage or Git credentials; do not ask to use insecure storage. The platform steps set up GitHub CLI as a Git credential helper only for `github.com`, after you need the fallback and its storage is approved.

## Enter the key through a hidden prompt

Choose the command for your terminal. Paste this command by itself, press Enter, then enter the key at the hidden prompt and press Enter again. Do not paste the export or conversion commands while the hidden prompt is waiting.

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

**Recovery:** Cancel the input and close that terminal. If the value was exposed, revoke it in OpenRouter and use a replacement. Ask for an accessible approved input method; do not turn off masking.

## Make it available only to this process and its children

Wait for the hidden-input command to finish before running the matching block. In PowerShell, the block briefly converts the secure string into the environment value the client needs, then clears and frees its unmanaged buffer and disposes of the secure-string object.

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

**Expected:** Only `SET` is printed. This means the key is present in this process; it does not check whether the key is valid, you have credit, the model is available, or a provider call succeeded.

**Stop:** The result is `MISSING`, conversion fails, or any key value appears in output.

**Recovery:** Re-enter through the isolated hidden-input step. Revoke an exposed key before doing anything else. Never print the environment to troubleshoot credentials.

## Check a separately opened terminal

A new terminal window opened fresh should not inherit a key from one you used earlier. A child shell started from that earlier window can inherit its exported environment, though. Seeing `SET` by itself does not mean the key was saved in a profile or leaked.

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

**Recovery:** Check how the terminal was launched and whether an approved parent process supplied the variable. Do not dump profiles or environment values into evidence. Revoke the key if you find an exposed or unauthorized persisted copy.

## End access when you finish

Closing the terminal removes its process environment. You can also remove the variable from the current process explicitly.

**Terminal: Bash or zsh, ordinary user.**

```bash
unset OPENROUTER_API_KEY
```

**Terminal: PowerShell, ordinary user.**

```powershell
Remove-Item Env:OPENROUTER_API_KEY -ErrorAction SilentlyContinue
```

**Expected:** The presence-only check now reports `MISSING` in that process.

**Stop:** A child process that already inherited the key may still hold its own copy. Removing the key from the environment doesn't revoke it at the provider.

**Recovery:** Close those processes. Revoke the provider key when access must end everywhere or a value was exposed.

Save the provider/model identity, `omp/18.3.5`, whether the check showed `SET` or `MISSING`, and redacted run outcomes. Never save any part of the key. Keeping it in the current process environment limits persistence, but it does not shield it from every other process running under your account.

Sources: [OpenRouter key settings](https://openrouter.ai/settings/keys), [Sonnet 4.6 through OpenRouter](https://openrouter.ai/anthropic/claude-sonnet-4.6), and [OMP model resolution at v18.3.5](https://github.com/can1357/oh-my-pi/blob/v18.3.5/docs/models.md).
