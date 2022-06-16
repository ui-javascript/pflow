<template>
  <Layout class="layout-demo">

    <LayoutSider collapsible>
      <div class="logo"></div>
      <Menu
        :default-open-keys="['1']"
        :default-selected-keys="['0_3']"
        :style="{ width: '100%' }"
        @menu-item-click="onClickMenuItem"
      >
        <MenuItem key="SysInfo">
          <IconHome></IconHome>
          [0-5]系统信息
        </MenuItem>
        <MenuItem key="0_1">
          <IconHome></IconHome>
          [0-9]加解密
        </MenuItem>
        <MenuItem key="0_2">
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
        </SubMenu>
        <SubMenu key="1">
          <template #title>
            <IconCalendar></IconCalendar> [1-7]格式转换
          </template>
          <MenuItem key="1_1">TXT转Word</MenuItem>
          <SubMenu key="2" title="PDF">
            <MenuItem key="2_1">PDF转图片</MenuItem>
            <MenuItem key="2_2">PDF转Word</MenuItem>
          </SubMenu>
          <SubMenu key="3" title="Markdown">
            <MenuItem key="3_1">slidev</MenuItem>
            <MenuItem key="3_2">coolma</MenuItem>
          </SubMenu>
        </SubMenu>
        <MenuItem key="0_3">
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
        <SubMenu key="4">
          <template #title>
            <IconCalendar></IconCalendar> [5-4]爬虫
          </template>
          <MenuItem key="4_1">豆瓣</MenuItem>
          <MenuItem key="4_2">知乎</MenuItem>
          <MenuItem key="4_3">掘金</MenuItem>
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
