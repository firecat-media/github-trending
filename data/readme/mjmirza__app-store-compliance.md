&nbsp;&nbsp;&nbsp; 

# App Store Compliance Playbook

Stop getting your iOS and Android apps rejected. The enterprise reference and automated guard that turns App Store and Google Play rejection into a designed out failure mode.

Read it as a website at [mjmirza.github.io/app-store-compliance](https://mjmirza.github.io/app-store-compliance/).

[ ](https://developer.apple.com/app-store/review/guidelines/)
[ ](https://play.google/developer-content-policy/)
[ ](#how-you-actually-use-this)
[ ](https://openroots.org/licenses/ora/2.3)
[ ](https://github.com/mjmirza/app-store-compliance/actions)
[ ](.github/CONTRIBUTING.md)

[ ](https://github.com/mjmirza/app-store-compliance/stargazers)
[ ](https://github.com/mjmirza/app-store-compliance/fork)
[ ](https://github.com/mjmirza)

**If this saves you even one rejection, leave a star, fork it, and follow along. That is the whole ask.**

[Star this repo](https://github.com/mjmirza/app-store-compliance) &nbsp;|&nbsp; [Fork it](https://github.com/mjmirza/app-store-compliance/fork) &nbsp;|&nbsp; [Follow on GitHub](https://github.com/mjmirza) &nbsp;|&nbsp; [Follow on X](https://twitter.com/MirzaJhanzaib) &nbsp;|&nbsp; [next8n.com](https://next8n.com)

## Start here

Pick one row. The time shown is for that first step.

| You are | Do this first | Time |
|---|---|---|
| About to submit, and you can open a terminal | Run the two commands below | 2 minutes |
| Already rejected | Open [the appeal playbook](docs/MISTAKE-PATTERNS.md#the-appeal-playbook) | 10 minutes |
| Not a developer | Open [the checklist](docs/PRE-SUBMISSION-CHECKLIST.md) and do its first two checks | 5 minutes |
| Using an AI coding tool (Claude Code, Codex, Gemini CLI, GitHub Copilot, Cursor, Grok, Qwen, Kimi and more), and want this on every submit | Go to [the install](#install-it-into-your-ai-coding-tool) | 1 minute |

The two commands. Needs git and bash. The first downloads this playbook. The second scans your app. Nothing is installed and nothing in your app is changed.

```
git clone https://github.com/mjmirza/app-store-compliance ~/repositories/app-store-compliance
bash ~/repositories/app-store-compliance/agent-os/hooks/app-store-compliance-guard.sh "/path/to/your/app"
```

Replace only `/path/to/your/app`, with the folder that holds your Xcode project or your Android app. Keep the quotes, they keep a folder name with a space in it whole. To get the path without typing it, drag the folder from Finder or your file manager into the terminal window. A small project scans in about a second, a large one can take up to a minute, and the guard prints the time it took. Findings print first, critical ones on top, each with the file and line that triggered it when there is one. The last lines tell you where you stand.

| Last line starts with | It means | Do next |
|---|---|---|
| `BLOCKED.` | A critical rejection risk was found | Fix each `[CRITICAL]` line using the `fix.` line under it, then run the same command again |
| `CLEAR.` | No critical ri
