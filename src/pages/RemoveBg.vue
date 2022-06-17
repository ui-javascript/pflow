<template>

  <Input v-model="apiKey" placeholder="请先输入API_KEY"/>

  <p style="margin-top: 10px;">
    <Button :disabled="!apiKey" @click="removeBg">选择图片, 抠除背景</Button>
  </p>

  <p>
    图片路径: <a target="_blank" :href="picPath">{{ picPath }}</a>
  </p>
  <p>
    处理后图片路径: <a target="_blank" :href="outPath">{{ outPath }}</a>
  </p>

  <Alert style="margin-top: 50px;">
    <template #title>
      API_KEY需要到 <a target="_blank" href="https://www.remove.bg/">www.remove.bg</a> 注册并免费生成
    </template>
    <p>
      <Image
          :preview-props="{
      actionsLayout: ['rotateRight', 'zoomIn', 'zoomOut'],
    }"
          width="100%"
          src="https://luo0412.oss-cn-hangzhou.aliyuncs.com/1655396504404-JBAJRxJp3rC8.png"/>
    </p>
    <TypographyTitle :heading="6">效果演示如下:</TypographyTitle>
    <p>
      <Image
          :preview-props="{
      actionsLayout: ['rotateRight', 'zoomIn', 'zoomOut'],
    }"
          width="300"
          src="https://luo0412.oss-cn-hangzhou.aliyuncs.com/1655396765593-F7yYQKeHWici.png"/>
    </p>
  </Alert>


  <!--  <Alert type="warning">-->
  <!--    <template #title>-->
  <!--      常见问题-->
  <!--    </template>-->

  <!--    <a target="_blank" href="https://docs.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170">ImportError: Microsoft Visual C++ Redistributable for Visual Studio 2019 not installed on the machine.</a>-->
  <!--  </Alert>-->

</template>

<script setup>
import {ref} from "vue"

const apiKey = ref(localStorage.getItem("rmBgApiKey"))
const picPath = ref(null)
const outPath = ref(null)

const removeBg = async () => {
  const picFilePath = await window.pywebview.api.openPicFile()
  if (!picFilePath) {
    return
  }

  picPath.value = picFilePath[0]

  const res = await window.pywebview.api.removeBg(picFilePath[0], apiKey.value)
  if (!res) {
    return
  }
  outPath.value = picFilePath + '_no_bg.png'

  localStorage.setItem("rmBgApiKey", apiKey.value)

}
</script>