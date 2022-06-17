<template>

  <Card title="前端项目SSH部署">
    <Row :gutter="10">
      <Col flex="auto">
        <Input placeholder="请输入工程目录(package.json)" v-model.trim="projectPath" allow-clear />
      </Col>
      <Col flex="100px">
        <Button type="outline" @click="openFolder">选择文件夹</Button>
      </Col>
    </Row>

    <p>
      <Input placeholder="请输入打包命令" v-model.trim="buildCmd"/>
    </p>

    <p>
      <Input placeholder="请输入打包目录" v-model.trim="distPath"/>
    </p>

    <p>
      <Input placeholder="请输入远程目录" v-model.trim="remotePath"/>
    </p>
    <p>
      <Input placeholder="请输入远程服务器IP" v-model.trim="hostname"/>
    </p>
    <p>
      <Input placeholder="请输入远程服务器用户名" v-model.trim="username"/>
    </p>

    <p>
      <Input placeholder="请输入远程服务器密码" v-model.trim="password"/>
    </p>

    <Button :disabled="!projectPath || !remotePath || !hostname || !username || !password || !buildCmd || !distPath" @click="deploy">部署</Button>

  </Card>


</template>

<script setup>
import {ref} from "vue"
import {Message} from "@arco-design/web-vue";

const projectPath = ref(localStorage.getItem("projectPath") || "E:\\workspace-electron\\qflow")
const buildCmd = ref(localStorage.getItem("buildCmd") || "vite build")
const distPath = ref(localStorage.getItem("distPath") || "dist")
const remotePath = ref(localStorage.getItem("remotePath") || "/opt/temp")
const hostname = ref(localStorage.getItem("hostname") || "x.x.x.x")
const username = ref(localStorage.getItem("username") || "root")
const password = ref(localStorage.getItem("password") || "password")

const deploy = async () => {
  const res = await window.pywebview.api.deployFe(projectPath.value, remotePath.value, hostname.value, username.value, password.value, buildCmd.value, distPath.value)
  if (!res) {
    return
  }

  localStorage.setItem("projectPath", projectPath.value)
  localStorage.setItem("buildCmd", buildCmd.value)
  localStorage.setItem("distPath", distPath.value)
  localStorage.setItem("remotePath", remotePath.value)
  localStorage.setItem("hostname", hostname.value)
  localStorage.setItem("username", username.value)
  localStorage.setItem("password", password.value)
  Message.success("前端项目部署成功")
}

const openFolder = async () => {
  const res = await window.pywebview.api.openFolder()
  if (!res) {
    return
  }
  // console.log(res)
  projectPath.value = res[0]
}

</script>