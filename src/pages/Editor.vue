<template>
  <div class="editor">

    <h1>{{ msg }}</h1>

    <p>本应用的视图层采用 HTML+JS+CSS</p>
    <p>业务层采用本地Python + 调用远程API</p>

    <Divider orientation="left">系统信息</Divider>

    <div style="margin-top: 10px;">
      <span>用户名：{{ creator }}</span>

      <Button type="outline" v-show="!creator" @click="getOwner">
        获取本机用户名
      </Button>

    </div>

    <Divider orientation="left">数学运算</Divider>

    <div style="margin-top: 10px;">
      <InputNumber :style="{ width: '100px' }" v-model="a"/>
      +
      <InputNumber :style="{ width: '100px' }" v-model="b"/>
      =
      <Button @click="getSum" style="margin-left: 5px">相加(decimal)</Button>
    </div>

    <Divider orientation="left">文件操作</Divider>


    <div style="margin-top: 10px;">
      <Button @click="openPdfFile" style="margin-left: 5px;">生成pdf目录大纲</Button>
      <Button @click="execPyFile" style="margin-left: 5px;">生成pdf目录大纲(安装依赖+选择Python脚本+选择PDF)</Button>

<!--      <Button @click="openFolder" style="margin-left: 5px;">打开文件夹</Button>-->

    </div>

    <Divider orientation="left">代码执行</Divider>

    <div style="height: 300px">
    <PythonEditor v-model="code"></PythonEditor>
    </div>

    <div style="margin-top: 10px;">
      <!-- <button @click="makeDir">创建文件夹</button> -->
      <Button @click="execCodeStr" style="margin-left: 5px;">执行代码</Button>

    </div>

    <Divider orientation="left">富文本编辑器</Divider>
    <div id="vditor" style="margin: 10px 0"></div>


    <Divider orientation="left">文件上传</Divider>

    <Upload style="margin-top: 10px;" draggable action="/"/>

  </div>
</template>


<script setup>
import {ref, onMounted, nextTick} from "vue";
import {Message} from '@arco-design/web-vue';


import Vditor from 'vditor'
import "vditor/dist/index.css"


import PythonEditor from '../components/PythonEditor.vue';

let creator = ref("");

let editor = ref(null);

const code = ref("def factorial(num):\n\tfact=1\n\tfor i in range(1,num+1):\n\t\tfact = fact*i\n\treturn fact\nprint(factorial(5))")
const a = ref(0.1);
const b = ref(0.2);
const filePath = ref("");

defineProps({
  msg: String,
});


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
    mode: 'wysiwyg',
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
    // code.value = "xxx"
    // code.value = "def factorial(num):\n\tfact=1\tfor i in range(1,num+1):\n\t\tfact = fact*i\n\treturn fact\nprint(factorial(5))"
  })

})




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
  Message.success({content: "已生成pdf大纲 " + outlinesPath})
  // window.open(outlinesPath)

};


const openFolder = async () => {
  const res = await window.pywebview.api.openFolder()
  if (!res) {
    return
  }
  Message.info("选择文件夹 " + res)
}

const execCodeStr = async () => {
  console.log(code.value)
  await window.pywebview.api.execCodeStr(code.value)
};

const execPyFile = async () => {
  const pyFilePath = await window.pywebview.api.openPyFile()
  if (!pyFilePath) {
    return
  }

  const pdfFilePath = await window.pywebview.api.openPdfFile()
  if (!pdfFilePath) {
    return
  }

  console.log(pyFilePath[0], pdfFilePath[0])

  const res = await window.pywebview.api.execPyFileWithArgv1(pyFilePath[0], pdfFilePath[0])
  if (!res) {
    return
  }
  Message.success("Python文件执行成功")
};


const getSum = async () => {
  const res = await window.pywebview.api.getSum(a.value, b.value)
  Message.info("计算结果: " + res);
};


</script>


<style scoped>
.editor {
  /*box-sizing: border-box;*/
}
</style>
