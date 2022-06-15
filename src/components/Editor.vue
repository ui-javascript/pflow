<template>
  <div class="editor">

    <h1>{{ msg }}</h1>

    <p>本应用的视图层采用 HTML+JS+CSS</p>
    <p>业务层采用本地Python + 调用远程API</p>

    <a-divider orientation="left">系统信息</a-divider>

    <div style="margin-top: 10px;">
      <span>用户名：{{ creator }}</span>

      <a-button type="outline" v-show="!creator" @click="getOwner">
        获取本机用户名
      </a-button>

    </div>

    <a-divider orientation="left">数学运算</a-divider>

    <div style="margin-top: 10px;">
      <a-input-number :style="{ width: '100px' }" v-model="a"/>
      +
      <a-input-number :style="{ width: '100px' }" v-model="b"/>
      =
      <a-button @click="getSum" style="margin-left: 5px">相加(decimal)</a-button>
    </div>

    <a-divider orientation="left">文件操作</a-divider>


    <div style="margin-top: 10px;">
      <a-button @click="openPdfFile" style="margin-left: 5px;">生成pdf目录大纲</a-button>

      <a-button @click="openFolder" style="margin-left: 5px;">打开文件夹</a-button>

      <!-- <input type="file" id="image" @change="preview($event)" />
      {{ filePath }} -->
    </div>

    <a-divider orientation="left">代码执行</a-divider>

    <div id="vditor" style="margin: 10px 0"></div>

    <div style="margin-top: 10px;">
      <!-- <button @click="makeDir">创建文件夹</button> -->
      <a-button @click="execCode" style="margin-left: 5px;">执行代码</a-button>

    </div>

    <a-divider orientation="left">文件上传</a-divider>

    <a-upload style="margin-top: 10px;" draggable action="/" />

  </div>
</template>


<script setup>
import {ref, onMounted, nextTick} from "vue";
import {Message} from '@arco-design/web-vue';

import Vditor from 'vditor'
import "vditor/dist/index.css"

let toolbar = [
  'emoji',
  'headings',
  'bold',
  'italic',
  'strike',
  'link',
  '|',
  'list',
  'ordered-list',
  'check',
  'outdent',
  'indent',
  '|',
  'quote',
  'line',
  'code',
  'inline-code',
  'insert-before',
  'insert-after',
  '|',
  'upload',
  // 'record',
  'table',
  '|',
  'undo',
  'redo',
  '|',
  'edit-mode',
  // 'content-theme',
  // 'code-theme',
  'export',
  {
    name: 'more',
    toolbar: [
      'fullscreen',
      'both',
      'preview',
      // 'info',
      // 'help',
    ],
  }]


onMounted(() => {

  editor = new Vditor('vditor', {
    // mode: 'wysiwyg',
    height: 500,
    outline: {
      enable: true,
      position: 'right',
    },
    debugger: true,
    typewriterMode: true,
    preview: {
      markdown: {
        toc: true,
        mark: true,
        footnotes: true,
        autoSpace: true,
      },
      math: {
        engine: 'KaTeX',
      },
    },
    toolbarConfig: {
      // pin: true,
    },
    counter: {
      enable: true,
      type: 'text',
    },
    toolbar,

  })

  // @fix
  nextTick(() => {
    editor.setValue("def factorial(num):\n\tfact=1\tfor i in range(1,num+1):\n\t\tfact = fact*i\n\treturn fact\nprint(factorial(5))")
  })

})


defineProps({
  msg: String,
});

let creator = ref("");

let editor = ref(null);

const a = ref(0.1);
const b = ref(0.2);
const filePath = ref("");

const getOwner = async () => {
  const res = await window.pywebview.api.getOwner()
  creator.value = res
};


// const makeDir = () => {
//   window.pywebview.api.makeDir(`E:\\workspace-xxx`).then((res) => {
//     Message.info(res);
//   });
// };

const openPdfFile = async () => {
  const pdfPath = await window.pywebview.api.openPdfFile()
  if (!pdfPath) {
    return
  }

  // console.log(pdfPath[0])
  const outlinesPath = await window.pywebview.api.genPdfOutlines(pdfPath[0])
  // console.log(outlinesPath)
  Message.success({content: "同目录已生成pdf大纲 " + outlinesPath })

};

const openFolder = async () => {
  const res = await window.pywebview.api.openFolder()
  if (!res) {
    return
  }
  Message.info("选择文件夹 " + res)
}

const execCode = async () => {
  console.log(editor.getValue())
  await window.pywebview.api.execCode(editor.getValue())
};


const getSum = async () => {
  const res = await window.pywebview.api.getSum(a.value, b.value)
  Message.info("计算结果: " + res);
};

const preview = (event) => {
  let files = document.getElementById("image").files[0];
  console.log(files);
  filePath.value = getObjectURL(files);
};

const getObjectURL = (file) => {
  let url = null;
  if (window.createObjectURL != undefined) {
    url = window.createObjectURL(file);
  } else if (window.webkitURL != undefined) {
    url = window.webkitURL.createObjectURL(file);
  } else if (window.URL != undefined) {
    url = window.URL.createObjectURL(file);
  }
  return url;
};
</script>


<style scoped>
.editor {
  /*box-sizing: border-box;*/
}
</style>
