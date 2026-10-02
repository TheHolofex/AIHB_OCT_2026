# Required tool identities

Use the exact OMP and n8n releases and provider/model pair below. A newer executable or a similarly named model is not an automatic substitute.

| Component | Required value | Check |
|---|---|---|
| Oh My Pi | 18.3.5 | The verified executable reports `omp/18.3.5`. |
| Provider/model | `openrouter/anthropic/claude-sonnet-4.6` | The launcher and actual run receipts agree on OpenRouter and Sonnet 4.6. |
| Credential | `OPENROUTER_API_KEY` | A presence-only check reports `SET` in the process that launches OMP. |
| Python | 3.12 or newer | Resolve its absolute executable path and inspect its version. |
| n8n | 2.41.5, local full official Docker stack | Check the running container version, service state, localhost port, editor access, and saved-workflow persistence separately from OMP. |
| Docker and Compose | Approved local engine and modern `docker compose` plugin | `docker info` and `docker compose version` succeed as the ordinary user in the intended new shell; version 5 is acceptable. |
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
| Native Windows OMP | Windows PowerShell 5.1 on an owner-supported Windows installation with WinGet; x64 or ARM64. PowerShell on macOS/Linux is a different environment. n8n alone uses a separate WSL 2 Ubuntu bridge with Docker Desktop integration; its host requirements and owner approvals also apply. |
| Windows with WSL 2 | Windows 10 build 19041+ or Windows 11 is the technical floor for Microsoft's install command; the host must also remain supported under the device owner's policy. Use Ubuntu 24.04 or 26.04 in WSL 2 and run course commands in Ubuntu Bash. |
| macOS | Bash or zsh on Apple Silicon or Intel. Homebrew's current supported-install requirements are macOS 15+; Intel is Tier 3. An OMP asset for Intel does not establish equal Homebrew support. |
| Ubuntu | Ubuntu 24.04 or 26.04 on x86-64 or ARM64, using Bash or zsh and the distribution's Python package. |
| Arch Linux | Current official Arch Linux on x86-64, using Bash or zsh. Arch Linux ARM is a separate distribution, not this package route. |

Check OS and architecture before installation. A binary's availability does not make an unsupported operating system supported. Keep a suitable existing tool; do not replace system Python or add a package source to get past a version hold.

The launcher isolates runtime configuration, exposes only declared course tools, and disables automatic retries, model fallback, cache warming, unrelated extensions, skills, and persistent sessions. Use that launcher for exercises rather than a personal OMP profile. A prerequisite report alone does not establish that these controls acted during a model turn; inspect the readiness check's receipts.

No additional model-provider key, agent CLI, or note-taking application is required. Local n8n is required for Module 6, with a local instance-owner login. No n8n Cloud signup, Assistant key, or paid model call is required for that module. If the pinned release or model is unavailable, retain the failure and hold that lane. Do not choose an unreviewed substitute to obtain a passing label.

## Local n8n stack contract

The reviewed [official installer source](https://raw.githubusercontent.com/n8n-io/n8n/master/docker/get-n8n.sh) identifies itself as **1.4.0**. The platform guides select n8n **2.41.5** with `--version 2.41.5 --no-start` and `N8N_DIR="$HOME/n8n-course"`. The live installer URL and Compose source can change; installer version is distinct from the running n8n version. Use the guide’s download-and-review alternative to inspect a completed script before execution. Preserve any existing destination, including partial attempts; an “existing install” response is not version or readiness evidence. A different running version remains HOLD pending owner resolution, without automatic upgrade or repinning.

The [official Compose stack](https://raw.githubusercontent.com/n8n-io/n8n/master/docker/get-n8n-compose.yml) contains six services: `n8n`, `runners`, `sandbox-certs`, `sandbox-api`, `sandbox-runner-1`, and `searxng`. Expect five long-running services and successful `sandbox-certs` completion (`Exited (0)`). The runner uses privileged Docker-in-Docker and needs device-owner approval even with Assistant off. Docker Desktop license eligibility also needs owner approval wherever Desktop is used. On Linux, approved ordinary-account daemon access is required; do not run the installer as root or make the socket world-writable.

For a fresh configuration, change only the n8n port mapping from `5678:5678` to `127.0.0.1:5678:5678` before startup. Keep the remaining services and named volumes. Do not display `.env` or resolved Compose secrets. Ordinary course `down` / `up -d` preserves named data; `down -v` does not belong in the course path.

The platform guide records an unused owner-approved project name once, in `.course-project`, for a fresh installation. Its `course_n8n` helper selects that project, `.env`, and `compose.yml` explicitly and refuses exported configuration overrides. Reuse the record on the same approved engine for every restart; a file path alone does not identify a Compose project. Existing installations retain their actual project identity and owner-managed lifecycle.

Runtime, UI, and persistence have been exercised on Apple Silicon only. Published amd64/arm64 images do not establish platform execution. Windows, Intel macOS, Ubuntu, and Arch still require checks on the actual device.
