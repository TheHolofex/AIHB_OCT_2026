# Required tool identities

Use the exact OMP release and provider/model pair below. A newer executable or a similarly named model is not an automatic substitute.

| Component | Required value | Check |
|---|---|---|
| Oh My Pi | 18.3.5 | The verified executable reports `omp/18.3.5`. |
| Provider/model | `openrouter/anthropic/claude-sonnet-4.6` | The launcher and actual run receipts agree on OpenRouter and Sonnet 4.6. |
| Credential | `OPENROUTER_API_KEY` | A presence-only check reports `SET` in the process that launches OMP. |
| Python | 3.12 or newer | Resolve its absolute executable path and inspect its version. |
| Git | A supported release for your operating system | Git runs and the intended checkout is readable. |
| Browser and text editor | An accessible combination you can operate | You can read instructions, edit plain-text work files, and inspect actual outputs. |

GitHub read access to the private course repository is required. If existing approved Git credentials already work, no additional login tool is needed. Otherwise the platform steps use [GitHub CLI (`gh`)](https://cli.github.com/manual/gh_auth_login) for browser authentication. Its package is `GitHub.cli` in WinGet, `gh` in Homebrew and Ubuntu Universe, and `github-cli` in Arch's official repositories. It is a conditional repository-access helper, not an AI runtime dependency.

Download the OMP binary and `SHA256SUMS.txt` from the [same v18.3.5 release](https://github.com/can1357/oh-my-pi/releases/tag/v18.3.5). Select the asset for the operating system in which it will run:

| Runtime | ARM64 asset | x86-64 asset |
|---|---|---|
| macOS | `omp-darwin-arm64` | `omp-darwin-x64` |
| Linux, including Ubuntu in WSL | `omp-linux-arm64` | `omp-linux-x64` |
| Native Windows | `omp-windows-arm64.exe` | `omp-windows-x64.exe` |

Verify the selected file's checksum before installation or first execution. The Unix user destination is `~/.local/bin/omp`; native Windows uses `%LOCALAPPDATA%\omp\omp.exe`. Preserve a different existing installation rather than overwrite it silently.

## Match the package route to the operating system

| Setup route | Operating-system and shell boundary |
|---|---|
| Native Windows | Windows PowerShell 5.1 on an owner-supported Windows installation with WinGet; x64 or ARM64. PowerShell on macOS/Linux is a different environment. |
| Windows with WSL 2 | Windows 10 build 19041+ or Windows 11 is the technical floor for Microsoft's install command; the host must also remain supported under the device owner's policy. Use Ubuntu 24.04 or 26.04 in WSL 2 and run course commands in Ubuntu Bash. |
| macOS | Bash or zsh on Apple Silicon or Intel. Homebrew's current supported-install requirements are macOS 15+; Intel is Tier 3. An OMP asset for Intel does not establish equal Homebrew support. |
| Ubuntu | Ubuntu 24.04 or 26.04 on x86-64 or ARM64, using Bash or zsh and the distribution's Python package. |
| Arch Linux | Current official Arch Linux on x86-64, using Bash or zsh. Arch Linux ARM is a separate distribution, not this package route. |

Check OS and architecture before installation. A binary's availability does not make an unsupported operating system supported. Keep a suitable existing tool; do not replace system Python or add a package source to get past a version hold.

The launcher isolates runtime configuration, exposes only declared course tools, and disables automatic retries, model fallback, cache warming, unrelated extensions, skills, and persistent sessions. Use that launcher for exercises rather than a personal OMP profile. A setup check alone does not prove these controls acted during a model turn; inspect the run's receipts.

No other model-provider key, vendor login, agent CLI, note-taking application, or workflow service is required. If the pinned release or model is unavailable, retain the failure and hold that lane. Do not choose an unreviewed substitute to obtain a passing label.
