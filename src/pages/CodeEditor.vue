<template>

<Button @click="execCodeStr">执行代码</Button>

<div style="height: calc(100% - 50px); margin-top: 10px;">
  <PythonEditor v-model="code"></PythonEditor>
</div>

</template>


<script setup>
import {ref} from "vue";
import PythonEditor from '../components/PythonEditor.vue';


const code = ref("def factorial(num):\n\tfact=1\n\tfor i in range(1,num+1):\n\t\tfact = fact*i\n\treturn fact\nprint(factorial(5))")


const execCodeStr = async () => {
  console.log(code.value)
  await window.pywebview.api.execCodeStr(code.value)
};

</script>


<style scoped>

</style>
