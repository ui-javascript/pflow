<template>
  <a-layout class="layout-demo">

    <a-layout-sider 
      collapsible 
      breakpoint="xl">
      <!-- <div class="logo"></div> -->
      <a-menu
        :default-open-keys="['1']"
        :default-selected-keys="['0_3']"
        :style="{ width: '100%' }"
        @menu-item-click="onClickMenuItem"
      >
        <a-menu-item key="0_1" disabled>
          <IconHome></IconHome>
          Menu 1
        </a-menu-item>
        <a-menu-item key="0_2">
          <IconCalendar></IconCalendar>
          Menu 2
        </a-menu-item>
        <a-menu-item key="0_3">
          <IconCalendar></IconCalendar>
          Menu 3
        </a-menu-item>
        <a-sub-menu key="1">
          <template #title>
            <IconCalendar></IconCalendar> Navigation 1
          </template>
          <a-menu-item key="1_1">Menu 1</a-menu-item>
          <a-menu-item key="1_2">Menu 2</a-menu-item>
          <a-sub-menu key="2" title="Navigation 2">
            <a-menu-item key="2_1">Menu 1</a-menu-item>
            <a-menu-item key="2_2">Menu 2</a-menu-item>
          </a-sub-menu>
          <a-sub-menu key="3" title="Navigation 3">
            <a-menu-item key="3_1">Menu 1</a-menu-item>
            <a-menu-item key="3_2">Menu 2</a-menu-item>
            <a-menu-item key="3_3">Menu 3</a-menu-item>
          </a-sub-menu>
        </a-sub-menu>
        <a-sub-menu key="4">
          <template #title>
            <IconCalendar></IconCalendar> Navigation 4
          </template>
          <a-menu-item key="4_1">Menu 1</a-menu-item>
          <a-menu-item key="4_2">Menu 2</a-menu-item>
          <a-menu-item key="4_3">Menu 3</a-menu-item>
        </a-sub-menu>
      </a-menu>

    </a-layout-sider>

    <a-layout-content>   
      <router-view></router-view>       
      <Editor msg="Hello Vue3 + pywebview + PyInstaller" />
    </a-layout-content>
  </a-layout>

</template>

<script setup>
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
import Editor from './components/Editor.vue'
import { Message} from '@arco-design/web-vue';

import {
  IconHome,
  IconCalendar,
} from '@arco-design/web-vue/es/icon';


const onClickMenuItem = (key) => {
  Message.info({ content: `You select ${key}`, showIcon: true });
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
  padding: 24px;
  color: var(--color-text-2);
  font-weight: 400;
  font-size: 14px;
  background: var(--color-bg-3);
}

.layout-demo :deep(.arco-layout-footer) {

}
</style>
