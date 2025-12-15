#!/bin/bash
echo "🚀 Preparing to push SamvaadAIoT to GitHub..."

# 1. Ask for new Repo URL
echo ""
echo "Please create a NEW Empty Repository on GitHub."
echo "Paste the URL here (e.g., https://github.com/yourname/samvaadaiot.git):"
read -r NEW_REPO_URL

if [ -z "$NEW_REPO_URL" ]; then
    echo "❌ Error: No URL provided."
    exit 1
fi

# 2. Reset Remote
echo "🔄 Updating Remote Origin..."
git remote remove origin
git remote add origin "$NEW_REPO_URL"

# 3. Add Files
echo "📦 Staging files..."
# Unignore the log fix directory to ensure it persists? No, logs shouldn't be committed.
# But we need the directory structure?
# We can just ignore logs.
git add .

# 4. Commit
echo "💾 Committing changes..."
git commit -m "Initial SamvaadAIoT Release: Rebranding and Docker Fixes"

# 5. Push
echo "⬆️ Pushing to GitHub..."
git push -u origin master

echo ""
echo "✅ Done! check your repository."
