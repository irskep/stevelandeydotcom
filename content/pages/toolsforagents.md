Title: Tools for Agents
Slug: toolsforagents

# Tools for Agents

I’ve created a few development tools streamline AI-assisted coding workflows.

## autowt

[GitHub](https://github.com/irskep/autowt) • [Documentation](https://steveasleep.com/autowt/) • [PyPI](https://pypi.org/project/autowt/)

Git worktree manager that eliminates context-switching friction between branches. I use autowt daily to run multiple AI agents on different tasks simultaneously without them interfering with each other's work.

autowt automates worktree creation, management, and cleanup, enabling true parallel development environments. Instead of manually juggling branches and stashing changes, you get instant isolated workspaces for each task.

## cimonitor

[GitHub](https://github.com/irskep/cimonitor) • [PyPI](https://pypi.org/project/cimonitor/)

Command-line tool for instant access to GitHub CI status, logs, and failure details. I use cimonitor daily to debug CI failures directly from the terminal without manual copy-pasting.

cimonitor provides filtered error logs, real-time CI monitoring, and detailed failure diagnostics. Compatible with all AI coding assistants, it eliminates the friction of switching between terminal and browser during development.

## persistproc

[GitHub](https://github.com/irskep/persistproc) • [Documentation](https://steveasleep.com/persistproc/) • [PyPI](https://pypi.org/project/persistproc/)

Process management MCP server that provides a shared process layer for multi-agent development workflows. Allows AI agents and humans to see and control long-running processes like web servers without configuration files.

persistproc exposes process control, listing, and output retrieval through a localhost MCP server. Designed to reduce copy-pasting between development environments and AI agents.