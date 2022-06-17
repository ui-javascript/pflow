<template>

  <Alert>
    <template #title>
      API_KEY需要到 <Link target="_blank" href="https://www.remove.bg/">www.remove.bg</Link> 注册并免费生成
    </template>

    <Image
        :preview-props="{
    actionsLayout: ['rotateRight', 'zoomIn', 'zoomOut'],
  }"
        width="100%"
        src="https://luo0412.oss-cn-hangzhou.aliyuncs.com/1655396504404-JBAJRxJp3rC8.png"/>

<!--    <TypographyTitle :heading="6">效果演示如下:</TypographyTitle>
    <p>
      <Image
          :preview-props="{
      actionsLayout: ['rotateRight', 'zoomIn', 'zoomOut'],
    }"
          width="300"
          src="https://luo0412.oss-cn-hangzhou.aliyuncs.com/1655396765593-F7yYQKeHWici.png"/>
    </p>-->
  </Alert>

  <Input style="margin-top: 10px;" v-model="apiKey" placeholder="请先输入API_KEY"/>

  <p style="margin-top: 10px;">
    <Button :disabled="!apiKey" @click="removeBg">选择图片, 抠除背景</Button>
  </p>

  <p>
    图片路径: <Link target="_blank" :href="picPath">{{ picPath }}</Link>
  </p>
  <p>
    处理后的图片路径: <Link target="_blank" :href="outPath">{{ outPath }}</Link>
  </p>



  <!--  <Alert type="warning">-->
  <!--    <template #title>-->
  <!--      常见问题-->
  <!--    </template>-->

  <!--    <Link target="_blank" href="https://docs.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170">ImportError: Microsoft Visual C++ Redistributable for Visual Studio 2019 not installed on the machine.</Link>-->
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