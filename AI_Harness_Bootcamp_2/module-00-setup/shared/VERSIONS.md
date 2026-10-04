# Required tool identities

Use the exact OMP and n8n releases and provider/model pair below. A newer executable or a similarly named model is not an automatic substitute.

| Component | Required value | Check |
|---|---|---|
| Oh My Pi | 18.3.5 | The verified executable reports `omp/18.3.5`. |
| Provider/model | `openrouter/anthropic/claude-sonnet-4.6` | The launcher and actual run receipts agree on OpenRouter and Sonnet 4.6. |
| Credential | `OPENROUTER_API_KEY` | A presence-only check reports `SET` in the process that launches OMP. |
| Python | 3.12 or newer | Resolve its absolute executable path and inspect its version. |
| Obsidian | Local desktop app required for Module 2; fresh reference 1.13.7 | Keep an existing version; record it, and watch the full GUI workflow in the Obsidian window separately from the disk check. |
| n8n | 2.41.5, local full official Docker stack | Check the running container version, service state, localhost port, editor access, and saved-workflow persistence separately from OMP. |
| Docker and Compose | Approved local engine and modern `docker compose` plugin | `docker info` and `docker compose version` succeed as the ordinary user in the intended new shell; version 5 is acceptable. |
| Git | A supported release for your operating system | Git runs and the intended checkout is readable. |
| Browser and text editor | An accessible combination you can operate | You can read instructions, edit plain-text work files, and inspect actual outputs. |

You need read access to the private course repository on GitHub. If your existing approved Git credentials work, you don't need another login tool. Otherwise, follow the platform steps to log in through your browser with [GitHub CLI (`gh`)](https://cli.github.com/manual/gh_auth_login). The package is `GitHub.cli` in WinGet, `gh` in Homebrew and Ubuntu Universe, and `github-cli` in Arch's official repositories. GitHub CLI helps you reach the repository; you do not need it to run the AI tools.

Download the OMP binary and `SHA256SUMS.txt` from the [same v18.3.5 release](https://github.com/can1357/oh-my-pi/releases/tag/v18.3.5). Select the asset for the operating system in which it will run:

| Runtime | ARM64 asset | x86-64 asset |
|---|---|---|
| macOS | `omp-darwin-arm64` | `omp-darwin-x64` |
| Linux, including Ubuntu in WSL | `omp-linux-arm64` | `omp-linux-x64` |
| Native Windows | `omp-windows-arm64.exe` | `omp-windows-x64.exe` |

Check the selected file's checksum before installing or first running it. Install it at `~/.local/bin/omp` on Unix or `%LOCALAPPDATA%\omp\omp.exe` on native Windows. If you already have a different installation, keep it rather than quietly overwriting it.

## Match the package route to the operating system

| Setup route | Operating-system and shell boundary |
|---|---|
| Native Windows OMP | Windows PowerShell 5.1 on an owner-supported Windows installation with WinGet; x64 or ARM64. PowerShell on macOS/Linux is a different environment. n8n alone uses a separate WSL 2 Ubuntu bridge with Docker Desktop integration; its host requirements and owner approvals also apply. |
| Windows with WSL 2 | Windows 10 build 19041+ or Windows 11 is the technical floor for Microsoft's install command; Obsidian needs the higher WSLg floor of Windows 10 build 19044+ or Windows 11. The host must also remain supported under the device owner's policy. Use Ubuntu 24.04 or 26.04 in WSL 2 and run course commands in Ubuntu Bash. |
| macOS | Bash or zsh on Apple Silicon or Intel. Homebrew's current supported-install requirements are macOS 15+; Intel is Tier 3. An OMP download for Intel doesn't mean Homebrew supports Intel equally. |
| Ubuntu | Ubuntu 24.04 or 26.04 on x86-64 or ARM64, using Bash or zsh and the distribution's Python package. |
| Arch Linux | Current official Arch Linux on x86-64, using Bash or zsh. Arch Linux ARM is a separate distribution, not this package route. |

Check your OS and architecture before installing. A binary may be available even when your operating system is not supported. Keep a suitable tool you already have, and do not replace system Python or add a package source just to get past a version hold.

The launcher keeps the runtime configuration separate, makes only the named course tools available, and turns off automatic retries, model fallback, cache warming, unrelated extensions, skills, and persistent sessions. Use it for exercises instead of your personal OMP profile. A prerequisite report shows what is set up, not what happened during a model turn; check the readiness receipts to see whether those controls worked.

You do not need another model-provider key or agent CLI. For Module 2, you need local Obsidian with Sync off and community plugins restricted, but you do not need an account, plugin, or MCP service. For Module 7, you need local n8n and a local instance-owner login, but not n8n Cloud signup, an Assistant key, or a paid model call. If the pinned release or model is unavailable, keep the failure and put that part of setup on hold. Do not use an unreviewed substitute to get a passing label.

## Local Obsidian for Module 2

Keep any existing installation, its profile, and personal vaults. Record the version you have, then complete the same workflow and check what happens in the app; do not upgrade or downgrade just to match the reference. For a fresh vendor installation, use **1.13.7**. The asset names and SHA-256 values come from an approved record of the [official release metadata](https://api.github.com/repos/obsidianmd/obsidian-releases/releases/tags/v1.13.7), and downloads come from the [official v1.13.7 release](https://github.com/obsidianmd/obsidian-releases/releases/tag/v1.13.7). Check the selected download before running it.

| Fresh route | Official asset | Exact SHA-256 |
|---|---|---|
| macOS, Apple Silicon or Intel | [Obsidian-1.13.7.dmg](https://github.com/obsidianmd/obsidian-releases/releases/download/v1.13.7/Obsidian-1.13.7.dmg) | `05daa54f5e1a4458f75da29f8faaa17e8e37ae16998432537f674c626db99bce` |
| Native Windows, x64 or ARM64 | [Obsidian-1.13.7.exe](https://github.com/obsidianmd/obsidian-releases/releases/download/v1.13.7/Obsidian-1.13.7.exe) | `f233dc24896b3f2d5f9e4b01111181a561d0760b2105f0a474024c5f3143a9bc` |
| Ubuntu/WSLg x86-64 | [obsidian_1.13.7_amd64.deb](https://github.com/obsidianmd/obsidian-releases/releases/download/v1.13.7/obsidian_1.13.7_amd64.deb) | `17dc33b49cb3e785ecc27edd2ea0c79e40207798b554fd2886e36ebee7af9ae0` |
| Ubuntu/WSLg ARM64 | [Obsidian-1.13.7-arm64.AppImage](https://github.com/obsidianmd/obsidian-releases/releases/download/v1.13.7/Obsidian-1.13.7-arm64.AppImage) | `e286fd2bb2a5d346a35a577bd764c73fd5537dddec2b99a1a3e5e35974085203` |

On Arch x86-64, install the signed [Arch Extra `obsidian` package](https://archlinux.org/packages/extra/x86_64/obsidian/) through the guide's approved `pacman -Syu` full upgrade. The reference package version was **1.13.7-2**. Arch maintains this package; it is not from AUR or a vendor download. Record the version you installed and check that the app is ready. Do not apply the vendor hashes to this package, downgrade Arch, or run a partial upgrade. See [Arch's full-upgrade guidance](https://wiki.archlinux.org/title/System_maintenance#Partial_upgrades_are_unsupported).

WSLg runs Linux Obsidian inside your existing Ubuntu distribution, using the same Linux home as OMP. To show the app window, it [needs Windows 10 build 19044+ or Windows 11 and WSL 2](https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps). Builds 19041–19043 can run the earlier CLI steps while Obsidian stays on HOLD. Keep the distribution and any active Docker workloads; get an owner-approved window for updates or restarts. Do not open a WSL UNC vault in native Windows Obsidian or move course files to `/mnt/c`.

On Ubuntu 24.04/26.04 ARM64, follow the guide's approved `libfuse2t64` package step to run AppImage. Keep FUSE 3, and do not install obsolete `fuse` instead. The [AppImage FUSE guidance](https://docs.appimage.org/user-guide/troubleshooting/fuse.html) explains the compatibility library is needed. The vendor's [AppImage launch instructions](https://github.com/obsidianmd/obsidian-help/blob/master/en/Getting%20started/Download%20and%20install%20Obsidian.md) use `chmod u+x` and `./Obsidian-1.13.7-arm64.AppImage --no-sandbox`. The second command turns off Chromium's renderer sandbox for this app, so you need separate device-owner approval. It does not add to or replace the course tool boundary. Without approval, Obsidian stays on HOLD; do not change kernel-wide security settings, permissions, or privileged sandbox files to force it to launch.

These Obsidian app steps have been checked only on **Obsidian 1.13.7 on Darwin arm64**. The app window on native Windows, WSLg, Intel macOS, Ubuntu, and Arch has not been checked here. Having an asset, a command that parses, or a disk PASS from the helper does not show that the app works on those systems. On each device, follow the link/edit/save/refresh/reopen practice in its [platform guide](../README.md#set-up-local-obsidian), using local files, Restricted community plugins, and Sync off.

## Local n8n stack contract

The [official installer source](https://raw.githubusercontent.com/n8n-io/n8n/master/docker/get-n8n.sh) that was checked identifies itself as **1.4.0**. The platform guides select n8n **2.41.5** with `--version 2.41.5 --no-start` and `N8N_DIR="$HOME/n8n-course"`. The live installer URL and Compose source can change, and the installer version is not the running n8n version. Use the guide’s download-and-review alternative to inspect the fully downloaded script before you run it. Keep any existing destination, including partial attempts; an “existing install” response does not tell its version or whether it is ready. If a different version is running, keep it on HOLD until the owner resolves it; do not automatically upgrade or change the pinned version.

The [official Compose stack](https://raw.githubusercontent.com/n8n-io/n8n/master/docker/get-n8n-compose.yml) has six services: `n8n`, `runners`, `sandbox-certs`, `sandbox-api`, `sandbox-runner-1`, and `searxng`. Five should keep running, and `sandbox-certs` should finish successfully (`Exited (0)`). The runner uses privileged Docker-in-Docker, so it needs device-owner approval even when Assistant is off. Wherever you use Docker Desktop, the owner must approve license eligibility. On Linux, you need approved daemon access from your ordinary account; do not run the installer as root or make the socket world-writable.

For a fresh configuration, change only the n8n port mapping from `5678:5678` to `127.0.0.1:5678:5678` before you start it. Leave the other services and named volumes in place, and do not display `.env` or resolved Compose secrets. The course's usual `down` / `up -d` commands keep named data; do not use `down -v` for course work.

For a fresh installation, the platform guide has you save one unused project name approved by the owner in `.course-project`. The `course_n8n` helper uses that name, `.env`, and `compose.yml`, and it refuses exported configuration overrides. Use the same saved name on the same approved engine for every restart; a file path by itself does not tell Compose which project to use. If you already have an installation, keep its existing project identity and let its owner manage its lifecycle.

The runtime, UI, and saved-workflow checks were done only on Apple Silicon. Published amd64/arm64 images do not show that those parts run on other platforms. If you use Windows, Intel macOS, Ubuntu, or Arch, check them on that device.
