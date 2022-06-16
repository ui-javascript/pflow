<template>
  <div style="margin-top: 10px;">
    <Button @click="openPdfFile" style="margin-left: 5px;">生成pdf目录大纲</Button>
    <Button @click="execPyFile" style="margin-left: 5px;">生成pdf目录大纲(安装依赖+选择Python脚本+选择PDF)</Button>

    <!--      <Button @click="openFolder" style="margin-left: 5px;">打开文件夹</Button>-->
  </div>


  <p v-show="pdfPath">
    pdf路径: <Link :href="pdfPath" icon>{{ pdfPath }}</Link>
  </p>

  <p v-show="outlinePath">
    大纲路径: <Link :href="outlinePath" icon>{{ outlinePath }}</Link>
  </p>

  <p v-show="pyFilePath">
    python脚本路径: <Link :href="pyFilePath" icon>{{ pyFilePath }}</Link>
  </p>

</template>

<script setup>
import {ref} from "vue";

const pyFilePath = ref(null)
const pdfPath = ref(null)
const outlinePath = ref(null)

import {Message} from "@arco-design/web-vue";
const openPdfFile = async () => {
  const pdfPath = await window.pywebview.api.openPdfFile()
  if (!pdfPath) {
    return
  }

  pdfPath.value = pdfPath[0]
  const outlinesFilePath = await window.pywebview.api.genPdfOutlines(pdfPath[0])
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
  console.log(pyFilePath[0], )

  const res = await window.pywebview.api.execPyFileWithArgv1(pyPath[0], pdfFilePath[0])
  if (!res) {
    return
  }
  Message.success("Python文件执行成功")
};



</script>