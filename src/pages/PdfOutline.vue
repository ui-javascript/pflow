<template>

  <p>
    <Button @click="openPdfFile" style="margin-left: 5px;">方式1: 生成pdf大纲-内置脚本(直接选择PDF)</Button>
  </p>

  <p style="margin-top: 10px;">
    <Button @click="execPyFile" style="margin-left: 5px;">方式2: 生成pdf大纲-自定义(自行安装依赖+先选择Python脚本+再选择PDF)</Button>
  </p>

  <!--      <Button @click="openFolder" style="margin-left: 5px;">打开文件夹</Button>-->

  <p v-show="pdfPath">
    pdf路径: <Link target="_blank" :href="pdfPath">{{ pdfPath }}</Link>
  </p>

  <p v-show="outlinePath">
    大纲路径: <Link target="_blank" :href="outlinePath">{{ outlinePath }}</Link>
  </p>

  <p v-show="pyFilePath">
    python脚本路径: <Link target="_blank" :href="pyFilePath">{{ pyFilePath }}</Link>
  </p>

</template>

<script setup>
import {ref} from "vue";

const pyFilePath = ref(null)
const pdfPath = ref(null)
const outlinePath = ref(null)

import {Message} from "@arco-design/web-vue";
const openPdfFile = async () => {
  const pdfFilePath = await window.pywebview.api.openPdfFile()
  if (!pdfFilePath) {
    return
  }

  pdfPath.value = pdfFilePath[0]

  const outlinesFilePath = await window.pywebview.api.genPdfOutlines(pdfFilePath[0])
  outlinePath.value = outlinesFilePath
  // Message.success({content: "已生成pdf大纲 " + outlinesPath})
  // window.open(outlinesPath)
};


const openFolder = async () => {
  const res = await window.pywebview.api.openFolder()
  if (!res) {
    return
  }
  Message.info("选择文件夹 " + res)
}

const execPyFile = async () => {
  const pyPath = await window.pywebview.api.openPyFile()
  if (!pyPath) {
    return
  }

  const pdfFilePath = await window.pywebview.api.openPdfFile()
  if (!pdfFilePath) {
    return
  }

  pyFilePath.value = pyPath[0]
  pdfPath.value = pdfFilePath[0]

  const res = await window.pywebview.api.execPyFileWithArgv1(pyPath[0], pdfFilePath[0])
  if (!res) {
    return
  }
  outlinePath.value = pdfPath.value + ".txt"
  // Message.success("Python文件执行成功")
};



</script>