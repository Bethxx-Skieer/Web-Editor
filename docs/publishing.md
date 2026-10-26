# 上传 GitHub 与后续维护

## 发布的内容是什么

公开仓库为 [Bethxx-Skieer/Web-Editor](https://github.com/Bethxx-Skieer/Web-Editor)，技能名为 `web-design-workflow`。仓库根目录中的 `README.md` 提供首页介绍，可安装的 skill 保持在 `skills/web-design-workflow/`。

以下首次上传说明适用于维护者建立新的分发仓库；使用本仓库时，直接下载或克隆后按 README 安装即可。维护当前仓库则从现有提交继续更新。

可用于 GitHub About 的简短介绍：

> 面向 AI 编程助手的网页设计工作流，统一视觉、内容、交互、媒体与本地交付，支持按需技能协作和关联一致性检查。

建议主题标签：`agent-skills`、`codex`、`web-design`、`frontend`、`design-workflow`。

无需启用 GitHub Pages。本仓库用于分享技能；实际网站由使用者在自己的项目中制作。

## 方式一：网页上传

1. 若要建立自己的分发仓库，在 GitHub 账户中创建公开仓库。准备上传本仓库已有 README 与 LICENSE 时，不必再生成同名模板。
2. 进入新仓库的文件上传入口，上传**解压后目录里的内容**，而不是只上传 ZIP。只上传压缩包不会让 README 成为首页，也不便于安装器读取技能路径。
3. 检查顶层能看到 README、LICENSE、docs、scripts、skills，再提交。
4. 打开 `skills/web-design-workflow/SKILL.md` 以及三份 references，确认结构完整。
5. 将实际仓库链接分享给使用者，并附上 README 的安装段落。

GitHub 的具体界面与上传限制可能变化，操作时以官方说明为准：[创建仓库](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)、[添加文件](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)。

## 方式二：Git 命令行

先在 GitHub 创建空仓库并完成本机 Git 身份与认证配置。进入**此分享仓库的根目录**，确认没有其他项目文件。下面命令用于首次发布：

```bash
git init
git add .
git diff --cached --stat
git status --short
git commit -m "Publish web-design-workflow"
git branch -M main
```

维护本项目时使用以下远端；若建立自己的分发仓库，先换成自己的实际地址，再执行：

```bash
git remote add origin https://github.com/Bethxx-Skieer/Web-Editor.git
git push -u origin main
```

如果目录已经有 Git 历史或 `origin`，先核对 `git status` 和 `git remote -v`，不要覆盖现有远端。若远端已有内容，采用已有项目的合并流程，不使用强制推送。上述命令只是发布指南，不代表打包时已经执行过上传。

## 分享与安装信息

分享时提供：实际 GitHub 仓库链接、简短用途说明、安装子路径 `skills/web-design-workflow` 和一个任务示例。

可给支持仓库安装的助手这段提示：

```text
请从 https://github.com/Bethxx-Skieer/Web-Editor 安装 web-design-workflow，
技能目录是 skills/web-design-workflow。
先检查是否已有同名技能；不要覆盖我的本地改动。
```

仓库 ZIP 用于完整源码分享。安装时取出技能子目录，不要把整个分享仓库错误地当成 skill 根目录。更新已有安装时，先比较并备份旧版本；完整替换经过确认的技能目录，避免残留已删除的参考文件。

## 发布前与更新后检查

- 运行 `python scripts/validate.py`，检查结构与内部链接。
- 对照 [验收场景](validation.md)，推演本次受影响的行为；必要时在临时网站中执行。
- 检查改动清单，确保没有账户凭据、个人素材、项目导出或第三方技能副本。
- 更新 `VERSION`，在提交或 Release 说明中写清行为变化、验证结果与兼容限制。
- 如果同时提供 ZIP，在所有修改结束后重新打包，并核对内容与最终源文件一致。

初始公开版为 `0.1.0`。这是本项目的版本号，与 Codex、Impeccable 或任何媒体工具的版本无关。

## 源码与分发包的关系

```text
分享仓库源文件
  ├─ Git 提交 → GitHub 仓库
  └─ 最终内容打包 → 分发 ZIP

使用者安装
  └─ skills/web-design-workflow → 自己客户端的技能目录
```

维护时先改仓库源文件，再更新 ZIP 和本地安装副本。不要只改压缩包中的文件。提交 GitHub 后，其他人已安装的本地副本不会因为你改了仓库就必然自动更新；更新方式取决于各自的安装工具。
