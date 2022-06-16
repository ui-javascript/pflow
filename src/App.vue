<template>
  <Layout class="layout-demo">

    <LayoutSider
      collapsible
      :collapsed-width="48"
      :width="280">
      <div class="logo"></div>
      <Menu
        :style="{ width: '100%' }"
        @menu-item-click="onClickMenuItem"
      >
        <MenuItem key="SysInfo">
          <IconHome></IconHome>
          [0-5]系统信息 <IconCheckCircle />
        </MenuItem>
        <SubMenu key="Security">
          <template #title>
            <IconCalendar></IconCalendar> [0-9]信息安全
          </template>
          <MenuItem key="PassWord">密码管理器</MenuItem>
          <MenuItem key="Crypto">加解密</MenuItem>
          <MenuItem key="Decode">编解码</MenuItem>
          <MenuItem key="FileCrypt">文件加密</MenuItem>
        </SubMenu>

        <SubMenu key="Translate">
          <template #title>
            <IconCalendar></IconCalendar> [1-2]语言翻译
          </template>
          <MenuItem key="Transl">翻译</MenuItem>
          <MenuItem key="Dict">词典</MenuItem>
        </SubMenu>
        <SubMenu key="News">
          <template #title>
            <IconCalendar></IconCalendar> [1-3]新闻资讯
          </template>
          <MenuItem key="TopHub">今日热榜</MenuItem>
          <MenuItem key="RSSFeed">RSS订阅</MenuItem>
        </SubMenu>
        <SubMenu key="Design">
          <template #title>
            <IconCalendar></IconCalendar> [1-5]设计素材
          </template>
          <MenuItem key="WallPaper">壁纸</MenuItem>
          <MenuItem key="IconFont">IconFont</MenuItem>
          <MenuItem key="EmojiFight">表情包</MenuItem>
        </SubMenu>
        <SubMenu key="Editor">
          <template #title>
            <IconCalendar></IconCalendar> [1-6]编辑器
          </template>
          <MenuItem key="MdEditor">Markdown编辑器 <IconCheckCircle /></MenuItem>
          <MenuItem key="CodeEditor">Python代码编辑器 <IconCheckCircle /></MenuItem>
        </SubMenu>
        <SubMenu key="Improve">
          <template #title>
            <IconCalendar></IconCalendar> [1-6]效率工具
          </template>
          <MenuItem key="TodoList">待办清单(TodoList)</MenuItem>
          <MenuItem key="PinMemo">备忘录</MenuItem>
<!--          <MenuItem key="CropperIt">截图</MenuItem>-->
          <MenuItem key="QrCode">二维码</MenuItem>
<!--          <MenuItem key="ColorPicker">颜色拾取</MenuItem>-->
          <MenuItem key="ShortUrl">短地址</MenuItem>
          <MenuItem key="Coin">汇率换算</MenuItem>
          <MenuItem key="RandomAvatar">随机头像</MenuItem>
          <MenuItem key="CountStat">字数统计</MenuItem>
        </SubMenu>
        <SubMenu key="Office">
          <template #title>
            <IconCalendar></IconCalendar> [1-7]办公文档
          </template>
          <MenuItem key="RenameBatch">批量重命名</MenuItem>
          <SubMenu key="Pic" title="图片">
            <MenuItem key="PicMin">图片压缩</MenuItem>
            <MenuItem key="RemoveBg">抠除背景 <IconCheckCircle /></MenuItem>
            <MenuItem key="PicStitch">图片拼接</MenuItem>
          </SubMenu>
          <SubMenu key="OfficePdf" title="PDF">
            <MenuItem key="PdfOutline">生成PDF目录大纲 <IconCheckCircle /></MenuItem>
          </SubMenu>
          <SubMenu key="Markdown" title="Markdown">
            <MenuItem key="MdSlidev">MD生成PPT(slidev)</MenuItem>
            <MenuItem key="MdCoolma">MD显示增强(coolma) <IconCheckCircle /></MenuItem>
          </SubMenu>
        </SubMenu>
        <SubMenu key="Convert">
          <template #title>
            <IconCalendar></IconCalendar> [1-7]格式转换
          </template>
          <MenuItem key="Zip">解压缩</MenuItem>
          <SubMenu key="TXT" title="TXT">
            <MenuItem key="Txt2Word">TXT转Word</MenuItem>
          </SubMenu>
          <SubMenu key="PDF" title="PDF">
            <MenuItem key="Pdf2Pic">PDF转图片</MenuItem>
            <MenuItem key="Pdf2Word">PDF转Word</MenuItem>
          </SubMenu>
        </SubMenu>
        <SubMenu key="Cloud">
          <template #title>
            <IconCalendar></IconCalendar> [3-6]云服务
          </template>
          <MenuItem key="OssUpload">OSS图床</MenuItem>
        </SubMenu>
        <MenuItem key="MathExpr">
          <IconCalendar></IconCalendar>
          [5-1]数学运算 <IconCheckCircle />
        </MenuItem>
        <SubMenu key="Spider">
          <template #title>
            <IconCalendar></IconCalendar> [5-4]网络爬虫
          </template>
          <MenuItem key="SpiderDouban">豆瓣</MenuItem>
          <MenuItem key="SpiderZhihu">知乎</MenuItem>
          <MenuItem key="SpiderJuejin">掘金</MenuItem>
        </SubMenu>
        <SubMenu key="Devops">
          <template #title>
            <IconCalendar></IconCalendar> [5-5]自动化脚本
          </template>
          <MenuItem key="Deploy">前端项目部署</MenuItem>
        </SubMenu>
        <SubMenu key="AI">
          <template #title>
            <IconCalendar></IconCalendar> [5-6]智能助手
          </template>
          <MenuItem key="OCR">OCR</MenuItem>
        </SubMenu>
        <SubMenu key="MiniGame">
          <template #title>
            <IconCalendar></IconCalendar> [6-5]小游戏
          </template>
          <MenuItem key="Snake">贪吃蛇</MenuItem>
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
  IconCheckCircle,
} from '@arco-design/web-vue/es/icon';
// Message.info({ content: `You select ${key}`, showIcon: true });

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
   /*min-width: 300px;*/
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
