<template>
  <Layout class="layout-demo">

    <LayoutSider collapsible>
      <div class="logo"></div>
      <Menu
        :style="{ width: '100%' }"
        @menu-item-click="onClickMenuItem"
      >
        <MenuItem key="SysInfo">
          <IconHome></IconHome>
          [0-5]系统信息
        </MenuItem>
        <MenuItem key="Crypt">
          <IconHome></IconHome>
          [0-9]加解密
        </MenuItem>
        <MenuItem key="Zip">
          <IconCalendar></IconCalendar>
          [1-7]解压缩
        </MenuItem>
        <SubMenu key="Editor">
          <template #title>
            <IconCalendar></IconCalendar> [1-7]编辑器
          </template>
          <MenuItem key="MdEditor">Markdown编辑器</MenuItem>
          <MenuItem key="CodeEditor">Python代码编辑器</MenuItem>
        </SubMenu>
        <SubMenu key="Office">
          <template #title>
            <IconCalendar></IconCalendar> [1-7]办公文档
          </template>
          <SubMenu key="OfficePdf" title="PDF">
            <MenuItem key="PdfOutline">生成PDF目录大纲</MenuItem>
          </SubMenu>
          <SubMenu key="Markdown" title="Markdown">
            <MenuItem key="MdSlidev">slidev</MenuItem>
            <MenuItem key="MdCoolma">coolma</MenuItem>
          </SubMenu>
        </SubMenu>
        <SubMenu key="Convert">
          <template #title>
            <IconCalendar></IconCalendar> [1-7]格式转换
          </template>
          <SubMenu key="TXT" title="TXT">
            <MenuItem key="Txt2Word">TXT转Word</MenuItem>
          </SubMenu>
          <SubMenu key="PDF" title="PDF">
            <MenuItem key="Pdf2Pic">PDF转图片</MenuItem>
            <MenuItem key="Pdf2Word">PDF转Word</MenuItem>
          </SubMenu>
        </SubMenu>
        <MenuItem key="Deploy">
          <IconCalendar></IconCalendar>
          [3-5]项目部署
        </MenuItem>
        <SubMenu key="Cloud">
          <template #title>
            <IconCalendar></IconCalendar> [3-6]云服务
          </template>
          <MenuItem key="OssUpload">OSS图床</MenuItem>
        </SubMenu>
        <MenuItem key="MathExpr">
          <IconCalendar></IconCalendar>
          [5-1]数学运算
        </MenuItem>
        <SubMenu key="Spider">
          <template #title>
            <IconCalendar></IconCalendar> [5-4]爬虫
          </template>
          <MenuItem key="SpiderDouban">豆瓣</MenuItem>
          <MenuItem key="SpiderZhihu">知乎</MenuItem>
          <MenuItem key="SpiderJuejin">掘金</MenuItem>
        </SubMenu>
      </Menu>

    </LayoutSider>

    <LayoutContent>   
       <router-view></router-view>
<!--      <Editor msg="Hello Vue3 + pywebview + PyInstaller" />-->
    </LayoutContent>
  </Layout>

</template>

<script setup>
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup

import { useRouter } from 'vue-router';
const router = useRouter();

import {
  IconHome,
  IconCalendar,
} from '@arco-design/web-vue/es/icon';
import {Message} from "@arco-design/web-vue";


const onClickMenuItem = (key) => {
  // Message.info({ content: `You select ${key}`, showIcon: true });
  router.push(key)
}

</script>


<style>
html, body {
  height: 100%;
}

#app {
  height: 100%;
  overflow-y: hidden;
}
</style>

<style scoped>
.layout-demo {
  box-sizing: border-box;
  height: 100%;
  background: var(--color-fill-2);
  border: 1px solid var(--color-border);
}

.layout-demo :deep(.arco-layout-sider) {
   width: 300px;
}

.layout-demo :deep(.arco-layout-sider) .logo {
  height: 32px;
  line-height: 32px;
  font-weight: bold;
  margin: 12px 8px;
  /* color: white; */
  background: rgba(255, 255, 255, 0.2);
  text-align: center;
}
.layout-demo :deep(.arco-layout-sider-light) .logo{
  background: var(--color-fill-2);
}
.layout-demo :deep(.arco-layout-header)  {
  height: 64px;
  line-height: 64px;
  background: var(--color-bg-3);
}
.layout-demo :deep(.arco-layout-footer) {
  height: 48px;
  font-weight: 400;
  font-size: 14px;
  line-height: 48px;
}
.layout-demo :deep(.arco-layout-content) {
  padding: 16px;
  color: var(--color-text-2);
  font-weight: 400;
  font-size: 14px;
  background: var(--color-bg-3);
}

.layout-demo :deep(.arco-layout-footer) {

}
</style>
