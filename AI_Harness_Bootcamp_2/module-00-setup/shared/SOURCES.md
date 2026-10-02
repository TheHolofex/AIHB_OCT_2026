# Primary setup sources


## Windows and WSL

- [WinGet overview](https://learn.microsoft.com/en-us/windows/package-manager/winget/)
- [Install WSL](https://learn.microsoft.com/en-us/windows/wsl/install)
- [Set up a WSL development environment](https://learn.microsoft.com/en-us/windows/wsl/setup/environment)
- [PowerShell environment variables](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables)
- [Windows PowerShell 5.1 execution policies and scopes](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-5.1)
- [Official GitHub CLI Windows installation](https://raw.githubusercontent.com/cli/cli/trunk/docs/install_windows.md)
- [Python on Windows](https://docs.python.org/3/using/windows.html)
- [Git for Windows](https://git-scm.com/downloads/win)

## macOS

- [Homebrew](https://brew.sh/)
- [Apple command-line tools through Homebrew prerequisites](https://docs.brew.sh/Installation)
- [Homebrew support tiers, including Intel](https://docs.brew.sh/Support-Tiers)
- [Apple Gatekeeper · Open a blocked app](https://support.apple.com/en-us/102445)

## Ubuntu and Arch

- [Ubuntu package management](https://documentation.ubuntu.com/server/how-to/software/package-management/)
- [Ubuntu 24.04 Python package](https://packages.ubuntu.com/noble/python3)
- [Ubuntu 26.04 Python package](https://packages.ubuntu.com/resolute/python3)
- [Ubuntu GitHub CLI package in Universe](https://packages.ubuntu.com/noble/gh)
- [Official Arch Linux platform definition](https://archlinux.org/about/)
- [Arch Linux pacman](https://wiki.archlinux.org/title/Pacman)
- [Arch Linux Python](https://wiki.archlinux.org/title/Python)
- [Arch GitHub CLI package](https://archlinux.org/packages/extra/x86_64/github-cli/)

## Shared tools

- [Git installation](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Clone a GitHub repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
- [GitHub CLI browser login and credential storage](https://cli.github.com/manual/gh_auth_login)
- [GitHub CLI authentication status](https://cli.github.com/manual/gh_auth_status)
- [GitHub CLI host-scoped Git credential helper](https://cli.github.com/manual/gh_auth_setup-git)
- [Oh My Pi v18.3.5 release and assets](https://github.com/can1357/oh-my-pi/releases/tag/v18.3.5)
- [OMP CLI at v18.3.5](https://github.com/can1357/oh-my-pi/blob/v18.3.5/docs/cli-reference.md)
- [OMP model resolution at v18.3.5](https://github.com/can1357/oh-my-pi/blob/v18.3.5/docs/models.md)
- [OMP approval policy at v18.3.5](https://github.com/can1357/oh-my-pi/blob/v18.3.5/docs/approval-mode.md)
- [OMP extension API at v18.3.5](https://github.com/can1357/oh-my-pi/blob/v18.3.5/docs/extensions.md)
- [Sonnet 4.6 through OpenRouter](https://openrouter.ai/anthropic/claude-sonnet-4.6)
- [OpenRouter authentication](https://openrouter.ai/docs/api-reference/authentication)
- [Python downloads](https://www.python.org/downloads/)

## Local Obsidian

- [Official Obsidian 1.13.7 release](https://github.com/obsidianmd/obsidian-releases/releases/tag/v1.13.7) and [release API metadata with asset digests](https://api.github.com/repos/obsidianmd/obsidian-releases/releases/tags/v1.13.7): the fresh reference assets and exact SHA-256 values are in [Required tool identities](VERSIONS.md#local-obsidian-for-module-2). Preserve an existing installed version and profile, then record its actual workflow result.
- [Official installation instructions](https://github.com/obsidianmd/obsidian-help/blob/master/en/Getting%20started/Download%20and%20install%20Obsidian.md): universal macOS/Windows installers and the AppImage execute permission and `--no-sandbox` launch. The course requires separate device-owner approval for that renderer-sandbox exception; this is not permission to change system-wide security.
- [Local Markdown storage and external-change refresh](https://github.com/obsidianmd/obsidian-help/blob/master/en/Files%20and%20folders/How%20Obsidian%20stores%20data.md): open the practice `vault` folder only. The course uses local storage, Restricted community plugins, and Sync off, without an Obsidian account, community plugin, or MCP service.
- [Microsoft WSL GUI requirements](https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps): Windows 10 build 19044+ or Windows 11, WSL 2, and working GUI support. The course uses Linux Obsidian in the existing Ubuntu Linux home, alongside OMP's files. A native Windows app on a WSL UNC vault is not the course route.
- [AppImage FUSE guidance](https://docs.appimage.org/user-guide/troubleshooting/fuse.html) and [Ubuntu `libfuse2t64`](https://packages.ubuntu.com/noble/libfuse2t64): the Ubuntu ARM64 route keeps FUSE 3 and adds only the approved compatibility library; obsolete `fuse` is not a replacement.
- [Arch Extra Obsidian package](https://archlinux.org/packages/extra/x86_64/obsidian/) and [Arch full-upgrade requirement](https://wiki.archlinux.org/title/System_maintenance#Partial_upgrades_are_unsupported): use the signed distribution package in the existing approved `pacman -Syu` transaction. Reference package 1.13.7-2 is an observation, not a downgrade instruction.
- [Supplied readiness helper](../scripts/obsidian_readiness.py): `initialize`, `refresh`, and `check` accept `--root` for a fresh external attempt. Its qualified disk PASS explicitly requires separate GUI observation; it cannot establish OMP or n8n readiness.

Actual reference GUI observation covers **Obsidian 1.13.7, Darwin arm64** only. Native Windows, WSLg, Intel macOS, Ubuntu, and Arch GUI lanes are unobserved in this record. Complete **Set up local Obsidian** in the learner's [platform guide](../README.md#set-up-local-obsidian), including link/edit/save/refresh/reopen observations on that device, before recording Obsidian READY. Official documentation and available binaries establish the intended route, not a successful local operation.

## Local n8n and Docker

- [Official n8n one-line setup, flags, and Windows shell guidance](https://docs.n8n.io/deploy/host-n8n/install-options/one-line-setup)
- [Live installer download](https://get.n8n.io) and [reviewable installer source](https://raw.githubusercontent.com/n8n-io/n8n/master/docker/get-n8n.sh): reviewed source reports installer 1.4.0; the course requests n8n 2.41.5 explicitly. The live URL is not an immutable installer pin.
- [Official six-service Compose source](https://raw.githubusercontent.com/n8n-io/n8n/master/docker/get-n8n-compose.yml): includes the privileged Docker-in-Docker runner and named data volumes.
- [Docker Desktop for macOS](https://docs.docker.com/desktop/setup/install/mac-install/)
- [Docker Desktop for Windows](https://docs.docker.com/desktop/setup/install/windows-install/)
- [Docker Desktop WSL integration](https://docs.docker.com/desktop/features/wsl/)
- [Docker Desktop licensing](https://docs.docker.com/subscription-billing/desktop-license/)
- [Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
- [Docker Linux post-install access and docker-group privileges](https://docs.docker.com/engine/install/linux-postinstall/)
- [Docker Compose installation](https://docs.docker.com/compose/install/)
- [Compose down and volume removal options](https://docs.docker.com/reference/cli/docker/compose/down/)
- [Compose project-name precedence](https://docs.docker.com/compose/how-tos/project-name/) and [environment-variable interpolation precedence](https://docs.docker.com/compose/how-tos/environment-variables/variable-interpolation/): the recorded project and explicit configuration files prevent accidental defaults; exported overrides still require a guard.
- [Arch Docker guidance](https://wiki.archlinux.org/title/Docker), [Docker package](https://archlinux.org/packages/extra/x86_64/docker/), and [Compose package](https://archlinux.org/packages/extra/x86_64/docker-compose/)

The course selects the full official stack, restricts the n8n host port to `127.0.0.1:5678`, and leaves Assistant off. The platform guides supply guarded installation and download-and-review alternatives. Upstream upgrade, uninstall, Assistant activation, or convenience-install examples are not course steps. A modern Compose plugin may report version 5; the required interface is `docker compose`, not a literal `2.x` version string.

The integration owner’s direct observations cover Apple Silicon only: local owner **Next**, optional survey **Get started**, free-license **Skip**, Assistant **Set up later in Settings**, and **Overview → Build a workflow** on an empty instance. Clicking the title, renaming, pressing **Enter**, and reloading proved automatic saving without requiring a **Saved** label. The observed stack had five long-running services, `sandbox-certs` at `Exited (0)`, localhost-only publication, and workflow persistence through ordinary `down` / `up -d`. These observations do not establish another platform’s execution.

## Source hierarchy

Use documentation for the pinned product release first, then operating-system documentation and the official package source. A community post can explain a symptom but does not establish the required command or grant permission to bypass device policy.
