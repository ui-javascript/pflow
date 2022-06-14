<script setup>
import { ref, onMounted } from "vue";


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
  'record',
  'table',
  '|',
  'undo',
  'redo',
  '|',
  'edit-mode',
  'content-theme',
  'code-theme',
  'export',
  {
    name: 'more',
    toolbar: [
      'fullscreen',
      'both',
      'preview',
      'info',
      'help',
    ],
  }]


onMounted(() => {
  editor = new Vditor('vditor', {
    mode: 'wysiwyg',
    height: window.innerHeight - 270,
    outline: {
      enable: true,
      position: 'right',
    },
    debugger: true,
    typewriterMode: true,
    placeholder: 
`def factorial(num): 
  fact=1 
  for i in range(1,num+1): 
      fact = fact*i 
  return fact 
print(factorial(5))
`,
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

})


defineProps({
  msg: String,
});

let creator = ref("pangao");

let editor = ref(null);

const a = ref(2);
const b = ref(3);
const filePath = ref("");

const getOwner = () => {
  window.pywebview.api.getOwner().then((res) => {
    creator.value = res;
  });
};

const makeDir = () => {
  window.pywebview.api.makeDir(`E:\\workspace-xxx`).then((res) => {
    alert(res);
  });

};

const openFile = () => {
  window.pywebview.api.openFile().then((res) => {
    alert(res)
  });
};

const execCode = () => {

  window.pywebview.api.execCode(editor.getValue()).then((res) => {
    // alert(res)
  });

};



const getSum = () => {
  window.pywebview.api.getSum(a.value, b.value).then((res) => {
    alert(res);
  });
};

const preview = (event) => {
  let files = document.getElementById("image").files[0];
  console.log(files);
  filePath.value = getObjectURL(files);
};

const getObjectURL = (file) => {
  let url = null;
  if (window.createObjectURL != undefined) {
    // basic
    url = window.createObjectURL(file);
  } else if (window.webkitURL != undefined) {
    // webkit or chrome
    url = window.webkitURL.createObjectURL(file);
  } else if (window.URL != undefined) {
    // mozilla(firefox)
    url = window.URL.createObjectURL(file);
  }
  return url;
};
</script>

<template>
  <div>



    <h1>{{ msg }}</h1>



    <p>本应用的视图层采用 HTML+JS+CSS</p>
    <p>业务层采用本地Python + 调用远程API</p>

    <div style="margin-top: 10px;">
      <span>用户名：{{ creator }}</span>

      <button v-if="creator == 'pangao'" type="button" @click="getOwner">
        获取本机用户名
      </button>
    </div>

    <div style="margin-top: 10px;">
      <input type="number" v-model="a" /> + <input type="number" v-model="b" />

      <button @click="getSum">相加</button>
    </div>

    <div style="margin-top: 10px;">
      <button @click="makeDir">创建文件夹</button>
      <button @click="execCode" style="margin-left: 5px;">执行代码</button>
    </div>

    <div style="margin-top: 10px;">
      <button @click="openFile" style="margin-left: 5px;">打开文件</button>

      <input type="file" id="image" @change="preview($event)" />
      {{ filePath }}
    </div>

    <div id="vditor" style="margin-top: 10px;"></div>


  </div>
</template>

<style scoped>

</style>
