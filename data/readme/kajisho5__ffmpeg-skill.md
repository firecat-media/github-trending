Give your coding agent a video editor.  
Claude Code, Cursor, Codex or any MCP client edits your footage with local FFmpeg, then checks its own output. 
No cloud · No API keys · Python standard library 

    Website   ·
    Quick start   ·
   Demos  ·
   Tools  ·
   MCP  ·
   npm 

```bash
npx ffmpeg-skill
```

         caption.py --animate pop --karaoke   
         fit.py --aspect 9:16 --fit crop   

         silence.py --threshold -35   
         loudness.py -I -14 --tp -1   

Left half is the input, right half is what the command produced. **[Every before/after demo, with the exact command under each one →](docs/demos.md)** — all of it built by `python3 demos/build.py`, so you can rebuild every frame of it yourself. The footage is synthetic (FFmpeg's own test sources) except in three demos, `reframe_talk`, `filler_en` and `pauses_en`, which use two AI-generated clips of people who do not exist ([demos/footage/](demos/footage/README.md)).

`ffmpeg-skill` is an [Agent Skill](https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills) for Claude Code, Cursor, Codex and any agent that reads `SKILL.md`. It teaches the agent a fixed workflow (probe → edit losslessly where possible → check → verify) and ships **42 tools** that do the actual work with `ffmpeg` / `ffprobe`: cut, join, silence removal, fit to duration and aspect, captions and karaoke, overlays and motion graphics, HDR → SDR and LUTs, audio clean-up and typed dynamics, sync with drift correction, multicam, loudness, delivery checks, whole-edit project rendering, batch folders. Every tool is also callable as an MCP tool (`tools/list` advertises a core 12 by default to keep client context small, with `FFMPEG_SKILL_MCP_FULL=1` listing all 42; every tool is reachable by name through `tools/call` either way), and the whole set is described by a machine-readable contract.

If `ffmpeg` and `python3` are on your PATH, it works: offline, on footage you would rather not upload.

> **SPEC** (Self-Producing Execution Contract): each tool's `input_schema` — the part of its
> contract and MCP tool definition that has to track the CLI flag-for-flag — is never
> hand-authored beside the code. It is derived, at run time, from the same `argparse` parser that
> already defines the CLI, and CI fails the build if any of it drifts.
> → [full explanation](#what-is-spec)

---

## Standalone, and in an ecosystem

**Standalone**, this is a local FFmpeg engine: probe → edit → verify, `npx ffmpeg-skill` and nothing else. No API key, no account, no other repo required. Everything above and below this section describes that standalone tool, and none of it changes if you never read the rest of this one.

**In [kajisho5](https://github.com/kajisho5)'s wider video-production ecosystem**, this repo is the *hands*: it cuts, measures and exports files, and reports back in structured JSON. It does not decide what to cut, whether a deliverable is approvable, what makes a highlight interesting, or what a caption should 
