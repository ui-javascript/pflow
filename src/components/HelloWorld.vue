<script setup>
import { ref } from "vue";

defineProps({
  msg: String,
});

let creator = ref("pangao");

const a = ref(2);
const b = ref(3);
const filePath = ref("");

const getOwner = () => {
  window.pywebview.api.getOwner().then((res) => {
    creator.value = res;
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

    <p>
      基于
      <a href="https://v3.cn.vuejs.org" target="_blank">Vue3</a>
      |
      <a href="https://pywebview.flowrl.com" target="_blank">pywebview</a>
      |
      <a href="https://pyinstaller.readthedocs.io" target="_blank"
        >PyInstaller</a
      >
      框架，构建macOS和windows平台的客户端。
    </p>

    <p>本应用的视图层采用HTML+JS+CSS，业务层采用本地Python+调用远程API。</p>

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
      <input type="file" id="image" @change="preview($event)" />

      {{ filePath }}
    </div>
  </div>
</template>

<style scoped>
a {
  color: #42b983;
}
</style>
