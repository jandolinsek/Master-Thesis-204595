ssh-keygen -t ed25519 -C "you@example.com"


eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

cat ~/.ssh/id_ed25519.pub
ssh -T git@github.com


git config --global user.name "Your Name"
git config --global user.email "you@example.com"

git remote -v


cd /home/dolinsek/00_scripts
git init
git branch -M main
git add .
git commit -m "Initial commit"
git remote add origin git@github.com:YOUR_USER/YOUR_PRIVATE_REPO.git
git push -u origin main

git add .
git commit -m "Describe the change"
git push


git pull --rebase origin main
git push origin main

