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

- [Official Obsidian 1.13.7 release](https://github.com/obsidianmd/obsidian-releases/releases/tag/v1.13.7) and [release API metadata with asset digests](https://api.github.com/repos/obsidianmd/obsidian-releases/releases/tags/v1.13.7): the downloads for a fresh install and their exact SHA-256 values are in [Required tool identities](VERSIONS.md#local-obsidian-for-module-2). Keep any installed version and profile, then record the result of the same workflow.
- [Official installation instructions](https://github.com/obsidianmd/obsidian-help/blob/master/en/Getting%20started/Download%20and%20install%20Obsidian.md): universal macOS/Windows installers, AppImage execute permission, and launching with `--no-sandbox`. Get separate device-owner approval for that renderer-sandbox exception; it does not allow you to change system-wide security.
- [Local Markdown storage and external-change refresh](https://github.com/obsidianmd/obsidian-help/blob/master/en/Files%20and%20folders/How%20Obsidian%20stores%20data.md): open only the practice `vault` folder. Use local storage with Restricted community plugins and Sync off; no Obsidian account, community plugin, or MCP service needed.
- [Microsoft WSL GUI requirements](https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps): Windows 10 build 19044+ or Windows 11, WSL 2, and working GUI support. Run Linux Obsidian in the existing Ubuntu Linux home beside OMP; do not use a native Windows app on a WSL UNC vault.
- [AppImage FUSE guidance](https://docs.appimage.org/user-guide/troubleshooting/fuse.html) and [Ubuntu `libfuse2t64`](https://packages.ubuntu.com/noble/libfuse2t64): on Ubuntu ARM64, keep FUSE 3 and add only the approved compatibility library. The older `fuse` package is not a replacement.
- [Arch Extra Obsidian package](https://archlinux.org/packages/extra/x86_64/obsidian/) and [Arch full-upgrade requirement](https://wiki.archlinux.org/title/System_maintenance#Partial_upgrades_are_unsupported): use the signed distribution package in your existing approved `pacman -Syu` transaction. The package was 1.13.7-2 when checked; do not downgrade to match it.
- [Supplied readiness helper](../scripts/obsidian_readiness.py): `initialize`, `refresh`, and `check` take `--root` for a fresh attempt outside the checkout. A disk PASS from this helper still needs a separate check in the Obsidian window and does not show OMP or n8n ready.

The Obsidian window was checked only on **Obsidian 1.13.7, Darwin arm64**. It hasn't been checked on native Windows, WSLg, Intel macOS, Ubuntu, or Arch. Complete **Set up local Obsidian** in your [platform guide](../README.md#set-up-local-obsidian) and check links, edits, saves, refreshed files, and reopening on your own device before recording Obsidian READY. Official documentation and available binaries show how to set it up, but not whether it works on your machine.

## Local n8n and Docker

- [Official n8n one-line setup, flags, and Windows shell guidance](https://docs.n8n.io/deploy/host-n8n/install-options/one-line-setup)
- [Live installer download](https://get.n8n.io) and [reviewable installer source](https://raw.githubusercontent.com/n8n-io/n8n/master/docker/get-n8n.sh): the reviewed source reports installer 1.4.0, and requested n8n version is 2.41.5. The live URL can change, so it does not pin the installer to one version.
- [Official six-service Compose source](https://raw.githubusercontent.com/n8n-io/n8n/master/docker/get-n8n-compose.yml): includes the privileged Docker-in-Docker runner and named data volumes.
- [Docker Desktop for macOS](https://docs.docker.com/desktop/setup/install/mac-install/)
- [Docker Desktop for Windows](https://docs.docker.com/desktop/setup/install/windows-install/)
- [Docker Desktop WSL integration](https://docs.docker.com/desktop/features/wsl/)
- [Docker Desktop licensing](https://docs.docker.com/subscription-billing/desktop-license/)
- [Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
- [Docker Linux post-install access and docker-group privileges](https://docs.docker.com/engine/install/linux-postinstall/)
- [Docker Compose installation](https://docs.docker.com/compose/install/)
- [Compose down and volume removal options](https://docs.docker.com/reference/cli/docker/compose/down/)
- [Compose project-name precedence](https://docs.docker.com/compose/how-tos/project-name/) and [environment-variable interpolation precedence](https://docs.docker.com/compose/how-tos/environment-variables/variable-interpolation/): the saved project name and named configuration files keep Compose from using its defaults; you still need to block exported overrides.
- [Arch Docker guidance](https://wiki.archlinux.org/title/Docker), [Docker package](https://archlinux.org/packages/extra/x86_64/docker/), and [Compose package](https://archlinux.org/packages/extra/x86_64/docker-compose/)

Use the full official stack, keep the n8n host port at `127.0.0.1:5678`, and leave Assistant off. Your platform guide gives guarded installation steps or a way to download and review the installer. Don't follow upstream examples for upgrades, uninstalling, turning on Assistant, or convenience installs. A modern Compose plugin may report version 5; the required command is `docker compose`, not a literal `2.x` version number.

The n8n app and stack were checked only on Apple Silicon. On a fresh instance, the local owner used **Next**, the optional survey **Get started**, the free-license **Skip**, the Assistant **Set up later in Settings**, and **Overview → Build a workflow**. Clicking the title, renaming it, pressing **Enter**, and reloading showed the editor saved automatically without a **Saved** label. The stack had five long-running services, `sandbox-certs` at `Exited (0)`, publication to localhost only, and a workflow that stayed saved through the usual `down` / `up -d`. The Apple Silicon result does not show how another platform will run.

## Source hierarchy

Start with documentation for the pinned product release, then check operating-system documentation and the official package source. A community post may explain a symptom, but check the official source for required command. A post cannot grant permission to bypass device policy.
