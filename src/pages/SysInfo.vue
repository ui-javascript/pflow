<template>
  <span>用户名：{{ creator }}</span>

  <Button type="outline" v-show="!creator" @click="getOwner">
    获取本机用户名
  </Button>

</template>

<script setup>
import {ref} from "vue";

let creator = ref("");
const getOwner = async () => {
  const res = await window.pywebview.api.getOwner()
  creator.value = res
};

</script>