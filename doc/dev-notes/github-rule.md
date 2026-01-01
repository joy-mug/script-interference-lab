# Git 指令速查筆記（stash / working tree / 任務切換）

> 本筆記整理自實務討論，聚焦在「暫停任務 → 處理緊急事項 → 回來繼續工作」的正確 Git 用法。

---

## 一、核心概念（一定要先記）

- **Working Tree**：你電腦上正在編輯、存檔的檔案（現場）
- **Staging Area**：準備要 commit 的內容
- **Repository**：已寫入 Git 歷史、可回朔的節點

> stash ≠ 回朔  
> commit 才是回朔點

---

## 二、狀態檢查

### `git status`
**用途**
- 查看目前 working tree / staging 狀態
- 判斷是否有未 commit 的修改
- stash / pop 前後一定要看

---

## 三、暫停目前工作（中斷任務）

### `git stash`
**用途**
- 暫存「尚未 commit 的修改（working tree + staging）」
- working tree 會回到最後一次 commit 的狀態

**心智模型**
> 暫停工作，不是建立歷史

---

### `git stash list`
**用途**
- 查看目前有哪些 stash
- 確認 stash 是否仍存在（很重要）

---

## 四、回來繼續原本工作

### `git stash pop`
**用途**
- 套用「最新一筆 stash」的修改回 working tree
- **成功才會刪除 stash**

**注意**
- 是「套用修改」，不是時間回朔
- 若同一檔案在其他 commit 有修改，可能產生 conflict

---

### `git stash apply`
**用途**
- 套用 stash，但不刪除
- 適合：
  - 不確定是否會衝突
  - 想保留保險

---

### `git stash drop`
**用途**
- 手動刪除某一筆 stash
- 常用於 `apply` 後確認沒問題

---

## 五、留下「緊急任務中有用的東西」

### `git add <file>`
**用途**
- 將 working tree 的修改放入 staging
- 表示「我打算留下這個版本」

---

### `git commit -m "message"`
**用途**
- 將 staging 內容寫成正式歷史節點
- **只有 commit 是安全、可回朔的**

**重要規則**
> 想留下來的東西，一定要 commit  
> stash 不會幫你保證

---

## 六、stash pop 發生衝突時

### `git add <file>`
**用途**
- 解完 conflict 後標記為已處理
- 讓 Git 知道你已做出選擇

---

## 七、放棄目前 working tree 修改（非歷史回朔）

### `git restore .`
（舊版等同：`git checkout -- .`）

**用途**
- 放棄目前 working tree 的修改
- 回到「最後一次 commit」的狀態

**注意**
- 只影響 working tree
- 不動 Git 歷史

---

## 八、切換任務（正確方式）

### `git switch <branch>`
（舊版：`git checkout <branch>`）

**用途**
- 切換工作線
- 搭配 stash 處理緊急任務的正確方式

---

## 九、不該混用的指令（目前階段）

### ⚠️ `git reset`
**重點一句話**
> `git reset` 是處理 commit / staging 歷史的，不是用來暫停或切換任務。

在 stash 流程中：
- ❌ 不需要
- ❌ 不建議使用

---

## 十、標準安全流程（推薦直接照用）

```bash
git stash
git switch hotfix
# 修緊急任務
git add .
git commit -m "hotfix + useful changes"
git switch main
git stash pop


# Git Branch 一頁速查（含 stash 對照）

> 本頁目的：  
> **在不中斷思考的情況下，安全地開 branch、切 branch、繼續開發，不傷 main**

---

## 一句話心智模型（最重要）

- **stash**：暫時放抽屜（未 commit 的修改）
- **branch**：開一條正式工作線（commit 的歷史）

👉 **功能開發一定用 branch，不用 stash**

---

## Git 基本層級（一定要知道）
開 branch 的各種指令
git switch -c feature/drawing-edit
意思
建立新 branch
立刻切換
從「目前所在 branch」分出去

git checkout -b feature/drawing-edit
意思
功能與 switch -c 一樣
但 checkout 功能混雜、容易誤用

切 branch 前的安全檢查（一定要做）
git status

```
# Scenario
#  You are on the target branch (where you want the files to appear)
#  You want to copy a folder from another branch
#  Step 1 — Switch to the target branch

git switch feature/drawing-edit

# Step 2 — Copy a folder from another branch

git restore --source main docs/dev-notes

# Step 3 — Commit it
git add docs/dev-notes
git commit -m "Copy dev-notes from main branch"

# Reset an Existing Local Repo
# Fetch the latest changes from GitHub
git fetch origin

# Reset your local branch to match the remote branch (e.g., main)
git reset --hard origin/main

# Remove any untracked files/folders
git clean -fd
