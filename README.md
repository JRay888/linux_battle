# 🚀 Linux Battle Royale - Deployment Guide

Welcome to **Linux Battle Royale**! This guide will help you deploy and run the game on your servers using **Ansible**. 

---

## **1️⃣ Setup Inventory**
Edit the `inventory.ini` file and add your target servers:

```ini
[linux_servers]
server1 ansible_host=192.168.1.100 ansible_user=root
server2 ansible_host=192.168.1.101 ansible_user=root
```

Replace `192.168.1.100` with the actual IP addresses of your servers.

---

## **2️⃣ Run the Ansible Deployment Playbook**
Execute the following command to deploy the project:

```sh
ansible-playbook -i inventory.ini deploy.yml
```

This will:
✅ Install dependencies  
✅ Deploy the **survival script**, **leaderboard script**, and **web app**  
✅ Start the **Flask web server**  

---

## **3️⃣ Access the Web Leaderboard**
Once deployed, open a browser and go to:

```
http://<server-ip>:5000
```

- Replace `<server-ip>` with the IP of any deployed server.
- The leaderboard will update dynamically as servers **"battle"**.

---

## **4️⃣ Monitor Game Logs**
Check the survival logs on any server:

```sh
cat /var/log/linux_battle.log
```

Check the leaderboard JSON data:

```sh
cat /var/log/leaderboard.json
```

---

## **5️⃣ Manually Run the Survival Script**
If you want to trigger a manual game round:

```sh
bash /usr/local/bin/survival_game.sh
```

This updates the leaderboard **immediately**.

---

## **🎯 Want More?**
- 🎨 Customize the **leaderboard UI** (`web_app/templates/index.html`).
- 📊 Integrate **Grafana/Prometheus** for real-time metrics.
- 🔔 Send battle updates to **Slack/Discord**.

**Enjoy the Linux Battle Royale!** 🚀🔥
