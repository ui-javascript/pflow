# README

![](https://luo0412.oss-cn-hangzhou.aliyuncs.com/1655383884455-cEBK4fyndyKZ.png)

---

# 启动 @run

```bash
npm run init

npm run dev # 启动前端

npm run start # 启动客户端
npm run start:cef # 或者兼容模式启动客户端
```

# 打包 @build

```bash
npm run build
npm run build:cef # 或者兼容模式
```

---

# 常见问题 @faq

- ReferenceError: queueMicrotask is not defined @tofix
  - https://apidocs.cn/blog/front/nodejs/queueMicrotaskIsNotDefined.html

```
cef兼容模式下 monaco-editor报错
```

![](https://luo0412.oss-cn-hangzhou.aliyuncs.com/1655412225995-MZ4iFANKsaNb.png)

- pip安装paramiko失败 -- Could not build wheels for pycuda which use PEP 517 and cannot be installed directly
  - https://visualstudio.microsoft.com/downloads/
  - https://blog.csdn.net/weixin_43400774/article/details/124042243

```
主要原因是pip(pyenv)版本问题 可以升级版本或指定路径单独安装

python -m pip install -U --force-reinstall pip

pip install paramiko --target=./pyenv/pyenv/Lib/site-packages
# pip install paramiko --target=./pyenv/pyenvCEF/Lib/site-packages

===
cryptography
需要安装rust
Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools"
```

---

# 参考 @ref

- https://github.com/pangao1990/vue-pywebview-pyinstaller