# Uptime Kuma

Uptime Kuma is an easy-to-use self-hosted monitoring tool.

[ ](https://github.com/sponsors/louislam)

## 🥔 Live Demo

Try it!

Demo Server (Location: Frankfurt - Germany):  

It is a temporary live demo, all data will be deleted after 10 minutes. Sponsored by [Uptime Kuma Sponsors](https://github.com/louislam/uptime-kuma#%EF%B8%8F-sponsors).

> [!WARNING]
> Be careful - the top result in Google, uptimekuma.co, is not our official website, we don't control the website. I recommend following the installation guide in this GitHub repo.

## ⭐ Features

- Monitoring uptime for HTTP(s) / TCP / HTTP(s) Keyword / HTTP(s) Json Query / Websocket / Ping / DNS Record / Push / Steam Game Server / Docker Containers
- Fancy, Reactive, Fast UI/UX
- Notifications via Telegram, Discord, Gotify, Slack, Pushover, Email (SMTP), and [90+ notification services, click here for the full list](https://github.com/louislam/uptime-kuma/tree/master/src/components/notifications)
- 20-second intervals
- [Multi Languages](https://github.com/louislam/uptime-kuma/tree/master/src/lang)
- Multiple status pages
- Map status pages to specific domains
- Ping chart
- Certificate info
- Proxy support
- 2FA support

## 🔧 How to Install

### 🐳 Docker Compose

```bash
mkdir uptime-kuma
cd uptime-kuma
curl -o compose.yaml https://raw.githubusercontent.com/louislam/uptime-kuma/master/compose.yaml
docker compose up -d
```

Uptime Kuma is now running on all network interfaces (e.g. http://localhost:3001 or http://your-ip:3001).

> [!WARNING]
> File Systems like **NFS** (Network File System) are **NOT** supported. Please map to a local directory or volume.

### 🐳 Docker Command

```bash
docker run -d --restart=always -p 3001:3001 -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma:2
```

Uptime Kuma is now running on all network interfaces (e.g. http://localhost:3001 or http://your-ip:3001).

If you want to limit exposure to localhost only:

```bash
docker run ... -p 127.0.0.1:3001:3001 ...
```

### 💪🏻 Non-Docker

Requirements:

- Platform
  - ✅ Major Linux distros such as Debian, Ubuntu, Fedora and ArchLinux etc.
  - ✅ Windows 10 (x64), Windows Server 2012 R2 (x64) or higher
  - ❌ FreeBSD / OpenBSD / NetBSD
  - ❌ Replit / Heroku
- [Node.js](https://nodejs.org/en/download/) >= 20.4
- [Git](https://git-scm.com/downloads)
- [pm2](https://pm2.keymetrics.io/) - For running Uptime Kuma in the background

```bash
git clone https://github.com/louislam/uptime-kuma.git
cd uptime-kuma
npm run setup

# Option 1. Try it
node server/server.js

# (Recommended) Option 2. Run in the background using PM2
# Install PM2 if you don't have it:
npm install pm2 -g && pm2 install pm2-logrotate

# Start Server
pm2 start server/server.js --name uptime-kuma
```

Uptime Kuma is now running on all network interfaces (e.g. http://localhost:3001 or http://your-ip:3001).

More useful PM2 Commands

```bash
# If you want to see the current console output
pm2 monit

# If you want to add it to startup

