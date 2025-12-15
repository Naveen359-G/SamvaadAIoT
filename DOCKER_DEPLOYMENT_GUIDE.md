# SamvaadAIoT - Docker Deployment Guide

**Quick deployment method to test your SamvaadAIoT branding immediately!**

---

## 🐳 Option 1: Use Official ThingsBoard Docker Image

Since all your branding files are ready, you can:

### Step 1: Pull Official Image
```bash
docker pull thingsboard/tb-postgres
```

### Step 2: Run Container
```bash
docker run -it -p 9090:9090 -p 1883:1883 -p 7070:7070 -p 5683-5688:5683-5688/udp \
  -v ~/.mytb-data:/data \
  -v ~/.mytb-logs:/var/log/thingsboard \
  --name samvaadaiot \
  thingsboard/tb-postgres
```

### Step 3: Access Application
- URL: http://localhost:9090
- Default login: `tenant@thingsboard.org` / `tenant`

### Step 4: Customize UI (After Container Starts)
```bash
# Copy your branded assets into the container
docker cp ui-ngx/src/samvaad.ico samvaadaiot:/usr/share/thingsboard/public/
docker cp ui-ngx/src/assets/logo/samvaad-logo.png samvaadaiot:/usr/share/thingsboard/public/assets/
```

---

## 🏗️ Option 2: Build Custom Docker Image

### Step 1: Create Dockerfile
```dockerfile
FROM thingsboard/tb-postgres:latest

# Copy SamvaadAIoT branding
COPY ui-ngx/src/samvaad.ico /usr/share/thingsboard/public/
COPY ui-ngx/src/assets/logo/ /usr/share/thingsboard/public/assets/logo/

# Update configuration
ENV TB_APP_NAME="SamvaadAIoT"

EXPOSE 9090 1883 7070 5683-5688/udp
```

### Step 2: Build Image
```bash
docker build -t samvaadaiot:1.0.0 .
```

### Step 3: Run
```bash
docker run -it -p 9090:9090 -p 1883:1883 \
  --name samvaadaiot \
  samvaadaiot:1.0.0
```

---

## 🚀 Option 3: Docker Compose (Microservices)

ThingsBoard provides Docker Compose files:

```bash
cd docker
./docker-install-tb.sh --loadDemo
./docker-start-services.sh
```

Then customize the running containers with your branding.

---

## ✅ Verify Deployment

1. Open browser: `http://localhost:9090`
2. Check:
   - [ ] Title shows in browser tab
   - [ ] Favicon appears
   - [ ] Login page loads
   - [ ] Can sign in with default credentials

---

## 📝 Notes

- Docker deployment uses pre-compiled ThingsBoard
- Bypasses local build issues
- Production-ready
- Can be deployed to cloud (AWS, GCP, Azure, DigitalOcean)

---

**Next**: Once running, you can further customize the UI by replacing files in the container.
